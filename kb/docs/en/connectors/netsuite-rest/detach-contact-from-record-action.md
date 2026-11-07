---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/detach-contact-from-record-action.md
description: >-
  The Detach contact from record action detaches a contact from a record in
  NetSuite REST.
---

# NetSuite REST - Detach contact from a record action

The **Detach contact from a record** action detaches a contact from a record in NetSuite REST.

Use this action to remove the association between a contact and a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to detach the contact from. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to detach the contact from. |
| Contact ID | Enter the internal ID of the contact to detach. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the contact was detached from the record successfully. |
