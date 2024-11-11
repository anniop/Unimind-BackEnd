from sqlalchemy.orm import Session
from app.models import Payment
from app.schemas import PaymentCreate
from sqlalchemy.exc import SQLAlchemyError
from app.exceptions import EntityNotFound, BadRequestError

# CRUD operations for payments

def create_payment(db: Session, payment_data: PaymentCreate, user):
    try:
        payment = Payment(**payment_data.dict(), user_id=user.id)
        db.add(payment)
        db.commit()
        db.refresh(payment)
        return payment
    except SQLAlchemyError as e:
        db.rollback()
        raise BadRequestError(detail="Error processing payment")

def get_payments(db: Session, user_id: int):
    return db.query(Payment).filter(Payment.user_id == user_id).all()

def get_payment_by_id(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()
