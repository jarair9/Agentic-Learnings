# Chapter 13: Safe Read-File Tool For AI

Agents often need to read files.

But file tools are powerful, so they need safety rules.

This chapter teaches a safe `read_text_file` tool.

The tool only reads inside this chapter's `workspace_files/` folder.

That means the AI cannot read private files like `.env`, system files, or random paths.

## Run

```powershell
python chapter_13_safe_read_file_tool/main.py
```

