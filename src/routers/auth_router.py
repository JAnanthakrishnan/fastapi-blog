from fastapi import APIRouter, HTTPException, status,Depends
from sqlalchemy import or_
from sqlalchemy.orm import Session
from ..models.user_model import User
from ..schemas.user_schema import UserCreate,UserDisplay,UserLogin
from ..utils.security import hash_password, verify_password
from ..utils.jwt_token import create_access_token
from ..database import get_db

router = APIRouter()

@router.post("/register",response_model=UserDisplay)
def register_user(user:UserCreate, db:Session=Depends(get_db)):
  db_user = db.query(User).filter(
    or_(User.email==user.email,User.username==user.username)
  ).first()
  # Check the results and respond accordingly
  if db_user:
    if db_user.email == user.email:
        raise HTTPException(status_code=400, detail="Email already registered")
    elif db_user.username == user.username:
        raise HTTPException(status_code=400, detail="Username already registered")

  hashed_password = hash_password(user.password)
  db_user = User(
              username = user.username,
              email = user.email,
              hashed_password = hashed_password,
              is_active = True)
  db.add(db_user)
  db.commit()
  db.refresh(db_user)
  return db_user

@router.post("/login")
def login_user(user:UserLogin, db:Session=Depends(get_db)):
  db_user = db.query(User).filter(User.username==user.username).first()
  if not db_user or not verify_password(user.password,db_user.hashed_password):
    raise HTTPException(status_code=400, detail = "Invalid Credentials")
  access_token = create_access_token(data={"sub": str(db_user.id)})
  return {"access_token":access_token, "token_type":"bearer"}