---
url: 'https://docs.workato.com/en/connectors/qdrant/retrieve-points-action.md'
description: >-
  Look up points by ID in a Qdrant collection and return their payloads and
  vectors.
---

# Qdrant - Retrieve points action

The **Retrieve points** action returns points from a Qdrant collection by ID. Use it to check whether an ID is already stored or to read a stored payload.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to read. |
| IDs | Enter the list of point IDs to retrieve. |
| Payload fields | Enter the payload fields for the collection. |

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Points | The points found, with their IDs and, if requested, payloads and vectors. |

---
