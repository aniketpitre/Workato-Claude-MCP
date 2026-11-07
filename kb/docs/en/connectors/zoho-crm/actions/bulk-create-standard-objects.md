---
url: >-
  https://docs.workato.com/en/connectors/zoho-crm/actions/bulk-create-standard-objects.md
description: >-
  The Bulk create standard objects action creates standard objects in bulk in
  Zoho CRM.
---

# Zoho CRM - Bulk create standard objects action

The **Bulk create standard objects** action creates standard objects in bulk in Zoho CRM.

## Input

| Input field | Description |
| --- | --- |
| Module name | Select the standard module for the objects. |
| Ignore empty | Specify whether to ignore empty rows. |
| File content | Provide the file content. The file must be in zip format. The maximum file size is 25 MB. |
| Csv header | Enter the CSV header as comma separated values. |
| Field mapping | Provide the field mapping configuration. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the bulk operation. |
| Resource | The resource details for the bulk operation. |
| Status (Resource) | The status of the resource. |
| Code (Resource) | The code for the resource. |
| Type (Resource) | The type of resource. |
| File (Resource) | The file details for the resource. |
| Status (File) | The status of the file. |
| Name (File) | The name of the file. |
| Added count (File) | The number of records added from the file. |
| Skipped count (File) | The number of records skipped from the file. |
| Updated count (File) | The number of records updated from the file. |
| Total count (File) | The total number of records in the file. |
| Field mappings (Resource) | The field mapping configuration for the resource. |
| Api name (Field mappings) | The API name of the mapped field. |
| Index (Field mappings) | The index position of the mapped field. |
| Format (Field mappings) | The format of the mapped field. |
| Find by (Field mappings) | The field to use for finding records. |
| Module (Field mappings) | The module for the mapped field. |
| Default value (Field mappings) | The default value for the mapped field. |
| ID | The unique identifier of the bulk operation. |
| Result | The result details of the bulk operation. |
| Download URL (Result) | The URL to download the result file. |
| Created by | The user who created the bulk operation. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the user who created the operation. |
| Operation | The type of operation performed. |
| Created time | The timestamp when the operation was created. |
