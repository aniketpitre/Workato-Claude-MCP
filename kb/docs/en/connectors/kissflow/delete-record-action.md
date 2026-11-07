---
url: 'https://docs.workato.com/en/connectors/kissflow/delete-record-action.md'
description: >-
  The Delete record action enables you to delete the specified record from
  Kissflow.
---

# Kissflow - Delete record action

The **Delete record** action enables you to delete the specified record from Kissflow.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete its record. Fields load dynamically based on the object you select. As of now, we only support Dataset record object for this action. |
| Dataset ID | Unique identifier of the dataset from which the record needs to be deleted. |
| Name | A unique identifier of the dataset record to delete. |

## Output

As of now, only the dataset record is supported for deleting a record.

| Output field | Description |
| --- | --- |
| Name | Unique identifier of the record that was deleted. |
| Status | Status of the operation. |

---
