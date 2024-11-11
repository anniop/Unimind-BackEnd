from fastapi import FastAPI
from app.routes import auth, course, enrollment, payment, admin
from app.database import engine, Base

# Initialize FastAPI app
app = FastAPI()

# Initialize the database (Create tables)
Base.metadata.create_all(bind=engine)

# Include routes from different modules
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(course.router, prefix="/courses", tags=["Courses"])
app.include_router(enrollment.router, prefix="/enrollments", tags=["Enrollments"])
app.include_router(payment.router, prefix="/payments", tags=["Payments"])
app.include_router(admin.router, prefix="/admin", tags=["Admin"])

# Define a simple root endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to Unimind Cognition API!"}
