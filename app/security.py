from fastapi import Depends
from app.utils import verify_token
from app.config import settings
from app.models import User
from sqlalchemy.orm import Session
from app.database import get_db

# Dependency to get the current user from the token
def get_current_user(token: str = Depends()) -> User:
    payload = verify_token(token)
    user_id = payload.get("sub")
    db = next(get_db())
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise Exception("User not found")
    return user
