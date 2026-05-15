# Chapter 58: Uncertainty And Clarifying Questions

Good agents should not pretend to know everything.

They should know when to ask questions.

## 1. Why Uncertainty Matters

Bad agent:

```text
Guesses confidently.
```

Good agent:

```text
Explains what it knows, what it does not know, and asks a useful question.
```

## 2. When To Ask A Clarifying Question

Ask when:

- the user's goal is unclear
- missing information blocks the task
- action could be risky
- multiple interpretations exist
- required file/path/account is unknown

## 3. When Not To Ask

Do not ask unnecessary questions when a reasonable safe assumption works.

Example:

```text
User: Explain loops.
```

No need to ask:

```text
Which exact loop definition do you mean?
```

Just teach loops.

## 4. Confidence

Agents can track confidence informally.

Example:

```text
high: answer from provided file
medium: answer from general knowledge
low: missing context
```

## 5. Good Clarifying Question

Bad:

```text
Clarify?
```

Good:

```text
Do you want the example as a simple script or as a clean multi-file project?
```

## Run

```powershell
python chapter_58_uncertainty_clarifying_questions/main.py
```

