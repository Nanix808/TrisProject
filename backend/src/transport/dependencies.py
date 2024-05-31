# from utils import IUnitOfWork, UnitOfWork
from typing import Annotated

from fastapi import Depends

# UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]


from .repositories import TransportRepository, CarRepository
from .service import TransportService, CarService


def transport_service():
    return TransportService(TransportRepository)


def car_service():
    return CarService(CarRepository)
