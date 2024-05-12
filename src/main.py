from fastapi import FastAPI
from .database import engine,Base

#Import routers
from .routers import auth_router
from .models import user_model,project_model,blog_model


app = FastAPI()
@app.on_event("startup")
def create_database_tables():
    Base.metadata.create_all(bind = engine)


#Including Routers
app.include_router(auth_router.router)

@app.get("/api/health")
def health() -> dict[str, str]:
    return {"message": "App is up and running"}

