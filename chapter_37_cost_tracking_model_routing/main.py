FAKE_PRICES_PER_1K_TOKENS = {
    "small": {"input": 0.001, "output": 0.002},
    "strong": {"input": 0.01, "output": 0.03},
}


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def estimate_cost(model_size: str, input_text: str, output_text: str) -> float:
    prices = FAKE_PRICES_PER_1K_TOKENS[model_size]
    input_tokens = estimate_tokens(input_text)
    output_tokens = estimate_tokens(output_text)

    return (
        input_tokens / 1000 * prices["input"]
        + output_tokens / 1000 * prices["output"]
    )


def route_model(task: str) -> str:
    hard_words = ["debug", "architecture", "security", "plan", "evaluate"]

    if any(word in task.lower() for word in hard_words):
        return "strong"

    return "small"


def main() -> None:
    task = "Plan a secure agent architecture."
    model_size = route_model(task)
    cost = estimate_cost(model_size, task, "Example answer text")

    print("Task:", task)
    print("Chosen model size:", model_size)
    print("Estimated fake cost:", round(cost, 6))


if __name__ == "__main__":
    main()

