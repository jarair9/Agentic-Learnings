from pro_agent.tools.functions import explain_python, read_note


def run_tool(name: str, arguments: dict) -> str:
    """Connect model-requested tool names to Python functions."""

    if name == "read_note":
        return read_note(arguments["filename"])

    if name == "explain_python":
        return explain_python(arguments["concept"])

    return f"Unknown tool: {name}"

