import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def get_python_concept(concept: str) -> str:
    """A tiny fake knowledge tool.

    In real apps, a tool could search a database, call an API, read files,
    send an email, or control a browser.
    """

    notes = {
        "loop": "A loop repeats code. for-loops repeat over items. while-loops repeat while a condition is true.",
        "function": "A function is a reusable block of code. You give it inputs, and it can return output.",
        "dictionary": "A dictionary stores key-value pairs, like {'name': 'Ali', 'age': 13}.",
    }

    return notes.get(concept.lower(), "I do not have notes for that concept yet.")


def main() -> None:
    client = get_client()

    # Tool schema: this tells the model the tool name, purpose, and arguments.
    tools = [
        {
            "type": "function",
            "name": "get_python_concept",
            "description": "Look up a simple explanation of a Python concept.",
            "parameters": {
                "type": "object",
                "properties": {
                    "concept": {
                        "type": "string",
                        "description": "The Python concept to explain, like loop or function.",
                    }
                },
                "required": ["concept"],
                "additionalProperties": False,
            },
        }
    ]

    input_messages = [
        {
            "role": "user",
            "content": "Use your tool to explain Python loops, then give me a tiny example.",
        }
    ]

    # First model call: the model may decide to call a tool.
    response = client.responses.create(
        model=get_model(),
        input=input_messages,
        tools=tools,
    )

    # Collect tool outputs here.
    tool_outputs = []

    # Loop over all output items because the model can request multiple tools.
    for item in response.output:
        if item.type != "function_call":
            continue

        # The model gives arguments as a JSON string.
        arguments = json.loads(item.arguments)

        if item.name == "get_python_concept":
            tool_result = get_python_concept(arguments["concept"])
        else:
            tool_result = "Unknown tool"

        # Give the tool result back to the model.
        # previous_response_id tells the API:
        # "This tool output belongs to the previous model response."
        tool_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": tool_result,
            }
        )

    if not tool_outputs:
        print_box("MODEL ANSWER", response.output_text)
        return

    # Second model call: now the model has the tool result and can answer.
    final_response = client.responses.create(
        model=get_model(),
        input=tool_outputs,
        previous_response_id=response.id,
        tools=tools,
    )

    print_box("FINAL ANSWER AFTER TOOL USE", final_response.output_text)


if __name__ == "__main__":
    main()
