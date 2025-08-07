# backend/pinecone_utils.py

import os
from pinecone import Pinecone, ServerlessSpec
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.docstore.document import Document

# Load environment variables
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "knowledge-assistant")

# Initialize Pinecone client
pc = Pinecone(api_key=PINECONE_API_KEY)

# Create or get index
def init_pinecone():
    if PINECONE_INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=PINECONE_INDEX_NAME,
            dimension=1536,
            metric="cosine",
            spec=ServerlessSpec(cloud="aws", region=PINECONE_ENV)
        )
    return pc.Index(PINECONE_INDEX_NAME)

# Upload knowledge
def ingest_text_to_pinecone(text: str):
    index = init_pinecone()

    embeddings = OpenAIEmbeddings()
    docs = [Document(page_content=text)]

    vectorstore = PineconeVectorStore(
    index_name=PINECONE_INDEX_NAME,
    embedding=embeddings,
    text_key="text")
    
    vectorstore.add_documents(docs)

    return {"status": "uploaded", "text": text}

# Search documents
def search_similar_documents(query: str):
    index = init_pinecone()

    embeddings = OpenAIEmbeddings()
    vectorstore = PineconeVectorStore(
    index_name=PINECONE_INDEX_NAME,
    embedding=embeddings,
    text_key="text")
    results = vectorstore.similarity_search(query, k=3)
    return results
