from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os


def load_react_and_mui_docs():
    # Load React docs
    react_loader = WebBaseLoader("https://react.dev/learn")
    react_docs = react_loader.load()

    # Load MUI docs (can pick more URLs if needed)
    mui_loader = WebBaseLoader("https://mui.com/material-ui/getting-started/overview/")
    mui_docs = mui_loader.load()

    print(f"Loaded {len(react_docs)} React docs and {len(mui_docs)} MUI docs.")

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    documents = splitter.split_documents(react_docs + mui_docs)

    # Embed using OpenAI
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Create FAISS vectorstore
    vectorstore = FAISS.from_documents(documents, embeddings)

    print("Vector store created successfully.")
    return vectorstore
