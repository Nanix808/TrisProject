from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession


from database import db_helper
from authorization.dependencies import get_current_active_auth_is_superuser_user
from .dependencies import user_by_id, user_service
from .repositories import UserRepository
from .service import UserService
from .schemas import (
    User,
    UserBase,
    UserCreate,
    UserCreated,
    UserUpdate,
    UserUpdatePartial,
)


user_router = APIRouter()

@user_router.get(
    "/",
    response_model=list[User],
)
async def get_users(
    user_service: Annotated[UserService, Depends(user_service)],
) -> list[User]:

    users = await user_service.get_users()
    return users


@user_router.post(
    "/",
    response_model=UserCreated,
    status_code=status.HTTP_201_CREATED,
    tags=["users"],
)
async def create_user(
    user_service: Annotated[UserService, Depends(user_service)],
    user_in: UserCreate,
) -> User:
    users = await user_service.add_one(user_in)
    return users


@user_router.get("/{user_id}", response_model=User)
async def get_user(user: User = Depends(user_by_id)):
    return user


@user_router.patch("/{user_id}", response_model=UserCreated)
async def update_user_partial(
    user_service: Annotated[UserService, Depends(user_service)],
    user_update: UserUpdate,
    user_id: int = Path(...),
):
    user = await user_service.update_user(user_id, user_update)
    return user


@user_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_service: Annotated[UserService, Depends(user_service)],
    user_id: int = Path(...),
) -> None:
    await user_service.delete_is_active(user_id)
