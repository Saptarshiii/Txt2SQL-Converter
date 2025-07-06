from fastapi import APIRouter, HTTPException
from app.models.schema import QueryRequest, QueryResponse, SQLExecuteRequest, SQLExecuteResponse
from app.services.sqlcoder import generate_sql
from app.services.db_executor import execute_sql

router = APIRouter()

@router.post("/generate-sql", response_model=QueryResponse)
def get_sql(query: QueryRequest):
    try:
        sql = generate_sql(query.prompt)
        return QueryResponse(sql=sql)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/execute-sql", response_model=SQLExecuteResponse)
def run_sql(query: SQLExecuteRequest):
    try:
        result = execute_sql(query.query)
        return SQLExecuteResponse(result=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
