---
url: 'https://docs.workato.com/en/data-tables/connector/search-records-action.md'
description: >-
  The search records batch action retrieves a list of entries that match the
  search criteria you specify from a data table.
---

# Search records action (batch)

The **Search records** batch action retrieves a list of entries that match the search criteria you specify from a data table.

## Input

| Input fields | Description |
| --- | --- |
| Data table | Select the data table you plan to search. Click the link in this field's description to view the selected data table. |
| Filters | Add filters to the query. Filters are chained using `AND` logic. This field has some additional sub-fields: Column name: Select the column you plan to filter by., Operand: Specify an operator to define how to compare the returned column values against the **Value** you set. Refer to [Available operands](#available-operands) to see the valid operators for each column type., Value: Provide the value to compare against the returned column values. The value you enter must match the data type of the column and the operand you select. |
| Sort by | Select a property to sort the results by. |
| Sort direction | Select whether to order search results in **Ascending** or **Descending** order. |
| Limit | Enter the maximum number of entries you plan to retrieve each trigger event. The default value is `100` and the maximum is `1,000`. |
| Next page token | Optional. Provide the token from a previous response here to return the next page of results. |
| Choose the desired output format | Optional. Specify how to map the retrieved record data to the table fields. Refer to the [Output formats](/en/data-tables/data-table-connector#output-formats) section for more information. |

## Output

| Output fields | Description |
| --- | --- |
| Records | Contains information about the retrieved records, such as their `Record ID`, `List index`, `Updated at` timestamp, and data from any of the data table's custom columns. |
| Next page token | The token for the next page of results. |

## Recreate Lookup table behavior

The **Data tables** connector doesn't include the [Get all entries](/en/features/lookup-tables#get-all-entries-action-batch) or [Lookup entry](/en/features/lookup-tables#lookup-entry-action) actions from the **Lookup tables** connector.

You can recreate similar behavior using the **Search records** action, though the results and structure may differ:

- **Get all entries**: Leave the **Filters** section blank to return all entries. Use the **Next page token** field to paginate through results.
- **Lookup entry**: Set the **Operand** field to `Equals`, then use the first item in the output `Records` list as the matching result.

## Available operands

The following table lists the operands available for each data table column type.

| Column type | Available operands |
| --- | --- |
| ID | `equals`, `not equals`, `in` |
| String, File | `equals`, `not equals`, `in`, `is null`, `is not null`, `starts with` |
| Integer, Number | `equals`, `not equals`, `in`, `greater than`, `less than`, `greater than or equals`, `less than or equals`, `is null`, `is not null` |
| Date, Date-time | `equals`, `not equals`, `in`, `is after`, `is before`, `is on or after`, `is on or before`, `is null`, `is not null` |
| Boolean | `is true`, `is false`, `is null`, `is not null` |
| Relation | `equals`, `not equals`, `in`, `is null`, `is not null` |
| Set types (string set, number set, integer set, date set, date-time set, relation set) | `contains`, `is null`, `is not null` |

The **Value** field accepts a list of values when you select the `in` operand. Add each value as a separate item. The action returns records that match any value in the list.

---
