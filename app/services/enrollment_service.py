from typing import List
from app.models import Enrollment
from app.schemas import EnrollmentCreate
from app.crud.enrollment import create_enrollment, get_enrollments, get_enrollment_by_id, delete_enrollment
from sqlalchemy.orm import Session
from app.exceptions import EntityNotFound

# Service to handle enrollment-related business logic

def enroll_user(enrollment_data: EnrollmentCreate, db: Session) -> Enrollment:
    enrollment = create_enrollment(db=db, enrollment_data=enrollment_data)
    if not enrollment:
        raise EntityNotFound(entity="Enrollment", entity_id=enrollment_data.course_id)
    return enrollment

def list_enrollments(db: Session) -> List[Enrollment]:
    return get_enrollments(db)

def get_enrollment(enrollment_id: int, db: Session) -> Enrollment:
    enrollment = get_enrollment_by_id(db=db, enrollment_id=enrollment_id)
    if not enrollment:
        raise EntityNotFound(entity="Enrollment", entity_id=enrollment_id)
    return enrollment

def cancel_enrollment(enrollment_id: int, db: Session):
    enrollment = get_enrollment_by_id(db=db, enrollment_id=enrollment_id)
    if not enrollment:
        raise EntityNotFound(entity="Enrollment", entity_id=enrollment_id)
    delete_enrollment(db=db, enrollment_id=enrollment_id)
