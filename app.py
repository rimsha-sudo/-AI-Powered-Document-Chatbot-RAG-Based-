import streamlit as st
from utility.filehandler import read_file
from utility.ragpipeline import create_chunks, create_vectorstore, build_rag_qa
import os

st.set_page_config(page_title="RAG Chatbot", layout="centered")
st.title("Document CHATBOT")

uploaded_file = st.file_uploader("Upload a document", type=["pdf", "docx", "txt"])

if uploaded_file:
    os.makedirs("temp", exist_ok=True)
    file_path = f"temp/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    try:
        text = read_file(file_path)
        st.success("File successfully read.")

        docs = create_chunks(text)
        vectorstore = create_vectorstore(docs)
        qa_chain = build_rag_qa(vectorstore)

        st.session_state.qa_chain = qa_chain
    except Exception as e:
        st.error(f"Error: {e}")

if "qa_chain" in st.session_state:
    query = st.text_input("Ask a question about the document:")

    if query:
        with st.spinner("Generating answer"):
            response = st.session_state.qa_chain.run(query)
            st.write("Answer:", response)
