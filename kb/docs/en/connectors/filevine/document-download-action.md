---
url: 'https://docs.workato.com/en/connectors/filevine/document-download-action.md'
description: >-
  The Batch document download action retrieves S3 download URLs for multiple
  documents from Filevine using their document IDs.
---

# Filevine - Batch document download action

The **Batch document download** action retrieves S3 download URLs for a list of documents in Filevine using their document IDs.

## Input

| Input field | Description |
| --- | --- |
| Documents source list | Provide a list datapill containing document entries. Each entry must include a document ID. |
| Document ID | Enter the ID of a document in each list item. |
| Download URL Time to Live | Optional. Enter the time-to-live value for the generated download URLs. |

## Output

| Output field | Description |
| --- | --- |
| Download URLs | A list of signed S3 URLs to download the documents. |

---
