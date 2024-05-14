from fastapi import FastAPI
from app.routers import document, health

app = FastAPI()

app.include_router(health.router, prefix="/api")
app.include_router(document.router, prefix="/api")
