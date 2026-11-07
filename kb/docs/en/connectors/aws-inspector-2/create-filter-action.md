---
url: 'https://docs.workato.com/en/connectors/aws-inspector-2/create-filter-action.md'
description: The Create filter action defines custom filters for findings.
---

# AWS Inspector2 - Create filter action

The **Create filter** action defines custom filters for findings. Filters help you narrow down security findings based on specific criteria, making prioritizing and addressing issues easier.

## Input

| Input field | Description |
| --- | --- |
| Action | Select the action to perform on findings that match the filter. |
| Name | Enter a custom name to identify the filter. |
| Filter criteria | Define the search criteria for findings. You can filter by criteria such as `severity`, `resource tags`, and more. Refer to Amazon's [Field criteria object](https://docs.aws.amazon.com/inspector/v2/APIReference/API_FilterCriteria.html) guide for more information. |
| Description | Enter a description for the filter. |
| Reason | Enter a reason for creating the filter. |
| Tags | Enter key-value pairs for the tags to assign to the resource. For example: `Environment: Production` |

## Output

| Output field | Description |
| --- | --- |
| Amazon Resource Number (ARN) | The Amazon Resource Name (ARN) of the filter that was created. This unique identifier manages or references the filter in future operations. |

---

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

---
