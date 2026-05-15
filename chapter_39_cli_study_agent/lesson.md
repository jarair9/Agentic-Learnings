# Chapter 39: Building A CLI Study Agent

CLI means command-line interface.

A CLI agent lets you talk to your agent from the terminal.

This is useful before building a web app.

## 1. Why Start With CLI?

CLI apps are:

- simple
- fast to build
- easy to debug
- good for learning loops

## 2. Basic CLI Loop

```text
while True:
    read user input
    if user typed exit, stop
    send input to agent
    print answer
```

## 3. Commands

CLI agents can support commands:

```text
/help
/memory
/clear
/exit
```

Commands are handled by normal Python before calling the model.

## 4. Why Commands Matter

Commands give users control.

Example:

```text
/clear
```

should clear conversation memory without needing the AI to understand it.

## Run

```powershell
python chapter_39_cli_study_agent/main.py
```

