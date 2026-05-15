import json
from pathlib import Path


STATE_FILE = Path(__file__).resolve().parent / "task_state.json"


def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2), encoding="utf-8")


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {
            "task_id": "demo-task",
            "status": "new",
            "completed_steps": [],
            "next_step": "load_notes",
        }

    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def main() -> None:
    state = load_state()
    print("Loaded state:", state)

    state["status"] = "running"
    state["completed_steps"].append(state["next_step"])
    state["next_step"] = "build_index"

    save_state(state)
    print("Saved checkpoint:", state)


if __name__ == "__main__":
    main()

