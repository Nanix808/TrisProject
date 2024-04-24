from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from .models import User
from .repositories import UserRepository
from .service import UserService

# from .crud import UsersCRUD


def user_service():
    return UserService(UserRepository)


async def user_by_id(
    user_id: int = Path(...),
    user_service: user_service = Depends(user_service),
) -> User:
    """
    Dependency to get User by id
    """
    user = await user_service.user_by_id(user_id)
    if user is not None:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User id={user_id} not found"
    )
