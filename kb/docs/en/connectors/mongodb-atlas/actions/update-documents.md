---
url: >-
  https://docs.workato.com/en/connectors/mongodb-atlas/actions/update-documents.md
description: >-
  The Update documents action in the MongoDB Atlas connector updates documents
  in a collection that match an optional custom filter query.
---

# MongoDB Atlas - Update documents action

This action updates documents in a [MongoDB](/en/connectors/mongodb-atlas) Collection that match an optional custom query.

* * *

## Limitations

Updates to `array` fields have a few limitations:

- Updates to `array` fields will replace values entirely
  
- Partial updates (appending and/or removing fields) to `array` fields isn't currently supported.
  
  To make partial updates, we recommend that you:
  
  1. Use the [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents) to obtain a copy of the field's existing values
     
  2. Manipulate the field
     
  3. Update the field using this action
     

* * *

## Input

| Field | Description |
| --- | --- |
| **Collection** | The name of the target database collection to update documents in. Note: Names are case-sensitive. |
| **Document schema** | Defines the schema of the documents to be updated. You can add fields manually or provide sample JSON using the **Schema generator**. **Note:** For `integer` and `decimal` data, there are a few [limitations](/connectors/mongodb-atlas/typing-fields-in-mongodb.html) to be aware of. |
| **Custom filter query** | A JSON query used to filter documents. Documents that match the query's criteria will be updated. Refer to the [Custom Filter Queries for MongoDB guide](/connectors/mongodb-atlas/guides/using-custom-filter-queries.html) for more info. |

* * *

## Output

| Field | Description |
| --- | --- |
| **Collection name** | The name of the target database collection where documents were updated. |
| **Documents updated count** | The total number of updated documents. |

* * *

## Resources

- [MongoDB Atlas](/en/connectors/mongodb-atlas)
- [Using Custom Filter Queries](/en/connectors/mongodb-atlas/guides/using-custom-filter-queries)
- [Data Typing Limitations](/en/connectors/mongodb-atlas/guides/typing-fields-in-mongodb)
- [Delete documents action](/en/connectors/mongodb-atlas/actions/delete-documents)
- [Insert documents action](/en/connectors/mongodb-atlas/actions/insert-documents)
- [Search documents action](/en/connectors/mongodb-atlas/actions/search-documents)
- [Replicate documents action](/en/connectors/mongodb-atlas/actions/replicate-documents)
