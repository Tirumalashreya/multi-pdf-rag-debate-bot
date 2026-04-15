import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# List models
models = genai.list_models()

for model in models:
    print("MODEL:", model.name)
    print("SUPPORTED METHODS:", model.supported_generation_methods)
    print("-" * 50)