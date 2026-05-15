from pathlib import Path


# Only files inside this folder can be read.
ALLOWED_FOLDER = Path(__file__).resolve().parents[1] / "workspace_files"


def read_text_file(relative_path: str) -> str:
    """Safely read a text file for the AI.

    Important safety lesson:
    Never let an AI read any path it wants.
    Always limit it to an allowed folder.
    """

    requested_path = (ALLOWED_FOLDER / relative_path).resolve()
    allowed_root = ALLOWED_FOLDER.resolve()

    # Check that the final resolved path is still inside ALLOWED_FOLDER.
    # This blocks tricks like ../../.env.
    if allowed_root not in requested_path.parents and requested_path != allowed_root:
        return "Error: that file path is outside the allowed folder."

    if not requested_path.exists():
        return f"Error: file not found: {relative_path}"

    if requested_path.suffix.lower() != ".txt":
        return "Error: only .txt files are allowed in this learning example."

    return requested_path.read_text(encoding="utf-8")

