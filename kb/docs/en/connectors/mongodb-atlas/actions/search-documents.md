---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/search-documents.md
description: >-
  The Search documents action in the MongoDB Atlas connector retrieves documents
  from a collection, with optional custom filter query, quota, and offset.
---

# MongoDB Atlas - Search documents action

This action retrieves documents from a [MongoDB](/en/connectors/mongodb-atlas) Collection.

* * *

## Limitations

Up to 10,000 documents can be retrieved at a time.

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to retrieve documents from. Note: Names are case-sensitive. |
| **Quota** | The maximum number of documents to retrieve from the collection. The default is 1,000; the maximum is 10,000. |
| **Offset** | The number of documents to skip. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be selected. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |
| **Document schema** | Defines the expected fields of retrieved documents. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were retrieved. |
| **Documents** | A list of the retrieved documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)
