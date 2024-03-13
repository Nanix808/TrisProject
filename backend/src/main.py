from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from starlette.middleware.base import BaseHTTPMiddleware
from auth.router import auth_router
from users.router import user_router
from authorization.router import authz_router

app = FastAPI()

app = FastAPI(debug=True)


origins = [
    "http://localhost",
    "http://localhost:5173",
    "http://localhost:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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


# Add the middleware to FastAPI
app.add_middleware(RBACMiddleware)


# Добавляем роуты из папки api
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(authz_router, prefix="/authorization", tags=["authorization"])


from fastapi.routing import APIRoute


def get_route_info(route: APIRoute):
    return {
        "path": route.path,
        "methods": route.methods,
        "dependencies": route.dependencies,
        # Add more attributes as needed
    }


for route in app.routes:
    if isinstance(route, APIRoute):
        route_info = get_route_info(route)
        print(route_info)
# Запуск сервера Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
