---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/delete-documents.md
description: >-
  The Delete documents action in the MongoDB Atlas connector deletes documents
  from a collection that match an optional custom filter query.
---

# MongoDB Atlas - Delete documents action

This action deletes documents from a [MongoDB](/en/connectors/mongodb-atlas) Collection that match an optional custom query.

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to delete documents from. Note: Names are case-sensitive. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be deleted. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were deleted. |
| **Documents deleted count** | The total number of deleted documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)
