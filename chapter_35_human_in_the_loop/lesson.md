# Chapter 35: Human-In-The-Loop Approvals

Human-in-the-loop means the agent must ask a human before risky actions.

This is one of the most important safety patterns.

## 1. Why Approval Matters

Some actions should not happen automatically:

- delete a file
- send an email
- spend money
- post online
- change a database
- run shell commands

The model can suggest the action.

The human approves or rejects it.

## 2. Approval Gate

An approval gate is code that pauses before a risky action.

Example:

```text
Agent wants to delete report.txt.
Human approval required.
```

## 3. Risk Levels

You can classify tools:

```text
safe: read_note, search_docs
medium: create_draft
risky: send_email, delete_file, publish_post
```

Only risky tools require approval.

## 4. Good Approval Message

A good approval message says:

- what will happen
- what data is affected
- why the agent wants it
- what could go wrong

## Run

```powershell
python chapter_35_human_in_the_loop/main.py
```

