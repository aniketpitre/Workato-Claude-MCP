---
url: 'https://docs.workato.com/en/connectors/salesforce/actions/download-file.md'
description: This action retrieves the contents of a file in Salesforce.
---

# Salesforce - Download file action

This action retrieves the contents of a file in Salesforce.

## Input

| Input fields | Description |
| --- | --- |
| File ID | Enter the unique Salesforce identifier for the file. You can obtain this ID from other connector actions, such as [Search records](/en/connectors/salesforce/actions/search-records). |
| Version number | Specify the version number of the file to retrieve. The action retrieves the latest version by default. |
| On-behalf-of user email | Optional. Enter the email of a Salesforce user to impersonate. Contact your Workato Customer Success Manager to enable this field. This field only supports JWT connections. |

## Output

| Output fields | Description |
| --- | --- |
| File | The file's contents. |
| Size | The size of the file in bytes. |

---
