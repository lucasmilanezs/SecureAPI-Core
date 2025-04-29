from pydantic import BaseModel, Field
from typing import Optional

class UserBase(BaseModel):
    username: str = Field(..., description="Unique username")
    role: str = Field(..., description="Users role identifier")

class UserCreate(UserBase):
    password_hash: str = Field(..., description="Hashed password of user")

class UserUpdate(BaseModel):
    id: int = Field(None, description="Unique user identifier")
    username: Optional[str] = Field(None, description="Unique username")
    password_hash: Optional[str] = Field(None, description="Hashed password of user")

class UserResponse(BaseModel):
    id: int
    username: str
    role: str

    class Config:
        orm_mode=True