from fastapi import Header, HTTPException, Security, Depends
from sqlalchemy.orm import Session
from models.user_model import User
from utils.jwt_token import verify_token
from .database import get_db

def get_current_user(token: str = Security(Header), db: Session = Depends(get_db)) -> User:
  credentials_exception = HTTPException(status_code=401,detail="Could not validate credentials",headers={"WWW-Authenticate":"Bearer"})
  user_id = verify_token(token,credentials_exception)
  user = db.query(User).filter(User.id==user_id).first()
  if user is None:
    raise credentials_exception
  return user