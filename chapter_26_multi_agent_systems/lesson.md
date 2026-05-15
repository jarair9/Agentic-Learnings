# Chapter 26: Multi-Agent Systems

Multi-agent systems use more than one agent role.

This can be useful, but it can also become messy.

## 1. Why Use Multiple Agents?

Different agents can specialize.

Examples:

- Planner agent
- Researcher agent
- Coder agent
- Reviewer agent
- Security agent

## 2. Simple Multi-Agent Flow

```text
Planner creates plan
Researcher gathers facts
Coder writes solution
Reviewer checks result
Final agent summarizes
```

## 3. Benefits

Multi-agent systems can:

- separate responsibilities
- improve review quality
- make complex workflows clearer
- allow specialized prompts

## 4. Problems

They can also:

- cost more
- take longer
- repeat work
- disagree
- create too much text
- be harder to debug

## 5. Manager Pattern

A manager agent assigns work.

```text
Manager -> Worker A
Manager -> Worker B
Manager -> combines results
```

## 6. Debate Pattern

Two agents argue different sides, then a judge decides.

Useful for:

- design choices
- risk analysis
- comparing approaches

But it can be overkill.

## 7. Reviewer Pattern

One agent creates, another reviews.

This is one of the most useful multi-agent patterns.

## Advice

Start with one agent.

Add more agents only when there is a clear reason.

