"""
vector_store.py - Stage 4: Vector Storage
Initializes persistent ChromaDB storage, stores chunk vectors, and handles vector searches.
"""
from importlib.metadata import metadata

import  chromadb
from chunking import chunk_documents
from embeddings import get_embedding
from ingestion import load_documents

CHROMA_PATH = "./chromadb"
COLLECTION_NAME = "it_support_doc"

def get_chroma_collections(
        collection_name:str=COLLECTION_NAME,db_path: str=CHROMA_PATH
):
    """
    Initializes a persistent ChromaDB client and gets or creates the collection.
    Uses cosine distance for similarity measurement.
    :param collection_name:
    :param db_path:
    :return:
    """
    client = chromadb.PersistentClient(path=db_path)
    collection = client.get_or_create_collection(
        name = collection_name,
        metadata={"hnsw:space":"cosine"},
    )
    return collection
def index_chunks(chunks: list[dict], collection=None):
    if collection is None:
        collection = get_chroma_collections()

    existing_count = collection.count()
    if existing_count >= len(chunks):
        print(f"[INFO] Collection already contains {existing_count} chunks. Skipping re-indexing.")
        return collection

    print(f"Indexing {len(chunks)} chunks into ChromaDB (this will take about 20-30 seconds)...")
    ids = []
    documents = []
    metadatas = []
    embeddings = []

    # 1. Collect ALL chunks first in the loop
    for chunk in chunks:
        ids.append(chunk["id"])
        documents.append(chunk["text"])
        metadatas.append({"source": chunk["source"], "chunk_index": chunk["chunk_index"]})
        embeddings.append(get_embedding(chunk["text"]))

    # 2. Add ALL chunks to ChromaDB outside the loop! (No indentation)
    collection.add(
        ids=ids,
        documents=documents,
        metadatas=metadatas,
        embeddings=embeddings,
    )
    print(f"[OK] Successfully indexed {collection.count()} chunks in ChromaDB!")
    return collection
def query_vector_store(query_text: str, n_results: int = 3, collection=None):
    """
    Embeds a query text and searches ChromaDB for the top-n most similar chunks.
    """
    if collection is None:
        collection = get_chroma_collections()
    query_vector = get_embedding(query_text)
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=n_results,
        include=["documents", "metadatas", "distances"],
    )
    return results
if __name__ == "__main__":
    # 1. Load documents and chunk them
    docs = load_documents()
    chunks = chunk_documents(docs)
    # 2. Index chunks into ChromaDB
    collection = get_chroma_collections()
    index_chunks(chunks, collection)
    print(f"\n[OK] Vector store is ready! Total items stored: {collection.count()}")