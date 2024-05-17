from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class TransportCreate(BaseModel):
    notice: str | None = None
    destination: str | None = None
    status: str
    contact: str | None = None
    car_id: int
    date_from: datetime
    date_to: datetime | None = None

    # class Config:
    #     orm_mode = True


class TransportUpdate(BaseModel):
    notice: str | None = None
    destination: str | None = None
    status: str | None = None
    contact: str | None = None
    car_id: int | None = None
    date_from: datetime | None = None
    date_to: datetime | None = None

    # class Config:
    #     orm_mode = True
