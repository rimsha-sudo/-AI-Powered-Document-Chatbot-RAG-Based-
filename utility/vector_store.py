from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_text_splitters import CharacterTextSplitter

def split_documents(documents):
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    return splitter.create_documents(documents)

def create_faiss_vectorstore(docs):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.from_documents(documents=docs, embedding=embedding)

