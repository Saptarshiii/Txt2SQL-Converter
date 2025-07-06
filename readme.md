# Text-to-SQL Generator (FastAPI + Cloudflare + PostgreSQL)

This project translates **natural language queries** into SQL using Cloudflare's hosted **SQLCoder-7B** model and optionally **executes** those queries on a local **PostgreSQL** database.

---

##  Features

-  Convert natural language questions to SQL queries using Cloudflare Workers AI: `@cf/defog/sqlcoder-7b-2`.
-  Query your PostgreSQL database directly via FastAPI.
-  Clean architecture with FastAPI best practices.
-  Schema-aware prompt engineering for accuracy.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Saptarshiii/Txt2SQL-Converter.git
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS:
venv\Scripts\activate     # For Windows:
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Replace the placeholders in `.env` file in the project root:

```
CLOUDFLARE_API_TOKEN=your_token
CLOUDFLARE_ACCOUNT_ID=your_account_id
DATABASE_URL=postgresql+psycopg2://username:password@localhost:5432/your_database
```

Replace:
- `your_token` = Cloudflare API Token (with Workers AI permission)
- `your_account_id` = Your Cloudflare account ID
- `username`, `password`, and `your_database` = Your PostgreSQL credentials

---
## 5. Running the App

### Start FastAPI server: (Execute from root directory \Txt2SQL-Converter)

```bash
uvicorn app.main:app --reload
```

Access docs at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

##  Folder Structure

```
txt2sql/
├── app/
│   ├── api/
│   │   └── endpoints.py           # FastAPI endpoints
│   ├── config.py                  # Loads .env variables
│   ├── main.py                    # App entrypoint
│   ├── models/
│   │   └── schema.py              # Pydantic schemas
│   ├── services/
│   │   ├── sqlcoder.py            # Cloudflare SQLCoder logic
│   │   └── db_executor.py         # PostgreSQL execution logic
│   └── utils/
│       ├── db_connect.py          # SQLAlchemy engine setup
│       └── db_schema.py           # Prompt-enhanced schema with column descriptions
├── database/
│   |── Table.sql                  # SQL file for creation of the assumed Database
│   |── Data.sql                   # SQL file for seeding dummy data in the database
│   └── schema.png                 # Visual representation of the schema of the database
├── requirements.txt
├── .env
└── README.md
```

---


##  Example Usage

### 1. Generate SQL

**POST** `/generate-sql`

#### Input:

```json
{
  "prompt": "list all employee name with their role "
}
```

#### Output:

```json
{
  "sql": " SELECT e.name, e.role FROM Employee e;"
}
```
#### Input:
```json
{
  "prompt": "name all the items that are supplied by the supplier who has made the most number of supplies"
}
```

#### Output:

```json
{
  "sql": " SELECT i.name, s.name AS supplier_name, COUNT(sb.supply_id) AS total_supplies FROM Items i JOIN Supplier_Billing sb ON i.item_id = sb.item_id JOIN Supplier s ON sb.supplier_id = s.supplier_id GROUP BY i.name, s.name ORDER BY total_supplies DESC LIMIT 1;"
}
```

---

### 2. Execute SQL

**POST** `/execute-sql`

#### Input:

```json
{
  "query": "SELECT name FROM Customer WHERE total_spent > 3000;"
}
```

#### Output:

```json
{
  "results": [
    {
      "name": "John Doe"
    },
    {
      "name": "Semanti"
    }
  ]
}
```

---
### Implemented Database Schema
![App Banner](database/schema.png)
##  Assumptions Made

- Cloudflare token has correct Workers AI permissions.
- The PostgreSQL database is hosted **locally** and accessible (for the second API to work).
- The schema is pre-loaded in SQLCoder's prompt for accuracy.
- Users have `psycopg2` installed for PostgreSQL interaction.

---


##  License

© 2025 Saptarshi Banik
