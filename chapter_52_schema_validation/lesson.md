# Chapter 52: Schema Validation

Agents often produce structured data.

But you should not blindly trust that data.

Schema validation means checking that data has the correct shape before your program uses it.

## 1. Why Validation Matters

Imagine the model should return:

```json
{
  "chapter": 12,
  "difficulty": "beginner",
  "next_action": "study"
}
```

But it returns:

```json
{
  "chapter": "twelve",
  "next": "do stuff"
}
```

Your code may break.

Validation catches this early.

## 2. What To Validate

Check:

- required fields
- field types
- allowed values
- number ranges
- string length
- unknown extra fields

## 3. Pydantic-Style Thinking

Pydantic is a popular Python library for validation.

Even before using it, learn the thinking:

```text
Define the shape.
Parse the data.
Reject bad data.
Return helpful errors.
```

## 4. Validation And Agents

Validate:

- model JSON
- tool arguments
- tool outputs
- memory files
- config values
- API inputs

## 5. Good Error Handling

Bad:

```text
Invalid.
```

Good:

```text
Invalid quiz result: score must be between 0 and 100.
```

## Run

```powershell
python chapter_52_schema_validation/main.py
```

