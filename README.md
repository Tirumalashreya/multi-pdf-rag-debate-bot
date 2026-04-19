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

👉 Goal: Build a system that **understands, compares, and reasons across multiple documents** instead of just summarizing them.

---

# 🎯 Key Features

- 📄 Multi-PDF comparison (Paper A vs Paper B)
- 🔍 Smart semantic retrieval using embeddings
- ⚡ Hybrid retrieval (vector search + reranking)
- 🧠 Local LLM (Ollama - llama3, no API limits)
- 🧩 Chunk-level reasoning (fine-grained understanding)
- 🔎 Debug visibility (inspect retrieved chunks)
- ❌ Reduced hallucination via grounding in source text

---

# 🧠 System Architecture

## Step-by-step pipeline

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
LLM Reasoning (Ollama - llama3)  
↓  
Final Answer  

---

# 🔁 Full Flow Diagram

<img width="1440" height="1254" alt="image" src="https://github.com/user-attachments/assets/5770f5a5-e72b-4b1d-8197-fd16b507fb28" />
  

---

# 🔍 How It Works (Detailed)

## 1. Data Input
- Input: Two PDF documents
- Type: Unstructured text

---

## 2. Text Extraction
Tool used:
- PyPDFLoader

Converts:
PDF → Pages → Raw Text

---

## 3. Chunking

Parameters:
- chunk_size = 500
- chunk_overlap = 150

Why:
- Fits LLM input limits
- Improves retrieval precision
- Maintains context continuity

---

## 4. Embedding Generation

Model:
- all-MiniLM-L6-v2

Details:
- 384 dimensions
- Lightweight & fast
- Semantic understanding

---

## 5. Vector Storage

Database:
- ChromaDB

Collections:
- paper_a
- paper_b

---

## 6. Query Processing

Example:
"Which approach handles contradictions better?"

Converted to embedding.

---

## 7. Retrieval

### Step 1: Similarity Search
- Cosine similarity
- Top K = 10

### Step 2: Reranking
Model:
- cross-encoder/ms-marco-MiniLM-L-6-v2

Select:
- Top 5 most relevant chunks

---

## 8. Context Formation

Final Input:
- Top 5 chunks (Paper A)
- Top 5 chunks (Paper B)

---

## 9. LLM Reasoning

Model:
- Ollama (llama3)

Tasks:
- Compare papers
- Identify contradictions
- Stay grounded in context

---

## 10. Output

- Answer
- Differences
- Contradictions
- Confidence (approx)

---

# ⚙️ Tech Stack

## Core
- Python
- LangChain

## Retrieval
- ChromaDB
- Sentence Transformers

## Reranking
- Cross Encoder (MS MARCO)

## LLM
- Ollama (llama3)

## UI
- Gradio

---

# 📁 Repository Structure

multipdf/
│
├── app.py
├── ingest.py
├── retriever.py
├── responder.py
│
├── chroma_db/
│
├── README.md
├── UNDERSTANDING.md
│
└── requirements.txt

---

# ▶️ How to Run

## Install dependencies
pip install -r requirements.txt

## Install model
ollama pull llama3

## Run app
python app.py

---

# 🧪 Example Queries

- Compare contradiction detection methods
- Which model generalizes better?
- Why is clinical contradiction harder?

---

# ⚠️ Limitations

- Chunk misalignment
- Retrieval misses
- Context dependency

---

# 🚀 Future Improvements

- Semantic chunking
- Hybrid BM25 + vector search
- Chunk alignment (A vs B)
- Evaluation metrics

---

# 🎯 Key Insight

Strong RAG systems depend more on retrieval quality than the LLM itself.
