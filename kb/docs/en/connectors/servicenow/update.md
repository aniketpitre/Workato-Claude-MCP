---
url: 'https://docs.workato.com/en/connectors/servicenow/update.md'
description: >-
  The Update record action in the ServiceNow connector lets you update a single
  record by its Sys ID in any table in your ServiceNow instance.
---

# ServiceNow - Update record actions

## Update record

This action updates a single record into any table in your ServiceNow instance.

![Update record action](/assets/update-record-action.CQHLMD3l.png)_Update record action_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to update a record in. |
| [Sys ID](#sys-id) | Sys ID of the record to be updated. |
| [Update record values](#columns-to-be-updated) | Provide data for each column of the record to be updated. |

### Output

The output datatree of this action contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

![Output fields](/assets/extended-output-update.CAQJ6pP1.png)_Output fields_

## Update record using a template

This action updates a single record into any table in your ServiceNow instance by applying a template to the record.

After a template is chosen, you can map additional datapills to the record. The template values will be applied on top of your mapping. You can choose to retain or override the template values in this action.

![Update record using a template action](/assets/update-record-using-template-action.DoK21IyW.png)_Update record using a template action_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to update a record in. |
| [Template](#template) | Select a template associated with the selected table. |
| [Override template](#override-template) | Choose whether you want to override the default template values with the data provided in **Update record values**. |
| [Sys ID](#sys-id) | Sys ID of the record to be updated. |
| [Update record values](#update-record-values) | Provide data for each column of the record to be updated. |

### Output

The output datatree of this action contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

Additionally, the sys ID of the template applied to this record is also included in the output.

## Input field definitions

### Table

Select the table to update a record in. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

Make sure that the connected user has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected table.

### Template

Select the template to be applied to the newly updated record. This can be done either by selecting a template from the pick list, or toggling the input field to text mode and providing the template sys ID. This template must be associated with the selected table.

Make sure that the connected user has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected template.

### Override template

You can choose to override the pre-defined template values that will be automatically applied to the record. If **Yes** is selected, any data provided for columns will be applied instead of template default values. This field defaults to **No**.

### Sys ID

Sys ID of the record to be updated. The record associated with this sys ID must belong to the selected table.

### Update record values

Provide data for every column that needs to be filled for the record update in the selected table. This can be done by mapping datapills from previous triggers or actions into the respective columns.

---
