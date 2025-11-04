
#encapsulates all Supabase connection and query logic

import pandas as pd
from sqlalchemy import create_engine,text

class DatabaseManager:
    def __init__(self,db_url:str):
        self.db_url=db_url
        self.engine=create_engine(db_url)
    
    def test_connection(self):
        try:
            with self.engine.connect() as conn:
                conn.execute(text("SELECT 1"))
            return True

        except Exception as e:
            return f"Query execution failed :{e}"

    def run_query(self,sql_query:str):
        try:
            with self.engine.connect() as conn:
                df=pd.read_sql(text(sql_query),conn)
            return df
        except Exception as e:
            raise RuntimeError(f"Query execution failed {e}")





