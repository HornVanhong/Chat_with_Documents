# Week 5 Homework: Baseline "Chat with Documents" App

This repository contains my Week 5 homework for RAG Fundamentals. It is a local Naive RAG application built in Python using ChromaDB and Ollama. It allows a user to ask IT support questions in the terminal and receive answers grounded strictly in documents placed inside the `data/` folder.

---

## Models and Database Used

- **Embedding Model**: `nomic-embed-text` (running locally via Ollama).
- **LLM for Generation**: `llama3.2` (running locally via Ollama).
- **Vector Database**: `ChromaDB` (using persistent mode saved to `./chroma_db` with cosine distance).

---

## Chunking Strategy and Why I Chose It

In `chunking.py`, I implemented a **sliding window chunking strategy with overlap**:
- **Chunk size**: 500 characters
- **Chunk overlap**: 100 characters

### Why I chose this strategy:
1. **Preserves Complete Instructions**: The documents provided are IT support Standard Operating Procedures (SOPs) containing numbered steps and specific instructions. A chunk size of 500 characters is long enough to keep an entire step or procedure intact without splitting it into pieces.
2. **Prevents Cut-Off Sentences**: The 100-character overlap ensures that if an important instruction begins near the end of a chunk, the full sentence will still appear in full within the next chunk.
3. **Improves Retrieval Accuracy**: Instead of embedding entire multi-page documents, breaking them into 500-character chunks allows ChromaDB to retrieve only the exact section that answers the question, keeping the prompt clean and focused for the LLM.

---

## Project Structure

```text
chat-with-document/
├── data/                    # 5 IT Support SOP text files
├── chroma_db/               # Persistent ChromaDB database folder
├── ingestion.py             # Stage 1: Reads all .txt and .md files from data/
├── chunking.py              # Stage 2: Splits text into overlapping chunks
├── embeddings.py            # Stage 3: Generates embeddings with nomic-embed-text
├── vector_store.py          # Stage 4: Stores vectors in ChromaDB and runs queries
├── demo_vector_check.py     # Step 4 check: Standalone vector test script
├── retriever.py             # Stage 5a: Embeds query and retrieves top-k chunks
├── generator.py             # Stage 5b: Builds prompt and calls llama3.2
├── pipeline.py              # Stage 5c: Connects retriever and generator into one function
├── main.py                  # Stage 6: Interactive terminal chat loop
├── generate_test_log.py     # Step 7: Runs the 5 benchmark questions
├── test_log.md              # Test output log with questions, chunks, and answers
├── reflection.md            # Homework reflection (Step 8)
├── pyproject.toml           # Poetry project configuration
└── .gitignore               # Ignores .venv, cache, and ChromaDB files
```

---

## How to Set Up and Run

### 1. Prerequisites
Make sure Ollama is installed and running, then pull the required models:
```bash
ollama pull nomic-embed-text
ollama pull llama3.2
```

### 2. Set Up Virtual Environment and Install Packages
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install chromadb ollama
```

### 3. Test Vector Store on its Own (Step 4)
Before running the full chat app, verify that ChromaDB retrieval works independently:
```bash
python demo_vector_check.py
```

### 4. Run the Interactive Chat App (Step 6)
To start asking questions in the terminal:
```bash
python main.py
```
- Type any question about company IT procedures (e.g., `How do I reset my forgotten PIN?` or `How do I set up VPN?`).
- Type `exit` to close the app.

### 5. Run the Automated Evaluation Test Suite (Step 7)
To run all 5 benchmark questions and update `test_log.md`:
```bash
python generate_test_log.py
```
