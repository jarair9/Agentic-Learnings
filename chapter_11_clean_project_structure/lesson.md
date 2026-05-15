# Chapter 11: Clean Project Structure

When a project is tiny, one file is okay.

But agent projects grow quickly because they often need:

- prompts
- tools
- tool schemas
- memory
- config
- safety checks
- logs
- tests later

A professional structure gives each file one job.

## The Idea

Bad structure:

```text
main.py
```

Everything is mixed together.

Better structure:

```text
chapter_11_clean_project_structure/
  main.py
  app/
    config.py
    prompts.py
    simple_agent.py
```

Each file has a clear purpose.

## Run

```powershell
python chapter_11_clean_project_structure/main.py
```

