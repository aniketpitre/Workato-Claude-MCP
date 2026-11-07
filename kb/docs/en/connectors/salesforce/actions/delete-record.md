---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/delete-record.md'
description: This action deletes a Salesforce record by its ID.
---

# Salesforce - Delete record action

This action deletes a Salesforce record by its ID.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the standard or custom object type to delete. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

An additional field loads dynamically based on the selected object. Use this field to specify the record's Salesforce ID.

## Output

There is no output for this action.

---

---
url: >-
  https://docs.workato.com/en/connectors/salesforce/actions/download-attachment.md
description: This action retrieves the contents of an attachment in Salesforce.
---

# Salesforce - Download attachment action

This action retrieves the contents of an attachment in Salesforce. The maximum attachment size is 25 MB.

## Input

| Input fields | Description |
| --- | --- |
| Attachment ID | Enter the unique Salesforce identifier for the attachment. You can obtain this ID from other Salesforce actions, such as [Search records](/en/connectors/salesforce/actions/search-records). |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| Attachment | The attachment's contents. |
| Size | The size of the attachment in bytes. |

---
