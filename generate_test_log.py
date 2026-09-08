"""
generate_test_log.py - Automated Runner for Homework Step 7
Runs 5 required evaluation questions through the pipeline and saves test_log.md.
"""

from pipeline import run_rag_pipeline

TEST_QUESTIONS = [
    {
        "id": 1,
        "type": "In-Document (PIN Reset)",
        "question": "How do I reset my forgotten PIN on a company device, and what happens if I fail too many times?",
    },
    {
        "id": 2,
        "type": "In-Document (VPN Setup)",
        "question": "What are the prerequisites and steps to configure VPN access for remote workers?",
    },
    {
        "id": 3,
        "type": "In-Document (Cisco Webex)",
        "question": "How do I schedule a conference call and invite participants using Cisco Webex?",
    },
    {
        "id": 4,
        "type": "Out-of-Document (Hallucination Test)",
        "question": "What is the recipe and baking temperature for chocolate fudge brownies?",
    },
    {
        "id": 5,
        "type": "Out-of-Document / Edge Case (Non-IT Policy)",
        "question": "How do I request a reimbursement for an international airline ticket?",
    },
]


def run_all_tests():
    print("=" * 65)
    print("      RUNNING HOMEWORK STEP 7 EVALUATION TEST SUITE")
    print("=" * 65)

    log_lines = [
        "# RAG System Evaluation Test Log (Step 7)\n",
        "This test log documents the execution of the 5 required benchmark questions.\n",
        "- **Embedding Model**: `nomic-embed-text` (Ollama)",
        "- **LLM Generation Model**: `llama3.2` (Ollama)",
        "- **Vector Database**: `ChromaDB` (Persistent, Cosine Distance)\n",
        "---\n",
    ]

    for item in TEST_QUESTIONS:
        qid = item["id"]
        qtype = item["type"]
        question = item["question"]

        print(f"\n[*] Running Test #{qid} [{qtype}]:")
        print(f"    \"{question}\"")

        res = run_rag_pipeline(question)

        print(f"    [+] Best Distance: {res['best_distance']:.4f} | Confident: {res['is_confident']}")
        print(f"    [+] Answer Preview: {res['answer'][:70]}...")

        # Format markdown entry
        log_lines.append(f"## Test #{qid}: {qtype}")
        log_lines.append(f"**Question**: `{question}`\n")
        log_lines.append(f"**Confidence Gate Passed**: `{res['is_confident']}` (Best Cosine Distance: `{res['best_distance']:.4f}`)\n")
        log_lines.append("### Retrieved Chunks:")
        for idx, c in enumerate(res["chunks"], start=1):
            snippet = c["text"].replace("\n", " ")[:180]
            log_lines.append(f"{idx}. **[{c['source']}]** (distance = `{c['distance']:.4f}`):")
            log_lines.append(f"   > \"{snippet}...\"\n")

        log_lines.append("### Generated Answer:")
        log_lines.append(f"{res['answer']}\n")
        log_lines.append("---\n")

    # Write to test_log.md
    with open("test_log.md", "w", encoding="utf-8") as f:
        f.write("\n".join(log_lines))

    print("\n" + "=" * 65)
    print("[OK] Test suite complete! All results saved to 'test_log.md'.")
    print("=" * 65)


if __name__ == "__main__":
    run_all_tests()