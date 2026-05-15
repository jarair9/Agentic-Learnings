def should_ask_clarifying_question(task: str) -> bool:
    vague_words = ["thing", "stuff", "it", "better", "fix"]
    risky_words = ["delete", "send", "publish", "pay"]

    lowered = task.lower()

    if any(word in lowered for word in risky_words):
        return True

    if len(task.split()) < 4:
        return True

    if any(word in lowered.split() for word in vague_words):
        return True

    return False


def main() -> None:
    tasks = [
        "Fix it",
        "Explain context compaction with examples",
        "Delete the project files",
    ]

    for task in tasks:
        print(task, "-> ask question:", should_ask_clarifying_question(task))


if __name__ == "__main__":
    main()

