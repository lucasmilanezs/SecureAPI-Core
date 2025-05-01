from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.controllers.user import handle_create_user, handle_get_user_list, handle_update_user
from src.database import get_db
from src.schemas.user import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return handle_create_user(user_data, db)

@router.get("/", response_model=List[UserResponse], status_code=200)
def get_users(db: Session = Depends(get_db)):
    return handle_get_user_list(db)

@router.put("/{user_id}", response_model=UserResponse, status_code=200)
def put_user(
    user_id: int,
    new_user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    return handle_update_user(db, user_id, new_user_data)