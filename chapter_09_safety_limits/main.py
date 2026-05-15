def is_safe_file_action(action: str, path: str) -> bool:
    """Decide if a fake file action should be allowed.

    This example does not touch real files.
    It teaches the safety idea before you build real tools.
    """

    blocked_actions = {"delete", "overwrite"}
    blocked_paths = {"C:/Windows", "/etc", "secrets.txt", ".env"}

    if action.lower() in blocked_actions:
        return False

    for blocked_path in blocked_paths:
        if blocked_path.lower() in path.lower():
            return False

    return True


def main() -> None:
    examples = [
        ("read", "notes.txt"),
        ("delete", "notes.txt"),
        ("read", ".env"),
        ("overwrite", "homework.py"),
    ]

    for action, path in examples:
        allowed = is_safe_file_action(action, path)

        print(f"Action: {action:9} Path: {path:12} Allowed: {allowed}")


if __name__ == "__main__":
    main()

