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
