from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import Userschemas
from database import get_db
from models.user import Usermodel
from hashing import Hash
import main


router = APIRouter(
    tags=["User"],
)

@router.post("/user", response_model=Userschemas, status_code=status.HTTP_201_CREATED)
def create_user(user: Userschemas, db: Session = Depends(get_db)):
    hashed_password = Hash(user.password)
    post_user = Usermodel(**user.dict())
    post_user.password = hashed_password
    db.add(post_user)
    db.commit()
    db.refresh(post_user)
    return post_user

@router.get("/getuser")
def get_user():
    main.cursor.execute("SELECT * FROM users")
    users = main.cursor.fetchall()
    return users
