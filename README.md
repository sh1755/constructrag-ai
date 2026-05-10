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

Installation
Clone Repository
git clone https://github.com/sh1755/constructrag-ai.git
cd constructrag-ai
Create Virtual Environment
python -m venv venv
Activate Environment

Windows:

venv\Scripts\activate
Install Dependencies
pip install -r requirements.txt
Run Ollama

Install Ollama from:

https://ollama.com

Pull model:

ollama pull phi3

Run model:

ollama run phi3
Create Vector Database
python ingest.py
Run Application
streamlit run app.py
Example Questions
Compare cement board and plasterboard for bathroom walls.
Which supplier offers the cheapest wall board?
Recommend products for humid environments.
Which construction material is water resistant?
Suggest compatible materials for tiles.
Future Improvements
PDF document ingestion
Cloud deployment
Chat memory
Agentic RAG
AWS/Azure deployment
Real-time supplier APIs
Author

Sajjad Hussain

PhD Researcher in  Artificial Intelligence
University of Brighton, UK

