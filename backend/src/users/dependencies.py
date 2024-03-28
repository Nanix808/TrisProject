from typing import Annotated

from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from .models import User


from .crud import UsersCRUD


async def user_by_id(
    user_id: int = Path(...),
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> User:
    """
    Dependency to get User by id
    """
    users_crud = UsersCRUD(session)
    user = await users_crud.get_user(user_id)
    if user is not None:
        return user
    await session.close()
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"User id={user_id} not found"
    )


# async def get_role_by_id(
#     role_id: Annotated[int, Path],
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ) -> User:
#     roles_crud = RolesCRUD(session)
#     role = await roles_crud.get_role_by_id(role_id)
#     if role is not None:
#         return None
#     return role
# raise HTTPException(
#     status_code=status.HTTP_404_NOT_FOUND, detail=f"User id={user_id} not found"
# )
