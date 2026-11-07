---
url: 'https://docs.workato.com/en/connectors/servicenow/bulk-triggers.md'
description: >-
  ServiceNow bulk triggers export new or new/updated records from a table as
  streamed CSV content for ELT and ETL processes in Workato.
---

# ServiceNow - Bulk triggers

## Export new or new/updated records in ServiceNow trigger (bulk)

This trigger activates when a record in the ServiceNow table you select is created or updated.

[Learn more about bulk triggers and ELT/ETL processes](/en/features/etl-elt-guide#bulk-vs-batch).

### Input

| Field | Description |
| --- | --- |
| Table | Choose **Select table** from the drop down to select a table from the picklist. Alternatively, select **Enter table name** to enter the table's name manually. You must use the exact internal name of the table. For example: **cmdb\_categories**. |
| When first started, this recipe should pick up events from | When you start recipe for the first time, it picks up trigger events from this specified date and time. Defaults to one hour from time of start of recipe. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Query | Enter in the ServiceNow query to filter the records you plan to retrieve. For example: **active=true^stateIN1,3**. |
| When exporting records to form the CSV, fetch them in batches of | This trigger fetches the records in a set batch before streaming it. Use this to control the size of the batch of records obtained from ServiceNow. Leave to default value in most cases. |

### Output

| Field | Description |
| --- | --- |
| CSV content | Datapill that contains the output of the trigger. Take note to utilize it primarily alongside streaming compatible actions like S3 upload file streaming action. |
| Object name | Name of the object being retrieved. The object name is issue for this trigger. |
| Object schema | The schema of the object being retrieved, based on the fields the user has selected. Each field has with it the associated name, label, original datatype and mapped datatype. This allows for easy processing with database uploads and any additional transformations that may be needed. |

## Export records (bulk)

This trigger checks for New or New/Updated records on a user specific schedule. Only records for which the linked ServiceNow account has sufficient permissions will be retrieved.

---
