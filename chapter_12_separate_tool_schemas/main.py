import json
import sys
from pathlib import Path


CHAPTER_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CHAPTER_DIR.parents[0]
sys.path.append(str(CHAPTER_DIR))
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box
from tools.router import run_tool
from tools.schemas import TOOL_SCHEMAS


def main() -> None:
    client = get_client()

    response = client.responses.create(
        model=get_model(),
        tools=TOOL_SCHEMAS,
        input="Use a tool to explain the Python concept 'function'.",
    )

    tool_outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        arguments = json.loads(item.arguments)
        result = run_tool(item.name, arguments)

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

    print_box("FINAL ANSWER", final_response.output_text)


if __name__ == "__main__":
    main()

