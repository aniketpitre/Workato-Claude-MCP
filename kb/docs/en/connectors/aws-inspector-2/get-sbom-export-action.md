---
url: >-
  https://docs.workato.com/en/connectors/aws-inspector-2/get-sbom-export-action.md
description: >-
  The Get SBOM Export action retrieves the status and details of a Software Bill
  of Materials (SBOM) export operation.
---

# AWS Inspector2 - Get SBOM export action

The **Get SBOM export** action retrieves the status and details of a Software Bill of Materials (SBOM) export operation. An SBOM provides a detailed inventory of software components and resource dependencies, helping with vulnerability management and compliance.

## Input

| Input field | Description |
| --- | --- |
| Report ID | Enter the unique ID of the SBOM report to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| Report ID | Unique ID of the generated SBOM report. |
| Filter criteria | The resource conditions used to generate the SBOM. |
| Format | Format of the SBOM file generated. |
| S3 Destination | Details of the S3 location where the SBOM is stored. |
| Status | Current status of the export process. |
| Error code | Code representing the reason for export failure (if any). |
| Error message | Descriptive message explaining the error (if any). |
