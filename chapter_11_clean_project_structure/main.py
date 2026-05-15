import sys
from pathlib import Path


# Add this chapter folder to Python's import path.
# This lets us import the local app/ package below.
CHAPTER_DIR = Path(__file__).resolve().parent
sys.path.append(str(CHAPTER_DIR))

from app.simple_agent import answer_question


def main() -> None:
    # main.py should usually be small.
    # It is the front door of the program.
    question = "Why should I split agent code into multiple files?"
    answer = answer_question(question)
    print(answer)


if __name__ == "__main__":
    main()

