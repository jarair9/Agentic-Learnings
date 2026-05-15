# Chapter 20: Memory Types In Agents

Memory is one of the most misunderstood agent concepts.

Memory does not mean “the AI magically remembers everything.”

Memory means your program stores information and gives the useful parts back to the model.

## 1. Short-Term Memory

Short-term memory is the current conversation or task context.

Example:

```text
User: My name is Ali.
Later: What is my name?
```

If the earlier message is still in context, the model can answer.

## 2. Working Memory

Working memory is temporary task state.

Example:

```python
current_goal = "build a file-reading tool"
completed_steps = ["created schema", "created function"]
```

This helps the agent track progress.

## 3. Long-Term Memory

Long-term memory is saved outside the current conversation.

Examples:

- database
- JSON file
- vector store
- notes folder

Use long-term memory for facts that should survive after the program ends.

## 4. Semantic Memory

Semantic memory stores general facts.

Example:

```text
The user is learning Python.
The user prefers simple explanations.
```

## 5. Episodic Memory

Episodic memory stores events.

Example:

```text
On May 15, the user built chapters 1-16 of an agentic AI course.
```

## 6. Procedural Memory

Procedural memory stores how to do things.

Example:

```text
When creating a new tool, create schema, function, router, and test.
```

## 7. Memory Problems

Memory can go wrong.

Problems:

- storing too much
- storing wrong facts
- retrieving irrelevant facts
- leaking private information
- making the agent overconfident

## 8. Good Memory Rules

Good memory should be:

- useful
- accurate
- small
- updateable
- safe
- easy to delete

## Mental Model

Think of memory like a notebook.

A smart student does not copy every word from every class. They write the important things clearly.

