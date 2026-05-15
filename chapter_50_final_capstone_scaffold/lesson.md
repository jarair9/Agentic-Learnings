# Chapter 50: Final Capstone Project Scaffold

This chapter is the bridge from learning to building.

The final project is:

```text
Agentic AI Study Coach
```

It should combine the whole course.

## Features

The capstone should:

- load lesson files
- build a local RAG index
- answer with citations
- quiz the student
- remember progress
- use safe tools
- track rough cost
- log tool calls
- block unsafe file paths
- support CLI commands

## Suggested Build Order

1. Create folders.
2. Add config.
3. Add prompts.
4. Add safe file reader.
5. Add RAG index.
6. Add tool schemas.
7. Add tool router.
8. Add agent runner.
9. Add memory.
10. Add CLI.
11. Add logging.
12. Add eval dataset.

## Do Not Build Everything At Once

Build one small working slice:

```text
CLI -> ask question -> read lesson -> answer
```

Then add:

```text
RAG -> citations -> memory -> quiz -> evals
```

## The Professional Mindset

A real agent is not just “AI call plus tools.”

It is a system:

- model
- prompts
- tools
- memory
- safety
- evaluation
- logs
- user experience

When those parts work together, you have a real agentic application.

