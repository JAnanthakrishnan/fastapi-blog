from sqlalchemy import Column,Integer,String,Boolean
from sqlalchemy.orm import relationship
from ..database import Base

class User(Base):
  __tablename__ = "users"

  id = Column(Integer, primary_key=True, index=True)
  username = Column(String,unique=True,index=True)
  email = Column(String,unique=True,index=True)
  hashed_password = Column(String,nullable=False)
  is_active = Column(Boolean,default=True)

  #Relationships
  projects = relationship("Project",back_populates="owner")
  blogs = relationship("Blog",back_populates="author")
