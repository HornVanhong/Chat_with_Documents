"""
compare_vectordb.py - Bonus Challenge: Vector Database Comparison
Compares ChromaDB vs. Qdrant on the same documents and queries:
- Setup complexity
- Data indexing & vector search
- Similarity scoring conventions (Cosine Distance vs Cosine Similarity)
"""

import time
from chunking import chunk_documents
from embeddings import get_embedding
from ingestion import load_documents
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams
from vector_store import get_chroma_collections, query_vector_store


def test_qdrant(chunks: list[dict], query_text: str, top_k: int = 3):
    """
    Sets up an in-memory Qdrant client, indexes chunks, and performs a search.
    """
    client = QdrantClient(":memory:")
    collection_name = "it_support_qdrant"

    # 1. Create collection in Qdrant
    client.create_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=768, distance=Distance.COSINE),
    )

    # 2. Insert points into Qdrant
    points = []
    for idx, chunk in enumerate(chunks):
        vector = get_embedding(chunk["text"])
        points.append(
            PointStruct(
                id=idx,
                vector=vector,
                payload={"source": chunk["source"], "text": chunk["text"]},
            )
        )

    t0 = time.time()
    client.upsert(collection_name=collection_name, points=points)
    index_time = time.time() - t0

    # 3. Query Qdrant
    query_vec = get_embedding(query_text)
    t1 = time.time()
    search_results = client.query_points(
        collection_name=collection_name,
        query=query_vec,
        limit=top_k,
    )
    query_time = time.time() - t1

    formatted_results = []
    for hit in search_results.points:
        formatted_results.append(
            {
                "source": hit.payload["source"],
                "score": hit.score,  # In Qdrant, Cosine is similarity (higher is better, 1.0 max)
                "text": hit.payload["text"],
            }
        )

    return formatted_results, index_time, query_time


def test_chroma(query_text: str, top_k: int = 3):
    """
    Queries the existing ChromaDB persistent collection.
    """
    t0 = time.time()
    raw = query_vector_store(query_text, n_results=top_k)
    query_time = time.time() - t0

    formatted_results = []
    for doc, meta, dist in zip(
        raw["documents"][0], raw["metadatas"][0], raw["distances"][0]
    ):
        formatted_results.append(
            {
                "source": meta["source"],
                "distance": dist,  # In ChromaDB, Cosine is distance (lower is better, 0.0 min)
                "text": doc,
            }
        )
    return formatted_results, query_time


def run_database_comparison():
    print("=" * 72)
    print("       BONUS CHALLENGE: VECTOR DATABASE COMPARISON (CHROMA VS QDRANT)")
    print("=" * 72)

    docs = load_documents()
    chunks = chunk_documents(docs)
    test_query = "What are the prerequisites and steps to configure VPN access?"

    print(f"Test Query: \"{test_query}\"")
    print(f"Documents Ingested: {len(docs)} | Chunks: {len(chunks)}\n")

    # 1. Query ChromaDB
    print("--- 1. ChromaDB (Persistent Client) ---")
    chroma_hits, chroma_time = test_chroma(test_query, top_k=3)
    print(f"Query search latency: {chroma_time*1000:.2f} ms")
    for idx, hit in enumerate(chroma_hits, start=1):
        print(f"  [{idx}] Source: {hit['source']} | Cosine Distance: {hit['distance']:.4f} (0=best)")

    # 2. Query Qdrant
    print("\n--- 2. Qdrant (Embedded Vector Client) ---")
    qdrant_hits, q_index_time, qdrant_time = test_qdrant(chunks, test_query, top_k=3)
    print(f"Indexing latency: {q_index_time:.2f}s | Query latency: {qdrant_time*1000:.2f} ms")
    for idx, hit in enumerate(qdrant_hits, start=1):
        print(f"  [{idx}] Source: {hit['source']} | Cosine Similarity: {hit['score']:.4f} (1=best)")

    # 3. Side-by-side analysis
    print("\n" + "=" * 72)
    print("                      COMPARISON SUMMARY")
    print("=" * 72)
    top_chroma = chroma_hits[0]["source"]
    top_qdrant = qdrant_hits[0]["source"]

    print(f"• Top Result ChromaDB : {top_chroma}")
    print(f"• Top Result Qdrant   : {top_qdrant}")
    print(f"• Agreement           : {'PERFECT MATCH (Both found the same document)' if top_chroma == top_qdrant else 'Differing'}")

    print("\n• Scoring Metrics:")
    print("  - ChromaDB reports Cosine DISTANCE (lower is better): dist = 1 - sim")
    print(f"    ChromaDB top distance: {chroma_hits[0]['distance']:.4f}")
    print("  - Qdrant reports Cosine SIMILARITY (higher is better): sim = 1 - dist")
    print(f"    Qdrant top similarity: {qdrant_hits[0]['score']:.4f}")
    converted_chroma_sim = 1.0 - chroma_hits[0]['distance']
    print(f"    Converted ChromaDB similarity: {converted_chroma_sim:.4f} (~ identical)")

    print("\n• Developer Experience & Setup Trade-offs:")
    print("  - ChromaDB: Extremely easy to set up for local Python scripts. Zero config,")
    print("    persistent directory out of the box (`./chroma_db`).")
    print("  - Qdrant: Fast, highly optimized in Rust. Offers rich metadata payload filtering,")
    print("    production clustering, and can run in embedded mode or client-server via Docker.")
    print("=" * 72)


if __name__ == "__main__":
    run_database_comparison()
