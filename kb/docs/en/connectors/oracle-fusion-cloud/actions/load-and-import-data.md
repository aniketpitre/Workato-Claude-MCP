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
