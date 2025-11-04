# AI SQL Sales Query Assistant

Lightweight Streamlit app that converts natural-language sales queries into SQL, runs them against a Supabase/Postgres database, and returns results (with CSV download). The app uses a configurable LLM for SQL generation.

## Features
- Natural-language → SQL generation
- Executes SQL on Supabase/Postgres
- Displays results in the browser and provides CSV download
- Simple Streamlit UI

## Quickstart (Windows)

1. Clone / open the repository in VS Code:
   - The active app entry is `app_trigger.py` at the project root.

2. Install dependencies (use a virtual environment):
```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1      # PowerShell
pip install -r requirements.txt
```
or (cmd)
```cmd
.venv\Scripts\activate.bat
pip install -r requirements.txt
```

3. Create environment variables
- Create a `.env` file or set system environment variables. Required keys (check `config/conf.py` for exact names):
  - `GEMINI_API_KEY` — API key for the LLM (Gemini or configured LLM)
  - `DATABASE_URL` or your Supabase/Postgres connection details (check `config/conf.py` for the exact variable name used by Config)

Example `.env`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
DATABASE_URL=postgresql://user:pass@host:5432/dbname
```

4. Run the app:
```powershell
streamlit run app_trigger.py
```
Open the provided localhost URL in your browser.

## Usage
- Enter a natural language question (e.g., "Show all reviews with ratings < 3 in Mumbai").
- Click "Run Query".
- The app shows the generated SQL, results table, and a "Download Results (CSV)" button.

## Architecture

Here’s a high-level architectural diagram for the AI SQL Sales Query Assistant:

```
+------------------------+
|   Streamlit Frontend   |
| (app_trigger.py)       |
+-----------+------------+
            |
            v
+------------------------+
|   AISQLAgent Module    |
| (db/ai_sql_agent.py)   |
+-----------+------------+
            |
            v
+------------------------+
|   LLM API (Gemini)     |<----> Environment/Config (config/conf.py)
+-----------+------------+
            |
            v
+------------------------+
|   Database Layer       |
| (Supabase/Postgres)    |
+------------------------+
```

- **Streamlit Frontend:** Entry point for user queries and displays results.
- **AISQLAgent:** Handles translation of natural language to SQL and executes queries.
- **LLM API (Gemini):** External model for generating SQL.
- **Config Loader:** Loads environment/configuration variables.
- **Database Layer:** Executes generated SQL on the database.

## Folder Structure

```
sales_AI_agent/
├── app_trigger.py        # Streamlit entrypoint (active document)
├── config/
│   └── conf.py           # Configuration loader (env keys and helpers)
├── db/
│   └── ai_sql_agent.py   # AISQLAgent that generates SQL and executes queries
├── requirements.txt      # Python dependencies (if present)
├── .env                  # Environment variables (not tracked in git)
├── README.md             # Project documentation
└── ...                   # Other files or folders as needed
```

## Troubleshooting
- DB connection error: confirm `DATABASE_URL` / Supabase credentials and network access.
- LLM errors: confirm `GEMINI_API_KEY` and rate limits.
- Missing dependencies: run `pip install -r requirements.txt`.

## Notes & Security
- Do not commit API keys or credentials. Use .env and gitignore.
- Validate and review generated SQL before running in production systems.

## Contributing
- Open issues or submit PRs. Keep changes minimal and include tests where appropriate.

## License

This project is licensed under a proprietary or restricted-use license.  
Usage, modification, and distribution may be subject to additional conditions or limitations set by the author.  
Contact the repository owner for details about specific usage permissions.

If you require a more permissive or fully open-source license, please open an issue for discussion.
