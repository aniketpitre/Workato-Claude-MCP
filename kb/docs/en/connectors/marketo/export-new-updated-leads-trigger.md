---
url: >-
  https://docs.workato.com/en/connectors/marketo/export-new-updated-leads-trigger.md
description: >-
  The Export new/updated leads trigger (bulk) in the Marketo connector runs on a
  schedule and returns new or updated leads as a CSV stream.
---

# Marketo - Export new/updated leads in Marketo trigger (bulk)

This trigger runs on a schedule you set and returns new or updated leads from Marketo.

Search results are returned as a complete CSV stream. You can write the CSV stream to a file using a file connector, such as [Box](/en/connectors/box) or [SFTP](/en/connectors/sftp), or parse it for use as a data list in Workato using the **Parse CSV** action in the [CSV by Workato utility connector](/en/features/handling-csv-files#csv-by-workato).

Processing times can vary and be delayed due to the time required for the query to be completed in Marketo. Because of this, Workato doesn't support test jobs for recipes with this trigger.

You can also use this trigger in conjunction with the [Get object schema](/en/connectors/marketo/get-objects-action) action to fetch schema information of a Marketo object and replicate it to your data warehouse. Learn more about [bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

## Input

| Field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, you can't change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| CSV format | Describe the formatting of the exported file. Column names default to Marketo API names. |
| Fields (CSV format) | Select the lead fields to export into the file. Workato permits a maximum combined field length of 7300 characters. |
| Column separator (CSV format) | Select the delimiter of the exported file. Available options include **Comma**, **Tab**, and **Semi-colon**. |

## Output

| Field | Description |
| --- | --- |
| Job ID | The unique identifier of the query job in Marketo. |
| CSV content | The datapill that contains the output of the trigger. |
| Object name | Name of the object being retrieved. |
| Created or updated from | The datetime the record was created or updated. |
| Object schema | The schema of the object being retrieved. |
| Field name (object schema) | The name of the field in the object schema. |
| Field label (object schema) | The label of the field in the object schema. |
| Original type (object schema) | The original data type of the field. |
| Mapped type (object schema) | The data type that the field is mapped to in the target system, if different. |
| Length (object schema) | The length or size of the field, if applicable. |
| Precision (object schema) | The number of digits to the right of the decimal point for numeric fields. |
| Scale (object schema) | The number of digits to the left of the decimal point for numeric fields. |
| Read only (object schema) | Indicates whether the field is read-only and can't be edited. |
