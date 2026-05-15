# Chapter 47: Browser Agents, Code Agents, And Research Agents

Different agent types need different safety and design patterns.

## 1. Browser Agents

Browser agents use a browser to:

- open pages
- click buttons
- type text
- inspect web apps
- test UI flows

Risks:

- submitting forms accidentally
- trusting malicious pages
- leaking private data
- clicking destructive buttons

Good browser agents ask before risky actions.

## 2. Code Agents

Code agents read and edit code.

They can:

- search files
- explain code
- write patches
- run tests
- fix bugs

Risks:

- deleting user work
- changing too much
- hiding failing tests
- editing unrelated files

Good code agents make focused changes and run verification.

## 3. Research Agents

Research agents gather information from multiple sources.

They should:

- compare sources
- track citations
- avoid unsupported claims
- separate facts from guesses
- notice dates

Research agents need strong citation habits.

## 4. Multi-Step Research

Research often follows:

```text
understand question
search sources
read sources
extract facts
compare facts
answer with citations
```

## 5. Choosing The Agent Type

Ask:

- Does it need a browser?
- Does it need to edit code?
- Does it need fresh information?
- Does it need citations?
- Does it need approvals?

The right agent type depends on the task.

