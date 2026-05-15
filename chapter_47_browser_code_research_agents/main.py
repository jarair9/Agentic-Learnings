def classify_agent_type(task: str) -> str:
    task_lower = task.lower()

    if "click" in task_lower or "browser" in task_lower or "website" in task_lower:
        return "browser agent"

    if "fix code" in task_lower or "test" in task_lower or "refactor" in task_lower:
        return "code agent"

    if "research" in task_lower or "latest" in task_lower or "sources" in task_lower:
        return "research agent"

    return "general assistant agent"


def main() -> None:
    tasks = [
        "Research the latest RAG techniques with sources.",
        "Fix code and run tests.",
        "Open the website and test the login flow.",
    ]

    for task in tasks:
        print(task)
        print("Agent type:", classify_agent_type(task))
        print()


if __name__ == "__main__":
    main()

