from datetime import datetime,timedelta
from jose import jwt,JWTError

SECRET_KEY = "ak_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data:dict)->str:
  to_encode = data.copy()
  expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
  to_encode.update({"exp":expire})
  encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
  return encoded_jwt

def verify_token(token:str,credentials_exception):
  try:
    payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    user_id: str = payload.get("sub")
    if user_id is None:
      raise credentials_exception
    return user_id
  except JWTError:
    raise credentials_exception