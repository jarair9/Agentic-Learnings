USER_ROLES = {
    "ali": "student",
    "teacher_mina": "teacher",
}

ROLE_PERMISSIONS = {
    "student": {"read_lesson", "take_quiz"},
    "teacher": {"read_lesson", "take_quiz", "create_lesson", "view_progress"},
}


def can_user_run_tool(username: str, tool_name: str) -> bool:
    role = USER_ROLES.get(username)

    if role is None:
        return False

    return tool_name in ROLE_PERMISSIONS[role]


def main() -> None:
    print("Ali create_lesson:", can_user_run_tool("ali", "create_lesson"))
    print("Teacher create_lesson:", can_user_run_tool("teacher_mina", "create_lesson"))


if __name__ == "__main__":
    main()

