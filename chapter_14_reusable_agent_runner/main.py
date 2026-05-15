import sys
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CHAPTER_DIR.parents[0]
sys.path.append(str(CHAPTER_DIR))
sys.path.append(str(PROJECT_ROOT))

from agent_runner import AgentRunner
from course_helpers import print_box
from tools.router import run_tool
from tools.schemas import TOOL_SCHEMAS


def main() -> None:
    runner = AgentRunner(
        tools=TOOL_SCHEMAS,
        tool_runner=run_tool,
        max_turns=5,
    )

    answer = runner.run(
        "Use tools to explain a Python list, then explain why lists are useful."
    )

    print_box("AGENT RUNNER ANSWER", answer)


if __name__ == "__main__":
    main()

