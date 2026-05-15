def explain_python(concept: str) -> str:
    notes = {
        "list": "A list stores many values in order. Example: scores = [10, 20, 30].",
        "function": "A function stores reusable steps under one name.",
        "loop": "A loop repeats code.",
    }

    return notes.get(concept.lower(), f"No note found for {concept}.")

