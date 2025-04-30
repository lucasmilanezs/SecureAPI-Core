from sqlalchemy.orm import Session
from src.models.user import Role

def get_role_by_name(db: Session, role_name: str) -> Role | None:
    return db.query(Role).filter(Role.name == role_name).first()