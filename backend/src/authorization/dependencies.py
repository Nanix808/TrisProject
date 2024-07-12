from typing import Annotated
from fastapi import Depends, Request
from auth.dependencies import get_current_token_payload
from .exceptions import not_admin_exc, not_permission_exc

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


def get_uid_from_request(request: Request):
    return request.state.uid


def get_role_from_token(
    request: Request,
    payload: dict = Depends(get_current_token_payload),
):
    is_superuser: bool | None = payload.get("is_superuser")
    if is_superuser:
        request.state.uid = 0
        return None
    role_id: int | None = payload.get("role_id")
    user_id: int | None = payload.get("sub_id")
    request.state.uid = user_id
    if role_id and user_id:
        return role_id
    raise not_permission_exc


def translate_method_to_action(method: str) -> str:
    method_permission_mapping = {
        "GET": "read",
        "POST": "write",
        "PATCH": "delete",
        "DELETE": "delete",
    }
    return method_permission_mapping.get(method.upper(), "read")


async def get_permissions(
    request: Request,
    role_service: Annotated[RoleService, Depends(role_service)],
    role_id: int | None = Depends(get_role_from_token),
):
    if request.state.uid == 0 or not role_id:
        return True
    role = await role_service.get_by_id(role_id)
    if not role:
        raise not_permission_exc
    request_method = str(request.method).upper()
    # action = translate_method_to_action(request_method)
    resource = request.url.path[1:].split("/")[0]

    permissions = role.permissions.get(resource, None)

    if permissions:
        if request_method in permissions or "ADMIN" in permissions:
            if "ADMIN" in permissions:
                request.state.uid = 0
            return True
    return False
    # if user.is_active:
    #     return user
    # raise unactive_exc
