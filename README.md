
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
```
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
# Project Structure



# Installation

## Clone Repository

```bash
git clone https://github.com/sh1755/constructrag-ai.git
cd constructrag-ai
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Environment

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```
venv\Scripts\activate

pip install -r requirements.txt

ollama pull phi3


# Pull Model
ollama pull phi3
Run Model
ollama run phi3
Create Vector Database
python ingest.py
Run Application
streamlit run app.py
# Example Questions

Compare cement board and plasterboard for bathroom walls.
Which supplier offers the cheapest wall board?
Recommend products for humid environments.
Which construction material is water resistant?
Suggest compatible materials for tiles.
Compare insulation materials for thermal efficiency.

# Future Improvements

PDF document ingestion
Cloud deployment
Chat memory integration
Agentic RAG architecture
AWS/Azure deployment
Real-time supplier APIs
Multi-agent workflow automation
Construction material analytics dashboard

# Author
Sajjad Hussain

PhD Researcher in Artificial Intelligence
University of Brighton, United Kingdom


