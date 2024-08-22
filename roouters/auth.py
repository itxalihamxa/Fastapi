from http.client import HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import Userschemas, User
from database import get_db
from models.user import Usermodel
from hashing import verify
from Oauth2 import create_access_token


router = APIRouter(
    tags=["Authentication"],
)


@router.post("/login")
def login(login:OAuth2PasswordRequestForm= Depends(), db: Session = Depends(get_db)):
    user = db.query(Usermodel).filter(Usermodel.email == login.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email or password incorrect")
    if not verify(login.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Email or password incorrect")

    access_token = create_access_token(data={'user_name':login.username})

    return {"access_token": access_token, "token_type": "bearer"}

