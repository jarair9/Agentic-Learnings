def plan_node(state: dict) -> dict:
    state["plan"] = ["draft answer", "review answer"]
    return state


def draft_node(state: dict) -> dict:
    state["draft"] = f"Draft answer for: {state['task']}"
    return state


def review_node(state: dict) -> dict:
    state["review"] = "pass" if "Draft" in state["draft"] else "fail"
    return state


def choose_next_after_review(state: dict) -> str:
    return "finish" if state["review"] == "pass" else "draft"


def main() -> None:
    state = {"task": "Explain planning graphs"}

    state = plan_node(state)
    state = draft_node(state)
    state = review_node(state)

    print(state)
    print("Next node:", choose_next_after_review(state))


if __name__ == "__main__":
    main()

