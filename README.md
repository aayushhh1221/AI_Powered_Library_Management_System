# AI Powered Library Management System

A practice project where I am building a Library Management System while learning backend development, Generative AI, RAG, and related technologies.

The project started as a basic library management API and is gradually being extended with AI-powered features.

> This is primarily a learning/practice project, so the architecture and features are still evolving.

## 🚀 Features

### Library Management
- Manage books
- Manage students/users
- Issue and return books
- Track library activity
- Dashboard APIs

### AI Features
- AI-based book recommendations
- Similar book suggestions
- Roadmap generation
- Intent-based request routing
- RAG-based question answering over uploaded books

### RAG
- PDF book ingestion
- Document loading
- Text splitting
- Gemini embeddings
- Chroma vector store
- Similarity-based retrieval
- LLM-generated answers using retrieved context

### Backend
- FastAPI
- SQLAlchemy
- MySQL
- Pydantic
- JWT authentication
- API rate limiting

## 🛠️ Tech Stack

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic / Pydantic Settings
- LangChain
- Google Gemini
- ChromaDB
- PyMuPDF
- SlowAPI

## 📁 Project Structure

```text
App/
├── config/
│   └── settings.py
├── core/
│   └── limiter.py
├── parsers/
├── rag/
│   ├── chain.py
│   ├── ingest.py
│   ├── loader.py
│   ├── splitter.py
│   └── vector_store.py
├── routers/
├── database.py
├── main.py
└── security.py

requirements.txt
.gitignore
