from fastapi import APIRouter, Depends, status

# from .crud import TransportCRUD
from database import db_helper
from sqlalchemy.ext.asyncio import AsyncSession

from .shemas import TransportCreate

# @transport_router.get("/")
# async def get_timetable_for_day():
#     return {"message": "Hello World"}
transport_router = APIRouter()


# @transport_router.get("/")
# async def get_transport(
#     session: AsyncSession = Depends(db_helper.scoped_session_dependency),
# ):
#     users_crud = TransportCRUD(session)
#     users = await users_crud.get_users()
#     return users


from typing import Annotated
from .service import TransportService
from .dependencies import transport_service


@transport_router.get("/wer/")
async def get_transports(
    transport_service: Annotated[TransportService, Depends(transport_service)],
):

    users = await transport_service.get_transport()
    return users


@transport_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_in: TransportCreate,
):
    transport = await transport_service.add_transport(transport_in)
    return transport
