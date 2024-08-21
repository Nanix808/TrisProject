import enum
from sqlalchemy import String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models import Base

from users.mixins import UserRelationMixin


class TypeTask(str, enum.Enum):
    LOAD_UNLOAD = "Загрузка"
    PICKUP = "Забрать"
    SIGN = "Подписать"


class Status(str, enum.Enum):
    CREATED = "Создана"
    ACCEPTED = "Принята"
    COMPLETED = "Выполнена"
    CANCELED = "Отменена"


class Transport(UserRelationMixin, Base):
    _user_back_populates = "transport"

    destination = mapped_column(String(200))
    notice: Mapped[str | None] = mapped_column(String(500))
    type_task: Mapped[TypeTask] = mapped_column(nullable=True)
    status: Mapped[Status] = mapped_column(nullable=True)
    contact: Mapped[str | None] = mapped_column(String(200))
    car_id: Mapped[int] = mapped_column(ForeignKey("car.id"))
    car: Mapped["Car"] = relationship("Car", back_populates="transport")
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=False), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=False), server_default=func.now(), onupdate=func.now()
    )
    date_from: Mapped[DateTime] = mapped_column(DateTime(timezone=False))
    date_to: Mapped[DateTime] = mapped_column(
        DateTime(timezone=False),
        nullable=True,
        server_default=None,
    )


class Car(Base):
    name: Mapped[str] = mapped_column(String(30))
    transport: Mapped["Transport"] = relationship(
        "Transport", back_populates="car"
    )
