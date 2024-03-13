from sqlalchemy import Column, String, Boolean, DateTime, Text, JSON, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from models import Base
from .mixins import UserRelationMixin
from sqlalchemy.orm import relationship


class User(Base):
    username: Mapped[str] = mapped_column(String(64), index=True, unique=True)
    password_hash: Mapped[str] = mapped_column(String(128), nullable=False)
    email: Mapped[str] = mapped_column(String(128), nullable=True)
    phone: Mapped[str] = mapped_column(String(128), nullable=True)
    is_verified: Mapped[bool] = Column(Boolean, default=True)
    is_active: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    is_superuser: Mapped[bool] = Column(Boolean, nullable=False, default=False)
    created_on: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    profile: Mapped["Profile"] = relationship("Profile", back_populates="user")
    role_id: Mapped[int] = mapped_column(
        ForeignKey("role.id"), nullable=True
    )
    role: Mapped["Role"] = relationship("Role", back_populates="user")
    # role_id: Mapped[list["Role"]] = relationship(
    #     "Role", back_populates="user", nullable=False
    # )
    refresh_token: Mapped[str] = Column(Text)

    def set_password(self, password):
        pass

    def check_password(self, password):
        pass

    @property
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
        }

    # def __repr__(self):
    #     return f"{self.id}{self.username}>"


class Profile(UserRelationMixin, Base):
    _user_id_unique = True
    _user_back_populates = "profile"

    first_name: Mapped[str | None] = mapped_column(String(40))
    last_name: Mapped[str | None] = mapped_column(String(40))
    bio: Mapped[str | None]


# class Role(Base):
#     name: Mapped[str | None] = mapped_column(String(40))
#     description: Mapped[str | None] = mapped_column(String(255))
#     permissions: Mapped[list | None] = mapped_column(JSON, nullable=False)
#     user: Mapped["User"] = relationship("User", back_populates="role")
