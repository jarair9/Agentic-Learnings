import json
from pathlib import Path


MEMORY_FILE = Path(__file__).resolve().parent / "memory.json"


def load_memory() -> dict:
    """Load long-term memory from a JSON file."""

    if not MEMORY_FILE.exists():
        return {"facts": []}

    return json.loads(MEMORY_FILE.read_text(encoding="utf-8"))


def save_memory(memory: dict) -> None:
    """Save long-term memory to a JSON file."""

    MEMORY_FILE.write_text(json.dumps(memory, indent=2), encoding="utf-8")


def remember_fact(fact: str) -> None:
    memory = load_memory()
    memory["facts"].append(fact)
    save_memory(memory)


def main() -> None:
    remember_fact("The student is learning agentic AI in Python.")
    print(load_memory())


if __name__ == "__main__":
    main()

