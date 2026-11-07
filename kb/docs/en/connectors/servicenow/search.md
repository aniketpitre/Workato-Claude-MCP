---
url: 'https://docs.workato.com/en/connectors/servicenow/search.md'
description: >-
  The Search records action in the ServiceNow connector returns a list of
  records from any table that match the search criteria you provide.
---

# ServiceNow - Search records action

## Search records

This action lets you search for records from any table matching a search criteria. Records that match all your search criteria will be returned as a list of records.

![Search records action](/assets/search-records-action.BIiNaC96.png)_Search records action_

### Input

| Input field | Description |
| --- | --- |
| [Table](#table) | Select a table to search records from. |
| [Search by column values](#search-by-column-values) | Provide data to match records. Only records that match all the search criteria will be returned in the output. |

### Output

The output of this action is a list of records that match your search criteria. The output datatree contains the full set of columns from the selected table. All default and custom columns are supported. The output fields will be displayed only after a table is provided, either by selecting a table from the pick list or by providing the full table name.

![Output fields](/assets/extended-output-search.MkhRfg1s.png)_Output fields_

## Input field definitions

### Table

Select the table to search records from. This can be done either by selecting a table from the pick list, or toggling the input field to text mode and typing the full table name.

Make sure that the connected user has [sufficient access control](/en/connectors/servicenow#roles-and-permissions-required-to-connect) to the selected table.

### Search by column values

Search criteria to match records against in the selected table. This action will only return records that match all your search criteria. Maximum size of batch of records returned is **100**.

You can search using all standard and custom columns in the selected table.

---
