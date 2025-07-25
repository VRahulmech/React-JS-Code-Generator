from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

VECTOR_DIR = "vectordb"

def load_pdfs(folder_path="books"):
    documents = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(folder_path, filename))
            documents.extend(loader.load())
    return documents

def setup_retriever():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if os.path.exists(VECTOR_DIR) and os.listdir(VECTOR_DIR):
        vectorstore = Chroma(
            persist_directory=VECTOR_DIR,
            embedding_function=embeddings
        )
    else:
        docs = load_pdfs("books")
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        split_docs = splitter.split_documents(docs)

        vectorstore = Chroma.from_documents(
            split_docs,
            embedding=embeddings,
            persist_directory=VECTOR_DIR
        )
        vectorstore.persist()

    return vectorstore.as_retriever()
