from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,ARRAY
from sqlalchemy.orm import relationship
from ..database import Base

class Project(Base):
  __tablename__ = "projects"

  id = Column(Integer,primary_key=True,index=True)
  title = Column(String,nullable=False)
  description = Column(String,nullable=False)
  tags = Column(ARRAY(String),nullable=True)
  project_link = Column(String,nullable=True)
  source_code_link = Column(String,nullable=True)
  cover_image = Column(String,nullable=True)
  images = Column(ARRAY(String),nullable=True)

#Foreign Key assoiciation to User
  user_id = Column(Integer,ForeignKey("users.id"),nullable=False)

#Relationship to the User model
  owner = relationship("User",back_populates="projects")
