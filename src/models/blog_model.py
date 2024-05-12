from sqlalchemy import Column,Integer,String,Boolean,ForeignKey,ARRAY,DateTime
from sqlalchemy.orm import relationship
from ..database import Base

class Blog(Base):
  __tablename__ = "blogs"

  id = Column(Integer,primary_key=True,index=True)
  title = Column(String,nullable=False)
  tags = Column(ARRAY(String),nullable=True)
  content = Column(String,nullable=False) #Markdown
  cover_image = Column(String,nullable=True) #URL to the cover image
  images = Column(ARRAY(String),nullable=True) #Array of image URLs
  created_at = Column(DateTime,nullable=False)

  #Foreign Key assoiciation to User
  user_id = Column(Integer,ForeignKey("users.id"),nullable=False)

  #Relationship to the User model
  author = relationship("User",back_populates="blogs")