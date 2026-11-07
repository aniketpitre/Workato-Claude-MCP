---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/upload-blob-action.md
description: >-
  The upload blob action uploads a blob to the connected Azure blob Storage
  account.
---

# Azure Blob Storage - Upload blob action

The **Upload blob** action uploads a blob to the connected Azure blob Storage account. This action is capable of [file streaming](/en/features/file-streaming).

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container in which to upload the blob. |
| Blob name | Enter the name of the blob when uploaded. If a blob with the same name already exists, that blob is replaced. |
| Blob contents | Enter the file contents of the blob. Map this from an upstream action that downloads a file. |
| Blob size | Enter the size of the entire blob. |
| Blob type | Select the type of blob, such as: `Block`, `Page`, or `Append`. The default is `Block`. |
| Custom metadata | Enter custom metadata to attach to the container. |
| Content type | Select the MIME type of the blob. |

## Output

The output of this action is datatree that contains information about the request sent to Azure Blob Storage. Use the [Search blob](/en/connectors/azure_blob_storage/search-blob-action) or [Get blob properties](/en/connectors/azure_blob_storage/get-blob-properties-action) actions to get information about the blob.
