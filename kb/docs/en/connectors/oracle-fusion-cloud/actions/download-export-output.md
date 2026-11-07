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
