---
url: 'https://docs.workato.com/en/features/file-streaming.md'
description: >-
  Learn how Workato file streaming transfers large files in chunks between apps,
  staying within source and destination memory quotas.
---

# File streaming

File streaming is a technique used to process a large file by dividing it into smaller pieces, transferring one piece at a time, and then putting the pieces back in order.

For example, when Workato uses file streaming to transfer a file between systems, each piece is downloaded from the source and uploaded to the destination in sequence.

File streaming is useful when processing a large file is impractical or impossible due to size or memory quotas at the source or destination app. With file streaming, you can stay within each app's constraints because Workato processes smaller chunks one at a time. This makes it possible for Workato to transfer files of any size between apps that support streaming. Workato also supports file streaming for large volume storage and data transformations.

The following diagram illustrates how file streaming works:

![How file streaming works](/assets/streaming-illustration.CyLcPq6_.jpg) _How file streaming works_

## Use cases

You can use Workato's file streaming for use cases such as the following:

- Send data in bulk to applications
- Receive data from applications using bulk triggers or bulk actions
- Store large files in [Workato FileStorage](/en/features/workato-filestorage) or other file systems such as [SFTP](/en/connectors/sftp) and [S3](/en/connectors/s3)
- Send or receive data from [SQL Transformations](/en/features/sql-transformations)

For example, with file streaming, you can:

- Extract a file with 1 million rows of leads data from an on-prem file server and load it into a Google BigQuery table
- Accumulate 100,000 rows from a non-streaming source such as HubSpot to Workato FileStorage using batch actions, and then stream the rows from FileStorage to [Salesforce bulk APIs](/en/connectors/salesforce/salesforce-bulk) all at once
- Extract new or updated contact records from [Marketo](/en/connectors/marketo) using bulk triggers and aggregate the records with other data sources in [SQL Transformations](/en/features/sql-transformations)

### Comparison with batch processing

Batch processing is when multiple jobs each process multiple records. The number of records that can be processed in a single job is determined by the batch size. Workato creates as many jobs as needed to process all relevant records, which makes it possible to process very large files. However, due to batch size and memory quotas, this approach can result in a high volume of API calls, and it does not scale well as the volume of data increases.

In contrast, file streaming uses a single job to process all relevant records in a single call to a streaming API, chunk by chunk. This results in fewer API calls and faster processing, even when the file is very large.

Batch triggers and actions should typically be paired with other batch actions. Likewise, streaming-compatible data producers (such as file downloads, bulk triggers, and bulk export actions) must be paired with streaming-compatible data consumers (such as file uploads and bulk create, bulk upsert, and bulk import actions).

