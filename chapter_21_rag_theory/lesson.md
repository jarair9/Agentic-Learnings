# Chapter 21: RAG Theory Deep Dive

RAG means Retrieval-Augmented Generation.

It gives the model information before asking it to answer.

## 1. Why RAG Exists

Models do not automatically know:

- your private documents
- your latest project files
- your company rules
- your notes
- your database content

RAG lets your app fetch relevant information and place it in the prompt.

## 2. Basic RAG Pipeline

```text
documents -> chunks -> embeddings -> vector database
question -> embedding -> search -> top chunks -> model answer
```

## 3. Chunking

Chunking means splitting documents into smaller pieces.

Bad chunk:

```text
Entire 200-page book
```

Better chunk:

```text
One section, one concept, or a few paragraphs
```

Good chunks are:

- small enough to fit context
- large enough to contain meaning
- not cut in the middle of important ideas

## 4. Embeddings

An embedding is a list of numbers that represents meaning.

Similar meanings have similar numbers.

Example:

```text
"AI agent tools"
```

should be closer to:

```text
"function calling in agents"
```

than:

```text
"how to bake a cake"
```

## 5. Vector Search

Vector search finds chunks with similar embeddings.

This is how RAG finds meaning, not just exact keywords.

## 6. Hybrid Search

Hybrid search combines:

- keyword search
- vector search

This often works better than either one alone.

## 7. Reranking

Reranking means:

1. retrieve many possible chunks
2. use a stronger scoring step to choose the best chunks

This improves answer quality.

## 8. Grounding

Grounding means the answer is based on provided sources.

Good RAG prompts say:

```text
Use only the provided context.
If the answer is missing, say you do not know.
```

## 9. RAG Failure Modes

RAG can fail when:

- chunks are bad
- retrieval finds wrong text
- context is too long
- model ignores the context
- documents are outdated
- question needs multiple sources but only one is retrieved

## 10. RAG Evaluation

You test RAG with questions and expected answers.

Important metrics:

- did retrieval find the right chunk?
- was the answer correct?
- did the answer cite the right source?
- did the model avoid unsupported claims?

