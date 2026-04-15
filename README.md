# 📚 Multi-PDF RAG Debate Bot

A Retrieval-Augmented Generation (RAG) system that compares two research papers and provides grounded, explainable answers about differences, contradictions, and methodologies.

---

# 🚀 Project Idea

This project allows users to:

- Upload two research papers (PDFs)
- Ask a question about them
- Automatically retrieve relevant content
- Compare both papers
- Generate a grounded answer using a local LLM

👉 Goal: Build a system that **understands, compares, and reasons across multiple documents**.

---

# 🎯 Key Features

- 📄 Multi-PDF comparison (Paper A vs Paper B)
- 🔍 Smart semantic retrieval using embeddings
- ⚡ Hybrid retrieval (vector search + reranking)
- 🧠 Local LLM (Ollama - llama3, no API limits)
- 🧩 Chunk-level reasoning
- 🔎 Debug visibility (see retrieved chunks)
- ❌ Reduced hallucination via grounding

---

# 🧠 System Architecture

## Step-by-step pipeline

```text
PDFs
↓
Text Extraction
↓
Chunking
↓
Embedding Generation
↓
Vector Storage (ChromaDB)
↓
Query Input
↓
Query Embedding
↓
Similarity Search (Top-K)
↓
Reranking (Cross Encoder)
↓
Context Formation
↓
LLM (Ollama - llama3)
↓
Final Answer




** FLOW DIAGRAM **
PDF A          PDF B
↓              ↓
Chunking      Chunking
↓              ↓
Embeddings    Embeddings
↓              ↓
Chroma DB (paper_a, paper_b)
        ↓
       Query
        ↓
   Query Embedding
        ↓
   Similarity Search (Top 10)
        ↓
   Reranking (Top 5)
        ↓
   Context Formation
        ↓
   LLM (llama3 via Ollama)
        ↓
   Final Answer
