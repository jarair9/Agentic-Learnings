# Chapter 14: Reusable Agent Runner

In earlier chapters, the agent loop lived inside `main.py`.

That is okay for learning, but not great for bigger projects.

Now we create an `AgentRunner` class.

The class owns:

- the model
- the tools
- the loop
- the max turn safety limit

`main.py` becomes small again.

## Run

```powershell
python chapter_14_reusable_agent_runner/main.py
```

