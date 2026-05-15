from enum import Enum


class State(Enum):
    START = "start"
    PLAN = "plan"
    EXECUTE = "execute"
    VERIFY = "verify"
    FINISH = "finish"


def next_state(current: State) -> State:
    """Define the allowed workflow transitions."""

    transitions = {
        State.START: State.PLAN,
        State.PLAN: State.EXECUTE,
        State.EXECUTE: State.VERIFY,
        State.VERIFY: State.FINISH,
    }

    return transitions.get(current, State.FINISH)


def main() -> None:
    state = State.START

    while state != State.FINISH:
        print("Current state:", state.value)
        state = next_state(state)

    print("Current state:", state.value)
    print("Workflow completed.")


if __name__ == "__main__":
    main()

