"""
compare_chunking.py - Bonus Challenge: Chunking Strategy Comparison
Compares two different text splitting strategies on the same documents:
- Strategy 1: Fixed-size chunking with ZERO overlap
- Strategy 2: Sliding window chunking with 100-character overlap
"""

from pathlib import Path
from chunking import split_text


def run_comparison():
    sample_file = Path("data/002_Resetting_a_Forgotten_PIN.txt")
    if not sample_file.exists():
        sample_file = list(Path("data").glob("*.txt"))[0]

    with open(sample_file, "r", encoding="utf-8") as f:
        text = f.read().strip()

    print("=" * 70)
    print("      BONUS CHALLENGE: CHUNKING STRATEGY COMPARISON")
    print("=" * 70)
    print(f"Document Tested : {sample_file.name}")
    print(f"Total Characters: {len(text)}\n")

    # Strategy 1: Fixed size, no overlap
    chunks_no_overlap = split_text(text, chunk_size=500, chunk_overlap=0)

    # Strategy 2: Sliding window with overlap
    chunks_with_overlap = split_text(text, chunk_size=500, chunk_overlap=100)

    print("--- 1. Chunk Count Comparison ---")
    print(f"• Strategy 1 (No Overlap, 500 chars)   : {len(chunks_no_overlap)} chunks")
    print(f"• Strategy 2 (With Overlap, 500/100)   : {len(chunks_with_overlap)} chunks")
    print(f"  --> The overlapping window generates more chunks to prevent information loss.\n")

    print("--- 2. Boundary Analysis (Chunk 0 -> Chunk 1 Transition) ---")
    print("\n[Strategy 1: Fixed (No Overlap)]")
    print(f"End of Chunk 0   : \"...{chunks_no_overlap[0][-90:]}\"")
    print(f"Start of Chunk 1 : \"{chunks_no_overlap[1][:90]}...\"")
    print("  Notice: Sentences right at the 500-character line are severed abruptly.")

    print("\n[Strategy 2: Sliding Window (100-Char Overlap)]")
    print(f"End of Chunk 0   : \"...{chunks_with_overlap[0][-90:]}\"")
    print(f"Start of Chunk 1 : \"{chunks_with_overlap[1][:90]}...\"")
    print("  Notice: The boundary text is preserved in both chunks, maintaining context.\n")

    print("=" * 70)
    print("[SUMMARY] Why Strategy 2 is better for RAG:")
    print("In technical SOPs, cutting an instruction in half causes vector search to miss")
    print("the context. A 100-character overlap guarantees that full instructions remain intact.")
    print("=" * 70)


if __name__ == "__main__":
    run_comparison()
