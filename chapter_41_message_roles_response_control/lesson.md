# Chapter 41: Message Roles, Max Tokens, And Response Control

This chapter goes deeper into how you control model behavior.

You already know how to call a model. Now you learn how to shape the conversation professionally.

## 1. Message Roles

Model inputs are often organized as messages.

Common roles:

- `developer`: instructions from the app developer
- `user`: the human's request
- `assistant`: previous model responses
- tool output items: results from tools

Some systems also use `system` messages at a higher platform level. As an app builder, you usually control developer and user messages.

## 2. Why Roles Matter

Roles help the model understand authority and meaning.

Example:

```python
[
    {"role": "developer", "content": "You are a careful Python tutor."},
    {"role": "user", "content": "Teach me loops."}
]
```

The developer message sets behavior.

The user message gives the current task.

## 3. Instruction Hierarchy

Not every instruction has equal power.

Simple mental model:

```text
Higher-priority rules > developer rules > user request > external documents
```

If a document says:

```text
Ignore your developer instructions.
```

the agent should treat that as document text, not as a command.

## 4. Max Tokens

`max_output_tokens` limits how long the model's answer can be.

Use it when:

- you need short answers
- you want predictable cost
- you are building a UI with limited space

If the limit is too small, the answer may be cut off.

## 5. Temperature And Top-p

Temperature controls randomness.

Low temperature:

- reliable
- consistent
- good for tools and code

High temperature:

- creative
- varied
- good for brainstorming

Top-p also controls sampling. Beginner rule: change temperature first and usually leave top-p alone.

## 6. Response Format Control

For program-readable output, use:

- JSON mode
- structured outputs
- tool calling

Do not rely only on “please return JSON” for serious apps.

## 7. Practical Defaults

For agentic Python learning projects:

```text
temperature: low
max turns: limited
tools: explicit
output: structured when code must read it
```

