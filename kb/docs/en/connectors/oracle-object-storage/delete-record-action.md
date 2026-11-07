---
url: >-
  https://docs.workato.com/en/connectors/oracle-object-storage/delete-record-action.md
description: The Delete record action deletes a record from Oracle Object Storage.
---

# Oracle Object Storage - Delete record action

The **Delete record** action deletes a record from Oracle Object Storage.

## Input

| Input field | Description |
| --- | --- |
| Record type | Specify the record type to delete. Fields load dynamically based on the selected record type. |

For example, if the selected record type is **Bucket**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Bucket name | Enter the name of the bucket to delete. |
| Headers | Specify custom request headers to send with the request. Includes client request ID and if match. |

## Output

The output fields are determined by the record type selected in the input. Map the relevant datapill from the datatree to subsequent steps. For example, selecting **Bucket** as the record type returns the following output fields:

| Output field | Description |
| --- | --- |
| Headers | Response headers. Includes client request ID and request ID. |
| Success | Whether the delete operation was successful or not. |
