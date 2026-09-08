"""
pipeline.py - RAG Pipeline Orchestrator
Connects retriever and generator into one unified function: run_rag_pipeline(query).
"""
from generator import generate_answer
from retriever import CONFIDENCE_THRESHOLD, retrieve_chunks
def run_rag_pipeline(query: str, top_k: int = 3) -> dict:
    """
    Executes the complete RAG loop for a user query:
    1. Retrieves top-k chunks from ChromaDB.
    2. Checks if top match is within confidence threshold.
    3. Generates grounded answer via local LLM.
    Returns a dictionary with query, chunks, and answer.
    """
    # 1. Retrieve matching chunks
    chunks = retrieve_chunks(query=query, top_k=top_k)
    # 2. Check confidence threshold (Bonus challenge: avoid hallucination on out-of-domain questions)
    best_distance = chunks[0]["distance"] if chunks else 1.0
    is_confident = best_distance <= CONFIDENCE_THRESHOLD
    if not is_confident:
        # If no chunk is relevant to the topic
        return {
            "query": query,
            "chunks": chunks,
            "answer": "I could not find this in your documents.",
            "is_confident": False,
            "best_distance": best_distance,
        }
    # 3. Generate grounded answer
    answer = generate_answer(query=query, retrieved_chunks=chunks)
    return {
        "query": query,
        "chunks": chunks,
        "answer": answer,
        "is_confident": True,
        "best_distance": best_distance,
    }
if __name__ == "__main__":
    # Test end-to-end pipeline with an in-domain question
    test_q = "How do I schedule a conference call using Cisco Webex?"
    print(f"Running pipeline for query: '{test_q}'...\n")
    result = run_rag_pipeline(test_q)
    print("--- Retrieved Chunks ---")
    for c in result["chunks"]:
        print(f"  [{c['source']}] (distance={c['distance']:.4f})")
    print("\n--- Answer ---")
    print(result["answer"])