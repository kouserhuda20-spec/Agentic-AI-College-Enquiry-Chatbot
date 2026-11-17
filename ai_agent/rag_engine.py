
import os
from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / "data" / "college_data.txt"
CHROMA_PATH = BASE_DIR / "data" / "chroma_db"

COLLECTION_NAME = "bengaluru_colleges"

# Reuse the embedding model
_embeddings = None


def get_embeddings():
    global _embeddings

    if _embeddings is None:
        _embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return _embeddings


def get_vectorstore():

    if not DATA_PATH.exists():
        raise FileNotFoundError(
            f"College data file not found: {DATA_PATH}"
        )

    embeddings = get_embeddings()

    # Reuse existing persistent vector database
    if (CHROMA_PATH / "chroma.sqlite3").exists():
        return Chroma(
            collection_name=COLLECTION_NAME,
            persist_directory=str(CHROMA_PATH),
            embedding_function=embeddings
        )

    # Create vector database for the first time
    loader = TextLoader(str(DATA_PATH), encoding="utf-8")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    splits = splitter.split_documents(documents)

    if not splits:
        raise ValueError("No college information found in the text file.")

    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings,
        collection_name=COLLECTION_NAME,
        persist_directory=str(CHROMA_PATH)
    )

    print("College RAG vector database created successfully.")

    return vectorstore


def rag_query(user_query: str) -> str:

    try:
        vectorstore = get_vectorstore()

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": 4}
        )

        results = retriever.invoke(user_query)

        if not results:
            return "No relevant college information was found."

        return "\n\n".join(
            document.page_content for document in results
        )

    except Exception as e:
        print("RAG Error:", str(e))
        return f"RAG retrieval error: {str(e)}"
