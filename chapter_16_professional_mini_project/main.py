import sys
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CHAPTER_DIR.parents[0]
sys.path.append(str(CHAPTER_DIR))
sys.path.append(str(PROJECT_ROOT))

from course_helpers import print_box
from pro_agent.agent import StudyAgent


def main() -> None:
    # main.py should read almost like plain English.
    agent = StudyAgent()

    answer = agent.run(
        "Read the note about agent loops, then teach it to me with one tiny Python example."
    )

    print_box("PROFESSIONAL MINI PROJECT ANSWER", answer)


if __name__ == "__main__":
    main()

