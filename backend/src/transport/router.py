from typing import Annotated

from fastapi import APIRouter, Depends, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from database import db_helper
from .service import TransportService
from .dependencies import transport_service
from .shemas import TransportCreate, TransportUpdate


transport_router = APIRouter()


@transport_router.get("/")
async def get_transports(
    transport_service: Annotated[TransportService, Depends(transport_service)],
):
    transport = await transport_service.get_transport()
    return transport


@transport_router.post("/", status_code=status.HTTP_201_CREATED)
async def add_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_in: TransportCreate,
):
    transport = await transport_service.add_transport(transport_in)
    return transport


@transport_router.delete("/{transport_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_id: int = Path(...),
) -> None:
    await transport_service.delete_hard(transport_id)
    return None


@transport_router.patch("/{transport_id}", status_code=status.HTTP_201_CREATED)
async def update_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_update: TransportUpdate,
    transport_id: int = Path(...),
) -> None:
    await transport_service.update_transport(transport_id, transport_update)
    return None
