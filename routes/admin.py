from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud
from app.database import get_db

router = APIRouter()

@router.get("/users", response_model=list[schemas.User])
def get_all_users(db: Session = Depends(get_db)):
    return crud.get_all_users(db=db)

@router.get("/courses", response_model=list[schemas.Course])
def get_all_courses(db: Session = Depends(get_db)):
    return crud.get_all_courses(db=db)

@router.get("/enrollments", response_model=list[schemas.Enrollment])
def get_all_enrollments(db: Session = Depends(get_db)):
    return crud.get_all_enrollments(db=db)

@router.delete("/user/{user_id}")
def delete_user_by_admin(user_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_user_by_admin(db=db, user_id=user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "User deleted successfully"}

@router.delete("/course/{course_id}")
def delete_course_by_admin(course_id: int, db: Session = Depends(get_db)):
    try:
        crud.delete_course_by_admin(db=db, course_id=course_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return {"message": "Course deleted successfully"}
