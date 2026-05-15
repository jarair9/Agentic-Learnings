FORBIDDEN_OUTPUT_TERMS = ["api_key", "password", "secret"]


def validate_output(answer: str, requires_citation: bool = False) -> tuple[bool, str]:
    lowered = answer.lower()

    for term in FORBIDDEN_OUTPUT_TERMS:
        if term in lowered:
            return False, f"Output blocked because it may contain {term}."

    if requires_citation and "[" not in answer:
        return False, "Output needs a citation but none was found."

    return True, "Output passed guardrails."


def main() -> None:
    answers = [
        "Agent loops use tools [agent_loops.txt chunk 1].",
        "The API_KEY is abc123.",
        "Agent loops use tools.",
    ]

    for answer in answers:
        print(answer)
        print(validate_output(answer, requires_citation=True))
        print()


if __name__ == "__main__":
    main()

