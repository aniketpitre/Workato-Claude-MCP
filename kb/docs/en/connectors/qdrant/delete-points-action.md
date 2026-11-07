---
url: 'https://docs.workato.com/en/connectors/qdrant/delete-points-action.md'
description: Permanently delete points from a Qdrant collection by ID or by payload filter.
---

# Qdrant - Delete points action

The **Delete points** action permanently deletes points from a Qdrant collection, either by ID or by payload filter.

> **DELETION IS PERMANENT**
> 
> You can't recover deleted points.

## Input

| Input field | Description |
| --- | --- |
| Collection name | Select the collection to delete points from. |
| Wait | Select whether to wait to apply deletions before returning. |
| Points | Enter any point IDs you plan to delete. Provide either Points or Filter. |
| Filter | Enter any payload conditions that points must meet to be deleted. Provide either Points or Filter. |

This action has a large amount of input fields. Refer to the [Qdrant API documentation](https://api.qdrant.tech/api-reference/points/delete-points) for more information on additional input fields.

## Output

| Output field | Description |
| --- | --- |
| Usage | Resources the request used. Includes hardware usage and inference usage. |
| Time | The time the request took to process, in seconds. |
| Status | The status of the request. Returns `ok` when the request succeeds. |
| Result | The result of the delete operation. |
| Operation ID | The ID of the delete operation. |

This action has a large amount of output fields. Refer to the [Qdrant API documentation](https://api.qdrant.tech/api-reference/points/delete-points) for more information on additional output fields.

---
