# Chapter 46: Planning Graphs And LangGraph-Style Workflows

Some agent workflows are not simple loops.

They are graphs.

## 1. What Is A Planning Graph?

A graph has nodes and edges.

Node:

```text
Plan
Search
Write
Review
Finish
```

Edge:

```text
Plan -> Search
Search -> Write
Write -> Review
Review -> Finish
```

## 2. Why Graphs Help

Graphs help when workflows branch.

Example:

```text
If review passes -> finish
If review fails -> revise
```

This is more structured than a free agent loop.

## 3. LangGraph-Style Idea

LangGraph-style workflows use graph nodes for agent steps.

You do not need the library to understand the idea.

Core concept:

```text
state flows through nodes
each node updates state
edges decide next node
```

## 4. State

State is the shared data carried through the graph.

Example:

```python
{
    "task": "teach RAG",
    "plan": [],
    "draft": "",
    "review": ""
}
```

## 5. Conditional Edges

Conditional edges choose the next node based on state.

Example:

```text
if review == "pass": finish
else: revise
```

## 6. When To Use Graphs

Use graph workflows when:

- there are branches
- you need reliable steps
- you need retries
- you need human approval
- you need durable progress

