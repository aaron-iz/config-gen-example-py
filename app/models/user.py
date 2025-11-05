import datetime
from pydantic import BaseModel, Field
from uuid import UUID, uuid4

USERNAME_MIN_LENGTH = 3
PASSWORD_MIN_LENGTH = 8

class User(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    username: str = Field(..., min_length=USERNAME_MIN_LENGTH)
    password: str = Field(..., min_length=PASSWORD_MIN_LENGTH)
    full_name: str = Field(..., min_length=1)
    time_created: datetime = Field(default_factory=datetime.utcnow)
    last_password_changed: datetime = Field(default_factory=datetime.utcnow)
