from typing import Annotated
from fastapi import Depends
from jwt.exceptions import InvalidTokenError
from .utils import decode_jwt
from fastapi.security import OAuth2PasswordBearer
from .schemas import UserLogin
from users.schemas import UserBase
from config import settings
from . import utils as auth_utils
from users.dependencies import user_service
from users.service import UserService
from .exceptions import (
    unauthed_exc,
    unactive_exc,
    token_invalide_exc,
    refresh_token_invalide_exc,
)

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=settings.auth_jwt.tokenUrl,
)


async def validate_auth_user(
    payload: UserLogin,
    user_service: Annotated[UserService, Depends(user_service)],
):
    user = await user_service.get_by_filter({"username": payload.username})
    if not user:
        raise unauthed_exc
    if not auth_utils.validate_password(
        password=payload.password,
        hashed_password=user.password_hash,
    ):
        raise unauthed_exc
    if not user.is_active:
        raise unactive_exc

    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    await user_service.update_user_refresh_token(user, jwt_payload)
    return user


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    if token == "null":
        raise token_invalide_exc
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise token_invalide_exc
    if not payload:
        raise token_invalide_exc
    return payload


async def get_current_auth_user(
    user_service: Annotated[UserService, Depends(user_service)],
    payload: dict = Depends(get_current_token_payload),
) -> UserBase:
    username: str | None = payload.get("sub")
    user = await user_service.get_by_filter({"username": username})
    if user:
        return user
    raise token_invalide_exc


def get_current_active_auth_user(
    user: UserBase = Depends(get_current_auth_user),
):
    if user.is_:
        return user
    raise unactive_exc


def get_current_active_auth_is_superuser_user(
    user: UserBase = Depends(get_current_active_auth_user),
):
    if user.is_superuser:
        return user
    raise unactive_exc


async def authorize(
    user_service: Annotated[UserService, Depends(user_service)],
    token: str = Depends(oauth2_scheme),
) -> dict:
    # validate the refresh jwt token
    if token == "null":
        raise refresh_token_invalide_exc
    payload = decode_jwt(token)
    if not payload:
        raise refresh_token_invalide_exc
    username = payload.get("username")
    user = await user_service.get_by_filter({"username": username})
    if not user or token != user.refresh_token:
        raise refresh_token_invalide_exc
    # generate new refresh token and update user
    # jwt_payload = {
    #     "sub": user.username,
    #     "username": user.username,
    #     "email": user.email,
    # }
    # await users_crud.update_user_refresh_token(user, jwt_payload)
    return user
