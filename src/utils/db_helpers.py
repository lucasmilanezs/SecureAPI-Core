from sqlalchemy.orm import Session
from src.exceptions import ResourceNotFound
from src.models.user import Role, User
from typing import Any

def get_role_by_name(db: Session, role_name: str) -> Role | None:
    return db.query(Role).filter(Role.name == role_name).first()

def get_object_by_any(db: Session, model, field_name: str, field_value: Any ):
    if not hasattr(model, field_name):
        raise AttributeError(f"Model '{model.__name__}' has no attribute '{field_name}'")
    
    field = getattr(model, field_name)
    instance = db.query(model).filter(field == field_value).first()

    if not instance:
        raise ResourceNotFound(f"{model.__name__} with attribute {field_value}")
    return instance

