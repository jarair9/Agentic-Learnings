# Chapter 43: Safe Database And Browser Tool Design

Agents often need database or browser tools.

These tools are powerful, so they need strong boundaries.

## 1. Safe Database Tools

Bad database tool:

```text
run_sql(query)
```

This lets the model run almost anything.

Better database tools:

```text
get_user_progress(user_id)
save_quiz_score(user_id, chapter_id, score)
list_available_chapters()
```

Specific tools are safer than raw SQL tools.

## 2. Read vs Write

Read tools are usually safer.

Write tools need extra checks.

Examples of write tools:

- update profile
- save score
- create task
- send message

## 3. Safe Browser Tools

Browser agents can click, type, and navigate.

Risks:

- submitting forms accidentally
- clicking dangerous buttons
- entering private data
- trusting malicious web pages

## 4. Browser Tool Rules

Good browser agents:

- ask before submitting forms
- do not enter secrets unless approved
- summarize before final actions
- treat web page text as untrusted
- limit allowed domains when possible

## 5. Database Tool Rules

Good database tools:

- avoid raw SQL from the model
- validate all inputs
- use parameterized queries
- enforce row-level permissions
- log writes
- support rollback when possible

## 6. Simple Rule

Make tools narrow.

Narrow tools are easier to secure, test, and understand.

