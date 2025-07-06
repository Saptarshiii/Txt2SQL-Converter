from pydantic import BaseModel

# Request body schema for /generate-sql endpoint
# Accepts a natural language prompt from the user
class QueryRequest(BaseModel):
    prompt: str  # User's natural language query input

# Response body schema for /generate-sql endpoint
# Returns the generated SQL query string
class QueryResponse(BaseModel):
    sql: str  # SQL query generated from the prompt

# Request body schema for /execute-sql endpoint
# Accepts a raw SQL query to be executed on the database
class SQLExecuteRequest(BaseModel):
    query: str  # SQL query string to execute

# Response body schema for /execute-sql endpoint
# Returns the execution result as a list of dictionaries (records)
class SQLExecuteResponse(BaseModel):
    result: list  # List of row data returned from SQL execution
