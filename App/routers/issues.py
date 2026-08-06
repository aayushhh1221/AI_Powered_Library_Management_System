from fastapi import FastAPI, Depends, HTTPException,Response,APIRouter
from sqlalchemy.orm import Session
from App.schemas import IssueCreate,BorrowHistoryResponse,OverdueResponse
from App.database import engine, get_db
from App.models import Issue,Student,Book,User
from datetime import datetime,timedelta,timezone,date
from App.security import get_current_user,admin_required

router=APIRouter(prefix="/issues",tags=["IssueBook"])


@router.post("/create")
def issue_book(issue:IssueCreate,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    stud=db.query(Student).filter(Student.id==issue.student_id).first()
    if stud is None:
         raise HTTPException(status_code=404,detail="Student Not Found with the given id")
    book=db.query(Book).filter(Book.id==issue.book_id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not Found with the given id")
    if(book.quantity==0):
        raise HTTPException(status_code=400,detail="Book is out of Stock")

    new_issue=Issue(
        student_id=issue.student_id,
        book_id=issue.book_id,
        issue_date=date.today()
    )
    book.quantity-=1
    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)
    return {"message":"Book Issued Successfully",
            "issue_id":new_issue.id}


#Return Book 

@router.post("/return")
def return_book(retbook:IssueCreate,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    stud=db.query(Student).filter(Student.id==retbook.student_id).first()
    if stud is None:
        raise HTTPException(status_code=404,detail="Student not Found")
    book=db.query(Book).filter(Book.id==retbook.book_id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not Found")
    issue=db.query(Issue).filter(Issue.status=="Issued").filter(Issue.student_id==retbook.student_id).filter(Issue.book_id==retbook.book_id).first()
    if issue is None:
        raise HTTPException(status_code=404,detail="Book not Issued")
    book.quantity+=1
    issue.status="Returned"
    issue.return_date=date.today()
    db.commit()
    db.refresh(issue)
    return{
        "message":"Book Returned Successfully",
        "book_quantity": book.quantity
    }

#fine

@router.get("/{id}/fine")
def fine_calculate(id:int,db:Session=Depends(get_db)):
    issue=db.query(Issue).filter(Issue.id==id).first()
    if issue is None:
        raise HTTPException(status_code=404,detail="Issue not found")
    student=db.query(Student).filter(Student.id==issue.student_id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student not found")
    book=db.query(Book).filter(Book.id==issue.book_id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not found")

    issue_date=issue.issue_date
    if issue.status=="Returned":
        return_date=issue.return_date
    else:
        return_date=date.today()
    days_borrowed=(return_date-issue_date).days

    if days_borrowed<=14:
        fine=0
    else:
        fine=(days_borrowed-14)*10

    return {
        "Days_Borrowed":days_borrowed,
        "Total_Fine: ": fine
    }

@router.get("/{id}/history",response_model=list[BorrowHistoryResponse])
def borrow_history(id:int,db:Session=Depends(get_db)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student not found")
    issues=db.query(Issue).filter(id==Issue.student_id).all()
    if not issues:
        raise HTTPException(status_code=404,detail="No Borrowing History")
    history=[]
    for issue in issues:
        book=db.query(Book).filter(Book.id==issue.book_id).first()
        history.append({
        "student_name":student.name,
        "book_title":book.title,
        "issue_date":issue.issue_date,
        "return_date":issue.return_date,
        "status":issue.status
                })
        
    return history

from datetime import date

@router.get("/overdue", response_model=list[OverdueResponse])
def overdue_books(db: Session = Depends(get_db),current_user: User = Depends(admin_required)):

    issues = db.query(Issue).filter(Issue.status == "Issued").all()

    overdue_list = []

    for issue in issues:

        days_borrowed = (date.today() - issue.issue_date).days

        if days_borrowed > 14:

            student = db.query(Student).filter(Student.id == issue.student_id).first()
            book = db.query(Book).filter(Book.id == issue.book_id).first()

            fine = (days_borrowed - 14) * 10

            overdue_list.append({
                "student_name": student.name,
                "book_title": book.title,
                "days_borrowed": days_borrowed,
                "days_overdue": days_borrowed - 14,
                "fine": fine
            })

    return overdue_list