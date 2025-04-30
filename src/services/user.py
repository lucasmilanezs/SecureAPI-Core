from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

from src.models.user import User
from src.schemas.user import UserCreate, UserUpdate
from src.utils.security import hash_password
from src.utils.db_helpers import get_role_by_name


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

# def get_user_list(db: Session) -> User:
#     user_list=db.query(User)
#     return user_list
