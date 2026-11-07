---
url: 'https://docs.workato.com/en/connectors/marketo/bulk-export-objects-action.md'
description: >-
  The Bulk export objects to file action in the Marketo connector lets you
  export activities, program members, leads, or custom objects to a CSV file.
---

# Marketo - Bulk export objects to file action (bulk)

This action exports objects in bulk to a file. Configure the **Filter** input field to retrieve objects that match a filter condition you specify, then describe the file format using the **CSV format** input field. You can access exported objects file contents in the output of this action.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object you plan to export in bulk. Options include **Activities**, **Program members**, **Leads**, and **Custom objects**. |

Refer to the relevant sections to learn how to configure the input fields for the object you plan to export in bulk:

- [Activities](#activities)
- [Program members](#program-members)
- [Leads](#leads)
- [Custom objects](#custom-objects)

### Activities input fields

| Field | Description |
| --- | --- |
| Filter | Expand to configure the filter for this action. |
| Created at (filter) | Fill in both the **Start at** and **End at** fields. The date range must be 31 days or fewer. |
| Start at (created at) | Specify the start date to retrieve records created on or after this date. |
| End at (created at) | Specify the end date to retrieve records created on or before this date. |
| Activity types (filter) | Select the activity types you plan to filter. |
| CSV format | Expand to specify the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the activity fields to export into the file. If left blank, all fields are included in the export. |
| Column separator (CSV format) | Choose the delimiter for the exported file. Options include **Comma**, **Tab**, and **Space**. |

### Program members input fields

| Field | Description |
| --- | --- |
| Filter | Expand to configure the filter for this action. |
| Program ID / Select program (filter) | Enter the ID or select the name of the program from which you plan to bulk export members. |
| CSV format | Expand to specify the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the program member fields to export into the file. If left blank, all fields are included in the export. |
| Column separator (CSV format) | Choose the delimiter for the exported file. Options include **Comma**, **Tab**, and **Space**. |

### Leads input fields

| Field | Description |
| --- | --- |
| Filter | Expand to configure the filter for this action. Set either the **Created at** or **Updated at** filter, not both. |
| Created at (filter) | Select this filter to retrieve records based on their creation date. |
| Start at (created at) | Specify the start date for the **Created at** filter. Only records created on or after this date are retrieved. |
| End at (created at) | Specify the end date for the **Created at** filter. Only records created on or before this date are retrieved. |
| Updated at (filter) | Select this filter to retrieve records based on their last update date. |
| Start at (updated at) | Specify the start date for the **Updated at** filter. Only records updated on or after this date are retrieved. |
| End at (updated at) | Specify the end date for the **Updated at** filter. Only records updated on or before this date are retrieved. |
| Static list name / Static list ID | Enter either the static list name or ID to retrieve records from the static list. Name must be exact. Not case-sensitive. |
| Smart list name / Smart list ID | Enter either the smart list name or ID to retrieve records from the smart list. Name must be exact. Not case-sensitive. |
| CSV format | Describe the formatting of the exported file. Column names default to Marketo API names. |
| Fields | Select the lead fields to export into the file. If left blank, all fields are included in the export. |
| Column separator | Select the delimiter for the exported file. Options include **Comma**, **Tab**, and **Space**. |

### Custom objects input fields

| Field | Description |
| --- | --- |
| Custom object name / Object name | Select a custom object name from the list, or enter an object name with the suffix `_c`. |
| Filter | Expand to configure the filter for this action. |
| Updated at (filter) | Select this option to filter records based on their last update date. Fill in both **Start at** and **End at** input fields. |
| Start a (updated at) | Specify the start date for filtering records updated on or after this date. |
| End at (updated at) | Specify the end date for filtering records updated on or before this date. |
| Static list name / Static list ID (filter) | Enter either the static list name or ID to retrieve records from the static list. The name must be exact and is not case-sensitive. |
| Smart list name / Smart list ID (filter) | Enter either the smart list name or ID to retrieve records from the smart list. The name must be exact and is not case-sensitive. |
| CSV format (filter) | Specify the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the custom object fields to export into the file. If left blank, all fields are included in the export. |
| Column separator (CSV format) | Select the delimiter for the exported file. Options include **Comma**, **Tab**, and **Space**. |

## Output

| Field | Description |
| --- | --- |
| Job ID | The unique identifier of the exported job. |
| CSV result | Result of the operation in CSV format. |

---
