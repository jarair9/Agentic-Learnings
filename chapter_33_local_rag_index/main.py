from pathlib import Path


KNOWLEDGE_DIR = Path(__file__).resolve().parent / "knowledge"


def chunk_text(text: str, words_per_chunk: int = 35) -> list[str]:
    words = text.split()
    chunks = []

    for start in range(0, len(words), words_per_chunk):
        chunks.append(" ".join(words[start : start + words_per_chunk]))

    return chunks


def build_index() -> list[dict]:
    """Load notes and build a tiny searchable index."""

    index = []

    for path in KNOWLEDGE_DIR.glob("*.txt"):
        text = path.read_text(encoding="utf-8")

        for chunk_number, chunk in enumerate(chunk_text(text), start=1):
            index.append(
                {
                    "source": path.name,
                    "chunk_number": chunk_number,
                    "text": chunk,
                }
            )

    return index


def search_index(index: list[dict], query: str, limit: int = 2) -> list[dict]:
    """Simple keyword search over chunks."""

    query_words = set(query.lower().split())
    scored = []

    for item in index:
        chunk_words = set(item["text"].lower().split())
        score = len(query_words.intersection(chunk_words))
        scored.append((score, item))

    scored.sort(reverse=True, key=lambda pair: pair[0])

    return [item for score, item in scored[:limit] if score > 0]


def main() -> None:
    index = build_index()
    results = search_index(index, "How do tools help agents?")

    for result in results:
        print(f"Source: {result['source']} chunk {result['chunk_number']}")
        print(result["text"])
        print()


if __name__ == "__main__":
    main()

