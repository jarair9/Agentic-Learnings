import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


DOCUMENTS = [
    {
        "title": "Agent Loop",
        "text": "An agent loop repeatedly asks the model what to do, runs tools, stores results, and continues until done.",
    },
    {
        "title": "Tool Calling",
        "text": "Tool calling lets a model request that your program runs a function, such as search, calculator, or database lookup.",
    },
    {
        "title": "Memory",
        "text": "Memory means storing useful conversation or task information so the agent can use it later.",
    },
]


def search_documents(query: str, limit: int = 2) -> list[dict]:
    """Very small keyword search.

    Real RAG often uses embeddings and a vector database.
    This simple version counts matching words so the core idea is clear.
    """

    query_words = set(query.lower().split())
    scored_docs = []

    for doc in DOCUMENTS:
        text_words = set((doc["title"] + " " + doc["text"]).lower().split())
        score = len(query_words.intersection(text_words))
        scored_docs.append((score, doc))

    scored_docs.sort(reverse=True, key=lambda item: item[0])

    return [doc for score, doc in scored_docs[:limit] if score > 0]


def main() -> None:
    client = get_client()

    question = "How does an agent use tools in a loop?"
    matches = search_documents(question)

    context = "\n\n".join(
        f"Title: {doc['title']}\nText: {doc['text']}" for doc in matches
    )

    prompt = f"""
Answer the question using only the notes below.
If the notes are not enough, say what is missing.

Notes:
{context}

Question:
{question}
"""

    response = client.responses.create(
        model=get_model(),
        input=prompt,
    )

    print_box("RETRIEVED NOTES", context)
    print_box("RAG ANSWER", response.output_text)


if __name__ == "__main__":
    main()

