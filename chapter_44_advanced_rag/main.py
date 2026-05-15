CHUNKS = [
    {
        "source": "agent_loops.txt",
        "chunk": 1,
        "text": "Agent loops repeat model calls, tool use, and observations.",
        "keyword_score": 3,
        "vector_score": 0.82,
    },
    {
        "source": "memory.txt",
        "chunk": 2,
        "text": "Memory stores useful facts for later turns or sessions.",
        "keyword_score": 1,
        "vector_score": 0.61,
    },
]


def hybrid_score(chunk: dict) -> float:
    """Combine keyword and vector scores."""

    return chunk["keyword_score"] * 0.4 + chunk["vector_score"] * 0.6


def main() -> None:
    ranked = sorted(CHUNKS, key=hybrid_score, reverse=True)

    for item in ranked:
        citation = f"[{item['source']} chunk {item['chunk']}]"
        print(citation, item["text"])


if __name__ == "__main__":
    main()

