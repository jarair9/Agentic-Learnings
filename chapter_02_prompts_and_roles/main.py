import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def ask_ai(prompt: str) -> str:
    """Send one prompt to the model and return the answer."""

    client = get_client()

    response = client.responses.create(
        model=get_model(),
        input=prompt,
    )

    return response.output_text


def main() -> None:
    weak_prompt = "Tell me about agents."

    strong_prompt = """
You are a friendly Python teacher.
Explain AI agents to a 13-year-old intermediate Python learner.
Use:
- one simple analogy
- three bullet points
- one tiny Python idea
Keep it short.
"""

    weak_answer = ask_ai(weak_prompt)
    strong_answer = ask_ai(strong_prompt)

    print_box("WEAK PROMPT ANSWER", weak_answer)
    print_box("STRONG PROMPT ANSWER", strong_answer)


if __name__ == "__main__":
    main()

