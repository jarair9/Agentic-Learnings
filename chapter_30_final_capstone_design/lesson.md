# Chapter 30: Final Capstone Agent Design

This is the big picture chapter.

You now know enough pieces to design a real learning agent.

## Capstone Goal

Build a Python Study Coach Agent.

It should:

- read safe lesson files
- explain concepts simply
- answer questions
- remember progress
- quiz the student
- use tools safely
- log what happened
- avoid prompt injection
- evaluate answers

## Suggested Folder Structure

```text
study_coach_agent/
  main.py
  app/
    agent.py
    config.py
    prompts.py
    memory.py
    logging_setup.py
    evaluation.py
    tools/
      schemas.py
      router.py
      file_tools.py
      quiz_tools.py
    knowledge/
      agent_loops.txt
      rag.txt
      tool_safety.txt
    tests/
      test_file_tools.py
      test_memory.py
      test_router.py
```

## Architecture

```text
User
  |
main.py
  |
StudyCoachAgent
  |
Agent loop
  |
Tool router
  |
Safe tools
```

## Important Design Choices

### 1. Keep `main.py` Small

`main.py` should start the app, not contain the whole brain.

### 2. Keep Prompts Separate

Prompts are part of your product.

They deserve their own file.

### 3. Keep Tools Safe

Every tool needs:

- clear schema
- validation
- allowed permissions
- helpful errors

### 4. Store Memory Carefully

Memory should not store secrets.

Memory should store useful learning progress.

Example:

```json
{
  "completed_chapters": [1, 2, 3],
  "weak_topics": ["tool schemas", "RAG"],
  "preferred_style": "simple examples"
}
```

### 5. Add Evaluation

The agent should know whether the student understood.

Example:

```text
Ask 3 quiz questions.
Grade the answer.
Suggest review topics.
```

## Build Order

1. Create folder structure.
2. Add config and prompts.
3. Add safe file-reading tool.
4. Add tool schemas and router.
5. Add agent loop.
6. Add memory.
7. Add quiz tool.
8. Add logging.
9. Add tests.
10. Improve prompts.

## Final Mindset

A great agent is not just a model call.

A great agent is:

- clear instructions
- good tools
- safe boundaries
- useful memory
- strong evaluation
- clean code

That is the real craft.

