# AI Museum Guide

A modern, modular, N-tier architecture FastAPI application that leverages LLMs and vector search to answer questions about museum exhibits. The project is designed for maintainability, scalability, and ease of extension.

---

## 🚀 Project Description

**AI Museum Guide** is an intelligent API that allows users to ask questions about museum exhibits and receive contextually relevant answers. It uses retrieval-augmented generation (RAG) with a local language model and vector search over exhibit data. The project is structured in a clean N-tier architecture for separation of concerns and maintainability.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **FastAPI** – Web API framework
- **Uvicorn** – ASGI server
- **LangChain** – LLM orchestration and RAG
- **Transformers** – Model and tokenizer loading
- **Sentence-Transformers** – Embeddings
- **FAISS** – Vector search
- **Torch** – Model backend
- **chromadb** – (Optional, for future extensions)
- **wikipedia** – External tool integration
- **python-dotenv** – Environment variable management

---

## 📁 Project Directory Structure

```
app/
  api/
    endpoints.py           # FastAPI routes (Presentation Layer)
  services/
    qa_service.py          # Q&A orchestration (Business Logic Layer)
  data_layer/
    vectorstore.py         # Vectorstore/data loading (Data Access Layer)
  data/
    musuem_data.json       # Museum exhibit data
  docs/
    example_queries.md     # Example queries for users
  cache.py                 # Conversation memory (if used)
  guardrails.py            # Query safety checks
  wiki_tool.py             # Wikipedia search tool
  main.py                  # App entrypoint (includes router)
  rag_agent.py             # (Legacy, now a pointer)
  vectorstore.py           # (Legacy, now a pointer)
requirements.txt           # Python dependencies
Dockerfile                 # Containerization
README.md                  # Project documentation
```

---

## ✨ Features

- **N-tier architecture** for clean separation of concerns
- **/ask** endpoint for natural language Q&A over museum data
- **/health** endpoint for health checks and monitoring
- **Retrieval-Augmented Generation (RAG)** using local models
- **Vector search** over exhibit descriptions
- **Guardrails** for query safety
- **Easily extensible** with new endpoints, data, or models
- **Example queries** provided in `app/docs/example_queries.md`

---

## ⚡ Quickstart

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-museum-guide
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
uvicorn app.main:app --reload
```

### 4. Access the API

- Interactive docs: [http://localhost:8000/docs](http://localhost:8000/docs)
- Health check: [http://localhost:8000/health](http://localhost:8000/health)
- Ask a question:
  - `POST /ask` with JSON body: `{"question": "Tell me about the Mona Lisa."}`

---

## 🧠 Example Queries

See `app/docs/example_queries.md` for sample questions you can ask.

---

## 🏗️ Extending the Project

- **Add new endpoints:** Create new files in `app/api/` and register routers in `main.py`.
- **Add new business logic:** Place service code in `app/services/`.
- **Add new data sources or models:** Place data access code in `app/data_layer/`.
- **Add more exhibit data:** Update `app/data/musuem_data.json`.

---

## 📝 License

MIT (or your chosen license)

---

## 🤝 Contributing

Pull requests and issues are welcome! Please open an issue to discuss your ideas or report bugs.
