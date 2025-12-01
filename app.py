import streamlit as st
from utils import list_folders, list_pdfs, ensure_dir
from rag_pipeline import load_or_create_vectorstore, generate_answer, embedding
import os

st.set_page_config(page_title="RAG App (Ollama)", layout="wide")
st.title("📄 InsurAInce")

# Ensure data & vector_store dirs exist
ensure_dir("data")
ensure_dir("vector_store")

# Select folder
folders = list_folders()
selected_folder = st.selectbox("Select document category:", folders)

if selected_folder:
    #pdf_files = list_pdfs(selected_folder)
    pdf_files = [
    os.path.join("data", selected_folder, f)
    for f in list_pdfs(selected_folder)
    ]

    if st.button("Load Documents"):
        st.session_state["vectorstore"] = load_or_create_vectorstore(pdf_files)
        st.session_state["messages"] = []
        st.success(f"Loaded {len(pdf_files)} PDFs!")
   
# Chat section
if "vectorstore" in st.session_state:
    for role, message in st.session_state["messages"]:
        if role == "user":
            st.markdown(f"**🧑 User:** {message}")
        else:
            st.markdown(f"**🤖 Assistant:** {message}")

    query = st.text_input("Ask your question:")

    if query:
        st.session_state["messages"].append(("user", query))

        answer, docs = generate_answer(
            query,
            st.session_state["vectorstore"]
            
        )

        st.session_state["messages"].append(("assistant", answer))

        st.subheader("Answer")
        st.write(answer)

        with st.expander("Sources (Click to view/download)"):
            for d in docs:
                pdf_path = d.metadata.get("source") if d.metadata else None
                file_name = pdf_path.split("/")[-1] if pdf_path else "Unknown"

                st.write(f"📄 **Source File:** {file_name}")
                st.write(d.page_content[:400] + "...")

                if pdf_path:
                    try:
                        with open(pdf_path, "rb") as f:
                            st.download_button(                                    label=f"⬇️ Download {file_name}",                                    data=f,                                    file_name=file_name,                                    mime="application/pdf"                                )
                    except Exception as e:
                        st.write(f"Could not add download button: {e}")

                st.markdown("---")
