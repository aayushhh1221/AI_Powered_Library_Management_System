from sqlalchemy import Column, Integer, String, ForeignKey, Date
from App.database import Base

class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(100))
    author=Column(String(100))
    isbn=Column(String(100),unique=True)
    category=Column(String(100))
    quantity=Column(Integer)



class Student(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(100))
    email=Column(String(100),unique=True)
    branch=Column(String(50))



class Issue(Base):
    __tablename__="issue"
    id=Column(Integer,primary_key=True,index=True)
    student_id=Column(Integer,ForeignKey("students.id"))
    book_id=Column(Integer,ForeignKey("books.id"))
    issue_date=Column(Date)
    return_date=Column(Date)
    status=Column(String(20),default="Issued")

class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String(300),unique=True,nullable=False)
    hashed_password=Column(String(300),nullable=False) 
    role=Column(String(20),default="Student")
