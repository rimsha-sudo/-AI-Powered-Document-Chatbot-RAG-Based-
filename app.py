import os
from dotenv import load_dotenv
import streamlit as st

from langchain.document_loaders import PyPDFLoader
from utility.ragpipeline import build_rag_qa
from utility.vector_store import create_vector_store

load_dotenv()

# App UI
st.title("RAG Chatbot")
uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    # Load and split document
    loader = PyPDFLoader("temp.pdf")
    pages = loader.load()

    # Created vectorstore
    vectorstore = create_vector_store(pages)

    # NOW Build QA chain
    qa_chain = build_rag_qa(vectorstore)

    # User input
    user_query = st.text_input("Ask a question about the document:")

    if user_query:
        response = qa_chain.run(user_query)
        st.write(" Answer:", response)
