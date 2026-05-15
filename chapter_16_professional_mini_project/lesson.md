# Chapter 16: Professional Mini Agent Project

This chapter shows a cleaner project shape.

It is still small, but it has professional habits:

- config in one file
- prompts in one file
- schemas separate from functions
- one tool router
- one agent runner
- small `main.py`

The goal is not to make code complicated.

The goal is to make every file easy to understand.

## Folder Structure

```text
chapter_16_professional_mini_project/
  main.py
  pro_agent/
    agent.py
    config.py
    prompts.py
    tools/
      functions.py
      router.py
      schemas.py
```

## Run

```powershell
python chapter_16_professional_mini_project/main.py
```

