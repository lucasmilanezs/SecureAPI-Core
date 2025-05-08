from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.exceptions import AuthenticationError, ResourceNotFound
from src.schemas.auth import LoginRequest, TokenResponse
from src.services.auth import authenticate_user

def handle_login(credentials: LoginRequest, db: Session) -> TokenResponse:
    try:
        token = authenticate_user(
            username=credentials.username,
            password=credentials.password,
            db=db
        )
        return TokenResponse(access_token=token)
    except AuthenticationError as e:
        raise HTTPException(status_code=401, detail=str(e))
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
