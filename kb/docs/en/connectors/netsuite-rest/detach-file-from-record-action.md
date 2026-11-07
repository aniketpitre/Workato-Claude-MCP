---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/detach-file-from-record-action.md
description: >-
  The Detach file from record action detaches a file from a record in NetSuite
  REST.
---

# NetSuite REST - Detach file from a record action

The **Detach file from a record** action detaches a file from a record in NetSuite REST.

Use this action to remove the association between a file and a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to detach the file from. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to detach the file from. |
| File ID | Enter the internal ID of the file to detach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the file was detached from the record successfully. |
