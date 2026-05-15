# Chapter 19: Agent Patterns Deep Dive

An agent pattern is a common shape for how the agent thinks and acts.

You should know patterns because not every task needs the same kind of agent.

## 1. Simple Tool Agent

Pattern:

```text
User asks -> model calls tool -> Python runs tool -> model answers
```

Use when:

- the task needs one or two tools
- the goal is clear
- no big plan is needed

Example:

```text
"Calculate 45 * 12 and explain the answer."
```

## 2. ReAct Pattern

ReAct means:

```text
Reason + Act
```

The model reasons about what it needs, then acts by using a tool.

Loop:

```text
think -> tool -> observe -> think -> tool -> observe -> final answer
```

Use when:

- the model must gather information step by step
- tool results decide the next action

## 3. Plan-And-Execute

Pattern:

```text
Make a plan first.
Then execute each step.
```

Use when:

- tasks are long
- steps can be listed before acting
- you want predictable progress

Example:

```text
"Analyze this project and suggest improvements."
```

## 4. Reflection Pattern

Pattern:

```text
answer -> review -> improve
```

Use when:

- writing explanations
- generating code
- creating plans
- checking correctness

Reflection is useful, but it is not magic. The reviewer model can also miss things.

## 5. Critic-Editor Pattern

Two roles:

- Creator: makes the first answer.
- Critic: finds problems.
- Editor: fixes them.

This is like writing an essay: first draft, review, final draft.

## 6. State Machine Agent

A state machine agent has fixed states.

Example:

```text
collect_goal -> plan -> execute -> verify -> finish
```

This is less “free” but more reliable.

Use in production when you need control.

## 7. When Not To Use An Agent

Do not use an agent when:

- a normal function is enough
- the task has one fixed path
- mistakes are expensive
- you cannot safely give tools
- latency/cost matters too much

Simple rule:

```text
If normal code can do it reliably, use normal code.
Use agents when flexible decision-making is valuable.
```

