"""
ingestion.py - Stage 1: Document Ingestion
Loads raw text documents (.txt, .md) from the data/ folder.
"""
from pathlib import Path
def load_documents(data_dir:str = "data") -> list[dict]:
    """
    Scans the data directory, reads all .txt and .md files,
    and returns a list of dictionaries with text and metadata.
    :param data_dir:
    :return:
    """
    folder = Path(data_dir)
    if not folder.exists():
        raise FileNotFoundError(f"Directory '{data_dir}' not found.")
    documents =[]

    #Find all .text and .md files
    file_paths = list(folder.glob("*.txt"))+list(folder.glob("*md"))
    for path in file_paths:
        with open(path,"r",encoding="utf-8") as f:
            content= f.read().strip()
        if content:
            documents.append({
                "filename": path.name,
                "text": content,
                "char_count": len(content),
            })
    return documents

if __name__ == "__main__":
        #Quick standalone test
        docs = load_documents()
        print(f"[ok] Sucessfully loaded{len(docs)} documents:")
        for doc in docs:
            print(f" - {doc['filename']} ({doc['char_count']} characters)")



