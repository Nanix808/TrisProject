from sqlalchemy import String, JSON
from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from sqlalchemy.orm import relationship


class Role(Base):
    name: Mapped[str | None] = mapped_column(String(40), unique=True)
    description: Mapped[str | None] = mapped_column(String(255))
    permissions: Mapped[list | None] = mapped_column(JSON, nullable=False)
    user: Mapped["User"] = relationship("User", back_populates="role")
