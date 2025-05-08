from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.auth import TokenResponse, LoginRequest
from src.controllers.auth import handle_login
from src.database import get_db

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    return handle_login(credentials, db)