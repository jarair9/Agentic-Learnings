# Chapter 59: Guardrails, Policy Checks, And Output Validation

Guardrails are safety and quality checks around the model.

They do not replace good prompts.

They support good prompts.

## 1. Input Guardrails

Input guardrails check user requests before the model acts.

Examples:

- block secrets
- detect dangerous requests
- detect prompt injection
- check file paths

## 2. Tool Guardrails

Tool guardrails check tool calls.

Examples:

- allowed tool?
- allowed arguments?
- needs approval?
- user has permission?

## 3. Output Guardrails

Output guardrails check final answers.

Examples:

- valid JSON
- no secrets leaked
- citations included
- answer length okay
- no unsupported claims

## 4. Policy Checks

Policy checks are rules your app enforces.

Example:

```text
The agent may summarize files but may not reveal API keys.
```

## 5. Guardrails Are Code

Do not rely only on asking the model to be safe.

Write code checks.

## 6. Guardrail Failure

When a guardrail fails, return a helpful message.

Example:

```text
I cannot read that path because it is outside the allowed folder.
```

## Run

```powershell
python chapter_59_guardrails_output_validation/main.py
```

