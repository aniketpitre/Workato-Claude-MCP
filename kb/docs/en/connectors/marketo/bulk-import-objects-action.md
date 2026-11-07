---
url: 'https://docs.workato.com/en/connectors/marketo/bulk-import-objects-action.md'
description: >-
  The Bulk import objects from file action in the Marketo connector lets you
  import program members, leads, or custom objects in bulk.
---

# Marketo - Bulk import objects from file action (bulk)

This action imports objects from a file in bulk into your Marketo instance.

Existing objects are updated if found; otherwise, new objects are created from the file data. Rows with failures and warnings are returned in the same format as the input, with an additional column for error or warning messages.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to import in bulk. Options include **Program members**, **Leads**, and **Custom objects**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to import in bulk:

- [Program members](#program-members)
- [Leads](#leads)
- [Custom objects](#custom-objects)

### Program members input fields

| Field | Description |
| --- | --- |
| File input | Expand to configure the file input for this action. |
| File input (file input) | Add the file contents containing the program members data to import into Marketo. |
| Column separator (file input) | Specify the delimiter used in your file. Options include **comma**, **space**, **tab**, **colon**, **semicolon**, and **pipe**. |
| Contains header line? (file input) | Select **Yes** if your file has a header line, **No** otherwise. The first line is skipped from import if a header exists. |
| Column names (file input) | Provide the column names in the same order as they appear in the CSV file. |
| Program ID / Select program | Enter the ID of the program to import members into, or select the program from the drop-down menu. |
| Program member status | Specify the status for members being added to the program. |
| File to Marketo program members field mapping | Define how columns in the input file map to Marketo fields. |

### Leads input fields

| Field | Description |
| --- | --- |
| File input | Expand to configure the file input for this action. |
| File input (file input) | Add the file contents containing the leads data to import into Marketo. |
| Column separator (file input) | Specify the delimiter used in your file. Options include **comma**, **space**, **tab**, **colon**, **semicolon**, and **pipe**. |
| Contains header line? (file input) | Select **Yes** if your file has a header line, **No** otherwise. The first line is skipped from import if a header exists. |
| Column names (file input) | Provide the column names in the same order as they appear in the CSV file. |
| Lookup field | Select or enter the unique field to deduplicate leads. If a lead with this field exists, it is updated; otherwise, a new lead is created. Select **ID** to only update existing leads. If entering the lookup field, provide the API name of the field. You can locate the API name in Marketo by going to **Admin > Database Management > Field Management** and selecting the field. |
| Partition name | If specified, all imported leads become members of this partition. |
| File to Marketo leads field mapping | Define how columns in the input file map to Marketo fields. |
| List / List name | If specified, all imported leads become members of this static list. If entering the list name, the name should be exact. Not case-sensitive. |

### Custom objects input fields

| Field | Description |
| --- | --- |
| File input | Expand to configure the file input for this action. |
| File input (file input) | Add the file contents containing the custom objects data to import into Marketo. |
| Column separator (file input) | Specify the delimiter used in your file. Options include **comma**, **space**, **tab**, **colon**, **semicolon**, and **pipe**. |
| Contains header line? (file input) | Select **Yes** if your file has a header line. Otherwise, select **No**. The first line is skipped from import if a header exists. |
| Column names (file input) | Provide the column names in the same order as they appear in the CSV file. |
| Custom object name / Object name | Select or enter the name of the custom object. If entering the object name, add the suffix `_c`. |
| File to Marketo custom objects field mapping | Select how your input file columns should map to your Marketo fields. |

## Output

| Field | Description |
| --- | --- |
| Result | Array of individual records in the operation. |
| Batch ID (result) | Unique integer ID of the import batch. |
| Import ID (result) | Unique identifier for the import operation. |
| Status (result) | Current status of the batch. |
| Message (result) | Status message for the batch. |
| Success | Indicates if the action was successful. |
| Number of rows failed | Total number of rows that failed. |
| Number of rows with warning | Total number of rows with warnings. |
| CSV content of failed rows | CSV data for rows that failed. |
| CSV content of warning rows | CSV data for rows with warnings. |

---

---
url: >-
  https://docs.workato.com/en/connectors/marketo/change-lead-program-status-action.md
description: >-
  The Change lead program status action in the Marketo connector lets you change
  the program status of a batch of leads in your instance.
---

# Marketo - Change lead program status action (batch)

This action changes the program status of leads in Marketo.

## Input

| Field | Description |
| --- | --- |
| Program ID | Enter the unique identifier of the program where the status is changed. |
| Status | Specify the new status to assign to the leads. |
| Leads | Expand this field to configure the leads for the program status change. |
| Leads source list (leads) | Input a list datapill from which the leads are derived. Learn more about [list input](/en/features/list-management#list-batch-action). |
| Lead ID (leads) | Provide the unique identifier of a lead record. |

## Output

| Field | Description |
| --- | --- |
| Result | An array of results for individual records in the operation. |
| ID (result) | The ID of the lead. |
| Status (result) | The new status of the lead. |

---
