from pydantic import BaseModel

class QueryRequest(BaseModel):
    prompt: str

class QueryResponse(BaseModel):
    sql: str
    
class SQLExecuteRequest(BaseModel):
    query: str

class SQLExecuteResponse(BaseModel):
    result: list
