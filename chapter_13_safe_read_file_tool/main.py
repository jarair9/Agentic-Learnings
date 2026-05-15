import json
import sys
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CHAPTER_DIR.parents[0]
sys.path.append(str(CHAPTER_DIR))
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box
from tools.file_tools import read_text_file
from tools.schemas import TOOL_SCHEMAS


def run_tool(name: str, arguments: dict) -> str:
    """Route file tool calls."""

    if name == "read_text_file":
        return read_text_file(arguments["relative_path"])

    return f"Unknown tool: {name}"


def main() -> None:
    client = get_client()

    response = client.responses.create(
        model=get_model(),
        tools=TOOL_SCHEMAS,
        input=(
            "Read the file agent_notes.txt, then explain the notes to me "
            "like I am learning agents for the first time."
        ),
    )

    tool_outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        result = run_tool(item.name, json.loads(item.arguments))

        tool_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result,
            }
        )

    if not tool_outputs:
        print_box("AI ANSWER", response.output_text)
        return

    final_response = client.responses.create(
        model=get_model(),
        tools=TOOL_SCHEMAS,
        input=tool_outputs,
        previous_response_id=response.id,
    )

    print_box("AI ANSWER AFTER READING FILE", final_response.output_text)


if __name__ == "__main__":
    main()
