---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/new-updated-document-trigger.md
description: >-
  The New/updated document trigger runs when a document is created or updated in
  Veeva Vault.
---

# Veeva Vault - New/updated document trigger

The **New/updated document** trigger runs when a document is created or updated in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| From date | Enter the date/time to only return documents modified after. Defaults to the recipe start time if left blank. |
| Status filter | Enter a document status to filter by, such as `Approved`. |
| Document type filter | Enter a document type to filter by, such as `Procedure`. |
| Classification filter | Enter a classification to filter by, for example `SOP`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The document ID. |
| Name | The document name. |
| Title | The document title. |
| Type | The document type. |
| Classification | The document classification. |
| Lifecycle | The document lifecycle. |
| Status | The document status. |
| Description | The document description. |
| Last modified date | The date the document version was last modified. |
