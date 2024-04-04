from fastapi import APIRouter, Depends, Header

# from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from .dependencies import (
    validate_auth_user,
    get_current_token_payload,
    get_current_active_auth_user,
    authorize,
)

# from src.database import get_db
from users.schemas import UserBase
from .schemas import TokenInfo
from . import utils as auth_utils
from database import db_helper

auth_router = APIRouter()


@auth_router.post("/login/", response_model=TokenInfo)
def auth_user_issue_jwt(
    user: UserBase = Depends(validate_auth_user),
):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
        "is_superuser": user.is_superuser,
    }
    access_token = auth_utils.create_access_jwt(jwt_payload)

    return TokenInfo(
        access_token=access_token,
        refresh_token=user.refresh_token,
        token_type="Bearer",
    )


@auth_router.get("/users/me/")
def auth_user_check_self_info(
    payload: dict = Depends(get_current_token_payload),
    user: UserBase = Depends(get_current_active_auth_user),
):
    iat = payload.get("iat")
    return {
        "username": user.username,
        "email": user.email,
        "logged_in_at": iat,
    }


@auth_router.post("/refresh/")
async def refresh(user: UserBase = Depends(authorize)):
    jwt_payload = {
        "sub": user.username,
        "username": user.username,
        "email": user.email,
        "is_superuser": user.is_superuser,
    }
    access_token = auth_utils.create_access_jwt(jwt_payload)
    return TokenInfo(
        access_token=access_token,
        refresh_token=user.refresh_token,
        token_type="Bearer",
    )
