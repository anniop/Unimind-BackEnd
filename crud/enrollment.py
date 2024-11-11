from sqlalchemy.orm import Session
from app.models import Enrollment
from app.schemas import EnrollmentCreate
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import EntityNotFound, BadRequestError

# CRUD operations for enrollments

def create_enrollment(db: Session, enrollment_data: EnrollmentCreate):
    try:
        enrollment = Enrollment(**enrollment_data.dict())
        db.add(enrollment)
        db.commit()
        db.refresh(enrollment)
        return enrollment
    except SQLAlchemyError as e:
        db.rollback()
        raise BadRequestError(detail="Error creating enrollment")

def get_enrollments(db: Session):
    return db.query(Enrollment).all()

def get_enrollment_by_id(db: Session, enrollment_id: int):
    return db.query(Enrollment).filter(Enrollment.id == enrollment_id).first()

def delete_enrollment(db: Session, enrollment_id: int):
    enrollment = get_enrollment_by_id(db, enrollment_id)
    if enrollment:
        db.delete(enrollment)
        db.commit()
    else:
        raise EntityNotFound(entity="Enrollment", entity_id=enrollment_id)
