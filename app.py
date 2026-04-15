import gradio as gr
import os
import shutil

from ingest import ingest_pdf
from retriever import retrieve
from responder import process


def run(query, pdf_a, pdf_b):

    # 🔄 Reset DB
    if os.path.exists("./chroma_db"):
        shutil.rmtree("./chroma_db")

    path_a = pdf_a.name
    path_b = pdf_b.name

    print("🔄 Ingesting PDFs...")

    # ✅ FIXED (with collection names)
    ingest_pdf(path_a, "paper_a")
    ingest_pdf(path_b, "paper_b")

    print("✅ Ingestion done")

    # 🔍 Retrieval
    chunks_a = retrieve(query, "paper_a")
    chunks_b = retrieve(query, "paper_b")

    # 🧠 Debug
    print("\n=== CHUNKS A ===")
    for c in chunks_a[:2]:
        print(c.page_content[:200])

    print("\n=== CHUNKS B ===")
    for c in chunks_b[:2]:
        print(c.page_content[:200])

    # 🤖 LLM
    result = process(query, chunks_a, chunks_b)

    return f"""
====================
FINAL RESULT
====================

{result['answer']}
"""


iface = gr.Interface(
    fn=run,
    inputs=[
        gr.Textbox(label="Query"),
        gr.File(label="Upload Paper A"),
        gr.File(label="Upload Paper B")
    ],
    outputs="text",
    title="Multi-PDF Debate Bot (Final)"
)

if __name__ == "__main__":
    iface.launch(server_name="127.0.0.1", server_port=7860)