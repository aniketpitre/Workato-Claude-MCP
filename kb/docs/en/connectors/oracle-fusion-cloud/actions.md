---
url: 'https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions.md'
description: >-
  Browse the actions available in the Oracle Fusion Cloud connector for Workato
  to create and manage records on Fusion Cloud objects.
---

# Oracle Fusion Cloud - Actions

The Oracle Fusion Cloud connector supports the following actions.

- [Append file comment action](/en/connectors/oracle-fusion-cloud/actions/append-file-comment)
- [Confirm extract consumption action](/en/connectors/oracle-fusion-cloud/actions/confirm-extract-consumption)
- [Create record action](/en/connectors/oracle-fusion-cloud/actions/create-record)
- [Create records action (batch)](/en/connectors/oracle-fusion-cloud/actions/create-records-batch)
- [Create user action](/en/connectors/oracle-fusion-cloud/actions/create-user)
- [Delete record action](/en/connectors/oracle-fusion-cloud/actions/delete-record)
- [Download ESS job execution details action](/en/connectors/oracle-fusion-cloud/actions/download-ess-job-execution-details)
- [Download export output action](/en/connectors/oracle-fusion-cloud/actions/download-export-output)
- [Export bulk data action](/en/connectors/oracle-fusion-cloud/actions/export-bulk-data)
- [Extract and purge action](/en/connectors/oracle-fusion-cloud/actions/extract-and-purge)
- [Fetch extract output action](/en/connectors/oracle-fusion-cloud/actions/fetch-extract-output)
- [Get flow task instance status action](/en/connectors/oracle-fusion-cloud/actions/get-flow-task-instance-status)
- [Get record action](/en/connectors/oracle-fusion-cloud/actions/get-record)
- [Import bulk data action](/en/connectors/oracle-fusion-cloud/actions/import-bulk-data)
- [List entities action](/en/connectors/oracle-fusion-cloud/actions/list-entities)
- [Load and import data action](/en/connectors/oracle-fusion-cloud/actions/load-and-import-data)
- [Search documents by file prefix action](/en/connectors/oracle-fusion-cloud/actions/search-documents-by-file-prefix)
- [Search records action](/en/connectors/oracle-fusion-cloud/actions/search-records-batch)
- [Search records using advanced query action (batch)](/en/connectors/oracle-fusion-cloud/actions/search-records-using-advanced-query-batch)
- [Submit and get flow instance ID action](/en/connectors/oracle-fusion-cloud/actions/submit-and-get-flow-instance-id)
- [Submit ESS job request action](/en/connectors/oracle-fusion-cloud/actions/submit-ess-job-request)
- [Submit job with output action](/en/connectors/oracle-fusion-cloud/actions/submit-job-with-output)
- [Update interface data action](/en/connectors/oracle-fusion-cloud/actions/update-interface-data)
- [Update record action](/en/connectors/oracle-fusion-cloud/actions/update-record)
- [Update records action (batch)](/en/connectors/oracle-fusion-cloud/actions/update-records-batch)
- [Upload to UCM action](/en/connectors/oracle-fusion-cloud/actions/upload-to-ucm)
- [Upsert record action](/en/connectors/oracle-fusion-cloud/actions/upsert-record)

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/append-file-comment.md
description: >-
  The Append file comment action adds a comment to a document in Oracle Fusion
  Cloud's Universal Content Management (UCM) system.
---

# Oracle Fusion Cloud - Append file comment action

The **Append file comment** action adds a comment to a document in Oracle Fusion Cloud's Universal Content Management (UCM) system.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Document ID | Enter the unique identifier of the target document. |
| Comments | Enter the comment to add to the document. |

## Output

| Output field | Description |
| --- | --- |
| Result | The result of the comment append operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/confirm-extract-consumption.md
description: >-
  The Confirm extract consumption action acknowledges and confirms that the
  download for a specific extract has completed.
---

# Oracle Fusion Cloud - Confirm extract consumption action

