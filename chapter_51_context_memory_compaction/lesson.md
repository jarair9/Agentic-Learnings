# Chapter 51: Context Memory Management And Compaction

You asked an excellent question:

How do we handle LLM context and memory?

This is one of the most important agent engineering skills.

An LLM does not have unlimited memory. It only sees what your program sends in the current request.

So your job as the developer is to decide:

```text
What should the model see right now?
What should be saved for later?
What should be summarized?
What should be forgotten?
```

## 1. Context vs Memory

These words are related, but not the same.

## Context

Context is the text currently sent to the model.

It may include:

- developer instructions
- user message
- recent conversation
- tool results
- retrieved documents
- summaries
- pinned facts

If it is not in the context, the model cannot directly use it for that call.

## Memory

Memory is information your app stores somewhere.

It may be stored in:

- Python variables
- JSON files
- databases
- vector stores
- logs
- summaries

Memory becomes useful only when your app retrieves it and puts the relevant parts back into context.

Simple idea:

```text
Memory is the library.
Context is the book open on the desk right now.
```

## 2. Why Context Becomes A Problem

LLMs have context windows, but they are still limited.

Problems happen when:

- conversation gets long
- tool outputs are huge
- RAG retrieves too many chunks
- logs are pasted into the prompt
- old irrelevant details remain

Bad context causes:

- higher cost
- slower responses
- confused answers
- missed instructions
- important facts getting buried

## 3. The Main Ways To Handle Context

There are several common strategies.

You can combine them.

## Strategy 1: Sliding Window

Keep only the most recent messages.

Example:

```text
Keep last 8 conversation messages.
Drop older messages.
```

Good for:

- simple chatbots
- short tasks
- quick prototypes

Weakness:

- old important facts may disappear

## Strategy 2: Running Summary

Summarize older conversation into a shorter note.

Example:

```text
Summary:
The user is learning agentic AI in Python.
They prefer simple examples and commented code.
They have built chapters 1-50.
They are now asking about context compaction.
```

Good for:

- long conversations
- tutoring agents
- project assistants

Weakness:

- summaries can lose details
- bad summaries can create wrong memory

## Strategy 3: Compaction

Compaction is a stronger form of summarization.

It means compressing a large context into a smaller state that preserves what matters.

Compaction usually includes:

- current goal
- important user preferences
- completed work
- unresolved questions
- important decisions
- relevant file paths
- next steps

Compaction is not just “make it shorter.”

It is:

```text
Keep the useful state, remove noise.
```

Good compaction:

```text
User wants to learn agentic AI deeply in Python.
Project has 51 chapter folders.
Python is not available on PATH, so code has not been executed.
Current topic: context memory and compaction.
Need beginner-friendly explanations with commented Python examples.
```

Bad compaction:

```text
User asked about AI stuff.
```

## Strategy 4: Pinned Facts

Pinned facts are important facts that should stay available.

Examples:

```text
User is intermediate in Python.
User wants explanations for a 13-year-old learner.
Never read .env files.
Current project root is C:\Users\JarairAhmad\Documents\agentic ai.
```

Good for:

- user preferences
- safety rules
- project settings

Weakness:

- too many pinned facts become clutter

## Strategy 5: Retrieval Memory

Store information outside context, then search for it when needed.

This is like RAG for memory.

Example:

```text
User asks about tool schemas.
System retrieves old notes about schemas and router design.
Only those notes go into context.
```

Good for:

- lots of notes
- long-term memory
- large projects

Weakness:

- retrieval can find the wrong memory
- important facts may not be retrieved

## Strategy 6: Structured State

Instead of storing memory as paragraphs, store it as structured data.

Example:

```json
{
  "current_goal": "learn context compaction",
  "completed_chapters": [1, 2, 3, 50],
  "preferences": ["simple words", "commented code"],
  "blockers": ["Python not on PATH"]
}
```

Good for:

- agents with workflows
- dashboards
- progress tracking
- reliable state updates

Weakness:

- less natural than conversation
- needs careful update logic

## Strategy 7: Checkpoints

Checkpoints save progress at important moments.

Example:

```text
Checkpoint after chapter creation:
- Chapters 1-51 created
- README updated
- Python verification blocked
- Next step: install Python or build capstone
```

Good for:

- long-running agents
- coding agents
- background jobs
- tasks that may resume later

## 4. What Should Go Into Context?

A good context often has layers:

```text
1. Developer instructions
2. Current user request
3. Current task state
4. Pinned facts
5. Recent messages
6. Retrieved relevant memory
7. Tool results needed now
```

Do not blindly include everything.

## 5. A Practical Context Recipe

For a study agent, use this:

```text
developer prompt
current user question
pinned user preferences
short running summary
last 4 messages
retrieved chapter notes
current quiz/progress state
```

This is much better than sending the whole history every time.

## 6. When To Compact

Compact when:

- conversation gets too long
- tool outputs are huge
- cost is rising
- model seems confused
- you are about to continue a task later
- you need to save task state

## 7. What Compaction Should Preserve

A good compaction should preserve:

- user goal
- constraints
- preferences
- decisions
- completed work
- open tasks
- important errors
- next action

It should remove:

- repeated text
- old greetings
- unimportant wording
- failed attempts that no longer matter
- huge raw outputs after summarizing them

## 8. Common Mistakes

Mistake 1:

```text
Keeping all messages forever.
```

Mistake 2:

```text
Summarizing too aggressively and losing important details.
```

Mistake 3:

```text
Letting retrieved documents override developer instructions.
```

Mistake 4:

```text
Storing secrets in memory.
```

Mistake 5:

```text
Putting huge tool outputs into context without cleaning them.
```

## 9. Best Beginner Design

Start with this simple system:

1. Keep a running summary.
2. Keep last 4-8 messages.
3. Keep pinned facts.
4. Retrieve relevant notes when needed.
5. Save structured state in JSON.

That is already a strong design.

## 10. Mental Model

Imagine the model is a student with a small desk.

Memory is the bookshelf.

Context is what you place on the desk.

Compaction is cleaning messy notes into one useful study sheet.

Retrieval is walking to the bookshelf and bringing back only the right book.

Your job is to keep the desk useful.

