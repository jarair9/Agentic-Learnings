# Chapter 12: Separate Tool Schemas From Tool Code

Tool calling has two different parts:

1. Tool schema: the description shown to the AI.
2. Tool function: the real Python code that runs.

Beginners often mix them in one giant file.

Professionals usually separate them:

```text
tools/
  schemas.py      # what the AI sees
  functions.py    # what Python runs
  router.py       # connects schema names to functions
```

This makes the code easier to read, test, and extend.

## Run

```powershell
python chapter_12_separate_tool_schemas/main.py
```

