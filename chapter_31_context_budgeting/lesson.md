# Chapter 31: Context Budgeting And Summarization

Agents can fail when they put too much information into the model context.

Context is limited, and large context can also cost more.

So professional agents manage context carefully.

## 1. What Is Context Budgeting?

Context budgeting means deciding how much text each part of the prompt is allowed to use.

Example:

```text
Developer prompt: 500 tokens
Conversation summary: 700 tokens
Recent messages: 1200 tokens
Retrieved notes: 2000 tokens
Tool outputs: 1000 tokens
```

This prevents one part from eating the whole context.

## 2. What Should Stay In Context?

Keep:

- the current goal
- recent user messages
- important decisions
- tool results needed for the answer
- small summaries of older work

Remove:

- repeated text
- old details no longer needed
- failed attempts unless useful
- huge documents after they are summarized

## 3. Summarization Memory

Instead of keeping 100 old messages, summarize them.

Example summary:

```text
The user is learning agentic AI in Python.
They finished chapters 1-30.
They prefer simple explanations and commented code.
They are now learning production engineering patterns.
```

## 4. Sliding Window Memory

A sliding window keeps only the latest messages.

Example:

```text
Keep last 6 messages.
Summarize older messages.
```

This is simple and useful.

## 5. Compression Rule

Good compression keeps meaning, not exact words.

Bad summary:

```text
We talked about stuff.
```

Good summary:

```text
We built a 30-chapter agentic AI course and covered tools, RAG, memory, security, testing, and production concepts.
```

## 6. Common Mistake

Beginners put everything in context “just in case.”

Better:

```text
Retrieve or summarize what is relevant.
```

Good agents are selective.

