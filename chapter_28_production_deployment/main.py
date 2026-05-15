import time
from dataclasses import dataclass


@dataclass
class TraceEvent:
    name: str
    detail: str
    timestamp: float


def main() -> None:
    trace = []

    trace.append(TraceEvent("user_request", "Explain agent loops", time.time()))
    trace.append(TraceEvent("tool_call", "read_note(agent_loops.txt)", time.time()))
    trace.append(TraceEvent("final_answer", "Returned explanation", time.time()))

    for event in trace:
        print(event)


if __name__ == "__main__":
    main()

