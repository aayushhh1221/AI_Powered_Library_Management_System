from fastapi import FastAPI
from App.database import engine,Base
from App.routers import books, students, issues, user, dashboard,ai
from App.core.limiter import limiter 
from slowapi.errors import RateLimitExceeded
from slowapi import _rate_limit_exceeded_handler
Base.metadata.create_all(bind=engine)

app=FastAPI()

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

app.include_router(books.router)
app.include_router(students.router)
app.include_router(issues.router)
app.include_router(user.router)
app.include_router(dashboard.router)
app.include_router(ai.router)

@app.get("/")
def hello():
    return{"message":"LIBRARY MANAGEMNT SYSTEM"}



