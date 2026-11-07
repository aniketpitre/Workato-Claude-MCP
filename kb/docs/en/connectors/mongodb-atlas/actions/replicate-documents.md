---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/replicate-documents.md
description: >-
  The Replicate documents action in the MongoDB Atlas connector inserts or
  updates documents in a collection, de-duping records by unique fields.
---

# MongoDB Atlas - Replicate documents action

This action inserts multiple documents into a [MongoDB](/en/connectors/mongodb-atlas) Collection. Additionally, this action allows you to update existing documents, thereby preventing duplicate documents in the collection.

**If you want to retain document histories**, use the [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents) instead. The Insert Documents Action doesn't perform de-duplication, meaning existing documents aren't updated, but inserted as new documents. This allows you to see how a document has changed over time.

* * *

## How it works

When Workato replicates documents into the target collection, it will use the **Unique fields** input to check for existing documents and update them. This is called de-duplication, or de-duping, and is used to prevent duplicate records.

To summarize:

- **If a document doesn't exist in the collection**, Workato will insert the document.
- **If a document does exist in the collection**, it will be overwritten with the incoming version of the document.

Let's look at an example using `unique_code` as the **Unique field**.

**Here's an existing document in our collection**:

This document has a `unique_code` value of `CHOSEN_1`.

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Anakin",
  "last_name": "Skywalker",
  "friends": ["c3po", "r2d2"]
}
```

**And an incoming version of the document:**

Note that even though the `unique_code` value is still `CHOSEN_1`, the other field values are different from the existing document:

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Darth",
  "last_name": "Vader",
  "master": "Palpatine"
}
```

**The document after replication**:

During replication, Workato searches for records with `unique_code: CHOSEN_1` and if there's a match, overwrites the existing record.

This is what the final document would look like for this example:

```json
{
  "unique_code": "CHOSEN_1",
  "first_name": "Darth",
  "last_name": "Vader",
  "master": "Palpatine"
}
```

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection where documents will be replicated. Note: Names are case-sensitive. |
| **Documents** | The documents to replicate into the collection. This field accepts a List datapill. |
| **Unique fields** | The field(s) that identify a document as unique. For example: A unique `customer_id` Workato uses these field(s) to de-dupe records. If a document already exists in the collection, the document will be updated. Otherwise, a new document will be inserted. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were replicated. |
| **Documents inserted** | The total number of documents inserted into the collection. |
| **Documents updated** | The total number of documents in the collection that were updated. |
| **Inserted IDs** | An array of `_id` values of documents that were inserted. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Update documents action](/en/connectors/mongodb-atlas/actions/update-documents)
