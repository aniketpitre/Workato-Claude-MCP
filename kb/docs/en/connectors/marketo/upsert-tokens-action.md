---
url: 'https://docs.workato.com/en/connectors/marketo/upsert-tokens-action.md'
description: >-
  The Upsert tokens action in the Marketo connector lets you create or update
  tokens in a folder or program by name, type, and value.
---

# Marketo - Upsert tokens action

This action creates or updates tokens in Marketo.

## Input

| Field | Description |
| --- | --- |
| Folder ID | Select or provide the ID of the folder to upsert tokens in. |
| Folder type | Select or provide the type of the folder. Accepted values include `Folder` and `Program`. |
| Name | Enter the name of the token. The maximum length is 50 characters. |
| Type | Select or provide the type of the token. Accepted values include `date`, `number`, `rich text`, `score`, `sfdc campaign`, and `text`. |
| Value | Enter the value of the token. |

## Output

| Field | Description |
| --- | --- |
| Success | Indicates whether the upsert operation was successful. |
| Request ID | The unique identifier for the request. |
| Errors | Any errors encountered during the upsert operation. |
| Code (errors) | The error code if there were any issues. |
| Message (errors) | A description of the error. |
| Warnings | Any warnings generated during the upsert process. |
| Result | The result of the upsert operation. |
| Tokens (result) | The list of tokens associated with the upsert operation. |
| Name (tokens) | The name of the token. |
| Type (tokens) | The type of the token. |
| Value (tokens) | The value of the token. |
| Computed URL (tokens) | The computed URL of the token if applicable. |
| Section (tokens) | The section where the token is located. |
| Group ID (tokens) | The group ID associated with the token. |
| Sort order (tokens) | The order in which the token is sorted. |
| Last modified (tokens) | The date and time when the token was last modified. |
| Folder (result) | The folder where the token is stored. |
| Type (folder) | The type of the folder. |
| Value (folder) | The specific value or identifier of the folder. |

---
