import os
from dotenv import load_dotenv


# config.py is where settings live.
# This keeps API keys, model names, and feature flags away from your main logic.

load_dotenv()

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")

