from fastapi import APIRouter, HTTPException
from app.models.schema import QueryRequest, QueryResponse, SQLExecuteRequest, SQLExecuteResponse
from app.services.sqlcoder import generate_sql
from app.services.db_executor import execute_sql

# Initialize the API router that will be included in the main FastAPI app
router = APIRouter()

@router.post("/generate-sql", response_model=QueryResponse)
def get_sql(query: QueryRequest):
    """
    Generate SQL from natural language prompt using the Cloudflare SQLCoder model.
    
    Args:
        query (QueryRequest): A Pydantic model containing a 'prompt' string.

    Returns:
        QueryResponse: A Pydantic model containing the generated SQL query string.
    """
    try:
        # Call the SQL generation service
        sql = generate_sql(query.prompt)
        return QueryResponse(sql=sql)
    except Exception as e:
        # Return a standardized 500 error if SQL generation fails
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/execute-sql", response_model=SQLExecuteResponse)
def run_sql(query: SQLExecuteRequest):
    """
    Execute a raw SQL query against the connected PostgreSQL database.

    Args:
        query (SQLExecuteRequest): A Pydantic model containing a SQL query string.

    Returns:
        SQLExecuteResponse: The execution result as a list of dictionaries (each representing a row).
    """
    try:
        # Call the SQL execution service
        result = execute_sql(query.query)
        return SQLExecuteResponse(result=result)
    except Exception as e:
        # Return a standardized 500 error if SQL execution fails
        raise HTTPException(status_code=500, detail=str(e))
