---
url: >-
  https://docs.workato.com/en/connectors/netsuite/export-new-updated-record-bulk-trigger.md
description: >-
  The bulk export triggers in the NetSuite SOAP connector run when standard or
  custom records are created or updated, streaming them as a CSV in batches.
---

# NetSuite SOAP - Export new and updated standard or custom records triggers (bulk)

These triggers run when a record in a custom or standard NetSuite object is created or updated. These triggers retrieve the records in batches and stream them as a CSV.

Workato has the following triggers:

- Export new standard records (bulk)
- Export new custom records (bulk)
- Export new/updated standard records (bulk)
- Export new/updated custom records (bulk)

### Input

| Input field | Description |
| --- | --- |
| Standard or custom object | Select a NetSuite object to fetch. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_. Use this field to control the size of the batch. The minimum value is 50 and the maximum value is 100. Defaults to 100 records. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

| Field | Description |
| --- | --- |
| File content | This datapill contains the output of the trigger. |
| Object name | The name of the retrieved object. |
| Object schema | The schema of the retrieved object, based on the user-selected fields. Each field contains an associated name, label, original datatype, mapped datatype, length, precision, scale, and custom field. This allows for easy processing. |
| Created or updated from | The time and date the record was created or updated. |
