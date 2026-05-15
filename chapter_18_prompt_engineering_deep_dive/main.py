PROMPT_TEMPLATE = """
Role:
You are a friendly Python tutor.

Task:
Explain the topic: {topic}

Audience:
A 13-year-old intermediate Python learner.

Rules:
- Use simple words.
- Give one tiny code example.
- Keep the answer short.

Output format:
1. Simple explanation
2. Tiny code
3. Practice challenge
"""


def build_prompt(topic: str) -> str:
    """Use a template so prompts stay consistent."""

    return PROMPT_TEMPLATE.format(topic=topic)


def main() -> None:
    print(build_prompt("Python functions"))


if __name__ == "__main__":
    main()

