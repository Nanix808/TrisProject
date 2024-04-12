import enum
from sqlalchemy import String, ForeignKey
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
    car: Mapped["Car"] = relationship("Car", back_populates="transport")


class Car(TransportRelationMixin, Base):
    _transport_back_populates = "car"

    name: Mapped[str] = mapped_column(String(30))
