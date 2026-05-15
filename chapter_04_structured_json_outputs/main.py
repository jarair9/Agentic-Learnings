import json
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from course_helpers import get_client, get_model, print_box


def main() -> None:
    client = get_client()

    prompt = """
Create a tiny study plan for learning AI agents.
Return only valid JSON with these keys:
- topic
- difficulty
- steps
- warning
"""

    response = client.responses.create(
        model=get_model(),
        input=prompt,
        # JSON mode tells the API we want valid JSON, not normal paragraphs.
        # Later, you can learn stricter JSON Schema validation too.
        text={"format": {"type": "json_object"}},
    )

    raw_text = response.output_text
    print_box("RAW JSON TEXT FROM MODEL", raw_text)

    # json.loads turns a JSON string into real Python data.
    # If the model returns invalid JSON, this line will raise an error.
    data = json.loads(raw_text)

    print("\nPython can now access the fields:")
    print("Topic:", data["topic"])
    print("Difficulty:", data["difficulty"])
    print("First step:", data["steps"][0])


if __name__ == "__main__":
    main()
