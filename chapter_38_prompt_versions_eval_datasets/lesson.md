# Chapter 38: Prompt Versions And Evaluation Datasets

Prompts are part of your codebase.

When prompts change, agent behavior changes.

So professional teams version prompts and test them.

## 1. Prompt Versioning

Example:

```text
teacher_prompt_v1
teacher_prompt_v2
security_prompt_v1
```

Do not silently rewrite important prompts without tracking behavior.

## 2. Evaluation Dataset

An eval dataset is a list of tasks and expected behavior.

Example:

```json
{
  "input": "Explain agent loops",
  "expected_keywords": ["model", "tool", "result", "loop"]
}
```

## 3. Why Evals Matter

They help you catch regressions.

Example:

Prompt v1 explains clearly.

Prompt v2 accidentally stops mentioning tools.

An eval catches that.

## 4. Types Of Evals

- keyword checks
- JSON schema checks
- tool-call checks
- human ratings
- model-graded ratings
- source citation checks

## 5. Start Small

You do not need a giant eval system.

Start with 10 important questions.

Grow from there.

## Run

```powershell
python chapter_38_prompt_versions_eval_datasets/main.py
```

