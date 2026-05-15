import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def calculator(expression: str) -> str:
    """Safely calculate a tiny math expression.

    Important: eval can be dangerous if used carelessly.
    Here we only allow digits and math symbols to keep the example safer.
    """

    allowed = set("0123456789+-*/(). ")

    if not set(expression).issubset(allowed):
        return "Error: expression contains characters that are not allowed."

    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as error:
        return f"Error: {error}"


TOOLS = [
    {
        "type": "function",
        "name": "calculator",
        "description": "Calculate a simple math expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "Simple math like '2 + 2' or '(12 * 3) / 4'.",
                }
            },
            "required": ["expression"],
            "additionalProperties": False,
        },
    }
]


def run_tool(name: str, arguments: dict) -> str:
    """Route tool calls to the correct Python function."""

    if name == "calculator":
        return calculator(arguments["expression"])

    return f"Unknown tool: {name}"


def run_agent(user_task: str, max_turns: int = 5) -> str:
    """Run a small agent loop until the model stops asking for tools."""

    client = get_client()

    messages = [
        {
            "role": "user",
            "content": user_task,
        }
    ]
    previous_response_id = None

    for turn in range(max_turns):
        print(f"\nAgent turn {turn + 1}")

        request = {
            "model": get_model(),
            "input": messages,
            "tools": TOOLS,
        }

        if previous_response_id is not None:
            request["previous_response_id"] = previous_response_id

        response = client.responses.create(**request)

        tool_calls = [item for item in response.output if item.type == "function_call"]

        # If there are no tool calls, the model has finished answering.
        if not tool_calls:
            return response.output_text

        for tool_call in tool_calls:
            arguments = json.loads(tool_call.arguments)
            tool_result = run_tool(tool_call.name, arguments)

            print(f"Tool called: {tool_call.name}")
            print(f"Tool arguments: {arguments}")
            print(f"Tool result: {tool_result}")

            messages.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": tool_result,
                }
            )

        previous_response_id = response.id
        messages = messages[-len(tool_calls) :]

    return "Agent stopped because it reached the max_turns safety limit."


def main() -> None:
    answer = run_agent(
        "What is 25 * 13? Use the calculator tool, then explain the answer simply."
    )

    print_box("AGENT FINAL ANSWER", answer)


if __name__ == "__main__":
    main()
