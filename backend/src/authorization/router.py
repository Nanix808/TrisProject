import re
from fastapi import APIRouter, Depends, HTTPException, status, Request
from fastapi.routing import APIRoute
from sqlalchemy.ext.asyncio import AsyncSession

from .schemas import Role, BaseRole, BaseRouter
from database import db_helper
from .crud import RolesCRUD
from .dependencies import get_current_active_auth_is_superuser_user

authz_router = APIRouter()


@authz_router.get(
    "/",
    response_model=list[Role],
    status_code=status.HTTP_200_OK,
)
async def get_roles(
    current_user: dict = Depends(get_current_active_auth_is_superuser_user),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Role]:
    role_crud = RolesCRUD(session)
    roles = await role_crud.get_roles()
    return roles


@authz_router.post(
    "/",
    response_model=BaseRole,
    status_code=status.HTTP_201_CREATED,
)
async def create_role(
    role_in: BaseRole,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Role:
    rolesCrud = RolesCRUD(session)
    roles = await rolesCrud.create_role(role_in=role_in)
    return roles


@authz_router.get("/list_endpoints/")
def list_endpoints(
    request: Request,
    current_user: dict = Depends(get_current_active_auth_is_superuser_user),
):
    pattern = re.compile("[^a-zA-Z]")
    my_dict = {}
    for route in request.app.routes:
        if isinstance(route, APIRoute):
            key = my_dict.setdefault(route.path.split("/")[1] + "/", set())
            key.add(re.sub(pattern, "", str(route.methods)))
    return my_dict


# @authz_router.get(
#     "/",
#     # response_model=BaseRole,
#     status_code=status.status.HTTP_200_OK,
# )
# async def get_all_routers(
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ) -> Role:
#     url_list = [
#         {"path": route.path, "name": route.name} for route in authz_router.app.routes
#     ]
#     return url_list


# for route in app.routes:
#     if isinstance(route, APIRoute):
#         route_info = get_route_info(route)
#         print(route_info)


# def get_route_info(route: APIRoute):
#     return {
#         "path": route.path,
#         "methods": route.methods,
#         "dependencies": route.dependencies,
#         # Add more attributes as needed
#     }


# for route in app.routes:
#     if isinstance(route, APIRoute):
#         route_info = get_route_info(route)
#         print(route_info)
