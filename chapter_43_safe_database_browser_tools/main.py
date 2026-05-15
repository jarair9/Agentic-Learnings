ALLOWED_DB_ACTIONS = {"get_progress", "list_chapters", "save_quiz_score"}
RISKY_BROWSER_ACTIONS = {"submit_form", "click_buy", "enter_password"}


def check_database_action(action: str) -> bool:
    """Allow only known database actions."""

    return action in ALLOWED_DB_ACTIONS


def check_browser_action(action: str, approved: bool = False) -> bool:
    """Require approval for risky browser actions."""

    if action in RISKY_BROWSER_ACTIONS:
        return approved

    return True


def main() -> None:
    print("run_sql allowed:", check_database_action("run_sql"))
    print("get_progress allowed:", check_database_action("get_progress"))
    print("submit_form allowed:", check_browser_action("submit_form"))
    print("submit_form approved:", check_browser_action("submit_form", approved=True))


if __name__ == "__main__":
    main()

