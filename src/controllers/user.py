from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.schemas.user import UserCreate, UserResponse
from src.services.user import create_user# get_user_list

def handle_create_user(user_data: UserCreate, db: Session) -> UserResponse:
    user = create_user(db, user_data)
    return UserResponse.model_validate(user)

# def handle_get_user_list(db: Session) -> UserResponse:
#     user = get_user_list()
#     return UserResponse.model_validate(user)