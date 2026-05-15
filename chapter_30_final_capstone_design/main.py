CAPSTONE_CHECKLIST = [
    "Create folder structure",
    "Write developer prompt",
    "Create safe read-file tool",
    "Separate tool schemas",
    "Create tool router",
    "Build agent loop",
    "Add memory",
    "Add logging",
    "Add tests",
    "Run evaluation questions",
]


def main() -> None:
    print("Final Capstone Build Checklist")
    print("=" * 32)

    for index, item in enumerate(CAPSTONE_CHECKLIST, start=1):
        print(f"{index}. {item}")


if __name__ == "__main__":
    main()

