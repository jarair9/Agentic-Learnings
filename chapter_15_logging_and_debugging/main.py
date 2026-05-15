import logging


def setup_logging() -> None:
    """Configure logs once when the program starts."""

    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s | %(message)s",
    )


def fake_tool(name: str, arguments: dict) -> str:
    """A fake tool so we can learn logging without paying for API calls."""

    logging.info("Tool requested: %s", name)
    logging.info("Tool arguments: %s", arguments)

    if name != "explain_python":
        logging.error("Unknown tool: %s", name)
        return "Unknown tool"

    return "A function is reusable code."


def main() -> None:
    setup_logging()

    logging.info("Agent started")

    result = fake_tool("explain_python", {"concept": "function"})

    logging.info("Tool result: %s", result)
    logging.info("Agent finished")


if __name__ == "__main__":
    main()

