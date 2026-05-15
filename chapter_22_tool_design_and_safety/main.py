from pathlib import Path


ALLOWED_DIR = Path(__file__).resolve().parent / "allowed"


def validate_filename(filename: str) -> bool:
    """Allow only simple .txt filenames."""

    path = Path(filename)

    if path.name != filename:
        return False

    if path.suffix != ".txt":
        return False

    return True


def main() -> None:
    filenames = [
        "notes.txt",
        "../secret.txt",
        "image.png",
        "study_plan.txt",
    ]

    for filename in filenames:
        print(filename, "allowed:", validate_filename(filename))


if __name__ == "__main__":
    main()

