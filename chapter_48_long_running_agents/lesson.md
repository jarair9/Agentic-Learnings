# Chapter 48: Long-Running Agents And Durable Task State

Some agents finish in seconds.

Others run for minutes, hours, or days.

Long-running agents need durable state.

## 1. What Is Durable State?

Durable state survives if the program stops.

Example:

```json
{
  "task_id": "study-report-001",
  "status": "running",
  "completed_steps": ["loaded notes", "built index"],
  "next_step": "write report"
}
```

If the app crashes, it can resume.

## 2. Why Long-Running Agents Are Hard

Problems:

- tool failures
- timeouts
- user changes mind
- process restarts
- partial progress
- duplicate actions

## 3. Checkpoints

A checkpoint saves progress after important steps.

Example:

```text
after loading files -> save checkpoint
after retrieval -> save checkpoint
after draft -> save checkpoint
```

## 4. Resuming

On resume, the agent should ask:

```text
What was done?
What is next?
Is it still safe to continue?
```

## 5. Idempotency Again

Long-running agents may repeat a step after restart.

So steps should be safe to repeat when possible.

Example:

```text
safe: read file
risky: send email twice
```

## 6. User Visibility

Long tasks should show progress.

Example:

```text
Status: indexing 12 of 40 files
Status: writing draft
Status: waiting for approval
```

