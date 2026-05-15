import json
from collections.abc import Callable

from course_helpers import get_client, get_model


class AgentRunner:
    """A reusable agent loop.

    This class is not magic.
    It just packages the same loop you already learned:
    model -> tool call -> Python function -> tool result -> model again.
    """

    def __init__(
        self,
        tools: list[dict],
        tool_runner: Callable[[str, dict], str],
        max_turns: int = 5,
    ) -> None:
        self.client = get_client()
        self.model = get_model()
        self.tools = tools
        self.tool_runner = tool_runner
        self.max_turns = max_turns

    def run(self, task: str) -> str:
        """Run the agent until it gives a final answer or hits max_turns."""

        input_items = [
            {
                "role": "user",
                "content": task,
            }
        ]
        previous_response_id = None

        for _turn in range(self.max_turns):
            request = {
                "model": self.model,
                "input": input_items,
                "tools": self.tools,
            }

            if previous_response_id is not None:
                request["previous_response_id"] = previous_response_id

            response = self.client.responses.create(**request)
            tool_calls = [item for item in response.output if item.type == "function_call"]

            if not tool_calls:
                return response.output_text

            input_items = []

            for tool_call in tool_calls:
                arguments = json.loads(tool_call.arguments)
                result = self.tool_runner(tool_call.name, arguments)

                input_items.append(
                    {
                        "type": "function_call_output",
                        "call_id": tool_call.call_id,
                        "output": result,
                    }
                )

            previous_response_id = response.id

        return "Agent stopped because it reached the max_turns safety limit."

