from google import genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))


def evaluate_answer(answer, chunks):

    context = "\n\n".join([c.page_content for c in chunks])

    prompt = f"""
Answer:
{answer}

Context:
{context}

Check:
1. Is answer grounded?
2. Any hallucination?

Return JSON:
{{
  "grounded": "yes/no",
  "hallucination": "yes/no",
  "score": 0-1,
  "reason": "..."
}}
"""

    res = client.models.generate_content(
        model="models/gemini-flash-latest",
        contents=prompt
    )

    try:
        return json.loads(res.text)
    except:
        return {"score": 0}