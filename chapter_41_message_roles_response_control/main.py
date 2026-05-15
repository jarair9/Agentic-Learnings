def build_messages(user_task: str) -> list[dict]:
    """Build clean model messages.

    Keep developer instructions separate from user input.
    This makes the conversation easier to reason about.
    """

    return [
        {
            "role": "developer",
            "content": "You are a careful Python tutor. Use simple examples.",
        },
        {
            "role": "user",
            "content": user_task,
        },
    ]


def main() -> None:
    messages = build_messages("Explain max_output_tokens.")

    for message in messages:
        print(message["role"].upper())
        print(message["content"])
        print()


if __name__ == "__main__":
    main()

