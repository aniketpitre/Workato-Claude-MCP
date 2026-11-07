---
url: 'https://docs.workato.com/en/connectors/kissflow/create-record-action.md'
description: The Create record action enables you to create a record in Kissflow.
---

# Kissflow - Create record action

The **Create record** action enables you to create a record in Kissflow.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create its record. Fields load dynamically based on the object you select. As of now, we only support Dataset record object for this action. |
| Dataset ID | A unique identifier of the dataset for which a new record will be created. |
| Key | Unique identifier of the new record. |

Custom input fields will load based on the dataset ID.

## Output

As of now, only the dataset record is supported for creating a record.

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the dataset record |
| Previous ID | Identifier of the record before update. Null in the case of creating a record. |
| Created at | Timestamp when the record was created. |
| Modified at | Timestamp when the record was last modified. |
| Created by | User details who created the record. |
| Modified by | User details who last modified the record. |
| Flow name | Name of the flow used while creating the dataset record. |
| Flow type | Type of the flow used while creating the dataset record. |
| Doc version | The version of the dataset after creating the dataset record. |

Custom output fields will be present based on the dataset ID.

---