The **Confirm extract consumption** action acknowledges that the download for a specific extract has completed in Oracle Fusion Cloud.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the job package name and job definition name, separated by a comma. |
| Document IDs | Provide a list of numeric document identifiers. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the status code for the operation. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/create-record.md
description: >-
  The Create record action creates a new record for a specified object in Oracle
  Fusion Cloud
---

# Oracle Fusion Cloud - Create record action

The **Create record** action creates a new record for a specified object in Oracle Fusion Cloud, such as a receivable invoice, product, or supplier.

All attributes and child objects appear as input fields after you select the object. Provide the required fields and populate required child objects to create the record.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to create a new record for. |

Additional fields load dynamically based on your selected object type.

## Output

The output returns a single object that represents the newly created record, including all fields and child objects defined by the selected object type.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/create-records-batch.md
description: >-
  The Create records batch action creates new records for a specified object in
  Oracle Fusion Cloud in batches.
---

# Oracle Fusion Cloud - Create records action (batch)

The **Create records** batch action creates multiple new records for a specified object in Oracle Fusion Cloud. For example, it can create multiple receivable invoices for a specific customer account.

All attributes and child objects appear as input fields after you select the object. Provide the required fields and populate required child objects to create the records.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the records to create. |
| Records | Expand this section to enter the field values for the records. |
| Records source list | Input a list datapill. |

Additional fields load dynamically based on the selected object.

## Output

| Output field | Description |
| --- | --- |
| Items | A list of the created records. |

Additional fields return based on the selected object.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/create-user.md
description: >-
  The Create user action creates a user in Oracle Fusion Cloud using HCM Data
  Loader.
---

# Oracle Fusion Cloud - Create user action

The **Create user** action creates a user in Oracle Fusion Cloud using the HCM Data Loader process.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Web key | Provide the authentication key for Oracle WebCenter Content service. |
| IDC service | Set to `CHECKIN_UNIVERSAL` for uploading HCM Data Loader files to create users. |
| User | Optional container for user-specific metadata configuration. |
| Fields (User) | Configure user-specific metadata fields and their values as needed. |
| Result set (User) | Optional result set configuration for user data. |
| Option list (User) | Optional option list configuration for user data. |
| Document | Container for the HCM Data Loader ZIP file and its metadata. |
| Fields (Documents) | Configure document metadata as key-value pairs: **dDocTitle**: Document title; **dDocType**: Document type (usually `Document`); **dDocAuthor**: Document author (your HCM username); **dSecurityGroup**: Security group (usually `FAFusionImportExport`); **dDocAccount**: Document account (usually `hcm$/dataloader$/import$`); **dDocName**: Content ID (optional, for versioning) |
| Result set (Documents) | Optional result set configuration for document data. |
| Option list (Documents) | Optional option list configuration for document data. |
| File (Documents) | Configure the HCM Data Loader file upload: **href**: File reference, **name**: File name (usually `primaryFile`), **Contents**: Base64 encoded ZIP file content containing the user.dat file |

### User.dat file format

Create a `user.dat` file with the following structure:

```text
METADATA|User|UserName|PersonNumber|StartDate|Active|EmailAddress
MERGE|User1|1001|2025/09/03|Y|<user1@example.com>
```

Convert the `user.dat` file to a ZIP file, then encode the ZIP file as Base64 before entering it in the **File (Documents) > Contents** field.

