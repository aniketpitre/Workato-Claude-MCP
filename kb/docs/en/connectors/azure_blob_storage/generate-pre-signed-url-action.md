---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/generate-pre-signed-url-action.md
description: >-
  The generate pre-signed URL action generates a pre-signed URL for a blob in
  Azure Blob Storage.
---

# Azure Blob Storage - Generate pre-signed URL action

The **Generate pre-signed URL** action generates a pre-signed URL for a blob in Azure Blob Storage.

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container that contains the blob you plan to generate a pre-signed URL for. |
| Blob name | Select the name of the blob you plan to generate a pre-signed URL for. |
| Permissions | Select the permissions for the blob resource to grant to the client through the pre-signed URL. |
| Expiry time | Select the time the pre-signed URL stays valid until. |

## Output

| Output field | Description |
| --- | --- |
| URL | Returns the pre-signed URL of the associated blob resource. |
