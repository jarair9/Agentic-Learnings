# Chapter 06: Basic Agent Loop

An agent loop is the engine of many agents.

The loop usually does this:

1. Ask the model what to do.
2. If the model calls a tool, run the tool.
3. Add the tool result to memory.
4. Ask the model again.
5. Stop when there are no more tool calls.

This chapter makes that loop reusable.

## Run

```powershell
python chapter_06_basic_agent_loop/main.py
```

