from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .models import Transport


class TransportRelationMixin:
    _transport_id_nullable: bool = False
    _transport_id_unique: bool = False
    _transport_back_populates: str | None = None

    @declared_attr
    def trransport_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("transport.id"),
            unique=cls._transport_id_unique,
            nullable=cls._transport_id_nullable,
        )

    @declared_attr
    def user(cls) -> Mapped["Transport"]:
        return relationship(
            "Transport",
            back_populates=cls._transport_back_populates,
        )
