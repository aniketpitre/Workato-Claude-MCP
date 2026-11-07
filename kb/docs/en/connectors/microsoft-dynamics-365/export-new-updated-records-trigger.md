---
url: >-
  https://docs.workato.com/en/connectors/microsoft-dynamics-365/export-new-updated-records-trigger.md
description: >-
  The deprecated Export new or updated records bulk trigger in the Microsoft
  Dynamics 365 connector retrieves records in batches and streams them as CSV.
---

# Microsoft Dynamics 365 - Export new or new/updated records trigger (bulk)

This trigger activates when a record in Microsoft Dynamics 365 is created or updated. This trigger retrieves records in batches and streams them as a CSV.

> **DEPRECATION NOTICE**
> 
> Workato has deprecated bulk triggers across platform connectors. You can't add new bulk triggers to recipes. Existing recipes with bulk triggers continue to run unless you delete the trigger from the recipe.
> 
> For batch processing use cases, we recommend that you use batch triggers or other [batch processing features](/en/features/batch-processing) instead.

You can use this trigger in conjunction with the [Get object schema](/en/connectors/dynamics-crm/actions/get-object-schema) action to retrieve the name and schema of a specific object and copy it to a database or data warehouse.

[Learn more about bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

## Input

| Input field | Description |
| --- | --- |
| Object | Select any standard or custom Microsoft Dynamics 365 object to monitor. For example, `Lead`. |
| CSV columns | Select the object fields you plan to use as columns in the CSV file content. If this field is left blank, Workato returns all fields as columns. |
| Filter condition | Condition to filter the records. Use OData $filter syntax. For example, `contains(name, 'sample')` and `revenue gt 1000000`. [Learn more about filters](https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/query-data-web-api#filter-results). |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour after the recipe starts. After the recipe runs or is tested, this value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| When exporting records to form the CSV, fetch them in batches of | _Optional_. This trigger fetches the records in a set batch before streaming it. Use this to control the size of the batch of records obtained from Microsoft Dynamics 365. The maximum value is 100. Defaults to 100 records. In most cases, Workato recommends using the default value. |

## Output

| Field | Description |
| --- | --- |
| File content | This datapill contains the output of the trigger. Take note to utilize it primarily alongside streaming compatible actions like S3 upload file streaming action. |
| Object name | Name of the object being retrieved. The object name is issue for this trigger. |
| Object schema | The schema of the object being retrieved, based on the fields the user has selected. Each field has with it the associated name, label, original datatype, and mapped datatype. This allows for easy processing. |
| Created or updated from | The time and date the record was created or updated. |
