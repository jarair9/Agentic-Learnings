# Chapter 33: Building A Local RAG Index

In Chapter 21 you learned RAG theory.

Now you learn the implementation shape.

This chapter builds a tiny local index:

1. Load `.txt` files.
2. Split them into chunks.
3. Store chunks with metadata.
4. Search chunks.
5. Return the best context.

## 1. What Is An Index?

An index is a searchable collection.

For RAG, an index usually stores:

- chunk text
- source filename
- chunk number
- embedding
- metadata

## 2. Why Metadata Matters

Metadata lets you know where an answer came from.

Example:

```json
{
  "source": "tools.txt",
  "chunk_id": 2
}
```

Good RAG should be able to show sources.

## 3. Local First

Before using a vector database, build a local version.

This teaches the pipeline without extra tools.

## Run

```powershell
python chapter_33_local_rag_index/main.py
```

