---
url: 'https://docs.workato.com/en/connectors/qdrant/upsert-points-action.md'
description: >-
  Insert or update points in a Qdrant collection, including their vectors and
  payloads.
---

# Qdrant - Upsert points action

The **Upsert points** action inserts points into a Qdrant collection. If a point with the same ID exists, the action overwrites it.

Vectors must be arrays of floats produced by an upstream embedding step. The vector size must match the size the collection is configured with.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to write to. |
| Payload fields | Add payload fields for the collection. |
| Points | Enter the points to upsert. |
| Batch | Enter the request body for the batch upsert. |
| Update filter | Enter filters that points must match to be upserted. |

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Result | The result of the upsert operation. |
| Operation ID | The ID of the upsert operation. |

---
