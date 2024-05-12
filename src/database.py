from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:postgres@db:5432/postgres"

#Create a database engine
engine = create_engine(DATABASE_URL)

#SessionLocal class, which is a factory for producing new sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class for declarative class definitions
Base = declarative_base()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
