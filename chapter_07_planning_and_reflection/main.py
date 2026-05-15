import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def ask(prompt: str) -> str:
    client = get_client()

    response = client.responses.create(
        model=get_model(),
        input=prompt,
    )

    return response.output_text


def main() -> None:
    task = "Teach me the difference between an AI chatbot and an AI agent."

    plan_prompt = f"""
You are planning a short lesson for a 13-year-old Python learner.
Task: {task}

Return a simple 3-step teaching plan.
"""

    plan = ask(plan_prompt)
    print_box("PLAN", plan)

    answer_prompt = f"""
Use this plan to write the lesson:

{plan}

Lesson task:
{task}

Keep it clear and friendly.
"""

    answer = ask(answer_prompt)
    print_box("FIRST DRAFT LESSON", answer)

    reflection_prompt = f"""
Review this lesson like a careful teacher.
Find anything confusing, too advanced, or missing.
Then rewrite the lesson better.

Lesson:
{answer}
"""

    improved_answer = ask(reflection_prompt)
    print_box("IMPROVED LESSON AFTER REFLECTION", improved_answer)


if __name__ == "__main__":
    main()

