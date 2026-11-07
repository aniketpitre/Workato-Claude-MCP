---
url: 'https://docs.workato.com/en/connectors/azure_blob_storage/new-event-trigger.md'
description: >-
  The New event trigger activates when specified blob storage events occur in
  monitored containers.
---

# Azure Blob Storage - New event trigger (real-time)

The **New event** trigger activates when a specified event occurs in a container you select. The **Management** scope is required to set up this trigger.

Ensure that the Azure user authenticated for this connection has the **EventGrid EventSubscription Contributor** role in the resource group provided.

> **MFA REQUIRED**
> 
> Starting October 1, 2025, Microsoft will enforce multi-factor-authentication (MFA) for [Azure Resource Manager API](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane#control-plane) operations used by this trigger. Ensure MFA is enabled for your Azure organization and re-authenticate your connection, or migrate to [Client Credentials Grant connections](/en/connectors/azure_blob_storage#create-a-client-credentials-grant) to maintain uninterrupted service.

## Input

| Input field | Description |
| --- | --- |
| Subscription | Select a subscription under which the webhook should be registered. |
| Resource group name | Select a resource group under which the webhook should be registered. |
| Container name | Select a container to monitor for events. If your container can't be found, toggle to **Enter container name** and provide the container name. |
| Events to monitor | Select the events to monitor. Refer to the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/event-grid/event-schema-blob-storage?tabs=event-grid-event-schema#blob-storage-events) to learn more about the supported Blob event types. |

## Output

| Output field | Description |
| --- | --- |
| Container name | The container where the event occurred. |
| Blob name | The name of the blob that triggered the event. |
| Topic | Full resource path to the event source. |
| Subject | Publisher-defined path to the event subject. |
| Event type | The type of event that occurred. |
| ID | Unique identifier for the event. |
| Data | Event data specific to the blob storage resource provider. |
| Data version | The schema version of the data object. |
| Metadata version | The schema version of the event metadata. |
| Event time | The time the event occurred, expressed in UTC. |

---

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

---

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

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/get-blob-properties-action.md
description: >-
  The get blob properties action retrieves the properties of a blob in the Azure
  Blob Storage account, including its metadata.
---

# Azure Blob Storage - Get blob properties action

The **Get blob properties** action retrieves the properties of a blob in the Azure Blob Storage account, including its metadata.

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container in which the blob you plan to retrieve properties from is stored. |
| Blob name | Select the name of the blob to download. |

## Output

The output of this action contains the properties of the blob, including its custom metadata.

---

---
url: >-
  https://docs.workato.com/en/connectors/azure_blob_storage/get-container-properties-action.md
description: >-
  The get container properties action retrieves the properties of a container in
  the Azure Blob Storage account.
---

# Azure Blob Storage - Get container properties action

The **Get container properties** action retrieves the properties of a container in the Azure Blob Storage account.

## Input

| Input field | Description |
| --- | --- |
| Container name | Select the name of the container you plan to retrieve properties from. |

## Output

The output of this action contains the properties of the container, except custom metadata.

---

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

---

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

---

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

---

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

---
