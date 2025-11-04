import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

#set keys

gemini_api_key=os.getenv("OPENAI_API_KEY")
# Set your Gemini API key
genai.configure(api_key=gemini_api_key)

# List all models
models = genai.list_models()
for m in models:
    print(m)
