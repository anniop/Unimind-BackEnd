from pydantic import BaseModel
from typing import List, Optional

# Pydantic model for Course
class CourseBase(BaseModel):
    title: str
    description: str
    price: int

class CourseCreate(CourseBase):
    pass

class Course(CourseBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic model for User (for registration and login)
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Pydantic model for Enrollment
class EnrollmentBase(BaseModel):
    course_id: int

class EnrollmentCreate(EnrollmentBase):
    pass

class Enrollment(EnrollmentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Pydantic model for Payment (just an example)
class PaymentBase(BaseModel):
    amount: int
    stripe_payment_id: str

class PaymentCreate(PaymentBase):
    pass

class Payment(PaymentBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
