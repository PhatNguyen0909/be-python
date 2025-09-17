from fastapi import FastAPI
from core.db import Base, engine
from routers import user_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI User CRUD")

app.include_router(user_router.router)
