from fastapi import (
    Depends,
    Form,
)
from jwt.exceptions import InvalidTokenError
from .utils import create_refresh_jwt, decode_jwt
from fastapi.security import (
    OAuth2PasswordBearer,
)

from .schemas import UserLogin
from users.schemas import UserBase
from config import settings

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=settings.auth_jwt.tokenUrl,
)


from . import utils as auth_utils
from sqlalchemy.ext.asyncio import AsyncSession
from users.crud import UsersCRUD
from database import db_helper
from .exceptions import (
    unauthed_exc,
    unactive_exc,
    token_invalide_exc,
    refresh_token_invalide_exc,
)


async def validate_auth_user(
    payload: UserLogin,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
):
    users_crud = UsersCRUD(session)
    user = await users_crud.get_user_by_username(payload.username)
    if not user:
        raise unauthed_exc
    if not auth_utils.validate_password(
        password=payload.password,
        hashed_password=user.password_hash,
    ):
        raise unauthed_exc
    if not user.available:
        raise unactive_exc

    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }
    await users_crud.update_user_refresh_token(user, jwt_payload)
    return user


def get_current_token_payload(
    token: str = Depends(oauth2_scheme),
) -> dict:
    print("token", token)
    try:
        payload = auth_utils.decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise token_invalide_exc
    return payload


async def get_current_auth_user(
    payload: dict = Depends(get_current_token_payload),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> UserBase:
    username: str | None = payload.get("sub")
    users_crud = UsersCRUD(session)
    user = await users_crud.get_user_by_username(username)
    if user:
        return user
    raise token_invalide_exc


def get_current_active_auth_user(
    user: UserBase = Depends(get_current_auth_user),
):
    if user.available:
        return user
    raise unactive_exc


async def authorize(
    token: str = Depends(oauth2_scheme),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> dict:
    # validate the refresh jwt token

    payload = decode_jwt(token)

    if not payload:
        raise refresh_token_invalide_exc
    # check if "mode": "refresh_token"
    # if "user_name" not in data and "mode" not in data:
    #     raise token_invalide_exc
    # if data["mode"] != "refresh_token":
    #     raise token_invalide_exc
    # check if user exists

    username = payload.get("username")
    print("user", username)
    users_crud = UsersCRUD(session)

    user = await users_crud.get_user_by_username(username)

    if not user or token != user.refresh_token:
        raise refresh_token_invalide_exc
    # generate new refresh token and update user
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
    }

    # await users_crud.update_user_refresh_token(user, jwt_payload)
    # generate new access token
    return user
