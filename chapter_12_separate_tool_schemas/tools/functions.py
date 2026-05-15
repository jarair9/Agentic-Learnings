# functions.py contains the real Python functions.
# These functions know nothing about OpenAI schemas.
# That makes them easy to test later.


def explain_python_concept(concept: str) -> str:
    notes = {
        "function": "A function is a reusable block of code. You define it once and call it many times.",
        "loop": "A loop repeats code while something is true or for every item in a collection.",
        "list": "A list stores many values in order.",
    }

    return notes.get(concept.lower(), f"I do not have notes for {concept} yet.")

