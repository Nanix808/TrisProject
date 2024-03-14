from typing import Any, Dict, Optional
from pydantic import BaseModel, Json


class Role(BaseModel):
    id: int
    name: str
    description: str | None = None
    permissions: Json[Any] | Optional[Dict]
