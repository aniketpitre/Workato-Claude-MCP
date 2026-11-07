---
url: 'https://docs.workato.com/en/connectors/qdrant/query-points-action.md'
description: >-
  Find the nearest points to an embedding in a Qdrant collection, with optional
  payload filters.
---

# Qdrant - Query points action

The **Query points** action searches a Qdrant collection for the points closest to a vector and returns them with similarity scores.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to search. |
| Payload fields | Enter the payload fields to return. |
| Prefetch | Enter subqueries to run before querying points. |
| Query | Enter a query vector as a JSON array of floats, a point ID, or a query object. |
| Filter | Enter filters to return points that meet these conditions. |
| Lookup from | Select the collection to look up points from. |

This action has a large amount of input fields. Refer to the [Qdrant API documentation](https://api.qdrant.tech/api-reference/search/query-points) for more information on additional input fields.

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Points | The matching points, ordered by score. Each point includes its ID, similarity score, and payload, if requested. |

This action has a large amount of output fields. Refer to the [Qdrant API documentation](https://api.qdrant.tech/api-reference/search/query-points) for more information on additional output fields.

---
