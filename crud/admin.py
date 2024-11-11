from sqlalchemy.orm import Session
from app.models import User, Course, Enrollment
from app.exceptions import EntityNotFound, BadRequestError

# CRUD operations for admin-related functions

def get_all_users(db: Session):
    return db.query(User).all()

def get_all_courses(db: Session):
    return db.query(Course).all()

def get_all_enrollments(db: Session):
    return db.query(Enrollment).all()

def delete_user_by_admin(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    else:
        raise EntityNotFound(entity="User", entity_id=user_id)

def delete_course_by_admin(db: Session, course_id: int):
    course = db.query(Course).filter(Course.id == course_id).first()
    if course:
        db.delete(course)
        db.commit()
    else:
        raise EntityNotFound(entity="Course", entity_id=course_id)
