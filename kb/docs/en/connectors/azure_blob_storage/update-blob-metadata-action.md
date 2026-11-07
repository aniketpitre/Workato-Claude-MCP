---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/update-blob-metadata-action.md
description: >-
  The update blob metadata action updates the metadata attached to a blob in the
  connected Azure Blob Storage account.
---

# Azure Blob Storage - Update blob metadata action

The **Update blob metadata** action updates the metadata attached to a blob in the connected Azure Blob Storage account.

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container that stores the blob. |
| Blob name | Enter the name of the blob you plan to update. |
| Custom metadata | Enter custom metadata to attach to the container. |

## Output

The output of this action is a datatree that contains information about the request sent to Azure Blob Storage. Use the [search blob](/en/connectors/azure_blob_storage/search-blob-action) or [get blob properties](/en/connectors/azure_blob_storage/get-blob-properties-action) actions to get information about the blob.
