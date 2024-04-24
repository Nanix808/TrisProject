# from typing import Annotated
from fastapi import Depends
from auth.dependencies import get_current_token_payload
from .exceptions import not_admin_exc

from .repositories import RoleRepository
from .service import RoleService


def role_service():
    return RoleService(RoleRepository)


def get_current_active_auth_is_superuser_user(
    payload: dict = Depends(get_current_token_payload),
):
    if payload.get("is_superuser"):
        return payload
    raise not_admin_exc
