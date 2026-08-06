from fastapi import FastAPI
from App.database import engine,Base
from App.routers import books, students, issues, user, dashboard,ai

Base.metadata.create_all(bind=engine)

app=FastAPI()

app.include_router(books.router)
app.include_router(students.router)
app.include_router(issues.router)
app.include_router(user.router)
app.include_router(dashboard.router)
app.include_router(ai.router)

@app.get("/")
def hello():
    return{"message":"LIBRARY MANAGEMNT SYSTEM"}



