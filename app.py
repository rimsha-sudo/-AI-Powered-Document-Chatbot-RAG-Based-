import streamlit as st
from utility.filehandler import read_files_from_folder
from utility.vector_store import create_vector_store
from utility.ragpipeline import build_rag_qa
from dotenv import load_dotenv
load_dotenv()

st.title("Doc RAG Chatbot")

folder_path = "data"
docs = read_files_from_folder(folder_path)
vectorstore = create_vector_store(docs)
qa_chain = build_rag_qa(vectorstore)

query = st.text_input("Ask a question about your documents:")

if query:
    with st.spinner("I am thinking give me time thanks"):
        response = qa_chain.run(query)
        st.success(response)
