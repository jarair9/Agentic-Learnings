# Chapter 09: Safety Limits

Agents can loop, call tools, and take actions.

That means we need guardrails.

Simple guardrails include:

- max turns
- allowed tools only
- input checks
- confirmation before risky actions
- clear error messages

This chapter shows a small safety gate before a tool runs.

## Run

```powershell
python chapter_09_safety_limits/main.py
```

