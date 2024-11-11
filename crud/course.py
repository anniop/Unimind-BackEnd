from sqlalchemy.orm import Session
from app.models import Course
from app.schemas import CourseCreate
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import EntityNotFound, BadRequestError

# CRUD operations for courses

def create_course(db: Session, course_data: CourseCreate):
    try:
        course = Course(**course_data.dict())
        db.add(course)
        db.commit()
        db.refresh(course)
        return course
    except SQLAlchemyError as e:
        db.rollback()
        raise BadRequestError(detail="Error creating course")

def get_courses(db: Session):
    return db.query(Course).all()

def get_course_by_id(db: Session, course_id: int):
    return db.query(Course).filter(Course.id == course_id).first()

def update_course(db: Session, course_id: int, course_data: CourseCreate):
    course = get_course_by_id(db, course_id)
    if course:
        for key, value in course_data.dict().items():
            setattr(course, key, value)
        db.commit()
        db.refresh(course)
        return course
    raise EntityNotFound(entity="Course", entity_id=course_id)

def delete_course(db: Session, course_id: int):
    course = get_course_by_id(db, course_id)
    if course:
        db.delete(course)
        db.commit()
    else:
        raise EntityNotFound(entity="Course", entity_id=course_id)
