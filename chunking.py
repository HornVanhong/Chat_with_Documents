"""
chunking.py - Stage 2: Text Chunking
Splits loaded documents into smaller overlapping text chunks.
"""
from ingestion import load_documents

def split_text(text:str,chunk_size:int = 500, chunk_overlap: int = 100) ->list[str]:
    """
    splits a single text into overlapping chunks of characters.
    :param text:
    :param chunk_size:
    :param chunk_overlap:
    :return:
    """
    if chunk_size <=chunk_overlap:
        raise ValueError("chunk_size must be greater than chunk_overlap")
    chunks =[]
    start =0
    text_length = len(text)
    step = chunk_size - chunk_overlap

    while start < text_length:
        end = start + chunk_size
        chunk=text[start:end].strip()
        if chunk:
            chunks.append(chunk)

        #Move forward by (chunk_size - overlap)
        start+=step
    return chunks
def chunk_documents(
        documents:list[dict], chunk_size: int = 500 , chunk_overlap: int = 100) -> list[dict]:
    """
    Takes a lsit of documents from ingestion.py,
    splits each document int chunks, and returns a list of chunk dicts.
    :param documents:
    :param chunk_size:
    :param chunk_overlap:
    :return:
    """
    all_chunks = []
    for doc in documents:
        filename = doc["filename"]
        text = doc["text"]
        raw_chunks = split_text(text,chunk_size,chunk_overlap)
        for idx, chunk_text in enumerate(raw_chunks):
            chunk_id = f"{filename}_chunk_{idx}"
            all_chunks.append(
                {
                    "id": chunk_id,
                    "text": chunk_text,
                    "source": filename,
                    "chunk_index": idx,
                }
            )
    return all_chunks

if __name__ == "__main__":
    docs = load_documents()
    chunks = chunk_documents(docs,chunk_size=500,chunk_overlap=100)
    print(f"[OK] Generated {len(chunks)} total chunks from {len(docs)} documents.")
    print("\n--- Sample Chunk 0 ---")
    print(f"ID: {chunks[0]['id']}")
    print(f"Source: {chunks[0]['source']}")
    print(f"Text Snippet:\n{chunks[0]['text'][:200]}...")