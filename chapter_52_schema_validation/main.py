def validate_quiz_result(data: dict) -> tuple[bool, str]:
    """Validate a quiz result without extra libraries.

    Later you can use Pydantic for this, but the core idea is the same.
    """

    required_fields = {"chapter", "score", "passed"}

    missing = required_fields - set(data)
    if missing:
        return False, f"Missing fields: {sorted(missing)}"

    if not isinstance(data["chapter"], int):
        return False, "chapter must be an integer."

    if not isinstance(data["score"], int):
        return False, "score must be an integer."

    if not 0 <= data["score"] <= 100:
        return False, "score must be between 0 and 100."

    if not isinstance(data["passed"], bool):
        return False, "passed must be true or false."

    return True, "Valid quiz result."


def main() -> None:
    examples = [
        {"chapter": 3, "score": 85, "passed": True},
        {"chapter": "three", "score": 85, "passed": True},
        {"chapter": 4, "score": 140, "passed": True},
    ]

    for example in examples:
        print(example)
        print(validate_quiz_result(example))
        print()


if __name__ == "__main__":
    main()

