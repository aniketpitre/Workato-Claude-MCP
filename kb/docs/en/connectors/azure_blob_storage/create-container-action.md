---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/create-container-action.md
description: >-
  The create container action creates a container in the connected Azure Blob
  Storage account.
---

# Azure Blob Storage - Create container action

The **Create container** action creates a container in the connected Azure Blob Storage account.

## Input

| Input field | Description |
| --- | --- |
| Container name | Enter the name of the container. The name can only contain lower-case characters with no spaces. |
| Custom metadata | Enter custom metadata to attach to the container. |
| Access level | Select the access level for this container. By default, all containers created are private, however you can make them public. |

## Output

The output of this action is a datatree that contains information about the request sent to Azure Blob Storage. Use the [Search container](/en/connectors/azure_blob_storage/search-containers-action) or [Get container properties](/en/connectors/azure_blob_storage/get-container-properties-action) actions to get information about the blob.
