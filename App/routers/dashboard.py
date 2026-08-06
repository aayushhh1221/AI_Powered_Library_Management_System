from fastapi import FastAPI, Depends,APIRouter
from sqlalchemy.orm import Session
from App.database import engine, get_db
from App.models import Book,Student,Issue
from sqlalchemy import func
from App.schemas import AvailableBooks
from App.security import get_current_user,oauth2_scheme
from App.models  import User

router=APIRouter(prefix="/dashboard",tags=["Dashbboard"])

@router.get("")
def dashboard(db:Session=Depends(get_db)):
    total_books=db.query(Book).count()
    total_students=db.query(Student).count()
    issued_books=db.query(Issue).filter(Issue.status=="Issued").count()
    available_copies = (db.query(func.sum(Book.quantity)).filter(Book.quantity > 0).scalar()) or 0


    return{"Total_Books":total_books,
     "Total_Students":total_students,
     "Issued_Books":issued_books,
     "Available_Copies":available_copies
 }

@router.get("/available",response_model=list[AvailableBooks])
def get_all_books(db:Session=Depends(get_db), current_user:User = Depends(get_current_user)):
    books=db.query(Book).filter(Book.quantity>0).all()
    return [{
        "title":book.title,
        "author":book.author,
        "category":book.category,
        "available_copies":book.quantity
    }for book in books
    ]