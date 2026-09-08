"""
retriever.py - Stage 5a: Retriever
Takes a user query, computes its embedding, and retrieves the top-k most relevant chunks.
"""
from vector_store import query_vector_store
# Distance threshold: in cosine distance, lower than 0.40 means a good topic match
CONFIDENCE_THRESHOLD = 0.40
def retrieve_chunks(query: str, top_k: int = 3) -> list[dict]:
    """
    Searches the vector store for chunks matching the query string.
    Returns a formatted list of chunk dictionaries.
    """
    raw_results = query_vector_store(query_text=query, n_results=top_k)
    documents = raw_results["documents"][0]
    metadatas = raw_results["metadatas"][0]
    distances = raw_results["distances"][0]
    retrieved = []
    for doc_text, meta, dist in zip(documents, metadatas, distances):
        retrieved.append(
            {
                "text": doc_text,
                "source": meta["source"],
                "distance": dist,
                "is_confident": dist <= CONFIDENCE_THRESHOLD,
            }
        )
    return retrieved
if __name__ == "__main__":
    # Test with an in-domain question
    sample_query = "What are the requirements to set up VPN for remote work?"
    print(f"Testing retriever with query: \"{sample_query}\"\n")
    chunks = retrieve_chunks(sample_query, top_k=2)
    for i, c in enumerate(chunks, start=1):
        print(f"[{i}] Source: {c['source']} | Distance: {c['distance']:.4f} | Confident: {c['is_confident']}")
        print(f"    Snippet: {c['text'][:120]}...\n")