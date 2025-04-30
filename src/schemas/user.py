from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., description="Unique username")
    role: str = Field(..., description="Users role identifier")

class UserCreate(UserBase):
    password: str = Field(..., description="Password of user", repr=False)

class UserUpdate(BaseModel):
    id: int = Field(None, description="Unique user identifier")
    username: Optional[str] = Field(None, description="Unique username")

class RoleResponse(BaseModel):
    id: int
    name: str

    model_config = ConfigDict(from_attributes=True)

class UserResponse(BaseModel):
    id: int
    username: str
    role: RoleResponse

    model_config = ConfigDict(from_attributes=True)