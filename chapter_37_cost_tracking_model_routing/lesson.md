# Chapter 37: Cost Tracking And Model Routing

Agents can become expensive.

Cost tracking helps you understand how much each request uses.

Model routing means choosing the right model for the job.

## 1. Why Cost Tracking Matters

Agents may:

- call the model many times
- send long context
- call tools
- retry failures
- run in the background

Small costs can grow quickly.

## 2. Token Budget

A simple cost estimate:

```text
cost = input_tokens * input_price + output_tokens * output_price
```

Prices depend on the model.

This chapter uses fake prices so you learn the idea.

## 3. Model Routing

Use smaller models for easy tasks.

Use stronger models for hard tasks.

Example:

```text
classification -> small model
deep planning -> reasoning model
simple rewrite -> small model
complex code review -> strong model
```

## 4. Good Routing Questions

Ask:

- does this need deep reasoning?
- does this need tools?
- how risky is a mistake?
- how long is the context?
- how fast must it be?

## Run

```powershell
python chapter_37_cost_tracking_model_routing/main.py
```

