---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/attach-file-to-record-action.md
description: The Attach file to record action attaches a file to a record in NetSuite REST.
---

# NetSuite REST - Attach file to a record action

The **Attach file to a record** action attaches a file to a record in NetSuite REST.

Use this action to associate an existing file with a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements..

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to attach the file to. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to attach the file to. |
| File ID | Enter the internal ID of the file to attach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the file was attached to the record successfully. |