> **HTTP CONNECTOR EXCEPTION**
> 
> The [Send request via HTTP](/en/developing-connectors/http/building-http-action) action is an exception to this rule. Set [**Wait for response**](/en/developing-connectors/http/building-http-action#configure-http-action-as-a-long-action) and [**Enable streaming**](/en/developing-connectors/http/building-http-action#stream-http-responses) to **Yes** to stream the response to any subsequent action, including actions that don't support file streaming.

We recommend using triggers and actions that support file streaming whenever possible to help:

- Simplify recipe design
- Reduce task count
- Reduce the number of API calls made between sources and destinations

## How to use file streaming

If either the source (such as a file download, bulk trigger, or bulk action) or the destination (such as a file upload or bulk action) supports file streaming, Workato automatically initiates file streaming when you pass a File contents or CSV contents datapill to the **File contents** input field. No additional configuration is required in the recipe.

![Passing a File contents datapill to a File contents input field](/assets/file-contents-datapill.1QK9pKm2.png) _Passing a File contents datapill to a **File contents** input field_

Note that the streaming transfer begins when the recipe reaches the consumer action step in the recipe. File streaming actions are usually [long or deferred actions](/en/recipes/long-actions). As a result, streaming actions do not time out, no matter how long the transfer takes.

## Triggers and actions that support file streaming

The following table lists the triggers and actions that support file streaming:

| Connector name | Triggers and actions that support file streaming |
| --- | --- |
| [Adobe Experience Manager](/en/connectors/adobe_experience_manager) | Upload asset by streaming action |
| [Amazon S3](/en/connectors/s3) | Download file contents action, Upload file (streaming) action, New file trigger, New/updated file or folder trigger |
| Anaplan | Download file action, Download dump file action, Upload file action |
| [Azure Blob Storage](/en/connectors/azure_blob_storage) | Download blob contents action, Upload blob action |
| [BIM360](/en/connectors/bim360) | Download document in a project action, Upload document to a project action |
| [Box](/en/connectors/box) | Download file action, Upload file using file contents action |
| [Bynder](/en/connectors/bynder) | Upload asset action, Download asset action |
| [Dropbox](/en/connectors/dropbox) | Upload file using file contents action |
| [Egnyte](/en/connectors/egnyte) | Download file from selected folder action, Upload file action |
| [File tools by Workato](/en/features/file-tools-by-workato) | Get file from URL action, Compress files action |
| [Freshdesk](/en/connectors/freshdesk) | Get ticket attachments action |
| [FTP/FTPS](/en/connectors/ftp) | Download large file action, Upload file action |
| [HTTP connector](/en/developing-connectors/http/building-http-action) | Send request via HTTP action (requires **Wait for response** and **Enable streaming** to both be set to **Yes**). The streamed response can be passed to any subsequent action, including actions that don't support file streaming. |
| [Google Cloud Storage](/en/connectors/google_cloud_storage) | Download object action, Upload object action |
| [Google Drive](/en/connectors/google-drive) | Download file action, Upload file action, New file or folder in folder hierarchy trigger, New file or folder trigger |
| [Jira](/en/connectors/jira) | Export new issues in Jira trigger, Export new/updated issues in Jira trigger |
| [Marketo](/en/connectors/marketo) | Export New leads in Marketo trigger, Export New/updated leads in Marketo trigger |
| [Microsoft Dynamics 365](/en/connectors/dynamics-crm) | Export New records trigger, Export New/updated records trigger |
| [Microsoft Sharepoint](/en/connectors/sharepoint) | Upload file in library action |
| [NetSuite](/en/connectors/netsuite) | Export new records trigger, Export New/updated records trigger |
| [OneDrive](/en/connectors/onedrive) | Download File action, Upload large file via session action |
| [On-prem](/en/connectors/on-prem-files) | Download file action, Upload file action, Upload file (Legacy) action, New file in folder trigger |
| [Outlook](/en/connectors/outlook/outlook) | Send email action |
| [Percolate](/en/connectors/percolate) | Download asset action |
| [PlanGrid](/en/connectors/plangrid) | Download object action |
| [Quickbase](/en/connectors/quickbase) | Create and update records in bulk from CSV file action |
| [Salesforce](/en/connectors/salesforce) | Upload file action |
| [ServiceNow](/en/connectors/servicenow) | Upload attachment action, Get attachment contents action, Export New records trigger, Export New/updated records trigger |
| [SFTP](/en/connectors/sftp) | Download file action, Upload file action |
| [SMB](/en/connectors/smb) | Download file action, Upload file action |
| [Workato FileStorage](/en/features/workato-filestorage) | Get file contents action, New File trigger |
| [Workfront](/en/connectors/workfront) | Download document action |
| [Zoom](/en/connectors/zoom) | Download cloud recording action |

> **BUILD CUSTOM CONNECTORS**
> 
> To learn how to build custom connectors that use file streaming, refer to the [Connector SDK file streaming guide](/en/developing-connectors/sdk/guides/building-actions/streaming).

> **SEE FILE STREAMING IN ACTION**
> 
> View a [sample recipe](https://www.workato.com/recipes/867852#recipe) that uses file streaming to transfer files from an on-prem file system to Amazon S3.

---
