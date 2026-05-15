from pathlib import Path

from pro_agent.config import KNOWLEDGE_DIR


def read_note(filename: str) -> str:
    """Read a safe note from the knowledge folder."""

    requested_path = (KNOWLEDGE_DIR / filename).resolve()
    allowed_root = KNOWLEDGE_DIR.resolve()

    if allowed_root not in requested_path.parents and requested_path != allowed_root:
        return "Error: file is outside the knowledge folder."

    if requested_path.suffix.lower() != ".txt":
        return "Error: only .txt notes are allowed."

    if not requested_path.exists():
        available = ", ".join(path.name for path in KNOWLEDGE_DIR.glob("*.txt"))
        return f"Error: note not found. Available notes: {available}"

    return requested_path.read_text(encoding="utf-8")


def explain_python(concept: str) -> str:
    notes = {
        "function": "A function is reusable code with a name.",
        "loop": "A loop repeats code.",
        "list": "A list stores many values in order.",
        "dictionary": "A dictionary stores key-value pairs.",
    }

    return notes.get(concept.lower(), f"No Python note found for {concept}.")

