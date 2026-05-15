from openai import OpenAI

from app.config import OPENAI_MODEL
from app.prompts import TEACHER_STYLE


def answer_question(question: str) -> str:
    """Ask the AI one question using our shared project structure."""

    client = OpenAI()

    response = client.responses.create(
        model=OPENAI_MODEL,
        input=[
            {
                "role": "developer",
                "content": TEACHER_STYLE,
            },
            {
                "role": "user",
                "content": question,
            },
        ],
    )

    return response.output_text

