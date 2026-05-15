from dataclasses import dataclass, field


def estimate_tokens(text: str) -> int:
    """Very rough token estimate for learning purposes."""

    return max(1, len(text) // 4)


@dataclass
class ContextManager:
    """A tiny context manager for learning.

    This is not a full production memory system.
    It teaches the main pieces:
    - pinned facts
    - running summary
    - recent messages
    - compaction
    """

    pinned_facts: list[str] = field(default_factory=list)
    running_summary: str = ""
    recent_messages: list[str] = field(default_factory=list)
    max_recent_messages: int = 6

    def add_message(self, role: str, content: str) -> None:
        """Add a message and keep only the newest messages."""

        self.recent_messages.append(f"{role}: {content}")

        # Sliding window: keep only the newest N messages.
        if len(self.recent_messages) > self.max_recent_messages:
            self.recent_messages = self.recent_messages[-self.max_recent_messages :]

    def compact_old_messages(self, older_messages: list[str]) -> None:
        """Compact older messages into a running summary.

        A real app may ask an LLM to summarize.
        This demo uses simple joining so you understand the shape.
        """

        if not older_messages:
            return

        compacted = " | ".join(older_messages)

        if self.running_summary:
            self.running_summary += " | " + compacted
        else:
            self.running_summary = compacted

    def build_context(self, current_request: str) -> str:
        """Build the final text context that would be sent to a model."""

        sections = [
            "DEVELOPER INSTRUCTION:\nTeach clearly and safely.",
            "PINNED FACTS:\n" + "\n".join(f"- {fact}" for fact in self.pinned_facts),
            "RUNNING SUMMARY:\n" + (self.running_summary or "No summary yet."),
            "RECENT MESSAGES:\n" + "\n".join(self.recent_messages),
            "CURRENT USER REQUEST:\n" + current_request,
        ]

        return "\n\n".join(sections)


def main() -> None:
    manager = ContextManager(
        pinned_facts=[
            "User is learning agentic AI in Python.",
            "User prefers simple explanations with commented code.",
            "Never include secrets like .env files in context.",
        ]
    )

    old_messages = [
        "User asked to create chapters 1-10.",
        "Assistant created beginner agent chapters.",
        "User asked for professional structure.",
        "Assistant added chapters about schemas, routers, and safe file tools.",
    ]

    manager.compact_old_messages(old_messages)

    manager.add_message("user", "How do I handle context memory?")
    manager.add_message("assistant", "Use sliding windows, summaries, and retrieval.")

    context = manager.build_context("Explain compaction deeply.")

    print(context)
    print("\nEstimated tokens:", estimate_tokens(context))


if __name__ == "__main__":
    main()

