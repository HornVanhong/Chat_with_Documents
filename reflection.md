# RAG Fundamentals — Homework Reflection (Step 8)

**Student:** [Horn Vanhong]  
**Assignment:** Week 5 — Build a Baseline "Chat with Documents" App  

---

### Reflection

Building this local Naive RAG application helped me understand how the offline indexing pipeline connects to the online query pipeline in practice. 

**What worked well:**
Using Ollama and ChromaDB completely on my local machine worked very well. Running `nomic-embed-text` for embeddings and `llama3.2` for generation allowed the app to run quickly with good privacy without needing paid cloud API keys. ChromaDB's persistent storage was fast and easy to work with. For specific technical topics like the Cisco Webex conference call and VPN setup, the vector search returned cosine distances under 0.15, giving the model exact passages to answer from.

**One thing that was harder than expected:**
Handling chunking and distance thresholds was more tricky than I thought. If the chunk size is too small, steps get separated; if it is too big, unrelated topics mix together. Also, without a confidence threshold check, the LLM sometimes tries to be overly helpful and answer questions about out-of-domain topics (like baking recipes) using its pre-trained memory. Adding a distance gate was important to ensure the model responds with "I could not find this in your documents" when information is missing.

**One Advanced RAG idea for future improvement:**
To make the system better, I would add a **Two-Stage Re-ranking step with a Cross-Encoder**. Right now, ChromaDB does bi-encoder similarity search to find the top 3 chunks. In a larger system, retrieving the top 10 chunks and then using a cross-encoder (like `bge-reranker`) to re-score each chunk against the question would filter out weak matches and ensure the LLM receives the single most accurate paragraph.