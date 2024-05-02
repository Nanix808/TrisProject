import enum
import datetime
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import Base


from .mixins import TransportRelationMixin
from users.models import User
from users.mixins import UserRelationMixin
from sqlalchemy.dialects.postgresql import ENUM as PgEnum


class Status(enum.Enum):
    LOAD_UNLOAD = "загрузка/разгрузка"
    PICKUP = "забрать"
    SIGN = "подписать"


class Transport(Base):
    data: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    time: Mapped[str | None] = mapped_column(String(30))
    destination = mapped_column(String(150))
    notice: Mapped[str | None] = mapped_column(String(500))
    status: Mapped[Status] = mapped_column(nullable=True)
    contact: Mapped[str | None] = mapped_column(String(50))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
    car: Mapped["Car"] = relationship("Car", back_populates="transport")
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=False), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=False), server_default=func.now(), onupdate=func.now()
    )
    date_from: Mapped[DateTime] = mapped_column(DateTime(timezone=False), nullable=True)
    date_to: Mapped[DateTime] = mapped_column(DateTime(timezone=False), nullable=True)


class Car(Base):
    name: Mapped[str] = mapped_column(String(30))
    transport: Mapped["Transort"] = relationship("Transport", back_populates="car")
