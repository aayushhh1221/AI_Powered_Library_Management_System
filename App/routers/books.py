from fastapi import FastAPI, Depends, HTTPException,Response,APIRouter
from sqlalchemy.orm import Session
from App.schemas import BookCreate
from App.database import engine, get_db
from App.models import Book,User
from App.security import get_current_user,oauth2_scheme,admin_required
from typing import Optional
from sqlalchemy import desc
from App.services.open_library_books import import_books

router=APIRouter(prefix="/books",tags=["Books"])

@router.post("/create")
def create_book(book:BookCreate,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    new_book=Book(
    title=book.title,
    author=book.author,
    category=book.category,
    quantity=book.quantity
)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book

@router.get("")
def get_books(
    skip: int = 0,
    limit: int = 10,
    search:Optional[str]="",
    sort_by:str="id",
    order:str="asc",
    category:Optional[str]=None,
    author:Optional[str]=None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):

    query=db.query(Book)
   
#sorting 

    allowed_fields=[
    "id",
    "title",
    "author",
    "isbn",
    "category",
    "quantity"]
    allowed_order=[
        "asc",
        "desc"
    ]
  
    if sort_by not in allowed_fields:
        raise HTTPException(status_code=400,detail="Invalid Sort Field")
    if order not in allowed_order:
         raise HTTPException(status_code=400,detail="Invalid order Field")
    field=getattr(Book,sort_by)
    if order=="asc":
        query=query.order_by(field)
    else:
        query=query.order_by(field.desc())
    #search
    query=query.filter(Book.title.contains(search))
      #filter
    if category is not None:
         query=query.filter(Book.category==category)
    if author is not None:
         query=query.filter(Book.author==author)
    total=query.count()
    #limit
    query=query.limit(limit)
    #skip
    query=query.offset(skip)
  

    books = query.all()
    
    return {
        "total": total,
        "skip": skip,
        "limit": limit,
        "books": books
    }


@router.get("/{id}")
def get_book(id:int,db:Session=Depends(get_db) ,current_user: User = Depends(get_current_user)):
    select_book=db.query(Book).filter(Book.id==id).first()
    if select_book is None:
        raise HTTPException(status_code=404,detail="Book not Found")
    else:
        return select_book


@router.put("/{id}")
def update_book(id:int,updated_book:BookCreate,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    book=db.query(Book).filter(Book.id==id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not Found")
    book.title=updated_book.title
    book.author=updated_book.author
    book.category=updated_book.category
    book.quantity=updated_book.quantity
    db.commit()
    db.refresh(book)
    return book

@router.delete("/{id}")
def delete_book(id:int,db:Session=Depends(get_db),current_user: User = Depends(admin_required)):
    book=db.query(Book).filter(Book.id==id).first()
    if book is None:
        raise HTTPException(status_code=404,detail="Book not Found")
    db.delete(book)
    db.commit()
    return {"message":"Book Deleted Successfully"}


@router.post("/import")
def import_book_api(
    q: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(admin_required)
):

    return import_books(q, db)