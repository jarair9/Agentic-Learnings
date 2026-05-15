import os
from dotenv import load_dotenv
from openai import OpenAI


# This file contains tiny helper functions shared by all chapters.
# Helpers keep the chapter files shorter, so you can focus on the new idea.


def get_client() -> OpenAI:
    """Create the OpenAI client after loading environment variables."""

    # load_dotenv reads a local .env file if you create one.
    # This is easier than typing the API key every time.
    load_dotenv()

    # The OpenAI() client automatically looks for OPENAI_API_KEY.
    return OpenAI()


def get_model() -> str:
    """Return the model name we want to use."""

    # You can change the model without editing code:
    # PowerShell: $env:OPENAI_MODEL="gpt-5-mini"
    return os.getenv("OPENAI_MODEL", "gpt-5-mini")


def print_box(title: str, text: str) -> None:
    """Print output in a simple readable box."""

    line = "=" * 70
    print(f"\n{line}")
    print(title)
    print(line)
    print(text)
    print(line)

