import stripe
from app.config import settings
from app.models import Payment, User
from sqlalchemy.orm import Session
from app.schemas import PaymentCreate

# Configure Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

# Function to handle payment processing
def create_payment_stripe(payment_data: PaymentCreate, db: Session, user: User):
    try:
        # Create a payment intent on Stripe
        intent = stripe.PaymentIntent.create(
            amount=payment_data.amount * 100,  # Convert to cents
            currency='usd',
            payment_method=payment_data.stripe_payment_id,
            confirm=True
        )

        # Save payment details in the database
        payment = Payment(
            amount=payment_data.amount,
            stripe_payment_id=intent.id,
            user_id=user.id
        )
        db.add(payment)
        db.commit()
        db.refresh(payment)
        
        return payment
    except stripe.error.CardError as e:
        raise Exception(f"Payment failed: {e.error.message}")
    except Exception as e:
        raise Exception(f"Error during payment processing: {str(e)}")

# Function to fetch payment history of a user
def get_payment_history(db: Session, user_id: int):
    return db.query(Payment).filter(Payment.user_id == user_id).all()
