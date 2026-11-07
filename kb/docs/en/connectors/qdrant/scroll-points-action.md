---
url: 'https://docs.workato.com/en/connectors/qdrant/scroll-points-action.md'
description: Page through points in a Qdrant collection that match a payload filter.
---

# Qdrant - Scroll points action

The **Scroll points** action reads points from a Qdrant collection in pages. Use it to find points by payload values, such as entries older than a cutoff date, without providing a vector.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to read. |
| Payload fields | Add payload fields for the collection. |
| Filter | Enter payload conditions that points must meet. |
| Order by | Enter a payload field to sort the results by. |

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Points | The points on this page, with their IDs and, if requested, payloads and vectors. |
| Next page offset | The cursor for the next page. Empty on the last page. |

---
