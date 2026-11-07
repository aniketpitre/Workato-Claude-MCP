---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/new-updated-record-scheduled-vql-trigger.md
description: >-
  The New/updated record (scheduled VQL) trigger runs your VQL SELECT statement
  on a fixed schedule and fires for each new or updated record in Veeva Vault.
---

# Veeva Vault - New/updated record (scheduled VQL) trigger

The **New/updated record (scheduled VQL)** trigger runs your VQL `SELECT` statement on a fixed schedule and fires for each new or updated record in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| VQL query | Enter a VQL `SELECT` statement without a date filter. |
| Date field (cursor) | Enter the field you plan to use as the moving cursor. Use `version_modified_date__v` for documents and `modified_date__v` for vobject records. Defaults to `modified_date__v`. |
| From date | Enter a date/time to start retrieving records from. Defaults to 1 hour ago. |

## Output

| Output field | Description |
| --- | --- |
| ID | The record ID. |
| Name | The record name. |
| Version modified date | The version modified date, if the query selected it. |
| Modified date | The modified date, if the query selected it. |
