# Chapter 36: Retries, Timeouts, And Error Handling

Real systems fail.

APIs fail.
Networks fail.
Tools fail.
Models return weird output sometimes.

Professional agents expect failure.

## 1. Retry

Retry means try again after a temporary failure.

Useful for:

- network errors
- rate limits
- temporary service problems

Do not retry forever.

## 2. Backoff

Backoff means wait longer each retry.

Example:

```text
wait 1 second
wait 2 seconds
wait 4 seconds
```

This avoids hammering a struggling service.

## 3. Timeout

A timeout stops waiting after too long.

Example:

```text
If tool takes more than 10 seconds, fail gracefully.
```

## 4. Useful Error Messages

Bad:

```text
Failed.
```

Good:

```text
Search tool timed out after 10 seconds. Try a smaller query.
```

## 5. Agent Error Strategy

When a tool fails, the agent can:

- try another tool
- ask the user for clarification
- explain the problem
- stop safely

## Run

```powershell
python chapter_36_retries_timeouts_errors/main.py
```

