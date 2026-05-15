MODELS = ["strong_model", "small_model", "offline_template"]


def fake_model_call(model: str, task: str) -> str:
    """Pretend the first model fails."""

    if model == "strong_model":
        raise RuntimeError("Rate limit")

    if model == "small_model":
        return f"{model} answered: {task}"

    return "Offline fallback: please try again later."


def call_with_fallback(task: str) -> str:
    errors = []

    for model in MODELS:
        try:
            return fake_model_call(model, task)
        except RuntimeError as error:
            errors.append(f"{model}: {error}")

    return "All model options failed. Errors: " + "; ".join(errors)


def main() -> None:
    print(call_with_fallback("Explain context compaction."))


if __name__ == "__main__":
    main()

