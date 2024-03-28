from typing import Any, Dict, Optional
from pydantic import BaseModel, Json


class BaseRole(BaseModel):
    name: str
    description: str | None = None
    permissions: Json[Any] | Optional[Dict]


class Role(BaseRole):
    id: int
