from typing import List
from app.models import Payment
from app.schemas import PaymentCreate
from app.crud.payment import create_payment, get_payments
from sqlalchemy.orm import Session
from app.exceptions import EntityNotFound
from app.utils import create_access_token

# Service to handle payment-related business logic

def process_payment(payment_data: PaymentCreate, db: Session, user) -> Payment:
    payment = create_payment(db=db, payment_data=payment_data, user=user)
    if not payment:
        raise EntityNotFound(entity="Payment", entity_id=payment_data.stripe_payment_id)
    return payment

def list_payments(db: Session, user_id: int) -> List[Payment]:
    return get_payments(db=db, user_id=user_id)
