from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from auth.router import auth_router
from users.router import user_router
from authorization.router import authz_router
from transport.router import transport_router

from middleware import auth_middleware


app = FastAPI(debug=True)

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


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Запуск сервера Uvicorn
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
