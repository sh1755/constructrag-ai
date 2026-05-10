# ConstructRAG AI

AI-powered construction product intelligence system using Retrieval-Augmented Generation (RAG), LangChain, FAISS, HuggingFace embeddings, Ollama, and Streamlit for semantic search, supplier comparison, and material recommendation.

---

# Overview

ConstructRAG AI is an end-to-end AI-powered construction product intelligence assistant designed for semantic product retrieval, supplier comparison, compatibility analysis, and intelligent recommendation generation.

The system leverages LangChain, FAISS vector databases, HuggingFace transformer embeddings, Ollama local large language models, and Streamlit to create an efficient Retrieval-Augmented Generation (RAG) pipeline for construction product analysis.

---

# Features

- Semantic construction product search
- AI-powered supplier comparison
- Material compatibility analysis
- Cost and recommendation analysis
- Local LLM inference using Ollama
- Streamlit interactive web interface
- Retrieval-Augmented Generation (RAG) pipeline
- Intelligent product recommendation system

---

# Tech Stack

- Python
- LangChain
- FAISS Vector Database
- HuggingFace Embeddings
- Ollama
- Streamlit
- Pandas

---

# System Architecture

```text
CSV/PDF Product Data
        ↓
Data Ingestion Pipeline
        ↓
Text Embeddings
        ↓
FAISS Vector Database
        ↓
Retriever
        ↓
Ollama Local LLM
        ↓
Streamlit User Interface

# Project Structure

constructrag-ai/
│
├── app.py
├── ingest.py
├── rag_chain.py
├── requirements.txt
├── README.md
│
├── data/
│   └── products.csv
│
└── vectorstore/
