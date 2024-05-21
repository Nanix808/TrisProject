from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


def translate_method_to_action(method: str) -> str:
    method_permission_mapping = {
        "GET": "read",
        "POST": "write",
        "PUT": "delete",
        "DELETE": "delete",
    }
    return method_permission_mapping.get(method.upper(), "read")


class RBACMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_method = str(request.method).upper()
        action = translate_method_to_action(request_method)
        resource = request.url.path[1:]
        print(request_method, resource, action)
        # if not resource in EXLUDED_PATHS:
        #     admin1 = USERS[
        #         "admin1"
        #     ]  # Switch bewtwenn user and admin by commenting this or the next line
        #     # user1 = USERS['user1']
        #     if not has_permission(admin1["role"], resource, action):
        #         raise HTTPException(status_code=403, detail="Insufficient permissions")
        response = await call_next(request)
        return response
