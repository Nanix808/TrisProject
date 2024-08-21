from fastapi import Depends, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from users.schemas import UserBase
from authorization.dependencies import get_permissions


async def auth_middleware(permission: bool = Depends(get_permissions)):
    if not permission:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
