# 🧠 Deep Understanding of RAG System

---

# 1) Why RAG?

## Why not pure LLM?

Pure LLM:
- Uses internal knowledge
- Hallucinates
- Cannot access new documents

RAG:
- Retrieves real data
- Grounds answers in documents
- Reduces hallucination

👉 Key Idea:
LLM = reasoning  
Retriever = knowledge  

---

# 2) Data Collection

## Source
- Research papers (PDFs)

## Format
- Unstructured text

## Structured vs Unstructured

Structured:
- Tables, SQL

Unstructured:
- PDFs, paragraphs

We use **unstructured data**

---

## Data Cleaning

Steps:
- Remove extra spaces
- Remove headers/footers
- Normalize text

---

## Noise Removal

- Remove irrelevant symbols
- Remove broken lines
- Fix encoding issues

---

# 3) Chunking

## Why chunking?

- LLM has token limits
- Retrieval works better on smaller text

---

## Fixed vs Dynamic

Fixed:
- Same size chunks
- Simple

Dynamic:
- Based on meaning/sections
- Better but complex

---

## Large vs Small Chunks

Large:
- More context
- Less precision

Small:
- High precision
- Risk of losing context

---

## Chunk Overlapping

Why:
- Prevent context loss
- Maintain continuity

---

# 4) Embedding Generation

## What are embeddings?

Numerical representation of text:
Text → Vector

---

## Embeddings vs Tokens

Tokens:
- Used by LLM

Embeddings:
- Used for retrieval

---

## Model Used

- all-MiniLM-L6-v2

---

## Dimension

- 384

---

## Max Tokens

- ~256–512 tokens per chunk (safe range)

---

# 5) Vector DB / Storage

## What used?

- ChromaDB

---

## SQL vs NoSQL

SQL:
- Structured queries

NoSQL:
- Flexible storage

---

## Vector DB vs Normal DB

Normal DB:
- Exact match

Vector DB:
- Semantic similarity

---

## Indexing

Why:
- Faster search
- Efficient retrieval

---

# 6) Query Embedding

## Model used

Same:
- all-MiniLM-L6-v2

---

## Why same model?

- Ensures same vector space
- Accurate similarity matching

---

# 7) Retrieval

## Method

- Vector similarity search

---

## Similarity Search

- Cosine similarity

---

## Hybrid Method

Combination of:
- Vector search
- Reranking (Cross Encoder)

---

## Top-K

- Top 10 retrieved
- Top 5 reranked

---

# 8) Prompt Construction

## Template

- Include context
- Include question
- Ask for comparison

---

## Checks added

- Answer only from context
- Avoid hallucination
- Mention uncertainty if needed

---

# 9) LLM Generation

## Hallucination

Occurs when:
- No relevant context
- Weak retrieval

---

## Retrieval Failures

If context is weak:
- LLM guesses
- Output becomes unreliable

Solution:
- Improve retrieval quality

---

# 10) Evaluation

## Tools Used

- Manual inspection
- Debug chunk viewing

---

## Metrics

- Relevance of answer
- Groundedness
- Consistency

---

# 🎯 Final Insight

RAG is not about the LLM.

It is about:
- Retrieval quality
- Chunking strategy
- Embedding accuracy
