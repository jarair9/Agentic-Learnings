def planner(task: str) -> list[str]:
    return [
        f"Understand the task: {task}",
        "Choose the right tools.",
        "Execute the steps.",
        "Review the answer.",
    ]


def reviewer(plan: list[str]) -> str:
    if "Review the answer." not in plan:
        return "Plan is missing a review step."

    return "Plan looks reasonable."


def main() -> None:
    task = "Build a safe file-reading agent."
    plan = planner(task)
    review = reviewer(plan)

    print("Planner output:")
    for step in plan:
        print("-", step)

    print("\nReviewer output:")
    print(review)


if __name__ == "__main__":
    main()

