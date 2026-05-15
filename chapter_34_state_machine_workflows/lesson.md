# Chapter 34: State Machines And Workflow Agents

Some agents should not be fully free.

Sometimes you want a controlled workflow.

A state machine is a fixed set of states and allowed transitions.

## 1. Why State Machines Help

They make agents:

- easier to debug
- easier to test
- safer
- more predictable

## 2. Example States

```text
START
COLLECT_GOAL
PLAN
EXECUTE
VERIFY
FINISH
```

The agent moves from one state to another.

## 3. Agent vs Workflow

Free agent:

```text
Model decides everything.
```

Workflow agent:

```text
Code controls the steps.
Model helps inside each step.
```

For production, workflow agents are often better.

## 4. When To Use State Machines

Use them when:

- safety matters
- steps are known
- you need approvals
- you need reliable progress
- debugging matters

## Run

```powershell
python chapter_34_state_machine_workflows/main.py
```

