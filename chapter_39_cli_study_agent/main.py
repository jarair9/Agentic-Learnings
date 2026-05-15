def answer_without_api(user_text: str) -> str:
    """Offline placeholder for the study agent.

    Later, you can replace this with an OpenAI call.
    """

    return f"Study buddy says: let's break down '{user_text}' step by step."


def main() -> None:
    print("CLI Study Agent")
    print("Type /help for commands. Type /exit to stop.")

    while True:
        user_text = input("\nYou: ").strip()

        if user_text == "/exit":
            print("Goodbye. Keep learning.")
            break

        if user_text == "/help":
            print("Commands: /help, /exit")
            continue

        if not user_text:
            continue

        print(answer_without_api(user_text))


if __name__ == "__main__":
    main()

