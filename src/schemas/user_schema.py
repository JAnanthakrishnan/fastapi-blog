from pydantic import BaseModel,EmailStr

class UserBase(BaseModel):
  username: str
  email:EmailStr

class UserLogin(BaseModel):
  username: str
  password: str

class UserCreate(UserBase):
  password: str

class UserDisplay(UserBase):
  id: int
  class Config:
    from_attributes = True