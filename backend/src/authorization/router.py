from fastapi import APIRouter, Depends, HTTPException, status
from .schemas import Role

# # from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import db_helper

# from .schemas import (
#     User,
#     UserBase,
#     UserCreate,
#     UserUpdate,
#     UserUpdatePartial,
# )
from .crud import RolesCRUD

# from .dependencies import user_by_id
# from fastapi import HTTPException


authz_router = APIRouter()


@authz_router.get(
    "/",
    response_model=list[Role],
    status_code=status.HTTP_200_OK,
)
async def get_roles(
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> list[Role]:
    role_crud = RolesCRUD(session)
    roles = await role_crud.get_roles()
    return roles


@authz_router.post(
    "/",
    response_model=Role,
    status_code=status.HTTP_201_CREATED,
)
async def create_role(
    role_in: Role,
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Role:
    rolesCrud = RolesCRUD(session)
    roles = await rolesCrud.create_role(role_in=role_in)
    return roles
