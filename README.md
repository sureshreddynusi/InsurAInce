<<<<<<< HEAD
# InsurAInce
InsuranceAI is a Streamlit RAG app that lets users query insurance PDFs. It loads documents, creates persistent vector embeddings with FAISS, and uses Llama3 via Ollama to answer queries. Responses include source documents, which can be downloaded, enabling fast, accurate, and traceable insurance insights.
=======
RAG App (Ollama embeddings + ChatOllama) - Persistent FAISS vector DB + Streamlit
===============================================================================

What this package contains
--------------------------
- app.py                : Streamlit UI
- rag_pipeline.py       : RAG logic (persistent FAISS caching per-folder)
- utils.py              : helper functions
- requirements.txt
- README.md (this file)

Model configuration used (already set in the code)
--------------------------------------------------
Embedding: OllamaEmbeddings(model="nomic-embed-text")
LLM:       ChatOllama(model="llama3.2:latest")

Notes
-----
- This project assumes you have Ollama running locally (https://ollama.com) and that the specified
  models (nomic-embed-text and llama3.2:latest) are available locally via Ollama.
- No API keys are required for Ollama if it is running locally.
- Install dependencies in a virtualenv: `pip install -r requirements.txt`
- Run the Streamlit app: `streamlit run app.py`

Folder structure expected at runtime
------------------------------------
rag_app/
├── app.py
├── rag_pipeline.py
├── utils.py
├── data/               # create this and add per-category folders with PDFs
│    ├── insurance/
│    └── banking/
└── vector_store/       # created automatically

Important: Place your PDFs in data/<category>/ ; e.g. data/insurance/policy1.pdf

Security & Production
---------------------
- For production, consider locking model access on the Ollama side or deploying a secured Ollama instance.
- Consider using a managed vector DB (Chroma, Pinecone, Milvus) for scaling.

>>>>>>> b6cbcb3 (Initial commit — InsurAInce app)
