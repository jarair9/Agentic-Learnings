import sys
from pathlib import Path


# This lets Python import course_helpers.py from the project root.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def main() -> None:
    # Step 1: Create a client.
    # Think of the client like a phone that can call the AI service.
    client = get_client()

    # Step 2: Pick a model.
    # A model is the AI brain we are asking for help.
    model = get_model()

    # Step 3: Write a simple user request.
    user_question = "Explain agentic AI to a 13 year old in 4 short lines."

    # Step 4: Send the request using the Responses API.
    response = client.responses.create(
        model=model,
        input=user_question,
    )

    # Step 5: Print the model's text answer.
    # output_text is the easy way to get the final text from the response.
    print_box("AI ANSWER", response.output_text)


if __name__ == "__main__":
    main()

