# Chapter 55: Authentication, Authorization, And Multi-User Agents

A local learning script has one user.

Real apps often have many users.

That changes memory, permissions, and safety.

## 1. Authentication

Authentication asks:

```text
Who are you?
```

Examples:

- login
- password
- OAuth
- session cookie

## 2. Authorization

Authorization asks:

```text
What are you allowed to do?
```

Example:

Ali can read Ali's progress.

Ali should not read Sara's progress.

## 3. Multi-User Memory

Never mix user memories.

Bad:

```text
memory.json
```

Better:

```text
memory/user_123.json
memory/user_456.json
```

## 4. Tool Permissions Per User

Different users may have different permissions.

Example:

```text
student: read lessons, take quizzes
teacher: create lessons, view class progress
admin: manage users
```

## 5. Security Rule

Every tool should know which user is calling it.

Do not let the model invent user IDs.

The app should provide trusted user identity.

## Run

```powershell
python chapter_55_auth_multi_user_agents/main.py
```

