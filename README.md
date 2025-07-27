RAG Document Chatbot

This is a Retrieval-Augmented Generation (RAG) based document chatbot built using Streamlit, LangChain, and HuggingFace Transformers. You can upload a `.pdf`, `.docx`, or `.txt` file and ask questions based on its content. The app will return answers by retrieving relevant sections from the document and passing them to a language model.

- Upload documents in PDF, Word, or plain text format  
- Automatically reads and chunks your documents  
- Uses vector search to find the most relevant parts of the file  
- Uses a language model to generate responses based on the retrieved text  

## Requirements

Install the required packages using pip:

pip install -r requirements.txt


## File Structure


project/
app.py               # Main Streamlit app  
 filehandler.py       # Code for reading uploaded files  
 ragpipeline.py       # Logic for embeddings and QA  
 vector_store.py  
 temp/                # Temporary file storage  
 README.md            # Project description


## How to Run

Use the command below to start the app:


streamlit run app.py


After running, the app will open in your browser. Upload a file, type your question, and get an answer based on the uploaded content.

## Important

* The app uses GPT-2 as the default language model.
* By default, it uses FAISS for vector storage. This allows fast similarity search over document chunks.
* You must create a Hugging Face account and generate an API key at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens), then save it in a `.env` file like this:

HUGGINGFACEHUB_API_TOKEN=your_token_here



