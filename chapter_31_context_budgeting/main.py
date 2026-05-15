def estimate_tokens(text: str) -> int:
    """Rough token estimate for learning.

    Real apps should use a tokenizer, but this is enough to understand budgeting.
    """

    return max(1, len(text) // 4)


def keep_recent_messages(messages: list[str], max_tokens: int) -> list[str]:
    """Keep newest messages until the token budget is full."""

    kept = []
    total = 0

    for message in reversed(messages):
        cost = estimate_tokens(message)

        if total + cost > max_tokens:
            break

        kept.append(message)
        total += cost

    return list(reversed(kept))


def main() -> None:
    messages = [
        "User learned basic model calls.",
        "User learned tool schemas.",
        "User learned safe file reading.",
        "User learned RAG theory.",
        "User now wants missing advanced implementation concepts.",
    ]

    recent = keep_recent_messages(messages, max_tokens=25)

    print("Messages kept in context:")
    for message in recent:
        print("-", message)


if __name__ == "__main__":
    main()

