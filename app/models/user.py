from datetime import datetime, timezone
from typing import List
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

from app.models.role import Role


USERNAME_MIN_LENGTH = 3
PASSWORD_MIN_LENGTH = 8


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(..., min_length=USERNAME_MIN_LENGTH)
    password: str = Field(..., min_length=PASSWORD_MIN_LENGTH)
    full_name: str = Field(..., min_length=1)
    time_created: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    last_password_changed: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    roles: List[Role] = Field(default_factory=list)
