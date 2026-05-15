ROADMAP = [
    "Create study_coach folder structure",
    "Add config.py and prompts.py",
    "Build safe read_lesson tool",
    "Build local RAG index over lesson.md files",
    "Create AgentRunner",
    "Add memory.json progress tracking",
    "Add quiz generation and grading",
    "Add logging and traces",
    "Add eval dataset",
    "Add CLI commands",
]


def main() -> None:
    print("Capstone Implementation Roadmap")
    print("=" * 35)

    for number, step in enumerate(ROADMAP, start=1):
        print(f"{number}. {step}")


if __name__ == "__main__":
    main()

