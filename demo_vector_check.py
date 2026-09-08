"""
demo_vector_check.py - Step 4 Verification
Standalone script to verify that vector database storage and search work correctly.
"""
from vector_store import query_vector_store
def run_standalone_check():
    # Test query from one of our IT SOP documents
    test_query = "How do I reset my forgotten PIN on a company device?"
    print("=" * 65)
    print("           STEP 4: STANDALONE VECTOR STORE CHECK")
    print("=" * 65)
    print(f"Query: \"{test_query}\"\n")
    print("Searching ChromaDB for top 3 matching chunks...\n")
    results = query_vector_store(test_query, n_results=3)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]
    distances = results["distances"][0]
    for rank, (doc, meta, dist) in enumerate(
        zip(documents, metadatas, distances), start=1
    ):
        print(f"--- Result #{rank} ---")
        print(f"  Source Document : {meta['source']}")
        print(f"  Cosine Distance : {dist:.4f} (Lower is closer match)")
        print(f"  Snippet Preview :")
        # Print first 200 characters of the chunk
        preview = doc.replace("\n", " ")[:200]
        print(f"  \"{preview}...\"\n")
    # Sanity check verification
    top_source = metadatas[0]["source"]
    print("=" * 65)
    if "PIN" in top_source:
        print(f"[PASSED] Search returned the correct document: '{top_source}'!")
    else:
        print(f"[WARNING] Top document was '{top_source}'. Check chunking/embeddings.")
    print("=" * 65)
if __name__ == "__main__":
    run_standalone_check()
