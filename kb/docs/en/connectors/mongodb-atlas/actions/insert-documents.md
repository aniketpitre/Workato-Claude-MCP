---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/insert-documents.md
description: >-
  The Insert documents action in the MongoDB Atlas connector inserts new
  documents into a collection based on a defined schema and field mapping.
---

# MongoDB Atlas - Insert documents action

This action inserts a batch of documents with a fixed structure into a [MongoDB](/en/connectors/mongodb-atlas) Collection. When we say "fixed", we mean that you know all the possible fields a document can have.

**Note**: If any of the following are true, use the [Replicate documents](/en/connectors/mongodb-atlas/actions/replicate-documents) action instead:

- The documents' schema is flexible or unknown, or
- You want to update existing records

* * *

## Limitations

- [MongoDB limits the size of a single document to 16MB](https://docs.mongodb.com/manual/reference/limits/#mongodb-limit-BSON-Document-Size).

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection where documents will be inserted. Note: Names are case-sensitive. |
| **Document schema** | Defines the schema of the documents to be inserted. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |
| **Input document** | Defines the mapping between source data and the MongoDB documents to be inserted. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were inserted. |
| **Inserted IDs** | An array of `_id` values of the inserted documents. |
| **Number of documents inserted** | The total number of documents inserted into the collection. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)
