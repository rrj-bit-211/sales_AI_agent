# AI SQL Sales Query Assistant

Lightweight Streamlit app that converts natural-language sales queries into SQL, runs them against a Supabase/Postgres database, and returns results (with CSV download). The app uses a configurable LLM connector (Gemini API key in this repo) and an SQL agent to generate and execute queries.

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

## Project layout
- app_trigger.py — Streamlit entrypoint (active document)
- config/conf.py — Configuration loader (env keys and helpers)
- db/ai_sql_agent.py — AISQLAgent that generates SQL and executes queries
- requirements.txt — Python dependencies (if present)

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
Add a LICENSE file or change this section to reflect your chosen license.