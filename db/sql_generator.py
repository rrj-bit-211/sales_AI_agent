import google.generativeai as genai


class SQLGenerator:
    def __init__(self,api_key:str):
        genai.configure(api_key=api_key)
        self.model=genai.GenerativeModel("gemini-flash-lite-latest")

        self.schema="""
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
        
    def generate_sql(self,question:str)->str:
        prompt = f"""
        You are an expert SQL assistant. Convert the question below into a safe PostgreSQL SELECT query.
        Use only this schema:

        {self.schema}

        Rules:
        - Only SELECT statements.
        - Always query from 'sales_pipeline'.
        - Limit 10 rows.
        - Ensure SQL syntax is valid.

        User question: "{question}"
        """
        response=self.model.generate_content(prompt)
        sql_query=response.text.strip("```sql").strip("```").strip() 

        return sql_query   
        