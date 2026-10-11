
import os

import chromadb
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Path to the persistent database created by PDF-RAG-Assistant.
RAG_DB_PATH = os.getenv("RAG_DB_PATH")

if not RAG_DB_PATH:
    raise RuntimeError(
        "Set RAG_DB_PATH to the PDF-RAG-Assistant chroma_db folder."
    )

try:
    chroma_client = chromadb.PersistentClient(path=RAG_DB_PATH)
    try:
        collection = chroma_client.get_collection(name="documents")
    except chromadb.errors.NotFoundError:
        collection = chroma_client.get_or_create_collection(name="documents")
except (FileNotFoundError, ValueError):
    collection = None


def search_documents(query: str) -> str:
    """Retrieve relevant context from the indexed documents."""
    if collection is None:
        return (
            "No relevant document content was found. "
            "The ChromaDB collection is not available yet."
        )

    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=query,
    )
    query_embedding = response.data[0].embedding

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3,
    )

    documents = results.get("documents", [[]])[0]

    if not documents:
        return "No relevant document content was found."

    return "\n\n".join(documents)
