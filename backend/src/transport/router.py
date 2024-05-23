from typing import Annotated

from fastapi import APIRouter, Depends, status, Path, Request

from .service import TransportService
from .dependencies import transport_service
from .shemas import TransportCreate, TransportUpdate
from users.schemas import User
from auth.dependencies import get_current_active_auth_user
from authorization.dependencies import get_uid_from_request

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


@transport_router.delete(
    "/{transport_id}", status_code=status.HTTP_204_NO_CONTENT
)
async def delete_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_id: int = Path(...),
    uid: int = Depends(get_uid_from_request),
) -> None:
    await transport_service.delete_hard(transport_id, uid)
    return None


@transport_router.patch("/{transport_id}", status_code=status.HTTP_201_CREATED)
async def update_transport(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    transport_update: TransportUpdate,
    transport_id: int = Path(...),
    uid: int = Depends(get_uid_from_request),
) -> None:

    await transport_service.update_transport(
        transport_id, transport_update, uid
    )
    return None
