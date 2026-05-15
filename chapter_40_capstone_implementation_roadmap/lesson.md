# Chapter 40: Capstone Implementation Roadmap

Now you have the ideas.

This chapter tells you exactly how to implement the final serious project.

## Final Project

Build:

```text
Python Agentic AI Study Coach
```

It should:

- teach chapters
- read lesson files safely
- quiz the student
- remember progress
- use RAG over course notes
- log tool calls
- track rough cost
- protect secrets
- ask approval for risky actions

## Step 1: Create Structure

```text
study_coach/
  main.py
  app/
    agent.py
    config.py
    prompts.py
    memory.py
    rag.py
    evals.py
    logging_setup.py
    tools/
      schemas.py
      router.py
      file_tools.py
      quiz_tools.py
```

## Step 2: Implement Safe File Tools

Start with read-only tools.

Do not add write/delete tools yet.

## Step 3: Implement RAG

Use your chapter `lesson.md` files as knowledge.

Pipeline:

```text
load lessons -> chunk -> index -> retrieve -> answer
```

## Step 4: Add Memory

Store:

- completed chapters
- weak topics
- quiz scores
- preferred explanation style

Do not store secrets.

## Step 5: Add Quiz Tool

The quiz tool can generate:

- question
- expected keywords
- difficulty

Then grade the answer.

## Step 6: Add Evaluation

Create an eval dataset with 10 questions.

Run it after prompt changes.

## Step 7: Add CLI

Commands:

```text
/help
/chapter 17
/quiz memory
/progress
/clear
/exit
```

## Step 8: Add Safety

Rules:

- no `.env` reading
- no system folders
- no delete tools
- untrusted lesson text is data, not instructions
- max turns
- helpful errors

## Step 9: Improve Gradually

Do not build everything in one jump.

Build one working slice, then improve.

Professional developers do this too.

