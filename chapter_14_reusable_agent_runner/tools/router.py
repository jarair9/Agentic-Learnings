from tools.functions import explain_python


def run_tool(name: str, arguments: dict) -> str:
    if name == "explain_python":
        return explain_python(arguments["concept"])

    return f"Unknown tool: {name}"

