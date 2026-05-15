# Chapter 22: Tool Design And Safety

Tools are where agents become powerful.

Tools are also where agents become risky.

A model can suggest an action, but your Python code decides what actually happens.

## 1. Tool Design Rule

Each tool should do one clear job.

Good:

```text
read_note(filename)
```

Bad:

```text
do_anything(command)
```

The second one is dangerous because it gives too much power.

## 2. Tool Names Matter

Good names:

- `read_note`
- `search_docs`
- `calculate_total`
- `create_task`

Bad names:

- `handle`
- `process`
- `run`
- `execute`

Clear names help the model choose correctly.

## 3. Tool Descriptions

The schema description should explain:

- what the tool does
- when to use it
- what inputs it expects
- what it does not do

## 4. Input Validation

Never trust tool arguments blindly.

Check:

- type
- allowed range
- allowed file path
- allowed action
- missing values

## 5. Idempotent Tools

Idempotent means safe to repeat.

Example:

```text
read_file("notes.txt")
```

Reading twice is usually safe.

Dangerous repeat:

```text
send_email(...)
```

Sending twice may annoy someone.

## 6. Human Confirmation

Ask for human confirmation before risky actions:

- delete files
- spend money
- send messages
- publish content
- change databases

## 7. Tool Errors

Tools should return helpful errors.

Bad:

```text
Error
```

Good:

```text
Error: file not found. Available files: agent_notes.txt, rag_notes.txt
```

## 8. Permissions

Give the agent the smallest power needed.

This is called least privilege.

Example:

If the agent only needs to read notes, do not give it a shell command tool.

