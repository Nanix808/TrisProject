# from utils import IUnitOfWork, UnitOfWork
from typing import Annotated

from fastapi import Depends

# UOWDep = Annotated[IUnitOfWork, Depends(UnitOfWork)]


from .repositories import TransportRepository
from .service import TransportService


def transport_service():
    return TransportService(TransportRepository)
