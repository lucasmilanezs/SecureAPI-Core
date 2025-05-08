from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from typing import List
import logging

from src.exceptions import AuthenticationError, ResourceNotFound
from src.models.user import User
from src.utils.db_helpers import get_object_by_any
from src.utils.security import password_decode, create_acess_token

logger = logging.getLogger(__name__)

def authenticate_user(username: str, password: str, db: Session) -> str:
    try:
        user = get_object_by_any(db, User, "username", username)
    except ResourceNotFound as e:
        logger.warning(f"Login failed: {str(e)}")
        raise AuthenticationError() from e

    if not user or not password_decode(password, user.password_hash):
        raise AuthenticationError()
    
    token = create_acess_token({
        "sub": str(user.id),
        "role": user.role.name
    })
    return token