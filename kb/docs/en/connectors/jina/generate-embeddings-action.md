---
url: 'https://docs.workato.com/en/connectors/jina/generate-embeddings-action.md'
description: >-
  Turn text into numeric vectors for search, retrieval, or classification
  pipelines, with configurable dimensions and encoding.
---

# Jina - Generate embeddings action

The **Generate embeddings** action creates vector embeddings for text in Jina.

## Input

| Input field | Description |
| --- | --- |
| Model | Select an embedding model, or enter a custom model ID. |
| Input | Enter one or more strings to embed. |
| Task | Optional. Select the intended use for the embedding, such as **Retrieval query**, **Retrieval passage**, or **Classification**. |
| Dimensions | Optional. Enter the number of dimensions for the output embedding. |
| Embedding type | Optional. Select the embedding encoding. Options are **float**, **base64**, **binary**, or **ubinary**. |
| Normalized | Optional. Select **Yes** or **No** to normalize the embedding vector. |
| Late chunking | Optional. Select **Yes** or **No** to enable late chunking. |
| Truncate | Optional. Select **Yes** or **No** to truncate input that exceeds the model's token limit. |
| Input type | Optional. Select the input type for ColBERT-style models. Options are **Query** or **Document**. |
| Return multivector | Optional. Select **Yes** or **No** to return multi-vector embeddings. |
| Return tokenized input | Optional. Select **Yes** or **No** to return the tokenized input. |

## Output

The following are a representative set of output fields. Refer to the Jina [Embeddings](https://jina.ai/embeddings/) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Model | The model used. |
| Object | The response type, for example `list`. |
| Usage | Token usage. |
| Total tokens (Usage) | Token usage. |
| Data | An array of embedding results. |
| Object (Data) | The result type. Typically `embedding` or `embeddings` when **Return multivector** is **Yes**. |
| Index (Data) | The input's position in the **Input** array, starting at 0. |
| Embedding (Data) | The embedding vector. |

---
