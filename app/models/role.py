from __future__ import annotations
from pydantic import BaseModel, Field
from enum import Enum


class RoleType(str, Enum):
    PARTICIPANT = "participant"
    STAFF = "staff"
    ADMIN = "admin"
    # You can add more later (e.g., ADMIN, GUEST, etc.)


class Role(BaseModel):
    user_id: str = Field(..., description="Identifier of the user")
    resource: str = Field(..., description="Identifier of the resource the role applies to")
    role_type: RoleType = Field(..., description="Type of role assigned to the user for this resource")
