from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound
from src.models.user import Role

def get_role_by_name(db: Session, role_name: str) -> Role | None:
    return db.query(Role).filter(Role.name == role_name).first()

def get_object_by_id(db: Session, model, object_id: int ):
    instance = db.query(model).filter(model.id == object_id).first()
    if not instance:
        raise NoResultFound(f"{model.__name__} with ID {object_id} not found")
    return instance