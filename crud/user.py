from sqlalchemy.orm import Session
from app.models import User
from app.schemas import UserCreate, UserUpdate
from app.security import hash_password
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import EntityNotFound, BadRequestError

# CRUD operations for users

def create_user(db: Session, user_data: UserCreate):
    try:
        hashed_password = hash_password(user_data.password)
        user = User(**user_data.dict(), password=hashed_password)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except SQLAlchemyError as e:
        db.rollback()
        raise BadRequestError(detail="Error creating user")

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user(db: Session, user_id: int, user_data: UserUpdate):
    user = get_user_by_id(db, user_id)
    if user:
        for key, value in user_data.dict().items():
            setattr(user, key, value)
        db.commit()
        db.refresh(user)
        return user
    raise EntityNotFound(entity="User", entity_id=user_id)

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    else:
        raise EntityNotFound(entity="User", entity_id=user_id)
