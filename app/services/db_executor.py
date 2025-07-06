from app.utils.db_connect import SessionLocal
from sqlalchemy import text

def execute_sql(query: str):
    try:
        with SessionLocal() as session:
            result = session.execute(text(query))
            data = [dict(row._mapping) for row in result]
        return data
    except Exception as e:
        raise Exception(f"SQL Execution failed: {e}")
