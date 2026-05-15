# Chapter 18: Prompt Engineering Deep Dive

Prompt engineering means communicating clearly with the model.

A prompt is not magic words. A prompt is a specification.

Good prompts reduce confusion.

## 1. The Four-Part Prompt

A strong prompt often has four parts:

1. Role: who should the model act like?
2. Task: what should it do?
3. Context: what information should it use?
4. Output format: how should the answer look?

Example:

```text
You are a Python tutor.
Explain loops to a 13-year-old learner.
Use the notes below.
Return 3 bullets and one tiny code example.
```

## 2. Bad Prompt vs Good Prompt

Bad:

```text
Explain agents.
```

Better:

```text
Explain AI agents to an intermediate Python learner.
Use a simple analogy, then explain tools, memory, and loops.
Keep it under 150 words.
```

## 3. Give The Model A Job

Models behave better when the job is clear.

Examples:

- “You are a careful code reviewer.”
- “You are a patient Python teacher.”
- “You are a strict JSON formatter.”
- “You are a security reviewer.”

## 4. Output Formats

If your program needs to read the answer, ask for structure.

Examples:

```text
Return JSON with keys: topic, difficulty, next_step.
```

Or:

```text
Return exactly:
Summary:
Risks:
Next actions:
```

## 5. Constraints

Constraints are rules.

Good constraints:

- “Use only the provided context.”
- “Do not invent file names.”
- “Ask a question if information is missing.”
- “Return valid JSON only.”

## 6. Few-Shot Prompting

Few-shot prompting means giving examples.

Example:

```text
Input: "loop"
Output: "A loop repeats code."

Input: "function"
Output:
```

The model learns the pattern from examples.

## 7. Chain Of Thought Warning

You do not always need to ask the model to show every hidden reasoning step.

Better:

```text
Think carefully, then give a concise answer with the key reasons.
```

For users, the final explanation matters more than a huge private scratchpad.

## 8. Prompt Versioning

In serious projects, prompts should be versioned like code.

Example:

```text
teacher_prompt_v1
teacher_prompt_v2
security_prompt_v1
```

When behavior changes, you know which prompt changed.

## Exercises

1. Rewrite a vague prompt into a clear prompt.
2. Add an output format.
3. Add one safety rule.
4. Add one example.

