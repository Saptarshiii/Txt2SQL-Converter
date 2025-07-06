import requests
from app.config import CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID
from app.utils.db_schema import grocery_schema

# This function takes a natural language prompt and generates a PostgreSQL SQL query using SQLCoder hosted on Cloudflare Workers AI.
def generate_sql(nl_prompt: str) -> str:
    # Define the Cloudflare SQLCoder API endpoint
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/defog/sqlcoder-7b-2"
    
    # Set the authorization and content headers
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    # Craft the final prompt sent to the model, including the full schema and rules to guide better query generation
    final_prompt = f'''This is the schema for the following SQL coder task.

Rules:
- Prefer direct column access over joins when the column is already present.
- Avoid window functions unless the user explicitly asks.
- Use GROUP BY only when aggregation across multiple rows is needed.

{grocery_schema}

Write a PostgreSQL query to: {nl_prompt}'''

    # Make a POST request to Cloudflare Workers AI
    response = requests.post(url, headers=headers, json={"prompt": final_prompt})
    data = response.json()

    # If successful, extract and return the generated SQL query
    if response.status_code == 200 and data.get("success"):
        return data["result"]["response"]
    else:
        # Raise an exception with full error context if the request failed
        raise Exception(f"Error from Cloudflare SQLCoder: {data}")
