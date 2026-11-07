---
url: >-
  https://docs.workato.com/en/connectors/filevine/document-confirmation-action.md
description: >-
  The Batch document upload confirmation action finalizes pending uploads and
  makes them available for use in Filevine.
---

# Filevine - Batch document upload confirmation action

The **Batch document upload confirmation** action finalizes uploaded documents in Filevine. Use this action after calling the **Batch document upload** action to make the files available for use.

## Input

| Input field | Description |
| --- | --- |
| Documents source list | Provide a list datapill containing the uploaded document entries. |
| Document ID | Enter the ID of each document in the list item. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the operation completed successfully. |
