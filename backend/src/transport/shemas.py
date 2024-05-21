from datetime import datetime
from pydantic import BaseModel

from .models import TypeTask, Status


class TransportCreate(BaseModel):
    notice: str | None = None
    destination: str | None = None
    status: Status
    type_task: TypeTask
    contact: str | None = None
    car_id: int
    user_id: int
    date_from: datetime
    date_to: datetime | None = None


class TransportUpdate(BaseModel):
    notice: str | None = None
    destination: str | None = None
    type_task: TypeTask | None = None
    status: Status | None = None
    contact: str | None = None
    car_id: int | None = None
    user_id: int | None = None
    date_from: datetime | None = None
    date_to: datetime | None = None
