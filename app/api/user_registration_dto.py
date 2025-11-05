from pydantic import BaseModel

class UserRegistrationDTO(BaseModel):
    username: str
    password: str
    full_name: str