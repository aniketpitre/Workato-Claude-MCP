---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/search-blob-action.md
description: The search blobs action searches blobs in your Azure Blob Storage account.
---

# Azure Blob Storage - Search blobs action

The **Search blobs** action searches blobs in your Azure Blob Storage account.

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container in which you plan to search blobs. |
| Prefix | Select the prefix to filter blobs by. |
| Page size | Enter the maximum number of results to return. |
| Next page marker | Optional. Enter the next page marker to use for pagination. |

## Output

The output of this action contains the properties of the containers matching the search. The output also contains the **Next Marker** which you can use for pagination.
