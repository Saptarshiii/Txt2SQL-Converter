from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI(
    title="NLP-to-SQL Generator",
    version="1.0"
)

app.include_router(router, prefix="/api")
