from fastapi import FastAPI, Depends, HTTPException,Response, APIRouter
from sqlalchemy.orm import Session
from App.schemas import StudentCreate
from App.database import engine, get_db
from App.models import Student,User
from App.security import get_current_user,oauth2_scheme,admin_required

router=APIRouter(prefix="/students",tags=["Student"])

@router.post("/add")
def create_students(student:StudentCreate,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    new_student=Student(
        name=student.name,
        email=student.email,
        branch=student.branch
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)

    return new_student

@router.get("")
def get_students(db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    students=db.query(Student).all()
    return students

@router.get("/{id}")
def get_student(id:int,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student not Found")
    return student

@router.put("/{id}")
def update_student(updated_student:StudentCreate,id:int,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student not Found")
    student.name=updated_student.name
    student.branch=updated_student.branch
    student.email=updated_student.email
    db.commit()
    db.refresh(student)
    return student

@router.delete("/{id}")
def delete_student(id:int,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    student=db.query(Student).filter(Student.id==id).first()
    if student is None:
        raise HTTPException(status_code=404,detail="Student not Found")
    db.delete(student)
    db.commit()
    return {"message":"Deleted Selected Student"}