from pydantic import BaseModel, Field, validator
from typing import Optional
import uuid
from enum import Enum
from datetime import datetime, datetime


class CoreModel(BaseModel):
    """
    Any common logic to be shared by all models goes here
    """

    pass


class Role(CoreModel):
    id: int
    name: str


class UserBase(CoreModel):
    username: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = False
    is_verified: bool | None = False
    is_superuser: bool | None = False
    refresh_token: str | None = None
    profile_id: int | None = None
    role: Role | None = None


class UserCreate(CoreModel):
    username: str
    password_hash: str
    role_id: int | None = None
    # email: str
    # phone: str


class UserCreated(CoreModel):
    id: int
    username: str


class UserUpdatePartial(UserBase):
    pass


class UserUpdate(CoreModel):
    username: str | None = None
    email: str | None = None
    phone: str | None = None
    is_active: bool | None = False
    is_verified: bool | None = False
    is_superuser: bool | None = False
    profile_id: int | None = None
    role_id: int | None = None


class User(UserBase):
    id: int


class OnlyUserId(UserBase):
    id: int
    created_on: datetime | None = None
    updated_at: datetime | None = None


# class Gender(Enum):
#     none: float = None
#     male: str = "m"
#     female: str = "f"


# class Education(Enum):
#     none: float = None
#     male = "high"
#     female = "low"


# class ResumeCreate(TunedModel):
#     url: str = Field(max_length=128)
#     source: str = Field(max_length=64, default="parsing")
#     content: str = Field()
#     available: Optional[bool]
#     content_limit: Optional[str]
#     content_gpt: Optional[str]
#     age: Optional[int]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     gender: Optional[Gender]
#     education: Optional[Education]
#     experience: Optional[str]
#     skills: Optional[str]
#     profession: Optional[str]
#     languages: Optional[str]
#     courses: Optional[str]
#     computer_skills: Optional[str]

#     class Config:
#         use_enum_values = True


class ShowResume(CoreModel):
    id: int
    url: str
    source: str
    content: str
    available: bool
    created_on: Optional[datetime]
    content_limit: Optional[str]
    content_gpt: Optional[str]
    age: Optional[int]
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[str]
    education: Optional[str]
    experience: Optional[str]
    skills: Optional[str]
    profession: Optional[str]
    languages: Optional[str]
    courses: Optional[str]
    computer_skills: Optional[str]


# class CreateShowResume(TunedModel):
#     id: int
#     url: str
#     source: str
#     content: str
#     available: bool
#     content_limit: Optional[str]
#     content_gpt: Optional[str]
#     age: Optional[int]
#     first_name: Optional[str]
#     last_name: Optional[str]
#     gender: Optional[str]
#     education: Optional[str]
#     experience: Optional[str]
#     skills: Optional[str]
#     profession: Optional[str]
#     languages: Optional[str]
#     courses: Optional[str]
#     computer_skills: Optional[str]

# @validator("content")
# def name_must_contain_space(cls, v):
#     return v[:100]


# class Resume_Get_Id(TunedModel):
#     id: Optional[int]


# class UpdateResume(TunedModel):
#     name: Optional[str]
#     url: Optional[str]
#     source: Optional[str]
#     content: Optional[str]
