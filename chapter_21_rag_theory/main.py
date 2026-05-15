def chunk_text(text: str, words_per_chunk: int = 30) -> list[str]:
    """Split text into simple word chunks.

    Real chunking can be smarter, but this teaches the core idea.
    """

    words = text.split()
    chunks = []

    for start in range(0, len(words), words_per_chunk):
        chunk = " ".join(words[start : start + words_per_chunk])
        chunks.append(chunk)

    return chunks


def main() -> None:
    text = """
    Agentic AI systems use models to decide what to do next.
    They can call tools, read files, search documents, and remember useful facts.
    RAG helps agents answer using external knowledge instead of guessing.
    """

    for number, chunk in enumerate(chunk_text(text, words_per_chunk=12), start=1):
        print(f"Chunk {number}: {chunk}")


if __name__ == "__main__":
    main()

