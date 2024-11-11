from typing import List
from app.models import Course
from app.schemas import CourseCreate
from app.crud.course import create_course, get_courses, get_course_by_id, update_course, delete_course
from sqlalchemy.orm import Session
from app.exceptions import EntityNotFound, BadRequestError

# Service to handle course-related business logic

def add_course(course_data: CourseCreate, db: Session):
    course = create_course(db=db, course_data=course_data)
    if not course:
        raise BadRequestError(detail="Error creating course")
    return course

def list_courses(db: Session) -> List[Course]:
    return get_courses(db)

def get_course(course_id: int, db: Session) -> Course:
    course = get_course_by_id(db=db, course_id=course_id)
    if not course:
        raise EntityNotFound(entity="Course", entity_id=course_id)
    return course

def modify_course(course_id: int, course_data: CourseCreate, db: Session) -> Course:
    course = get_course_by_id(db=db, course_id=course_id)
    if not course:
        raise EntityNotFound(entity="Course", entity_id=course_id)
    return update_course(db=db, course_id=course_id, course_data=course_data)

def remove_course(course_id: int, db: Session):
    course = get_course_by_id(db=db, course_id=course_id)
    if not course:
        raise EntityNotFound(entity="Course", entity_id=course_id)
    delete_course(db=db, course_id=course_id)
