import re
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Request, Path
from fastapi.routing import APIRoute
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Role, BaseRole, BaseRouter
from database import db_helper


from .dependencies import (
    get_current_active_auth_is_superuser_user,
    role_service,
)
from .service import RoleService

authz_router = APIRouter()


@authz_router.get(
    "/",
    response_model=list[Role],
    status_code=status.HTTP_200_OK,
)
async def get_roles(
    role_service: Annotated[RoleService, Depends(role_service)],
) -> list[Role]:
    roles = await role_service.get_roles()
    return roles


@authz_router.post(
    "/",
    response_model=BaseRole,
    status_code=status.HTTP_201_CREATED,
)
async def create_role(
    role_in: BaseRole,
    role_service: Annotated[RoleService, Depends(role_service)],
) -> Role:
    role = await role_service.create_role(role_in=role_in)
    return role


@authz_router.patch("/{role_id}", status_code=status.HTTP_201_CREATED)
async def update_role(
    role_service: Annotated[RoleService, Depends(role_service)],
    role_update: BaseRole,
    role_id: int = Path(...),
    isSuperAdmin: int = Depends(get_current_active_auth_is_superuser_user),
) -> None:

    await role_service.update_role(role_id, role_update)
    return None


@authz_router.delete("/{role_id}", status_code=status.HTTP_201_CREATED)
async def delete_role(
    role_service: Annotated[RoleService, Depends(role_service)],
    role_id: int = Path(...),
    isSuperAdmin: int = Depends(get_current_active_auth_is_superuser_user),
) -> None:
    await role_service.delete(role_id)
    return None


@authz_router.get("/list_endpoints/")
def list_endpoints(
    request: Request,
    current_user: dict = Depends(get_current_active_auth_is_superuser_user),
):
    pattern = re.compile("[^a-zA-Z]")
    my_dict = {}
    for route in request.app.routes:
        if route.path.split("/")[1] in ["auth", "users", "authorization"]:
            continue
        if isinstance(route, APIRoute):
            key = my_dict.setdefault(route.path.split("/")[1], set())
            key.add(re.sub(pattern, "", str(route.methods)))
    return my_dict
