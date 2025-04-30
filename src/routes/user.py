from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.controllers.user import handle_create_user#, handle_get_user_list
from src.database import get_db
from src.schemas.user import UserCreate, UserResponse

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=201)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    return handle_create_user(user_data, db)


# @router.get("/", response_model=UserResponse, status_code=200)
# def get_user(db: Session = Depends(get_db)):
#     return handle_get_user_list