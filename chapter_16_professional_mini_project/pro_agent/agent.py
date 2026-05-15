import json

from openai import OpenAI

from pro_agent.config import MAX_TURNS, MODEL
from pro_agent.prompts import DEVELOPER_PROMPT
from pro_agent.tools.router import run_tool
from pro_agent.tools.schemas import TOOL_SCHEMAS


class StudyAgent:
    """A small professional-style study agent."""

    def __init__(self) -> None:
        self.client = OpenAI()
        self.model = MODEL
        self.max_turns = MAX_TURNS

    def run(self, task: str) -> str:
        input_items = [
            {
                "role": "developer",
                "content": DEVELOPER_PROMPT,
            },
            {
                "role": "user",
                "content": task,
            },
        ]
        previous_response_id = None

        for _turn in range(self.max_turns):
            request = {
                "model": self.model,
                "input": input_items,
                "tools": TOOL_SCHEMAS,
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
                result = run_tool(tool_call.name, arguments)

                input_items.append(
                    {
                        "type": "function_call_output",
                        "call_id": tool_call.call_id,
                        "output": result,
                    }
                )

            previous_response_id = response.id

        return "I stopped because I reached my safety limit."

