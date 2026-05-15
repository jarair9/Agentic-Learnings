import asyncio


TOOL_PERMISSIONS = {
    "read_note": "safe",
    "search_docs": "safe",
    "send_email": "risky",
    "delete_file": "forbidden",
}


def is_tool_allowed(tool_name: str) -> bool:
    return TOOL_PERMISSIONS.get(tool_name) in {"safe", "medium"}


async def fake_tool(tool_name: str) -> str:
    """Pretend to run a tool asynchronously."""

    if not is_tool_allowed(tool_name):
        return f"Blocked tool: {tool_name}"

    await asyncio.sleep(0.1)
    return f"Finished tool: {tool_name}"


async def main() -> None:
    results = await asyncio.gather(
        fake_tool("read_note"),
        fake_tool("search_docs"),
        fake_tool("delete_file"),
    )

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())

