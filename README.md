<<<<<<< HEAD
<<<<<<< HEAD
# InsurAInce
InsuranceAI is a Streamlit RAG app that lets users query insurance PDFs. It loads documents, creates persistent vector embeddings with FAISS, and uses Llama3 via Ollama to answer queries. Responses include source documents, which can be downloaded, enabling fast, accurate, and traceable insurance insights.
=======
=======
>>>>>>> 6e4db04c1eaae2595f0d62ed0a617998fc2cc077
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
<<<<<<< HEAD
├── app.py
├── rag_pipeline.py
├── utils.py
├── data/               # create this and add per-category folders with PDFs
│    ├── insurance/
│    └── banking/
└── vector_store/       # created automatically
=======
  ├── app.py 
  ├── rag_pipeline.py 
  ├── utils.py 
  ├── data/                # create this and add per-category folders with PDFs
  │    ├── insurance/ 
  │    └── banking/ 
  └── vector_store/        # created automatically
>>>>>>> 6e4db04c1eaae2595f0d62ed0a617998fc2cc077

Important: Place your PDFs in data/<category>/ ; e.g. data/insurance/policy1.pdf

Security & Production
---------------------
- For production, consider locking model access on the Ollama side or deploying a secured Ollama instance.
- Consider using a managed vector DB (Chroma, Pinecone, Milvus) for scaling.

<<<<<<< HEAD
>>>>>>> b6cbcb3 (Initial commit — InsurAInce app)
=======

<img width="1912" height="961" alt="image" src="https://github.com/user-attachments/assets/79414fd2-19d3-4ea1-9b8f-ad108190a7c4" />
<img width="1720" height="427" alt="image" src="https://github.com/user-attachments/assets/cb6d84db-47c6-43ed-9672-4b67d6accbb7" />
<img width="1717" height="531" alt="image" src="https://github.com/user-attachments/assets/fa4f7025-242d-488e-b5eb-c942dcfbacd2" />
<img width="1911" height="966" alt="image" src="https://github.com/user-attachments/assets/02193553-8067-4fc2-9297-a73d6d72d726" />



>>>>>>> 6e4db04c1eaae2595f0d62ed0a617998fc2cc077
