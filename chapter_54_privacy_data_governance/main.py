SENSITIVE_WORDS = ["password", "api_key", "secret", "token"]


def should_store_memory(text: str) -> bool:
    """Decide if a memory is safe to store."""

    lowered = text.lower()

    for word in SENSITIVE_WORDS:
        if word in lowered:
            return False

    return True


def main() -> None:
    memories = [
        "User prefers simple Python examples.",
        "User API_KEY is abc123.",
        "User is weak in RAG concepts.",
    ]

    for memory in memories:
        print(memory)
        print("Store:", should_store_memory(memory))
        print()


if __name__ == "__main__":
    main()

