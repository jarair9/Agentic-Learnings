# Chapter 27: Agent Evaluation

Evaluation means measuring whether your agent is good.

Without evaluation, you are only guessing.

## 1. What Should You Evaluate?

Evaluate:

- final answer correctness
- tool choice
- tool arguments
- safety behavior
- citation accuracy
- cost
- speed
- user satisfaction

## 2. Task Success

Ask:

```text
Did the agent complete the user's real goal?
```

This matters more than sounding nice.

## 3. Tool Accuracy

Check:

- did it call the right tool?
- did it call tools too many times?
- did it pass correct arguments?
- did it handle tool errors?

## 4. Safety Evaluation

Test dangerous cases:

- prompt injection
- unsafe file path
- request to reveal secrets
- request to delete data

The agent should refuse or ask for confirmation.

## 5. RAG Evaluation

For RAG:

- did retrieval find the right documents?
- did answer use the documents?
- did it invent unsupported facts?
- did it cite sources?

## 6. Regression Suite

Keep a list of test tasks.

Run them whenever you change:

- prompts
- tools
- model
- retrieval settings
- memory logic

## 7. Human Evaluation

Human review asks:

- Is this helpful?
- Is it clear?
- Is it correct?
- Would I trust it?

## 8. Model-Based Evaluation

Another model can grade answers, but be careful.

Model graders can also be wrong.

Use them as helpers, not absolute truth.

