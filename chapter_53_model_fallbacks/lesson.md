# Chapter 53: Model Fallback, Routing, And Graceful Degradation

Production agents should not collapse when one model call fails.

Model fallback means using another option when the first one fails or is too expensive.

## 1. Model Routing

Routing chooses a model based on the task.

Example:

```text
easy classification -> small fast model
hard debugging -> stronger reasoning model
long summarization -> model with large context
```

## 2. Fallback

Fallback means:

```text
Try model A.
If model A fails, try model B.
If model B fails, return a helpful message.
```

## 3. Graceful Degradation

Graceful degradation means the app still helps even when a feature fails.

Example:

```text
RAG search failed, but I can still answer from the current chapter summary.
```

## 4. When To Fallback

Fallback when:

- model is unavailable
- rate limit happens
- output validation fails
- latency is too high
- cost budget is exceeded

## 5. Do Not Hide Problems

If the fallback gives a lower-quality answer, say so when needed.

Users trust honest systems.

## Run

```powershell
python chapter_53_model_fallbacks/main.py
```

