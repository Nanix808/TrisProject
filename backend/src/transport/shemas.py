from datetime import datetime
from pydantic import BaseModel, validator

from .models import TypeTask, Status
from users.schemas import UserCreated


class TransportCreate(BaseModel):
    notice: str | None = None
    destination: str | None = None
    status: Status | None = Status.CREATED
    type_task: TypeTask | None = TypeTask.LOAD_UNLOAD
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


# class DateFromRequest(BaseModel):
#     date_in: str | None = None
#     car_id: int | None = None

#     @validator("date_in")
#     def parse_date_in(cls, v):
#         date_obj = datetime.strptime(v, "%m/%d/%Y")
#         return date_obj


class TransportReturn(BaseModel):
    id: int
    notice: str | None = None
    destination: str | None = None
    status: Status
    type_task: TypeTask | None = None
    contact: str | None = None
    car_id: int
    date_from: datetime
    date_to: datetime | None = None
    user: UserCreated | None = None
