# constructrag-ai
AI-powered construction product intelligence system using RAG, LangChain, FAISS, HuggingFace embeddings, Ollama, and Streamlit for semantic search, supplier comparison, and material recommendation.

# ConstructRAG AI

AI-powered construction product intelligence assistant using Retrieval-Augmented Generation (RAG), semantic search, and local large language models.

---

## Overview

ConstructRAG AI is an end-to-end AI system designed for construction product recommendation, supplier comparison, compatibility analysis, and semantic product retrieval.

The system uses LangChain, FAISS vector databases, HuggingFace embeddings, Ollama local LLMs, and Streamlit to provide intelligent responses from structured construction product datasets.

---

## Features

- Semantic construction product search
- AI-powered supplier comparison
- Material compatibility analysis
- Cost and recommendation analysis
- Local LLM inference using Ollama
- Streamlit web interface
- Retrieval-Augmented Generation (RAG) pipeline

---

## Tech Stack

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Ollama
- Streamlit
- Pandas

---

## System Architecture

```text
CSV/PDF Product Data
        ↓
Data Ingestion
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
