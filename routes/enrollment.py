from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.exceptions import EntityNotFound

router = APIRouter()

@router.post("/", response_model=schemas.Enrollment)
def create_enrollment(enrollment_data: schemas.EnrollmentCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_enrollment(db=db, enrollment_data=enrollment_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.Enrollment])
def get_enrollments(db: Session = Depends(get_db)):
    return crud.get_enrollments(db=db)

@router.get("/{enrollment_id}", response_model=schemas.Enrollment)
def get_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    enrollment = crud.get_enrollment_by_id(db=db, enrollment_id=enrollment_id)
    if not enrollment:
        raise HTTPException(status_code=404, detail="Enrollment not found")
    return enrollment

@router.delete("/{enrollment_id}")
def delete_enrollment(enrollment_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_enrollment(db=db, enrollment_id=enrollment_id)
    except EntityNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Enrollment deleted successfully"}
