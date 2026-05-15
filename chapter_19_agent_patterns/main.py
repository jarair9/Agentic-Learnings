def choose_agent_pattern(task: str) -> str:
    """A tiny rule-based pattern chooser.

    Real systems can use better logic, but this teaches the decision idea.
    """

    task_lower = task.lower()

    if "calculate" in task_lower:
        return "Simple Tool Agent"

    if "research" in task_lower or "find" in task_lower:
        return "ReAct Tool Agent"

    if "project" in task_lower or "many steps" in task_lower:
        return "Plan-And-Execute Agent"

    if "improve" in task_lower or "review" in task_lower:
        return "Reflection Agent"

    return "Simple Chat"


def main() -> None:
    tasks = [
        "Calculate my weekly study hours.",
        "Research what files are in a project.",
        "Review and improve my explanation.",
        "Plan a many steps learning project.",
    ]

    for task in tasks:
        print(task)
        print("Suggested pattern:", choose_agent_pattern(task))
        print()


if __name__ == "__main__":
    main()

