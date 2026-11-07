---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/attach-contact-to-record-action.md
description: >-
  The Attach contact to record action attaches a contact to a record in NetSuite
  REST.
---

# NetSuite REST - Attach contact to a record action

The **Attach contact to a record** action attaches a contact to a record in NetSuite REST.

Use this action to associate an existing contact with a NetSuite record. Refer to [REST Web Services prerequisites and setup](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html) for setup requirements.

## Input

| Input field | Description |
| --- | --- |
| Record | Select the NetSuite record type to attach the contact to. The picklist shows only records supported by NetSuite REST Web Services. Toggle the field to use a custom record. |
| Internal ID | Enter the internal ID of the record to attach the contact to. |
| Contact ID | Enter the internal ID of the contact to attach. |
| Contact role ID | Optional. Enter the internal ID of the contact role to assign to the contact. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the contact was attached to the record successfully. |
