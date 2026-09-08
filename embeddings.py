"""
embeddings.py - Stage 3: Embedding Generation
Converts text chunks into dense vector embeddings using nomic-embed-text via Ollama.
"""
from urllib import response

import ollama

EMBEDDING_MODEL = "nomic-embed-text"

def get_embedding(text:str, model: str = EMBEDDING_MODEL) -> list[float]:
    """
    Takes a string of text, calls Ollama nomic-embed-text,
    and returns a 768-dimensional float vector.
    :param text:
    :param model:
    :return:
    """
    cleaned_text = text.replace("\n", " ").strip()
    response = ollama.embeddings(
        model = model,
        prompt=cleaned_text,
    )
    return response["embedding"]

def get_embeddings_batch(
        texts: list[str],model: str = EMBEDDING_MODEL) -> list[list[float]]:
    """
    Generates embeddings for a list of texts.
    :param texts:
    :param str:
    :return:
    """
    embeddings = []
    for text in texts:
        vector = get_embedding(text,model=model)
        embeddings.append(vector)
    return embeddings

if __name__ == "__main__":
    # Test embedding generation with a sample phrase
    test_phrase = "How do I reset my forgotten PIN on a company device?"
    print(f"Generating embedding for: '{test_phrase}'...")
    vector = get_embedding(test_phrase)
    print("[OK] Embedding successfully generated!")
    print(f"  - Vector dimensions: {len(vector)} (Expected: 768)")
    print(f"  - Preview of first 5 numbers: {vector[:5]}")
