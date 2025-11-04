from pydantic import BaseModel, Field

USERNAME_MIN_LENGTH = 3
PASSWORD_MIN_LENGTH = 8

class User(BaseModel):
    username: str = Field(..., min_length=USERNAME_MIN_LENGTH)
    password: str = Field(..., min_length=PASSWORD_MIN_LENGTH)
