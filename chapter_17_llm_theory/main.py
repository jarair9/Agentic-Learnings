def estimate_tokens(text: str) -> int:
    """Very rough token estimate.

    Real tokenizers are more complex.
    This beginner estimate helps you think about context size.
    A common rough rule is about 4 characters per token for English text.
    """

    return max(1, len(text) // 4)


def main() -> None:
    examples = [
        "Hello!",
        "Agentic AI uses tools, memory, planning, and loops.",
        "A long prompt costs more because it uses more tokens.",
    ]

    for text in examples:
        print(f"Text: {text}")
        print(f"Rough token estimate: {estimate_tokens(text)}")
        print()


if __name__ == "__main__":
    main()

