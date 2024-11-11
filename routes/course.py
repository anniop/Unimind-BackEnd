from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db
from app.exceptions import BadRequestError

router = APIRouter()

@router.post("/", response_model=schemas.Course)
def create_course(course_data: schemas.CourseCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_course(db=db, course_data=course_data)
    except BadRequestError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.Course])
def get_courses(db: Session = Depends(get_db)):
    return crud.get_courses(db=db)

@router.get("/{course_id}", response_model=schemas.Course)
def get_course(course_id: int, db: Session = Depends(get_db)):
    course = crud.get_course_by_id(db=db, course_id=course_id)
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course

@router.put("/{course_id}", response_model=schemas.Course)
def update_course(course_id: int, course_data: schemas.CourseCreate, db: Session = Depends(get_db)):
    try:
        return crud.update_course(db=db, course_id=course_id, course_data=course_data)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/{course_id}")
def delete_course(course_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_course(db=db, course_id=course_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Course deleted successfully"}
