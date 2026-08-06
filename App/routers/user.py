from fastapi import FastAPI, Depends, HTTPException,Response, APIRouter
from sqlalchemy.orm import Session
from App.schemas import UserCreate,UserLogin
from App.database import engine, get_db
from App.models import Issue,Student,Book,User
from App.security import hash_password,verify_password,password_hash,create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router=APIRouter(tags=["user"])


#register
@router.post("/register")
def register_user(user:UserCreate,db:Session=Depends(get_db)):
    get_email=db.query(User).filter(User.email==user.email).first()
    if get_email is not None:
        raise HTTPException(status_code=400,detail="Email already exists")
    new_user=User(
        email=user.email,
        hashed_password=hash_password(user.password),
        role="Student"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return{
        "message":"User Created Successfully"
    }


#login

@router.post("/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(),db:Session=Depends(get_db)):
    user_email=db.query(User).filter(User.email==form_data.username).first()
    if user_email is None:
        raise HTTPException(status_code=401,detail="Invalid Credentials")
    is_valid_password=verify_password(form_data.password,user_email.hashed_password)
    if not is_valid_password:
       raise HTTPException(status_code=401,detail="Invalid Credentials")

    token = create_access_token({
    "sub": user_email.email
})
    return{"access_token":token,
           "token_type":"bearer"}