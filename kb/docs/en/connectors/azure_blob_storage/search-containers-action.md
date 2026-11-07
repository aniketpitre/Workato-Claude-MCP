---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/search-containers-action.md
description: >-
  The search containers action searches the containers in your Azure Blob
  Storage account.
---

# Azure Blob Storage - Search containers action

The **Search containers** action searches the containers in your Azure Blob Storage account.

## Input

| Input field | Description |
| --- | --- |
| Prefix | Enter the prefix of container names to filter containers by. |
| Page size | Enter the maximum number of results for the action to return. |
| Next page marker | Optional. Enter the next page marker to use for pagination. |

## Output

The output of this action includes the properties of the containers matching the search. The output also contains the next page marker which you can use for pagination.
