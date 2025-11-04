import os
import urllib.parse
from dotenv import load_dotenv

# Handles environment variables and setup.
class Config:
    def __init__(self):
        load_dotenv()
        self.db_user = os.getenv("SUPABASE_DB_USER")
        self.db_password = urllib.parse.quote_plus(os.getenv("SUPABASE_DB_PASSWORD"))
        self.db_host = os.getenv("SUPABASE_DB_HOST")
        self.db_port = os.getenv("SUPABASE_DB_PORT", 5432)
        self.db_name = os.getenv("SUPABASE_DB_NAME")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")

    def get_db_url(self):
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}@"
            f"{self.db_host}:{self.db_port}/{self.db_name}"
        )


