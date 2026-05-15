EVAL_DATASET = [
    {
        "input": "Explain an agent loop.",
        "answer": "An agent loop lets a model choose a tool, read the result, and continue until finished.",
        "expected_keywords": ["model", "tool", "result", "loop"],
    },
    {
        "input": "Explain RAG.",
        "answer": "RAG retrieves relevant notes and gives them to the model before it answers.",
        "expected_keywords": ["retrieves", "notes", "model"],
    },
]


def grade(answer: str, expected_keywords: list[str]) -> float:
    answer_lower = answer.lower()
    matches = [word for word in expected_keywords if word in answer_lower]
    return len(matches) / len(expected_keywords)


def main() -> None:
    for item in EVAL_DATASET:
        score = grade(item["answer"], item["expected_keywords"])
        print(item["input"])
        print("Score:", score)
        print()


if __name__ == "__main__":
    main()

