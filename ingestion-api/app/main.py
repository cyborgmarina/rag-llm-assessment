from fastapi import FastAPI
from app.routers import document, health

app = FastAPI()

app.include_router(health.router)
app.include_router(document.router)

