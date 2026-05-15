RISKY_TOOLS = {"delete_file", "send_email", "publish_post"}


def needs_approval(tool_name: str) -> bool:
    return tool_name in RISKY_TOOLS


def run_tool(tool_name: str, arguments: dict, approved: bool = False) -> str:
    """Block risky tools unless approved."""

    if needs_approval(tool_name) and not approved:
        return (
            f"Approval required before running {tool_name} "
            f"with arguments {arguments}."
        )

    return f"Ran {tool_name} with {arguments}."


def main() -> None:
    print(run_tool("read_note", {"filename": "agent_loops.txt"}))
    print(run_tool("send_email", {"to": "teacher@example.com"}))
    print(run_tool("send_email", {"to": "teacher@example.com"}, approved=True))


if __name__ == "__main__":
    main()

