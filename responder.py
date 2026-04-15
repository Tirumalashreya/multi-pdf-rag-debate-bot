from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="llama3")


def process(query, chunks_a, chunks_b):

    context_a = "\n\n".join([c.page_content for c in chunks_a])
    context_b = "\n\n".join([c.page_content for c in chunks_b])

    prompt = f"""
You are comparing TWO research papers.

Focus ONLY on the SAME concept.

Compare:
- data type (real vs synthetic)
- method
- real-world applicability

If missing info → say "Not enough evidence"

--------------------

Paper A:
{context_a}

--------------------

Paper B:
{context_b}

--------------------

Question:
{query}

--------------------

Output format:

Answer:
<clear comparison>

Contradiction:
yes/no

Confidence:
0-1
"""

    try:
        res = llm.invoke(prompt)

        return {
            "answer": res
        }

    except Exception as e:
        print("❌ LLM ERROR:", e)

        return {
            "answer": "LLM failed — check Ollama or model"
        }