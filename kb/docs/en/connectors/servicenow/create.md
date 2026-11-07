---
url: 'https://docs.workato.com/en/connectors/servicenow/create.md'
description: >-
  The Create record action in the ServiceNow connector lets you create a single
  record in any table in your ServiceNow instance.
---

# ServiceNow - Create record actions

## Create record

This action creates a single record into any table in your ServiceNow instance.

![Create record action](/assets/create-record-action.B2APz5m-.png)_Create record action_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to create a record in. |
| [New record values](#new-record-values) | Provide data for each column of the record to be created. |

### Output

The output datatree of this action contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

![Output fields](/assets/extended-output-create.OT0jPopo.png)_Output fields_

## Create record using a template

This action creates a single record into any table in your ServiceNow instance by applying a template to the newly created record.

After a template is chosen, you can map additional datapills to the new record. The template values will be applied on top of your mapping. You can choose to retain or override the template values in this action.

![Create record using a template action](/assets/create-record-using-template-action.ofzlbud8.png)_Create record using a template action_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to create a record in. |
| [Template](#template) | Select a template associated with the selected table. |
| [Override template](#override-template) | Choose whether you want to override the default template values with the data provided in **New record values**. |
| [New record values](#new-record-values) | Provide data for each column of the record to be created. |

### Output

The output datatree of this action contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

Additionally, the sys ID of the template applied to this record is also included in the output.

![Output fields](/assets/extended-output-create.OT0jPopo.png)_Output fields_

## Input field definitions

### Table

Select the table to create a record in. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

Make sure that the connected user has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected table.

### Template

Select the template to be applied to the newly created record. This can be done either by selecting a template from the pick list, or toggling the input field to text mode and providing the template sys ID. This template must be associated with the selected table.

Make sure that the connected user has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected template.

### Override template

You can choose to override the pre-defined template values that will be automatically applied to the newly created record. If **Yes** is selected, any data provided for columns will be applied instead of template default values. This field defaults to **No**.

### New record values

Provide data for every column that needs to be filled for the new record in the selected table. This can be done by mapping datapills from previous triggers or actions into the respective columns.

---
