# Chapter 49: Complete Concept Checklist And Study Map

This chapter answers your question directly:

Are all important concepts completed?

For a beginner-to-strong-intermediate agentic AI course, yes, this roadmap now covers the main concepts.

But mastery comes from building projects, not only reading chapters.

## 1. LLM Basics

Covered:

- What is an LLM?
- Tokens
- Context windows
- Temperature
- Top-p
- Max output tokens
- Hallucinations
- Reasoning models
- Message roles
- Instruction hierarchy

Practice:

- build prompts
- compare short and long context
- test low vs high temperature

## 2. Agent Theory

Covered:

- what makes something an agent
- agent loops
- ReAct
- plan-and-execute
- reflection
- multi-agent systems
- human-in-the-loop
- memory types
- when not to use agents

Practice:

- implement a simple loop
- implement a planner
- implement a reviewer

## 3. Tool Use

Covered:

- tool design
- schemas
- routers
- error handling
- retries
- parallel tools
- permissions
- safe file tools
- safe database/browser tool design
- idempotency

Practice:

- build read-only tools first
- add one write tool with approval
- log every tool call

## 4. RAG And Knowledge

Covered:

- embeddings
- vector search
- vector databases conceptually
- chunking
- ranking
- reranking
- hybrid search
- citations
- grounding
- RAG evaluation
- RAG failure modes

Practice:

- build local RAG over lesson files
- show citations
- inspect failed retrievals

## 5. Architecture

Covered:

- config
- environment variables
- logging
- testing tools without AI
- mocking model responses
- prompt separation
- app logic separation
- retries
- async
- streaming concepts

Practice:

- keep `main.py` small
- separate `schemas.py`, `functions.py`, `router.py`
- write tests for tool functions

## 6. Security

Covered:

- prompt injection
- data leakage
- tool abuse
- allowed file paths
- confirmations
- secrets
- sandboxing concept
- rate and cost limits

Practice:

- block `.env`
- block path traversal
- ask approval for risky tools

## 7. Production

Covered:

- observability
- tracing
- eval datasets
- regression tests
- cost tracking
- latency
- caching
- background jobs
- deployment
- monitoring

Practice:

- trace agent steps
- create 10 eval questions
- track rough token cost

## 8. Advanced Agents

Covered:

- memory stores
- task decomposition
- planning graphs
- state machines
- LangGraph-style workflows
- MCP
- browser agents
- code agents
- research agents
- long-running agents
- agent evaluation

Practice:

- build graph workflow
- save task checkpoints
- classify agent type by task

## What Is Still Beyond This Course?

There are always deeper topics:

- fine-tuning
- advanced model evaluation statistics
- production vector databases in depth
- distributed queues
- enterprise identity and permissions
- large-scale observability platforms
- reinforcement learning
- custom model training

You do not need those yet.

Your next real step is the capstone project.

