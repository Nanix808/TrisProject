from typing import Annotated

from fastapi import APIRouter, Depends, status, Path, Request, Body

from .service import TransportService, CarService
from .dependencies import transport_service, car_service
from .shemas import (
    TransportCreate,
    TransportUpdate,
    DateFromRequest,
    TransportReturn,
)
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


@transport_router.post("/get_by_date", response_model=list[TransportReturn])
async def get_transports_by_date(
    transport_service: Annotated[TransportService, Depends(transport_service)],
    payload: DateFromRequest,
):

    transport = await transport_service.get_transport_by_date(
        payload.date_in, payload.car_id
    )
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


@transport_router.get("/cars")
async def get_cars(
    car_service: Annotated[CarService, Depends(car_service)],
):
    cars = await car_service.get_cars()
    return cars
