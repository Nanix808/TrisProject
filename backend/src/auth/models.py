from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

from src.models import Base


class User(Base):
    username: Mapped[str] = mapped_column(String(64), index=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(128), nullable=False)
    available: Mapped[bool] = Column(Boolean, default=True)
    is_active: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    is_superuser: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass
