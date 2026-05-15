from collections import deque


job_queue = deque()


def add_job(job_type: str, payload: dict) -> None:
    job_queue.append({"type": job_type, "payload": payload, "status": "pending"})


def run_next_job() -> None:
    if not job_queue:
        print("No jobs.")
        return

    job = job_queue.popleft()
    job["status"] = "running"
    print("Running job:", job)
    job["status"] = "completed"
    print("Completed job:", job)


def main() -> None:
    add_job("build_rag_index", {"folder": "chapters"})
    add_job("grade_quiz", {"user": "ali", "chapter": 51})

    run_next_job()
    run_next_job()


if __name__ == "__main__":
    main()

