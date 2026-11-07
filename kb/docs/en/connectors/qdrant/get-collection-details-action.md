---
url: 'https://docs.workato.com/en/connectors/qdrant/get-collection-details-action.md'
description: 'Get the status, point counts, and vector configuration of a Qdrant collection.'
---

# Qdrant - Get collection details action

The **Get collection details** action returns the status, point counts, and vector configuration of a Qdrant collection. Use it to confirm that your embedding model's dimension matches the collection's vector size before you index data.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to return details about. |

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The collection status. |
| Points count | The number of points in the collection. |
| Indexed vectors count | The number of vectors that are indexed. |
| Vector size | The number of dimensions each vector has. |
| Distance | The distance metric the collection uses to compare vectors. |

---
