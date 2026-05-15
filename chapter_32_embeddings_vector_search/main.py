import math


VOCABULARY = ["agent", "tool", "memory", "rag", "python", "loop"]


def embed_text(text: str) -> list[float]:
    """Create a tiny fake embedding using word counts."""

    words = text.lower().split()
    return [float(words.count(word)) for word in VOCABULARY]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Compare two vectors."""

    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))

    if length_a == 0 or length_b == 0:
        return 0.0

    return dot / (length_a * length_b)


def main() -> None:
    documents = [
        "agent loop uses tool results",
        "python list and python function",
        "rag retrieves memory notes",
    ]

    query = "agent tool loop"
    query_vector = embed_text(query)

    scored = []
    for document in documents:
        score = cosine_similarity(query_vector, embed_text(document))
        scored.append((score, document))

    scored.sort(reverse=True)

    for score, document in scored:
        print(f"{score:.2f} - {document}")


if __name__ == "__main__":
    main()

