from google import genai
import os
import json
from dotenv import load_dotenv

from langchain_community.llms import Ollama


llm = Ollama(model="llama3")


def detect_contradiction(docA, docB):
    prompt = f"""
You are an expert in contradiction detection.

Compare the two passages carefully.

Passage A:
{docA}

Passage B:
{docB}

Answer STRICTLY in this format:

Contradiction: Yes or No
Explanation: <short explanation>
Confidence: <0 to 1>
"""

    try:
        response = llm.invoke(prompt)
        return response
    except Exception as e:
        return f"❌ LLM FAILED: {str(e)}"