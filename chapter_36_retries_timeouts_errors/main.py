import time


def flaky_tool(attempt: int) -> str:
    """Pretend this tool fails at first and succeeds later."""

    if attempt < 3:
        raise RuntimeError("Temporary API problem")

    return "Tool succeeded"


def run_with_retries(max_attempts: int = 4) -> str:
    for attempt in range(1, max_attempts + 1):
        try:
            return flaky_tool(attempt)
        except RuntimeError as error:
            wait_seconds = 2 ** (attempt - 1)
            print(f"Attempt {attempt} failed: {error}")

            if attempt == max_attempts:
                return "Tool failed after all retries."

            print(f"Waiting {wait_seconds} seconds before retrying.")
            time.sleep(0.1)  # Short sleep for learning demo.

    return "Unexpected retry state."


def main() -> None:
    print(run_with_retries())


if __name__ == "__main__":
    main()

