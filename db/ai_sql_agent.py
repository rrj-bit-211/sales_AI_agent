#Coordinates the interaction between LLM and database

from db.db_manager import DatabaseManager
from db.sql_generator import SQLGenerator

class AISQLAgent:
    def __init__(self,db_url:str,gemini_api_key:str):
        self.db=DatabaseManager(db_url)
        self.sql_gen=SQLGenerator(gemini_api_key)
        
    def ask(self,question:str):
        sql_query=self.sql_gen.generate_sql(question)
        try:
            df=self.db.run_query(sql_query)
            return sql_query,df
        except Exception as e:
            return sql_query,None,str(e)    
