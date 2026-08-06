from pydantic import BaseModel, EmailStr, Field
from typing import Annotated,Optional
from datetime import datetime,timezone,timedelta,date

class BookCreate(BaseModel):
    title:Annotated[str,Field(min_length=2,max_length=100)]
    author:Annotated[str,Field(min_length=2,max_length=50)]
    category:Annotated[str,Field(min_length=2,max_length=50)]
    quantity:Annotated[int,Field(gt=-1)]

class StudentCreate(BaseModel):
    name:Annotated[str,Field(min_length=3,max_length=50)]
    email:EmailStr
    branch:Annotated[str,Field(min_length=2,max_length=20)]

class IssueCreate(BaseModel):
    student_id:Annotated[int,Field(gt=0)]
    book_id:Annotated[int,Field(gt=0)]
   

class UserCreate(BaseModel):
    email:EmailStr
    password:str

class UserLogin(BaseModel):
    email:EmailStr
    password:str


class AvailableBooks(BaseModel):
    title:str
    author:str
    category:str
    available_copies:int  


class BorrowHistoryResponse(BaseModel):
    student_name: str
    book_title: str
    issue_date: date
    return_date: Optional[date]
    status: str

class OverdueResponse(BaseModel):
    student_name: str
    book_title: str
    days_borrowed: int
    days_overdue: int
    fine: int

