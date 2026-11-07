---
url: 'https://docs.workato.com/en/connectors/hive/list-record.md'
description: >-
  The List records batch action in the Hive connector lets you retrieve a list
  of records for a selected object, such as actions or projects.
---

# Hive - List records action (batch)

The **List records** batch action retrieves a list of records for a selected object, such as actions or projects, in Hive.

## Input

| Input field | Description |
| --- | --- |
| Object | Select a Hive object, such as **Project** or **Action**. |
| Page size | Enter the maximum number of records to return. This field appears when you select **Action**, **Label**, or **Resource Assignment**. |
| Next page token | Enter a token to retrieve the next page of results. This field appears when you select **Action** or **Resource Assignment**. |

## Output

The output fields depend on the object you select in the input. Each object returns a unique set of fields based on its type. Common fields may include the following:

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the record. |
| Name | Name of the record, if applicable. |
| Created at | Timestamp indicating when the record was created. |
| Created by | ID of the user who created the record. |
| Modified at | Timestamp indicating when the record was last updated. |
| Modified by | ID of the user who last modified the record. |
| List size | Total number of records retrieved in the batch. |
| List index | Position of the record within the retrieved batch. |

---
