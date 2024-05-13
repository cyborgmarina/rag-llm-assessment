from fastapi import FastAPI
from app.routers import retrieval, health

app = FastAPI()

app.include_router(health.router)
app.include_router(retrieval.router)
