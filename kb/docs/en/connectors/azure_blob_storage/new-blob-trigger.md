---
url: 'https://docs.workato.com/en/connectors/azure_blob_storage/new-blob-trigger.md'
description: >-
  The New blob trigger picks up new blobs that are created in Azure Blob Storage
  immediately.
---

# Azure Blob Storage - New blob trigger (real-time)

The **New blob trigger** immediately picks up new blobs that are created in Azure Blob Storage. An Azure webhook picks up events. Workato listens to these webhooks and processes them in real-time.

> **MFA REQUIRED**
> 
> Starting October 1, 2025, Microsoft will enforce multi-factor-authentication (MFA) for [Azure Resource Manager API](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/control-plane-and-data-plane#control-plane) operations used by this trigger. Ensure MFA is enabled for your Azure organization and re-authenticate your connection, or migrate to [Client Credentials Grant connections](/en/connectors/azure_blob_storage#create-a-client-credentials-grant) to maintain uninterrupted service.

## How to set up Azure webhook event

Complete the following steps to set up this trigger using a webhook event in your Azure portal:

1. Configure your Azure Blob Storage connection in Workato. Refer to [Azure Blob Storage](/en/connectors/azure_blob_storage#connection-setup) for more information.
   
2. Select **New blob trigger**. This provides a **Webhook URL**. This Webhook URL is specific to this recipe. Copy this webhook URL for use later in Azure.
   
3. Go to your Azure storage account.
   
4. Go to **Events**.
   
5. Create a new **Event Subscription**.
   
6. Enter the following information in the subscription form:
   
   - Set **Event Type** to `Blob created`.
   - Set **Subscriber Endpoint** to the Webhook URL provided in the trigger.
7. Return to Workato and click **Start recipe**. This is required for Workato to send the validation response to Azure for this webhook URL.
   
8. Select **Create** in your Azure instance to finish setting up your new Azure event subscription.
   

## Output

| Field | Description |
| --- | --- |
| Topic | The topic of the event subscription in Azure. |
| Subject | The subject of the event subscription in Azure. |
| Event type | The event type. |
| ID | The unique ID of the event. |
| Container | The container the event occurred in. |
| Blob Name | The name of the blob which caused the event. |
| ID | The unique ID of the event. |
| Data | Contains information about the blob that was created. |
| Data version | The data version of the blob. This increases when there are multiple blob snapshots. |
| Metadata version | The metadata version of the blob. |
| Event time | The exact time of the event. |

---
