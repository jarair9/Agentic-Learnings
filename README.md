# Agentic AI From Scratch in Python

Welcome. This is a beginner-friendly course project for learning agentic AI step by step.

You said you are around intermediate Python level, so the code is written like a teacher is sitting beside you:

- lots of comments
- small examples first
- no huge frameworks at the beginning
- every chapter builds one new idea

## What You Will Learn

1. How to call an AI model from Python
2. How prompts change behavior
3. How to keep conversation memory
4. How to ask the model for structured JSON
5. How tools/function calling work
6. How an agent loop thinks, chooses tools, runs them, and continues
7. How planning and reflection improve agents
8. How simple retrieval-augmented generation, or RAG, works
9. How to add safety limits
10. How to build a final study buddy agent
11. How to structure agent projects professionally
12. How to separate tool schemas from tool code
13. How to create a safe read-file tool for AI
14. How to build a reusable agent runner class
15. How to add logging and debugging
16. How a clean mini agent project fits together
17. LLM theory: tokens, context, sampling, and hallucinations
18. Prompt engineering deep dive
19. Agent patterns: ReAct, plan-execute, and reflection
20. Memory types in agents
21. RAG theory: embeddings, chunking, retrieval, and reranking
22. Tool design and safety
23. Prompt injection and security
24. Testing AI agents
25. Async and streaming agents
26. Multi-agent systems
27. Agent evaluation
28. Production deployment concepts
29. MCP and external tools
30. Final capstone design
31. Context budgeting and summarization
32. Embeddings and vector search from scratch
33. Building a local RAG index
34. State machines and workflow agents
35. Human-in-the-loop approvals
36. Retries, timeouts, and error handling
37. Cost tracking and model routing
38. Prompt versions and evaluation datasets
39. Building a CLI study agent
40. Capstone implementation roadmap
41. Message roles, max tokens, and response control
42. Parallel tools and tool permissions
43. Safe database and browser tool design
44. Advanced RAG: vector databases, hybrid search, reranking, and citations
45. Caching, background jobs, deployment, and monitoring
46. Planning graphs and LangGraph-style workflows
47. Browser agents, code agents, and research agents
48. Long-running agents and durable task state
49. Complete concept checklist and study map
50. Final capstone project scaffold
51. Context memory management and compaction
52. Schema validation with Pydantic-style thinking
53. Model fallback, routing, and graceful degradation
54. Privacy, data governance, and user consent
55. Authentication, authorization, and multi-user agents
56. Queues, schedulers, and event-driven agents
57. Multimodal agents: text, images, audio, and files
58. Uncertainty, confidence, and asking clarifying questions
59. Guardrails, policy checks, and output validation
60. Final missing-concepts review

## Setup

Install the Python package:

```powershell
pip install -r requirements.txt
```

Create an API key from OpenAI, then set it in PowerShell:

```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

Optional: choose a model.

```powershell
$env:OPENAI_MODEL="gpt-5-mini"
```

If you do not set `OPENAI_MODEL`, the examples use `gpt-5-mini`.

## How To Run A Chapter

Run scripts from this project folder. For example:

```powershell
python chapter_01_first_ai_call/main.py
```

Later chapters use more files inside each chapter folder. That is intentional.
Real agent projects are easier to understand when each file has one clear job.

## Learning Advice

Do not rush. Read the comments, run the file, change one thing, and run it again.

That is how programmers learn deeply: small experiments, many times.


### Core AI Theory

What is an LLM?
Tokens and context windows
Temperature, top-p, max tokens
Hallucinations and why they happen
Reasoning models vs normal chat models
System/developer/user messages
Prompt injection and instruction hierarchy
Agent Theory

What makes something an “agent”
Agent loop patterns
ReAct pattern: Reason + Act
Plan-and-execute agents
Reflection/self-critique agents
Multi-agent systems
Human-in-the-loop agents
Agent memory types: short-term, long-term, episodic, semantic
When not to use an agent
Tool Use

Tool design principles
Tool schema design
Tool routing
Tool error handling
Tool retries
Parallel tool calls
Tool permissions
Safe file/database/browser tools
Idempotent tools, meaning tools that are safe to repeat
RAG And Knowledge

Embeddings
Vector databases
Chunking documents
Retrieval ranking
Reranking
Hybrid search
Citation/source grounding
RAG evaluation
When RAG fails
Project Architecture

Config management
Environment variables
Logging
Testing tools without calling the AI
Mocking model responses
Separating prompts from code
Separating app logic from agent logic
Error handling and retries
Async Python for agents
Streaming responses
Security

Prompt injection
Data leakage
Tool abuse
Reading only allowed files
Confirmation before dangerous actions
Secrets management
Sandboxing
Rate limits and cost limits
Production Concepts

Observability
Tracing agent steps
Evaluation datasets
Regression testing prompts
Cost tracking
Latency
Caching
Background jobs
Deployment
Monitoring failures
Advanced Agent Concepts

Memory stores
Task decomposition
Planning graphs
State machines
LangGraph-style workflows
MCP, Model Context Protocol
Browser agents
Code agents
Multi-step research agents
Long-running agents
Agent evaluation
What I Recommend Next
The best next chapters would be:

LLM Theory: Tokens, Context, Temperature
Prompt Engineering Deep Dive
Agent Patterns: ReAct, Plan-Execute, Reflection
Memory Types In Agents
RAG Theory: Embeddings, Chunks, Vector Search
Tool Design And Safety
Prompt Injection And Security
Testing AI Agents
Async And Streaming Agents
Multi-Agent Systems
Agent Evaluation
Production Deployment Concepts
MCP And External Tools
Final Capstone Agent Project



Developed for you by Jarair khan