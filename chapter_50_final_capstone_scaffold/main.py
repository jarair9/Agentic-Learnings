from pathlib import Path


FOLDERS = [
    "study_coach/app/tools",
    "study_coach/app/knowledge",
    "study_coach/app/evals",
    "study_coach/tests",
]

FILES = [
    "study_coach/main.py",
    "study_coach/app/__init__.py",
    "study_coach/app/agent.py",
    "study_coach/app/config.py",
    "study_coach/app/prompts.py",
    "study_coach/app/memory.py",
    "study_coach/app/rag.py",
    "study_coach/app/logging_setup.py",
    "study_coach/app/tools/schemas.py",
    "study_coach/app/tools/router.py",
    "study_coach/app/tools/file_tools.py",
]


def print_scaffold_plan() -> None:
    print("Folders to create:")
    for folder in FOLDERS:
        print("-", folder)

    print("\nFiles to create:")
    for file in FILES:
        print("-", file)


def main() -> None:
    # This chapter prints the scaffold plan only.
    # Later, you can turn this into a real project generator.
    print("Capstone scaffold root:")
    print(Path(__file__).resolve().parent / "study_coach")
    print()
    print_scaffold_plan()


if __name__ == "__main__":
    main()

