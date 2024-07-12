from fastapi import FastAPI, Request, Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
import uvicorn
from auth.router import auth_router
from users.router import user_router
from authorization.router import authz_router
from transport.router import transport_router

from middleware import auth_middleware


app = FastAPI(debug=True)


origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:5173",
    "https://localhost:5173/",
    "http://127.0.0.1:5173",
    "https://127.0.0.1:5173/",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# router = APIRouter(dependencies=[Depends(auth_middleware)])

# Add the middleware to FastAPI
# app.add_middleware(RBACMiddleware)


# Add the router to FastAPI
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["users"])
app.include_router(
    authz_router, prefix="/authorization", tags=["authorization"]
)
app.include_router(
    transport_router,
    prefix="/transport",
    tags=["transport"],
    dependencies=[Depends(auth_middleware)],
)


# from fastapi.routing import APIRoute


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
# Запуск сервера Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
