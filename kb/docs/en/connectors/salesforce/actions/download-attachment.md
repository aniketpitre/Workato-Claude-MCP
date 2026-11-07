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
