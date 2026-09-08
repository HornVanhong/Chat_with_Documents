"""
main.py - Stage 6: Interactive Terminal Chat Loop
Provides a user-friendly CLI loop to query documents in real time.
"""
"""
main.py - Stage 6: Interactive Terminal Chat Loop
Provides a user-friendly terminal interface to chat with your documents.
"""

from pipeline import run_rag_pipeline


def print_banner():
    print("=" * 65)
    print("         LOCAL CHAT-WITH-DOCUMENTS RAG APPLICATION")
    print("=" * 65)
    print("• Powered by: Ollama (nomic-embed-text + llama3.2) & ChromaDB")
    print("• Type your IT support question and press Enter.")
    print("• Type 'exit' or 'quit' to end the session.\n")


def chat_loop():
    print_banner()

    while True:
        try:
            user_question = input("You: ").strip()

            if not user_question:
                continue

            # Check for exit command
            if user_question.lower() in ["exit", "quit", "q"]:
                print("\nGoodbye! Session ended.")
                break

            print("\nSearching documents and generating grounded answer...")
            result = run_rag_pipeline(user_question)

            # Bonus Challenge: Display retrieved sources and evidence
            print("\n[Retrieved Evidence]")
            for rank, chunk in enumerate(result["chunks"], start=1):
                source = chunk["source"]
                dist = chunk["distance"]
                print(f"  ({rank}) {source} (distance: {dist:.4f})")

            # Display the LLM's grounded answer
            print("\nAssistant:")
            print(result["answer"])
            print("-" * 65 + "\n")

        except KeyboardInterrupt:
            print("\n\nSession interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\n[Error]: {e}\n")


if __name__ == "__main__":
    chat_loop()