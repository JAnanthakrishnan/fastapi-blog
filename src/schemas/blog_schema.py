from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
  title:str
  tags: Optional[List[str]] = None
  content: str
  cover_image: Optional[str] = None
  images: Optional[List[str]] = None
  created_at: Optional[str] = None

class BlogCreate(BlogBase):
  pass

class BlogUpdate(BlogBase):
  pass

class BlogDisplay(BlogBase):
  id:int
  user_id:int
  class Config:
    from_attributes = True