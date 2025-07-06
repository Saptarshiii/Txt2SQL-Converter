from app.utils.db_connect import SessionLocal
from sqlalchemy import text

# Function to execute raw SQL query on the connected PostgreSQL database
def execute_sql(query: str):
    try:
        # Create a new session using the session factory
        with SessionLocal() as session:
            # Execute the raw SQL query (use text() to safely wrap the SQL string)
            result = session.execute(text(query))
            
            # Convert result rows into list of dictionaries for JSON serializability
            data = [dict(row._mapping) for row in result]
        
        # Return the final result as a list of dictionaries
        return data
    
    except Exception as e:
        # Raise a detailed exception in case SQL execution fails
        raise Exception(f"SQL Execution failed: {e}")
