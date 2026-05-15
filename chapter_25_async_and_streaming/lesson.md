# Chapter 25: Async And Streaming Agents

Agents can feel slow because they may:

- call the model
- call tools
- read files
- search databases
- call APIs

Async and streaming help.

## 1. What Is Async?

Async lets Python wait for slow tasks without freezing everything.

Example:

```text
While waiting for an API response, do another task.
```

Useful for:

- web apps
- multiple tool calls
- background agents
- chat interfaces

## 2. What Is Streaming?

Streaming means showing the answer while it is being generated.

Instead of:

```text
wait... wait... wait... full answer appears
```

You get:

```text
word by word or chunk by chunk
```

This feels faster to users.

## 3. Async Tool Calls

Some tools can run in parallel.

Example:

```text
search docs
fetch user profile
read config
```

If they do not depend on each other, async can help.

## 4. When Not To Use Async

Do not use async just to look advanced.

For simple scripts, normal sync code is easier.

Use async when you really need concurrency or responsive apps.

## 5. Streaming In Agents

Streaming agent output is harder because the model may call tools in the middle.

You may need to stream:

- text deltas
- tool call progress
- tool result summaries
- final answer

## Mental Model

Sync code is like one student doing one task at a time.

Async code is like one student starting homework, waiting for a download, then using that waiting time to sharpen pencils.

