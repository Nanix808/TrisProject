from pydantic import BaseModel
from datetime import date, datetime, time, timedelta


class TransportCreate(BaseModel):
    data: str
    time: str
    notice: str | None = None
    destination: str | None = None
    status: str
    contact: str | None = None
    car_id: int
    date_from: datetime | None = None
    date_to: datetime | None = None
