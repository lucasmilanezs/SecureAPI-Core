from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import List

from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.utils.security import hash_password
from src.utils.db_helpers import get_role_by_name, get_object_by_id



def create_user(db: Session, user_data: UserCreate) -> User:
    existing = db.query(User).filter(User.username == user_data.username).first()
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    
    role = get_role_by_name(db, user_data.role)
    if not role:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid or non-existent role"
        )
    
    hashed = hash_password(user_data.password)
    new_user = User(
        username=user_data.username,
        password_hash=hashed,
        role_id=role.id
    )
    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Intregrity error. Invalid data."
        )
    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while creating user,"
        )

def get_user_list(db: Session) -> List[User]:
    return db.query(User).all()

def update_user(db: Session, user_id: int, new_user_data: UserUpdate) -> User:
    user = get_object_by_id(db, User, user_id)
    if new_user_data.username is not None:
        existing_user = db.query(User).filter(User.username == new_user_data.username).first()
        if existing_user and existing_user.id != user.id:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        user.username = new_user_data.username

    try:
        db.commit()
        db.refresh(user)
        return user
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Unexpected error while updating user"
        )