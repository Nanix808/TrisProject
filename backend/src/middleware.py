from fastapi import Depends, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from users.schemas import UserBase
from authorization.dependencies import get_permissions


# class RBACMiddleware(BaseHTTPMiddleware):
#     async def dispatch(
#         self,
#         request: Request,
#         call_next,
#     ):
#         request_method = str(request.method).upper()
#         action = translate_method_to_action(request_method)
#         resource = request.url.path[1:]
#         print("--------------------------", request_method, resource, action)
#         # if not resource in EXLUDED_PATHS:
#         #     admin1 = USERS[
#         #         "admin1"
#         #     ]  # Switch bewtwenn user and admin by commenting this or the next line
#         #     # user1 = USERS['user1']
#         #     if not has_permission(admin1["role"], resource, action):
#         #         raise HTTPException(status_code=403, detail="Insufficient permissions")
#         response = await call_next(request)
#         return response


async def auth_middleware(permission: bool = Depends(get_permissions)):
    if not permission:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions",
        )
