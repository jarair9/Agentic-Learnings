# Chapter 44: Advanced RAG

Basic RAG retrieves notes and gives them to the model.

Advanced RAG improves retrieval quality, grounding, and trust.

## 1. Vector Databases

A vector database stores embeddings and searches by similarity.

Common stored fields:

```text
id
embedding
text
source
metadata
```

You use a vector database when your knowledge base becomes too large for simple local search.

## 2. Retrieval Ranking

Ranking decides which chunks are most relevant.

Bad ranking gives the model bad context.

Bad context leads to bad answers.

## 3. Hybrid Search

Hybrid search combines:

- vector search for meaning
- keyword search for exact terms

Example:

If the query contains an exact function name like `read_text_file`, keyword search helps.

If the query says “how do agents remember things,” vector search helps.

## 4. Reranking

Reranking is a second scoring step.

Pipeline:

```text
retrieve top 20 chunks
rerank to best 5 chunks
send best 5 to model
```

This often improves quality.

## 5. Citations

Citations tell the user where information came from.

Good answer:

```text
Agent loops use repeated model-tool cycles [agent_loops.txt chunk 1].
```

Bad answer:

```text
Trust me.
```

## 6. Source Grounding

Grounding means the answer must be based on sources.

Strong RAG prompt:

```text
Use only the provided sources.
If the answer is not in the sources, say you do not know.
Include source names.
```

## 7. When RAG Fails

RAG can fail because:

- chunks are too small
- chunks are too large
- retrieval found wrong sources
- model ignored sources
- documents are outdated
- question needs reasoning across many chunks
- answer is not in the knowledge base

## 8. RAG Debugging

When RAG fails, inspect:

1. Was the right document loaded?
2. Was it chunked correctly?
3. Was the right chunk retrieved?
4. Was the prompt clear?
5. Did the model cite the source?

