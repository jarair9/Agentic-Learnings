# Chapter 24: Testing AI Agents

Testing agents is different from testing normal code.

Normal code:

```text
same input -> same output
```

AI code:

```text
same input -> similar but not always identical output
```

So we test in layers.

## 1. Test Normal Python First

Test:

- tool functions
- routers
- file safety
- JSON parsing
- validators

These should be deterministic.

## 2. Mock Model Responses

Do not call the real model in every test.

Instead, fake a response:

```text
model asks for read_note
tool returns note text
agent continues
```

## 3. Golden Tests

A golden test stores expected behavior.

Example:

```text
Question: What is an agent loop?
Expected: mentions model, tool, result, loop, safety limit
```

Do not require exact wording. Check important ideas.

## 4. Evaluation Datasets

For serious agents, create a small dataset:

```text
input question
expected tool
expected facts
bad answer examples
```

Run it after prompt or tool changes.

## 5. Regression Testing

A regression means something used to work but now fails.

Agent changes can break old behavior quietly.

Keep test cases for important tasks.

## 6. Human Review

For learning projects, human review is enough.

For production, combine:

- automated tests
- model-based grading
- human review
- logs/traces

