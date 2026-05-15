def calculator(expression: str) -> str:
    allowed = set("0123456789+-*/(). ")

    if not set(expression).issubset(allowed):
        return "Error: unsafe expression."

    return str(eval(expression, {"__builtins__": {}}, {}))


def test_calculator() -> None:
    """Tiny test function without a testing framework."""

    assert calculator("2 + 2") == "4"
    assert calculator("10 * 3") == "30"
    assert calculator("__import__('os')") == "Error: unsafe expression."


def main() -> None:
    test_calculator()
    print("All tests passed.")


if __name__ == "__main__":
    main()

