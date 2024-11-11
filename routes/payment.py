from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from app.exceptions import BadRequestError
from app.services.payment_service import process_payment

router = APIRouter()

@router.post("/", response_model=schemas.Payment)
def create_payment(payment_data: schemas.PaymentCreate, db: Session = Depends(get_db)):
    try:
        # Process payment logic here (e.g., Stripe integration)
        user = crud.get_user_by_id(db, payment_data.user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return crud.create_payment(db=db, payment_data=payment_data, user=user)
    except BadRequestError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{payment_id}", response_model=schemas.Payment)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = crud.get_payment_by_id(db=db, payment_id=payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@router.get("/user/{user_id}", response_model=list[schemas.Payment])
def get_user_payments(user_id: int, db: Session = Depends(get_db)):
    return crud.get_payments(db=db, user_id=user_id)
