import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()

MODEL = os.getenv("OPENAI_MODEL", "gpt-5-mini")
MAX_TURNS = 6

# The agent can only read files from this folder.
PROJECT_DIR = Path(__file__).resolve().parents[1]
KNOWLEDGE_DIR = PROJECT_DIR / "knowledge"

