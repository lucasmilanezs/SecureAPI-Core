from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., description="Unique username")
    password: str = Field(..., description="Password of user")

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"