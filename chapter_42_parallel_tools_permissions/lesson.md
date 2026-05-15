# Chapter 42: Parallel Tools And Tool Permissions

Some agent tasks need more than one tool.

Sometimes tools can run at the same time.

But power must be controlled with permissions.

## 1. Parallel Tool Calls

Parallel tool calls mean running independent tools together.

Example:

```text
read profile
search notes
load settings
```

These do not depend on each other, so they can run in parallel.

## 2. When Not To Parallelize

Do not run tools in parallel when one depends on another.

Example:

```text
1. Search for filename
2. Read that filename
```

Step 2 needs step 1 first.

## 3. Tool Permissions

Every tool should have a permission level.

Example:

```text
read_note: safe
search_docs: safe
create_draft: medium
send_email: risky
delete_file: forbidden
```

## 4. Permission Checks

The model can request a tool.

Your code decides if it is allowed.

This is extremely important.

## 5. Least Privilege

Least privilege means giving the agent only the power it needs.

If the task is “answer questions from notes,” the agent needs read-only tools, not delete tools.

## 6. Audit Trail

For serious apps, log:

- tool name
- arguments
- permission level
- allowed or blocked
- result summary

This helps with debugging and safety.

