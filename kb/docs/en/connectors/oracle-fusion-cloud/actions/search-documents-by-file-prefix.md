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
