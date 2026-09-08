# Week 5 Homework: Baseline "Chat with Documents" App

This repository contains my Week 5 homework for RAG Fundamentals. It is a local Naive RAG system built with Python, ChromaDB, and Ollama that allows a user to ask questions in the terminal and get answers based on documents inside the `data/` folder.

---

## Models and Database Used

- **Embedding Model**: `nomic-embed-text` (running locally via Ollama).
- **LLM for Generation**: `llama3.2` (running locally via Ollama).
- **Vector Database**: `ChromaDB` (using persistent mode saved to `./chroma_db` with cosine similarity).

---

## Chunking Strategy and Why I Chose It

For the chunking stage in `chunking.py`, I used a **sliding window text splitting strategy with overlap**:
- **Chunk size**: 500 characters
- **Chunk overlap**: 100 characters

**Why I chose this:** The sample documents provided are IT support SOPs (Standard Operating Procedures) with numbered steps and technical instructions.
1. A chunk size around 500 characters is long enough to hold a complete step or guideline without mixing multiple unrelated topics together.
2. The 100-character overlap prevents sentences from being cut in half at the boundary. If a step starts near the end of a chunk, the overlap makes sure the full context appears in the following chunk as well.
3. It also tries to split on paragraph breaks (`\n\n`) or sentence endings (`. `) rather than cutting words in the middle.

---

## Project File Structure

The project follows the modular layout requested in class:

```text
chat-with-documents/
├── data/                    # 5 IT Support SOP documents
├── chroma_db/               # Local ChromaDB database folder (created automatically)
├── ingestion.py             # Reads all .txt and .md files from data/
├── chunking.py              # Splits documents into overlapping chunks
├── embeddings.py            # Generates embeddings using nomic-embed-text via Ollama
├── vector_store.py          # Saves chunks and embeddings to ChromaDB, runs queries
├── demo_vector_check.py     # Standalone script to test vector search (Step 4)
├── retriever.py             # Finds the top relevant chunks for a question
├── generator.py             # Builds the prompt and generates an answer with llama3.2
├── pipeline.py              # Connects retriever and generator into one function
├── main.py                  # Interactive terminal chat loop
├── generate_test_log.py     # Runs the 5 test questions and writes test_log.md
├── test_log.md              # Output log from testing (Step 7)
├── reflection.md            # Homework reflection (Step 8)
└── pyproject.toml           # Poetry project configuration
```

---

## How to Setup and Run

### 1. Prerequisites
Make sure Ollama is installed and running, then pull the two models:
```bash
ollama pull llama3.2
ollama pull nomic-embed-text
```

### 2. Environment Setup
Install dependencies with Poetry:
```bash
poetry install
```
Or using standard Python virtual environment:
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install chromadb ollama
```

### 3. Check the Vector Store (Step 4)
Before starting the chat interface, run the standalone vector check script to index the documents and verify that search returns sensible chunks:
```bash
python demo_vector_check.py
```

### 4. Run the Chat App (Step 6)
To start chatting with your documents:
```bash
python main.py
```
Type your question at the prompt. To exit the program, type `exit` or `quit`.

---

## Bonus Features Implemented

- **Retrieved Chunks Display**: In `main.py`, the system prints the matching chunks (source file and similarity distance) to the screen before printing the answer, so the user can verify where the answer came from.
- **Distance Threshold Check**: In `retriever.py` and `pipeline.py`, if a question has weak similarity to the stored documents (like asking about cooking or unrelated topics), it avoids guessing and replies with *"I could not find this in your documents."*
