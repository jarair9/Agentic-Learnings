import asyncio


async def fake_tool(name: str, delay: float) -> str:
    """Pretend this tool is waiting for a slow API."""

    print(f"Starting {name}")
    await asyncio.sleep(delay)
    print(f"Finished {name}")
    return f"{name} result"


async def main() -> None:
    # These tools run at the same time.
    results = await asyncio.gather(
        fake_tool("search_notes", 1.0),
        fake_tool("read_profile", 1.5),
        fake_tool("load_config", 0.5),
    )

    print(results)


if __name__ == "__main__":
    asyncio.run(main())

