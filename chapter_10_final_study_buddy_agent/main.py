import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def explain_python(concept: str) -> str:
    """Return a simple explanation for a Python concept."""

    notes = {
        "variable": "A variable is a name that stores a value, like score = 10.",
        "loop": "A loop repeats code. Use it when you want to do something many times.",
        "function": "A function is a named block of reusable code.",
        "list": "A list stores many values in order, like ['apple', 'banana'].",
        "dictionary": "A dictionary stores key-value pairs, like {'name': 'Ali'}.",
    }

    return notes.get(concept.lower(), "I do not know that concept yet.")


def calculator(expression: str) -> str:
    """Calculate simple math with a small safety check."""

    allowed = set("0123456789+-*/(). ")

    if not set(expression).issubset(allowed):
        return "Error: unsafe expression."

    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except Exception as error:
        return f"Error: {error}"


TOOLS = [
    {
        "type": "function",
        "name": "explain_python",
        "description": "Explain a beginner/intermediate Python concept.",
        "parameters": {
            "type": "object",
            "properties": {
                "concept": {
                    "type": "string",
                    "description": "A Python concept like variable, loop, function, list, or dictionary.",
                }
            },
            "required": ["concept"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "calculator",
        "description": "Calculate a simple math expression.",
        "parameters": {
            "type": "object",
            "properties": {
                "expression": {
                    "type": "string",
                    "description": "A simple math expression.",
                }
            },
            "required": ["expression"],
            "additionalProperties": False,
        },
    },
]


def run_tool(name: str, arguments: dict) -> str:
    """Run only tools that we have approved."""

    if name == "explain_python":
        return explain_python(arguments["concept"])

    if name == "calculator":
        return calculator(arguments["expression"])

    return f"Tool not allowed: {name}"


def study_buddy_agent(task: str, max_turns: int = 6) -> str:
    """A small but real agent loop."""

    client = get_client()

    messages = [
        {
            "role": "developer",
            "content": (
                "You are a kind study buddy for a 13-year-old intermediate Python learner. "
                "Use tools when useful. Explain ideas simply. Give tiny code examples."
            ),
        },
        {
            "role": "user",
            "content": task,
        },
    ]
    previous_response_id = None

    for turn in range(max_turns):
        print(f"\nStudy buddy turn {turn + 1}")

        request = {
            "model": get_model(),
            "input": messages,
            "tools": TOOLS,
        }

        if previous_response_id is not None:
            request["previous_response_id"] = previous_response_id

        response = client.responses.create(**request)

        tool_calls = [item for item in response.output if item.type == "function_call"]

        if not tool_calls:
            return response.output_text

        for tool_call in tool_calls:
            arguments = json.loads(tool_call.arguments)
            result = run_tool(tool_call.name, arguments)

            print(f"Tool: {tool_call.name}")
            print(f"Arguments: {arguments}")
            print(f"Result: {result}")

            messages.append(
                {
                    "type": "function_call_output",
                    "call_id": tool_call.call_id,
                    "output": result,
                }
            )

        previous_response_id = response.id
        messages = messages[-len(tool_calls) :]

    return "I stopped because I reached my safety limit. Try asking a smaller question."


def main() -> None:
    answer = study_buddy_agent(
        "Teach me Python loops, then calculate how many practice problems I do if I solve 4 problems per day for 7 days."
    )

    print_box("STUDY BUDDY ANSWER", answer)


if __name__ == "__main__":
    main()
