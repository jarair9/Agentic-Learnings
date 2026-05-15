from tools.functions import explain_python_concept


def run_tool(name: str, arguments: dict) -> str:
    """Run the correct Python function for a model-requested tool."""

    # The router is like a reception desk.
    # The model asks for a tool by name.
    # The router sends the request to the correct Python function.
    if name == "explain_python_concept":
        return explain_python_concept(arguments["concept"])

    return f"Unknown tool: {name}"

