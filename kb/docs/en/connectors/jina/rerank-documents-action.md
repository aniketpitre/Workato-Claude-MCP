---
url: 'https://docs.workato.com/en/connectors/jina/rerank-documents-action.md'
description: >-
  Improve search and RAG pipelines by ranking a document list against a query,
  with optional embeddings for each result.
---

# Jina - Rerank documents action

The **Rerank documents** action scores and reorders documents by relevance to a query in Jina.

## Input

| Input field | Description |
| --- | --- |
| Model | Select a rerank model, or enter a custom model ID. |
| Query | Enter the query to rank documents against. |
| Documents | Enter the documents to rank. |
| Top N | Optional. Enter the number of top-ranked documents to return. |
| Return documents | Optional. Select **Yes** or **No** to include the document text in the response. The default is **Yes**. |
| Max document length | Optional. Enter the maximum number of characters per document. |
| Return embeddings | Optional. Select **Yes** or **No** to return each document's embedding. |

## Output

| Output field | Description |
| --- | --- |
| Model | The model used. |
| Object | The response type, for example `list`. |
| Usage | Token usage. |
| Total tokens (Usage) | Token usage. |
| Results | The ranked documents. |
| Index (Results) | The document's original position in the **Documents** array, starting at 0. |
| Relevance score (Results) | The document's relevance score, between 0 and 1. |
| Document (Results) | The document's text. The **Document** field is only available when **Return documents** is **Yes**. |
| Embedding (Results) | The document's embedding vector. The **Embedding** field is only available when **Return embeddings** is **Yes**. |

---
