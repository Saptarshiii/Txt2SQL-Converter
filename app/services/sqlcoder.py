import requests
from app.config import CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID
from app.utils.db_schema import grocery_schema

def generate_sql(nl_prompt: str) -> str:
    url = f"https://api.cloudflare.com/client/v4/accounts/{CLOUDFLARE_ACCOUNT_ID}/ai/run/@cf/defog/sqlcoder-7b-2"
    
    headers = {
        "Authorization": f"Bearer {CLOUDFLARE_API_TOKEN}",
        "Content-Type": "application/json"
    }

    final_prompt = f'''This is the schema for a the following sql coder task 
    Rules:
- Prefer direct column access over joins when the column is already present.
- Avoid window functions unless the user explicitly asks.
- Use GROUP BY only when aggregation across multiple rows is needed.
{grocery_schema}\n\nWrite an postgreSQL query to: {nl_prompt}'''

    response = requests.post(url, headers=headers, json={"prompt": final_prompt})
    data = response.json()

    if response.status_code == 200 and data.get("success"):
        return data["result"]["response"]
    else:
        raise Exception(f"Error from Cloudflare SQLCoder: {data}")
