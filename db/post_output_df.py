import os
import pandas as pd
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import google.generativeai as genai
import urllib.parse

# ---------- Load environment variables ----------
load_dotenv()

SUPABASE_DB_USER = os.getenv("SUPABASE_DB_USER")         
SUPABASE_DB_PASSWORD = urllib.parse.quote_plus(os.getenv("SUPABASE_DB_PASSWORD")) 
SUPABASE_DB_HOST = os.getenv("SUPABASE_DB_HOST")         
SUPABASE_DB_PORT = os.getenv("SUPABASE_DB_PORT", 5432)   
SUPABASE_DB_NAME = os.getenv("SUPABASE_DB_NAME")      


# ---------- Gemini setup ----------
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-flash-lite-latest") #("gemini-1.5-pro")

# ---------- Table Schema ----------
schema = """
Table: sales_pipeline
Columns:
- id (integer) 
- agent_name (text)
- rating (numeric)
- review_text (text)
- delivery_time_min (bigint)
- location (text)
- order_type (text)
- customer_feedback_type (text)
- price_range (text)
- discount_applied (text)
- product_availability (text)
- customer_service_rating (bigint)
- order_accuracy (text)
"""

# ---------- Step 1: Generate SQL ----------
def generate_sql(user_question):
    prompt = f"""
    You are a helpful AI assistant that converts English questions into SQL queries.
    Use ONLY the following table:

    {schema}

    The user asked: "{user_question}"

    Return a valid SQL SELECT query using only the columns in this schema.
    Always query the table 'sales_pipeline'.
    Limit results to 10 rows.
    """
    response = model.generate_content(prompt)
    sql_query = response.text.strip("```sql").strip("```").strip()
    return sql_query

# ---------- Step 2: Create SQLAlchemy engine ----------
def get_engine():
    # Correct SQLAlchemy connection string
    DATABASE_URL = f"postgresql+psycopg2://{SUPABASE_DB_USER}:{SUPABASE_DB_PASSWORD}@{SUPABASE_DB_HOST}:{SUPABASE_DB_PORT}/{SUPABASE_DB_NAME}"
    print(DATABASE_URL)
    engine = create_engine(DATABASE_URL)
    
    # Test connection
    try:
        with engine.connect() as conn:
            print("Connection successful!")
    except Exception as e:
        print(f"Failed to connect: {e}")
    
    return engine

# ---------- Step 3: Query Supabase and return DataFrame ----------
def query_supabase(sql_query, engine):
    try:
        with engine.connect() as connection:
            df = pd.read_sql(text(sql_query), con=connection)
        return df
    except Exception as e:
        print(f"Failed to execute query: {e}")
        return pd.DataFrame()

# ---------- Step 4: Usage ----------
engine = get_engine()

user_question = "Show me the reviews with ratings less than 3"
sql_query = generate_sql(user_question)
print("Generated SQL:\n", sql_query)

df = query_supabase(sql_query, engine)
print("\nQuery Results:")
print(df)
