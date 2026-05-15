TOOLS_FROM_FAKE_MCP_SERVER = [
    {
        "name": "search_notes",
        "description": "Search learning notes.",
    },
    {
        "name": "read_note",
        "description": "Read one note by filename.",
    },
]


def list_available_tools() -> None:
    """Pretend we asked an external tool server what it supports."""

    for tool in TOOLS_FROM_FAKE_MCP_SERVER:
        print(f"{tool['name']}: {tool['description']}")


def main() -> None:
    list_available_tools()


if __name__ == "__main__":
    main()