Refer to the [Oracle Fusion Cloud documentation](https://docs.oracle.com/en/solutions/load-data-into-hcm-cloud/use-webcenter-content-generic-soap-web-service-upload-hcm-data-loader-zip-file1.html#GUID-D2C49B89-5973-4971-977B-CC5D9CBBED7E) for more information.

## Output

| Output field | Description |
| --- | --- |
| IDC service | WebCenter Content service used. |
| User | User metadata response. |
| Fields (User) | User field responses. |
| Result set (User) | User result set data. |
| Option list (User) | User option list data. |
| Document | Document metadata response. |
| Fields (Document) | Document field responses. |
| Result set (Document) | Document result set data. |
| Option list (Document) | Document option list data. |
| File (Document) | File upload response details. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/delete-record.md
description: The Delete record action deletes an existing record.
---

# Oracle Fusion Cloud - Delete record action

The **Delete record** action deletes an existing record. Select an object and provide its primary key to identify the record to delete.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the record to delete. |
| Object ID | Provide the ID of the record to delete. |

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates whether the result of the delete operation was successful. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/download-ess-job-execution-details.md
description: >-
  The Download ESS job execution details action downloads the Enterprise
  Scheduling Service (ESS) job output and logs as a ZIP file for specified ESS
  request ID.
---

# Oracle Fusion Cloud - Download ESS job execution details action

The **Download ESS job execution details** action downloads the Enterprise Scheduling Service (ESS) job output and logs as a ZIP file for specified ESS request ID.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Request ID | Enter the request ID of the submitted Enterprise Scheduling Service (ESS) job. |
| File type | Specify the file type to determine the execution details to download: `Log` to download the log files.; `Out` to download the output files.; `All` to download both log and output files. By default, file type is `All`. |
| Include debug | Select whether to include detailed debug information in the response. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the downloaded execution details file. |
| Content type | The content type of the downloaded file. |
| Document title | The title assigned to the execution details document. |
| Document author | The author or creator of the execution details document. |
| Document security group | The security group associated with the document for access control. |
| Document account | The account identifier associated with the document. |
| Document name | The internal document name used by Oracle Fusion Cloud. |
| Document ID | The unique identifier for the document in Oracle Fusion Cloud. |
| File content | The actual content of the execution details file. |
| Zip contents | Contains extraction information when the downloaded file is a ZIP archive. |
| Debug info (Zip contents) | Technical information about the ZIP file processing. |
| Content size (Debug info) | The size of the ZIP file content in bytes. |
| Content preview (Debug info) | A preview of the ZIP file content for debugging purposes. |
| Is zip (Debug info) | Indicates whether the content is a ZIP file. |
| Files (Zip contents) | An array of files extracted from the ZIP archive. |
| Name (Files) | The name of the individual file within the ZIP archive. |
| Size (Files) | The size of the individual file in bytes. |
| Path (Files) | The full path of the file within the ZIP archive structure. |
| Content (Files) | The content of the individual file. |
| Is binary (Files) | Indicates whether the file contains binary content. |
| Error (Files) | Any error message encountered during file extraction. |
| Content | Container for content reference information. |
| Include (Content) | Reference information for included content or attachments. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/download-export-output.md
description: >-
  The Download export output action downloads the Enterprise Scheduling Service
  (ESS) job output and logs as a ZIP file for the specified ESS request ID.
---

# Oracle Fusion Cloud - Download export output action

The **Download export output** action downloads the Enterprise Scheduling Service (ESS) job output and logs as a ZIP file for the specified ESS request ID.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Request ID | Enter the request ID of the Enterprise Scheduling Service (ESS) job. |

## Output

| Output field | Description |
| --- | --- |
| File name | The name of the downloaded export output file. |
| Content type | The content type of the downloaded file. |
| Document title | The title assigned to the export output document. |
| Document author | The author or creator of the export output document. |
| Document security group | The security group associated with the document for access control. |
| Document account | The account identifier associated with the document. |
| Document name | The internal document name used by Oracle Fusion Cloud. |
| Document ID | The unique identifier for the document in Oracle Fusion Cloud. |
| File content | The actual content of the export output file. |
| Zip contents | Contains extraction information when the downloaded file is a ZIP archive. |
| Debug info (Zip contents) | Technical information about the ZIP file processing. |
| Content size (Debug info) | The size of the ZIP file content in bytes. |
| Content preview (Debug info) | A preview of the ZIP file content for debugging purposes. |
| Is zip (Debug info) | Indicates whether the content is a ZIP file. |
| Files (Zip contents) | An array of files extracted from the ZIP archive. |
| Name (Files) | The name of the individual file within the ZIP archive. |
| Size (Files) | The size of the individual file in bytes. |
| Path (Files) | The full path of the file within the ZIP archive structure. |
| Content (Files) | The content of the individual file. |
| Is binary (Files) | Indicates whether the file contains binary content. |
| Error (Files) | Any error message encountered during file extraction. |
| Content | Container for content reference information. |
| Include (Content) | Reference information for included content or attachments. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/export-bulk-data.md
description: >-
  The Export bulk data action submits an ESS job request to export large
  datasets from Oracle Fusion Cloud.
---

# Oracle Fusion Cloud - Export bulk data action

The **Export bulk data** action submits an ESS job request to export large datasets from Oracle Fusion Cloud. After the job completes, it automatically uploads the output and log files to Universal Content Management (UCM) for download.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the ESS job package and job name, separated by a semicolon. |
| Parameter list | Specify the parameters used to invoke the ESS job. The only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. If a parameter value contains a comma, enclose the parameter value within double quotes. |
| Job options | Specify processing parameters as key-value pairs, separated by commas. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#extractAndPurge) to define when to send a bell or email notification. |
| Callback URL | Provide the web service callback URL to receive the ESS job status. Use `#NULL` if no callback is required. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted ESS job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/extract-and-purge.md
description: >-
  The Extract and purge action extracts data from Oracle Fusion Cloud and
  removes the extracted records from the source system.
---

# Oracle Fusion Cloud - Extract and purge action

The **Extract and purge** action extracts data from Oracle Fusion Cloud and removes the extracted records from the source system. This action uploads load and import job output to the Universal Content Management (UCM) server and purges interface tables with callback and notification support.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Request IDs | Provide the request IDs of load job and import jobs. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#extractAndPurge) to define when to send a bell or email notification. |
| Callback URL | Provide the web service based callback URL of the web service that has been implemented to receive the ESS job status upon job completion. Pass `#NULL` if web service based callback isn't needed. |
| Job options | Specify processing parameters as key-value pairs separated by commas to control extract-and-purge variations. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the first submitted Enterprise Scheduling Service job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/fetch-extract-output.md
description: >-
  The Fetch extract output action retrieves the archived XML output produced by
  an extract process.
---

# Oracle Fusion Cloud - Fetch extract output action

The **Fetch extract output** action retrieves the archived XML output produced by an extract process.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Instance name | Enter the name of the archived flow instance. |
| Task name | Enter the name of the flow task. |
| Mode | Enter the name of the running mode, either `ARCHIVER` or `FLOW`. If mode is `ARCHIVER`, the output is returned based on flow instance name. If mode is `FLOW`, the output is returned based on flow instance name and flow task name. |
| Output fields | Define the schema for the expected output data structure using the schema designer. |

## Output

| Output field | Description |
| --- | --- |
| Result | The XML output. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/get-flow-task-instance-status.md
description: >-
  The Get flow task instance status action retrieves the current execution
  status of a specific task within a flow instance in Oracle Fusion Cloud's
  Human Capital Management (HCM) system.
---

# Oracle Fusion Cloud - Get flow task instance status action

The **Get flow task instance status** action retrieves the execution status of a specific task within a flow instance in Oracle Fusion Cloud's Human Capital Management (HCM) system.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Flow instance name | Enter the name of the flow instance that contains the task. |
| Flow task instance name | Specify the name of the specific task instance within the flow. |
| Legislative data group name | Enter the legislative data group name to scope the status check. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the current status of the flow task instance, such as running, completed, failed, or another execution state. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/get-record.md
description: The Get record action retrieves a specific record by its internal ID.
---

# Oracle Fusion Cloud - Get record action

The **Get record** action retrieves a specific record by its internal ID. For example, to fetch a product, provide the **Inventory item ID**. The required field appears automatically after the object is selected.

> **MIXED API PROTOCOLS**
> 
> This action includes several SOAP-based objects alongside the standard REST objects:
> 
> - Get ESS job status
> - Get document IDs for file prefix
> - Get document for document ID
> - Get ESS execution details
> - Get default object attribute hints
> - Get service last update time

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object type of the record you plan to retrieve. |
| Object ID | Provide the ID of the record to retrieve. |
| Expand | Select related child and grandchild objects to include. By default, only the record and its child objects return. For example, under **Receivable credit memo**, include **attachments** (grandchild) for each **credit memo line** (child). |

## Output

The output contains details about the retrieved record.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/import-bulk-data.md
description: >-
  The Import bulk data action uploads a file to the Oracle Universal Content
  Management (UCM) server based on the document details specified and submits an
  ESS job to load and import the uploaded files to an application table.
---

# Oracle Fusion Cloud - Import bulk data action

The **Import bulk data** action uploads a file to the Oracle Universal Content Management (UCM) server and submits an ESS job to load and import the uploaded file into an application table.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Document | Provide the complete document object containing the file and its metadata. |
| Content (Document) | Provide the base64 encoded string of the document. |
| File name (Document) | Enter the name of the file specified by the document. |
| Content type (Document) | Specify the content type of the document. |
| Document title (Document) | Enter the title of the document. |
| Document author (Document) | Specify the author of the document. |
| Document security group (Document) | Specify the security group that secures the document. |
| Document account (Document) | Specify the account to which the document belongs to. |
| Document name (Document) | Enter the name of the document. |
| Document ID (Document) | Specify the document identifier. |
| Job list | Configure the import jobs to process the uploaded document. |
| Job name (Job list) | Enter the ESS job package and job name, separated by a semicolon. |
| Job request ID (Job list) | Enter the request ID of the submitted ESS job. |
| Parameter list (Job list) | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` if the parameter isn't required. |
| Interface details | Specify the interface option ID for which data must be loaded. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#importBulkData) to define when to send a bell or email notification. |
| Callback URL | Provide the web service callback URL to receive the ESS job status. Use `#NULL` if no callback is required. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request identifier for the first ESS job in the job list, which is a Load Interface File for Import Job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/list-entities.md
description: >-
  The List entities action retrieves the list of service data objects associated
  with the ERP Integration Service.
---

# Oracle Fusion Cloud - List entities action

The **List entities** action retrieves the list of service data objects associated with the ERP Integration Service.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

This action doesn't require any input.

## Output

| Output field | Description |
| --- | --- |
| Entities | An array of entity objects containing information about available business entities in Oracle Fusion Cloud. |
| Name (Entities) | The name of the entity or business object. |
| Type name (Entities) | The technical type name or classification of the entity. |
| Can create (Entities) | Indicates whether the entity supports create operations. |
| Can update (Entities) | Indicates whether the entity supports update operations. |
| Can merge (Entities) | Indicates whether the entity supports merge operations. |
| Can delete (Entities) | Indicates whether the entity supports delete operations. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/load-and-import-data.md
description: >-
  The Load and import data action uploads a file to the Oracle Universal Content
  Management (UCM) server based on the document details specified and submits an
  ESS job(s) to load and import the uploaded files to an application table.
---

# Oracle Fusion Cloud - Load and import data action

The **Load and import data** action uploads a file to the Oracle Universal Content Management (UCM) server and submits one or more ESS jobs to load and import the uploaded file into an application table.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Document | Provide the complete document object containing the file and its metadata. |
| Content (Document) | Provide the content of the document. |
| File name (Document) | Enter the name of the file specified by the document. |
| Content type (Document) | Specify the content type of the document. |
| Document title (Document) | Enter the title of the document. |
| Document author (Document) | Specify the author of the document. |
| Document security group (Document) | Specify the security group that secures the document. |
| Document account (Document) | Specify the account to which the document belongs to. |
| Document name (Document) | Enter the name of the document. |
| Document ID (Document) | Specify the document identifier. |
| Job list | Configure the import jobs that process the uploaded document. |
| Job name (Job list) | Enter the ESS job package and job name, separated by a semicolon. |
| Job request ID (Job list) | Enter the request ID of the submitted ESS job. |
| Parameter list (Job list) | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. |
| Interface details | Specify the interface option ID for which data is loaded. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#loadAndImportData) to define when to send a bell or email notification. |
| Callback URL | Provide the web service callback URL to receive the ESS job status. Pass `#NULL` if web service based callback isn't needed. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the first ESS job in the job list (Load Interface File for Import). |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/search-documents-by-file-prefix.md
description: >-
  The Search documents by file prefix action searches and retrieves document
  information and content from Oracle Fusion Cloud based on a file prefix
  pattern.
---

# Oracle Fusion Cloud - Search documents by file prefix action

The **Search documents by file prefix** action retrieves document information and content from Oracle Fusion Cloud based on a file prefix pattern.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Prefix | Enter the file prefix pattern to search for documents. |
| Account | Specify the account identifier to scope the document search. |
| Comments | Add optional comments or additional search criteria for the document search operation. |

## Output

| Output field | Description |
| --- | --- |
| Result | An array of document objects containing document information and content. |
| File name (Result) | The name of the document file. |
| Content type (Result) | The content type of the document. |
| Document title (Result) | The title assigned to the document in Oracle Fusion Cloud. |
| Document author (Result) | The author or creator of the document. |
| Document security group (Result) | The security group associated with the document for access control. |
| Document account (Result) | The account identifier associated with the document. |
| Document name (Result) | The internal document name used by Oracle Fusion Cloud. |
| Document ID (Result) | The unique identifier for the document in Oracle Fusion Cloud. |
| File content (Result) | The content of the document file. |
| Zip contents (Result) | Contains extraction information when the document is a ZIP file. |
| Debug info (Zip contents) | Returns technical information about ZIP processing. |
| Content size (Debug info) | The size of the ZIP file content in bytes. |
| Content preview (Debug info) | A preview of the ZIP file content for debugging purposes. |
| Is zip (Debug info) | Indicates whether the content is a ZIP file. |
| Files (Zip contents) | An array of files extracted from the ZIP archive. |
| Name (Files) | The name of the individual file within the ZIP archive. |
| Size (Files) | The size of the individual file in bytes. |
| Path (Files) | The full path of the file within the ZIP archive structure. |
| Content (Files) | The content of the individual file. |
| Is binary (Files) | Indicates whether the file contains binary content. |
| Error (Files) | Any error message encountered during file extraction. |
| Content (Result) | Container for content reference information. |
| Include (Content) | Reference information for included content or attachments. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/search-records-batch.md
description: >-
  The Search records batch action allows searching by specifying attribute
  values directly.
---

# Oracle Fusion Cloud - Search records action

The **Search records** batch action finds records by specific attribute values.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Search operation | Select the operator for combined expressions. Options include **And** and **OR**. **And** returns records matching all specified attributes. **Or** returns records matching at least one specified attribute. |
| Limit | Specify the number of resources to return. The minimum is 1, and the maximum is 500. Defaults to 100. |
| Offset | Define the starting position of the resource collection. Default value is 0. |
| Expand | Select the child and grandchild objects to include in the output. |
| Order by | This parameter orders a resource collection based on the specified attributes. The parameter value is a comma-separated string of attribute names, each optionally followed by a colon and `asc` or `desc`. Specify `asc` for ascending and `desc` for descending. The default value is `asc`. e.g. field1:asc,field2:desc |
| Search by | Expand this field to specify how you plan to search for a record. |

## Output

Returns a list of records that match the search criteria, including record details, the total number of matches, quota and offset values, and an indicator showing whether more records are available in a separate job.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/search-records-using-advanced-query-batch.md
description: >-
  The Search records using advanced query batch action searches for records
  using flexible query options.
---

# Oracle Fusion Cloud - Search records using advanced query action (batch)

The **Search records using advanced query** batch action searches for records using flexible query options.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Query | Define the WHERE clause, similar to SQL. For example, `InvoiceAmount>=10 and InvoiceAmount<=30 and Supplier!='NY'`. Refer to the [Oracle documentation](https://docs.oracle.com/en/cloud/saas/financials/22d/farfa/Collections.html#Collections-261C5653__concept-108-55605D77) for more information. |
| Fields | Specify which fields to return in the output to reduce response size. If you provide both **Fields** and **Expand**, only **Fields** applies. |
| Finder | Use a predefined finder query associated with the object. For example: `PrimaryKey;InvoiceId=3`. Refer to the [Oracle documentation](https://docs.oracle.com/en/cloud/saas/financials/22d/farfa/Collections.html#Collections-261C5653__concept-108-55605D77) for more information. |
| Limit | Specify the maximum number of records to return. The minimum is 1, and the maximum is 500. Defaults to 100. |
| Offset | Specify the starting position for results. Defaults to 0. |
| Expand | Select the child and grandchild objects to include in the output. |
| Order by | Sort results by specified fields. Use comma-separated format: `field1:asc,field2:desc`. Specify `asc` for ascending or `desc` for descending order. Defaults to ascending. For example: `amount:asc,date:desc` |

## Output

The output contains a list of records matching your search criteria. The specific fields vary based on the selected object. The response also includes the following pagination and metadata fields:

| Output field | Description |
| --- | --- |
| Count | Number of records returned in this response. |
| Total results | Total number of matching records. |
| Has more | Whether additional results are available. |
| Limit | Maximum records per page used in the request. |
| Offset | Starting position used in the request. |
| Links | Navigation links for pagination. |
| Hyperlink reference (Links) | URL for the navigation link. |
| Relation (Links) | Type of link relationship. |
| Name (Links) | Display name for the link. |
| Kind (Links) | Link category or type. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/submit-and-get-flow-instance-id.md
description: >-
  The Submit and get flow instance ID action creates and submits a new flow
  instance in Oracle Fusion Cloud's Human Capital Management (HCM) system and
  returns the unique instance identifier.
---

# Oracle Fusion Cloud - Submit and get flow instance ID action

The **Submit and get flow instance ID** action creates and submits a new flow instance in Oracle Fusion Cloud's Human Capital Management (HCM) system and returns the unique instance identifier.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Cross flow interaction list | Enter a list of flow instance and task identifiers to create cross-flow interactions. |
| From flow instance name (Cross flow interaction list) | Specify the name of the source flow instance in the flow interactions. |
| From flow task name (Cross flow interaction list) | Enter the name of the source task in the flow interactions. |
| Impact calculation flag (Cross flow interaction list) | Specify whether the flow interaction impacts calculation. |
| To flow instance name (Cross flow interaction list) | Enter the name of the destination flow instance in the flow interactions. |
| To flow task name (Cross flow interaction list) | Specify the name of the destination task in the flow interactions. |
| Parameter values | Provide the parameters required for the flow execution. `Effective Date` is a required parameter. |
| Parameter values source list (Parameter values) | Input a list datapill containing the parameter values. |
| Parameter name (Parameter values) | Enter the parameter name. `Effective Date` is required for all flow submissions. |
| Parameter value (Parameter values) | Specify the value for the corresponding parameter. |
| Flow name | Enter the name of the flow to execute. |
| Flow instance name | Specify a unique name for this flow instance execution. |
| Legislative data group name | Enter the legislative data group name to scope the flow execution. |
| Schedule formula type name | Specify the name of the formula type for the scheduling formula, such as `Flow Schedule`. |
| Schedule formula name | Enter the name of the specific scheduling formula to use for flow execution timing. |
| Scheduled date | Select the date and time for flow execution. |
| Recurring flag | Indicate whether the flow instance is recurring or non-recurring. |
| End date | Specify the end date for recurring flow instances to stop the recurring execution. |

## Output

| Output field | Description |
| --- | --- |
| Result | The unique flow instance identifier generated by Oracle Fusion Cloud for the submitted flow. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/submit-ess-job-request.md
description: >-
  The Submit ESS job request action submits an Enterprise Scheduling Service
  (ESS) job request for the specified job definition.
---

# Oracle Fusion Cloud - Submit ESS job request action

The **Submit ESS job request** action submits an Enterprise Scheduling Service (ESS) job request for a specified job definition.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job package name | Enter the ESS job package name. |
| Job definition name | Enter the ESS job definition name. |
| Parameter list | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted Enterprise Scheduling Service job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/submit-job-with-output.md
description: >-
  The Submit job with output action submits an Enterprise Scheduling Service
  (ESS) job request for a specified job definition and sends a callback message
  to the specified callback URL when the job completes.
---

# Oracle Fusion Cloud - Submit job with output action

The **Submit job with output** action submits an Enterprise Scheduling Service (ESS) job request for a specified job definition. The action sends a callback message to the specified URL when the job completes.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job package name | Enter the ESS job package name. |
| Job definition name | Enter the ESS job definition name. |
| Callback URL | Enter the web service callback URL to receive the ESS job status. |
| Parameter list | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted ESS job. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/update-interface-data.md
description: >-
  The Update interface data action updates error data in interface tables
  pertaining to the specified import process and load request ID.
---

# Oracle Fusion Cloud - Update interface data action

The **Update interface data** action updates error data in interface tables for the specified import process and load request ID.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Process name | Enter ERP interface options import job details. Separate the job path and job name with a semicolon. |
| Load request ID | Specify the load request ID. |
| Document | Provide the corrected interface table data as a user-uploaded blobDomain. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the result of the interface data update. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/update-record.md
description: The Update record action updates an existing record.
---

# Oracle Fusion Cloud - Update record action

The **Update record** action updates an existing record. Select an object to load its input fields. The object's primary key is required to identify the record.

For example, to update a receivables invoice, select **Receivables invoice** and provide the **Customer transaction ID**. You can use the [Search records action](/en/connectors/oracle-fusion-cloud/actions/search-records-batch) to retrieve the ID, then map it into the update input.

To update a child object, provide the IDs of both the main object and the child object. For example, provide the **Line number ID** to update an invoice line.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the record you plan to update. |
| Object ID | Select the ID of the record you plan to update. |

Additional fields load dynamically depending on the object you select.

## Output

The output of this action contains details about the updated record.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/update-records-batch.md
description: The Update records batch action updates existing records in batches.
---

# Oracle Fusion Cloud - Update records action (batch)

The **Update records** batch action updates existing records in batches. Select the object to populate its input fields.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the records you plan to update. |
| Records | Expand this section to fill in information related to the records you plan to update. |
| Records source list | Input a list datapill. |

Additional input fields are available based on the object you select.

## Output

| Output field | Description |
| --- | --- |
| Items | A list of the updated records. |

Additional output fields are available based on the object you select.

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/upload-to-ucm.md
description: >-
  The Upload to UCM action uploads a document to the Universal Content
  Management (UCM) server based on provided document details.
---

# Oracle Fusion Cloud - Upload to UCM action

The **Upload to UCM** action uploads a document to the Universal Content Management (UCM) server based on provided document details.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Document | Provide the complete document object containing the file and its metadata. |
| Content (Document) | Provide the content of the document. |
| File name (Document) | Enter the name of the file specified by the document. |
| Content type (Document) | Specify the content type of the document. |
| Document title (Document) | Enter the title of the document. |
| Document author (Document) | Specify the author of the document. |
| Document security group (Document) | Specify the security group that secures the document. |
| Document account (Document) | Specify the account to which the document belongs to. |
| Document name (Document) | Enter the name of the document. |
| Document ID (Document) | Provide the document identifier. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the numeric document identifier of the uploaded file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/upsert-record.md
description: The Upsert record action creates or updates a record.
---

# Oracle Fusion Cloud - Upsert record action

The **Upsert record** action creates or updates a record. If the primary key, such as the Invoice ID, is present, the record is updated. If no primary key is provided, the action creates a new record.

The same logic applies to child objects:

- If the primary key is present, the record is updated.
- If no primary key is provided, the record is inserted into the existing or new parent object.

Common use cases include:

- Adding new invoice lines to an existing invoice
- Updating a specific invoice line
- Updating an invoice with new currency rates
- Inserting or updating products from a Google Sheet based on Inventory item ID

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type of the record you plan to upsert. |

Additional fields load dynamically based on the object you select.

## Output

The output of this action includes details about the upserted record.

---
