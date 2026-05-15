import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def main() -> None:
    client = get_client()

    # We store messages in a list.
    # Each message has a role and content.
    # "user" means the human spoke.
    # "assistant" means the AI spoke.
    conversation = [
        {
            "role": "user",
            "content": "My name is Ali. I want to learn agentic AI in Python.",
        }
    ]

    first_response = client.responses.create(
        model=get_model(),
        input=conversation,
    )

    print_box("FIRST ANSWER", first_response.output_text)

    # Now we add the assistant answer to memory.
    conversation.append(
        {
            "role": "assistant",
            "content": first_response.output_text,
        }
    )

    # Ask a follow-up question that depends on memory.
    conversation.append(
        {
            "role": "user",
            "content": "What is my name, and what topic do I want to learn?",
        }
    )

    second_response = client.responses.create(
        model=get_model(),
        input=conversation,
    )

    print_box("SECOND ANSWER WITH MEMORY", second_response.output_text)


if __name__ == "__main__":
    main()

