CONCEPT_GROUPS = {
    "LLM Basics": [
        "tokens",
        "context windows",
        "temperature",
        "top-p",
        "max tokens",
        "hallucinations",
        "message roles",
    ],
    "Agent Theory": [
        "agent loop",
        "ReAct",
        "plan-execute",
        "reflection",
        "multi-agent",
        "human approval",
    ],
    "Tool Use": [
        "schemas",
        "routing",
        "permissions",
        "retries",
        "safe tools",
        "idempotency",
    ],
    "RAG": [
        "embeddings",
        "chunking",
        "ranking",
        "reranking",
        "hybrid search",
        "citations",
    ],
}


def main() -> None:
    for group, concepts in CONCEPT_GROUPS.items():
        print(group)
        for concept in concepts:
            print(f"  - {concept}")
        print()


if __name__ == "__main__":
    main()

