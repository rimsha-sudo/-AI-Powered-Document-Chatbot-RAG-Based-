from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_chunks(text):
    splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=500,
        chunk_overlap=100,
        length_function=len
    )
    docs = splitter.create_documents([text])
    return docs

def create_vectorstore(docs):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    return vectorstore

def build_rag_qa(vectorstore):
 
    pipe = pipeline("text-generation", model="gpt2", max_new_tokens=200)
    local_llm = HuggingFacePipeline(pipeline=pipe)

    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template="""Use the following context to answer the question.
        Context:
        {context}

        Question: {question}
        Answer:"""

    )

    
    qa_chain = RetrievalQA.from_chain_type(
        llm=local_llm,
        retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
        chain_type="stuff", 
        chain_type_kwargs={"prompt": prompt_template}
    )

    return qa_chain
