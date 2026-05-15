EXPECTED_KEYWORDS = ["tool", "model", "loop", "result"]


def simple_answer_grade(answer: str) -> dict:
    """Tiny keyword-based evaluator.

    This is not perfect, but it shows how evaluation can be automated.
    """

    answer_lower = answer.lower()
    found = [word for word in EXPECTED_KEYWORDS if word in answer_lower]

    return {
        "score": len(found) / len(EXPECTED_KEYWORDS),
        "found_keywords": found,
        "missing_keywords": [word for word in EXPECTED_KEYWORDS if word not in found],
    }


def main() -> None:
    answer = "An agent loop lets a model choose a tool, read the result, and continue."
    print(simple_answer_grade(answer))


if __name__ == "__main__":
    main()

