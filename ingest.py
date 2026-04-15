from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import os


def ingest_pdf(pdf_path, collection_name):

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(docs)

    for i, c in enumerate(chunks):
        c.metadata["chunk_id"] = i

    os.makedirs("./chroma_db", exist_ok=True)

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name=collection_name,
        persist_directory="./chroma_db"
    )