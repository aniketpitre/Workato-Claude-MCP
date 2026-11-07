---
url: 'https://docs.workato.com/en/connectors/bamboo-hr/get-report-by-id-v2-action.md'
description: >-
  The Get report by ID (v2) action retrieves a report from BambooHR using the
  Custom Reports API.
---

# BambooHR – Get report by ID (v2) action

The **Get report by ID (v2)** action retrieves a report from BambooHR using BambooHR's Custom Reports API. You must specify the report ID.

Use this action instead of the deprecated [Get company employee report by ID](/en/connectors/bamboo-hr/get-company-report-by-id-action) action. It works with both legacy and custom report IDs.

## Input

| Input field | Description |
| --- | --- |
| Report ID | Enter the ID of the report to retrieve. You can use a legacy report ID or a custom report ID. Workato automatically translates migrated legacy IDs to their new ID. |
| Page | Enter the page number to retrieve. Defaults to `1`. |
| Page size | Enter the number of records to retrieve per page. Defaults to `500`. The maximum is `1000`. |
| Output fields | Provide a sample JSON of the expected output fields from the report, or add the fields manually. Workato uses this schema to generate the output datatree for subsequent recipe steps. |

## Output

The output includes a datatree for the report records, shaped by the schema you provide in **Output fields**, along with the report's fields, aggregations, and pagination details.

| Output field | Description |
| --- | --- |
| Fields | The fields configured in the report. |
| Aggregations | The aggregations configured in the report. |
| Pagination | Pagination details for the page of records returned. |

---
