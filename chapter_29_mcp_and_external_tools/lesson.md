# Chapter 29: MCP And External Tools

MCP means Model Context Protocol.

It is a standard way for AI apps to connect models to external tools and data.

Think of MCP like a plug system for agents.

## 1. Why MCP Exists

Without a standard, every app connects tools differently.

MCP helps tools expose:

- functions
- files/resources
- prompts
- structured context

## 2. MCP Mental Model

```text
AI app <-> MCP server <-> external system
```

External systems can be:

- GitHub
- databases
- file systems
- browsers
- calendars
- docs
- internal company tools

## 3. MCP Server

An MCP server provides capabilities.

Example:

```text
Tool: search_issues
Tool: read_file
Resource: project_docs
```

## 4. MCP Client

The AI application is usually the MCP client.

It asks:

```text
What tools are available?
Call this tool with these arguments.
Read this resource.
```

## 5. Why This Matters For Agents

Agents need tools.

MCP makes tool connection more reusable and organized.

Instead of writing every integration from scratch, you can connect to tool servers.

## 6. Security Still Matters

MCP does not remove safety concerns.

You still need:

- permissions
- allowed actions
- confirmation for risky operations
- logging
- secret protection

## 7. Beginner Advice

Learn normal Python tools first.

Then learn MCP once you understand:

- schemas
- routing
- tool outputs
- agent loops

MCP will make much more sense after that.

