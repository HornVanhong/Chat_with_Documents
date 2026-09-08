"""
generator.py - Stage 5b: Generator
Builds grounded prompt with retrieved chunks and queries the local LLM via Ollama.
"""
"""
generator.py - Stage 5b: Grounded Answer Generator
Formats retrieved context passages into a prompt and calls Ollama LLM (llama3.2).
"""

import ollama

GENERATION_MODEL = "llama3.2"


def build_context_string(chunks: list[dict]) -> str:
    """
    Combines retrieved chunks into a single formatted context string.
    """
    context_blocks = []
    for idx, chunk in enumerate(chunks, start=1):
        source = chunk.get("source", "Unknown Document")
        text = chunk.get("text", "").strip()
        context_blocks.append(f"--- Passage {idx} [Source: {source}] ---\n{text}")
    return "\n\n".join(context_blocks)


def generate_answer(
    query: str,
    retrieved_chunks: list[dict],
    model: str = GENERATION_MODEL,
) -> str:
    """
    Constructs a grounded prompt from the retrieved chunks and queries the LLM.
    """
    # Guard check: if no chunks provided, return fallback immediately
    if not retrieved_chunks:
        return "I could not find this in your documents."

    context_text = build_context_string(retrieved_chunks)

    system_prompt = (
        "You are an IT support assistant. Your task is to answer user questions "
        "strictly and only based on the provided context passages below.\n"
        "Rules:\n"
        "1. Only use facts directly stated in the context.\n"
        "2. Do NOT use any outside knowledge or assumptions.\n"
        "3. If the answer is not contained in the context, you must reply EXACTLY:\n"
        "   'I could not find this in your documents.'\n"
        "4. Keep the answer clear, helpful, and concise."
    )

    user_message = (
        f"Context:\n{context_text}\n\n"
        f"User Question: {query}\n\n"
        "Answer:"
    )

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        options={"temperature": 0.1},  # Low temperature for factual, grounded answers
    )

    return response["message"]["content"].strip()


if __name__ == "__main__":
    # Test generator with mock context
    mock_chunks = [
        {
            "source": "002_Resetting_a_Forgotten_PIN.txt",
            "text": "Step 1: Access the PIN Reset Tool on the IT Support portal. Enter your employee ID and confirm your identity via SMS code.",
        }
    ]
    test_question = "How do I access the PIN reset tool?"

    print(f"Generating answer for: \"{test_question}\"...\n")
    answer = generate_answer(test_question, mock_chunks)
    print("--- LLM Grounded Answer ---")
    print(answer)