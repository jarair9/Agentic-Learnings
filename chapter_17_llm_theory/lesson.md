# Chapter 17: LLM Theory Deep Dive

Before you build powerful agents, you should understand the engine: the large language model, or LLM.

An LLM is not a normal database. It does not look up one perfect answer from a table. It predicts text based on patterns learned from huge amounts of training data.

That sounds simple, but it leads to many important behaviors.

## 1. What Is A Token?

A token is a small piece of text.

Sometimes a token is:

- one word
- part of a word
- punctuation
- a space plus a word

Example sentence:

```text
Agentic AI is powerful.
```

A model may see something like:

```text
Agent | ic | AI | is | powerful | .
```

Not exactly this, but close enough for learning.

## 2. Context Window

The context window is how much text the model can see at once.

It includes:

- your prompt
- conversation history
- tool results
- retrieved documents
- model instructions

Important lesson: if something is not in the context, the model cannot directly use it.

For agents, context is like the agent's current desk. Only papers on the desk can be used right now.

## 3. Why Context Management Matters

If your agent keeps adding everything forever, context becomes messy and expensive.

Good agents decide what to keep:

- current user goal
- important facts
- recent tool results
- summaries of old work
- final decisions

Bad agents keep every tiny detail and confuse themselves.

## 4. Temperature

Temperature controls randomness.

Low temperature:

- more predictable
- good for coding
- good for extraction
- good for tool decisions

High temperature:

- more creative
- good for brainstorming
- can be less reliable

Simple idea:

```text
temperature = 0.1  -> careful student
temperature = 1.0  -> creative storyteller
```

For most agent work, start low.

## 5. Top-p

Top-p is another sampling control.

It limits the model to a group of likely next tokens.

Beginner advice: do not change both temperature and top-p at the same time unless you know why.

## 6. Hallucinations

A hallucination is when the model says something that sounds confident but is wrong.

Why it happens:

- the model predicts likely text, not guaranteed truth
- the prompt lacks enough information
- the model tries to be helpful even when unsure
- retrieved context is bad or missing

How agents reduce hallucination:

- use tools
- read real files
- retrieve documents
- cite sources
- say “I do not know” when context is missing
- validate outputs with code

## 7. Reasoning Models vs Normal Chat Models

Some models are optimized for deeper reasoning.

They are useful for:

- planning
- coding
- complex debugging
- multi-step decisions

But they can cost more or take longer.

Simple rule:

- easy task: cheaper/faster model
- hard planning: stronger reasoning model
- production: measure cost, speed, and quality

## 8. Instruction Hierarchy

Messages can have different authority.

Common order:

1. System/platform rules
2. Developer instructions
3. User request
4. Tool outputs and other context

If a user says “ignore all previous instructions,” the agent should not obey that if higher-priority instructions say otherwise.

This matters a lot for security.

## Key Takeaways

- LLMs predict text from context.
- Tokens are the pieces of text the model reads.
- Context is limited and must be managed.
- Temperature affects randomness.
- Hallucinations are normal unless you design against them.
- Agents become stronger by connecting models to real tools and reliable data.

