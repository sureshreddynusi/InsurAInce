# rag_pipeline.py

from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os, hashlib
import PyPDF2

# ---------------- GLOBAL MODELS ----------------
embedding = OllamaEmbeddings(model="nomic-embed-text")
llm = ChatOllama(model="llama3.2:latest")


# ---------------- HELPERS ----------------
def pdf_fingerprint(pdf_paths):
    h = hashlib.md5()
    for pdf in sorted(pdf_paths):
        h.update(pdf.encode())
        h.update(str(os.path.getsize(pdf)).encode())
    return h.hexdigest()


def load_pdfs(pdf_paths):
    texts, metadatas = [], []
    for pdf in pdf_paths:
        reader = PyPDF2.PdfReader(pdf)
        full_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=200)
        chunks = splitter.split_text(full_text)

        for i, chunk in enumerate(chunks):
            texts.append(chunk)
            metadatas.append({"source": pdf, "chunk": i})
    return texts, metadatas


# ---------------- VECTOR STORE BUILDER ----------------
def create_vectorstore(pdf_paths, store_path):
    texts, metadatas = load_pdfs(pdf_paths)

    vectorstore = FAISS.from_texts(texts, embedding, metadatas=metadatas)
    vectorstore.save_local(store_path)
    return vectorstore


def load_or_create_vectorstore(pdf_paths):
    store_path = "vector_store/cache"
    os.makedirs(store_path, exist_ok=True)

    sig_file = os.path.join(store_path, "signature.txt")
    current_sig = pdf_fingerprint(pdf_paths)

    # If signature exists → load cached FAISS
    if os.path.exists(sig_file):
        with open(sig_file, "r") as f:
            saved_sig = f.read().strip()

        if saved_sig == current_sig:
            try:
                return FAISS.load_local(
                    store_path,
                    embeddings=embedding,
                    allow_dangerous_deserialization=True,
                )
            except Exception:
                pass  # fallback rebuild

    # Otherwise rebuild
    vectorstore = create_vectorstore(pdf_paths, store_path)

    with open(sig_file, "w") as f:
        f.write(current_sig)

    return vectorstore


# ---------------- ANSWER GENERATION ----------------
def generate_answer(query, vectorstore, embedding=None):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    docs = retriever.get_relevant_documents(query)

    context = "\n\n".join([d.page_content for d in docs])

    prompt = f"""
    You are an insurance domain expert. Use ONLY the context below to answer the query.

    ### Context:
    {context}

    ### Question:
    {query}

    Answer clearly and accurately.
    """

    response = llm.invoke(prompt)
    final_answer = response.content if hasattr(response, "content") else str(response)

    return final_answer, docs
