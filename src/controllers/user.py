from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from typing import List

from src.schemas.user import UserCreate, UserResponse, UserUpdate
from src.services.user import create_user, get_user_list, update_user

def handle_create_user(user_data: UserCreate, db: Session) -> UserResponse:
    user = create_user(db, user_data)
    return UserResponse.model_validate(user)

def handle_get_user_list(db: Session) -> List[UserResponse]:
    users = get_user_list(db)
    return users

def handle_update_user(db: Session, user_id: int, new_user_data: UserUpdate) -> UserResponse:
    try:
        updated_user = update_user(db, user_id, new_user_data)  
        return UserResponse.model_validate(updated_user)
    except NoResultFound:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )