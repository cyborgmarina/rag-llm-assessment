from fastapi import FastAPI
from app.routers import retrieval, health

app = FastAPI()

app.include_router(health.router, prefix="/api")
app.include_router(retrieval.router, prefix="/api")
