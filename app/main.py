from fastapi import FastAPI
from app.api.endpoints import router

# Create a FastAPI application instance
app = FastAPI(
    title="NLP-to-SQL Generator",  # API documentation title
    version="1.0"                  # API version
)

# Include API routes from the endpoints module under the /api prefix
app.include_router(router, prefix="/api")
