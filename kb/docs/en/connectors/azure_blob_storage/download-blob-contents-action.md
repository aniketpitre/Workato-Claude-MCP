---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/download-blob-contents-action.md
description: >-
  The download blob contents action downloads a blob in the connected Azure Blob
  Storage account.
---

# Azure Blob Storage - Download blob contents action

The **Download blob contents** action downloads a blob in the connected Azure Blob Storage account. This action is [streaming compatible.](/en/features/file-streaming)

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container in which the blob you plan to download is stored. |
| Blob name | Select the name of the blob you plan to download. |
| Chunk size | Enter the chunk size to download the file by. Refer to the [File streaming](/en/features/file-streaming) guide for more information on this input field. |

## Output

| Output field | Description |
| --- | --- |
| Blob contents | The content the blob contains. |
| Size | The size of the blob. |
