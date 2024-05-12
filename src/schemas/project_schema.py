from pydantic import BaseModel
from typing import List,Optional

class ProjectBase(BaseModel):
  title:str
  description: Optional[str] = None
  tags: Optional[List[str]] = None
  project_link: Optional[str] = None
  source_code_link: Optional[str] = None
  cover_image: Optional[str] = None
  images: Optional[List[str]] = None

class ProjectCreate(ProjectBase):
  pass

class ProjectUpdate(ProjectBase):
  pass


class ProjectDisplay(ProjectBase):
  id:int
  user_id:int
  class Config:
    from_attributes = True