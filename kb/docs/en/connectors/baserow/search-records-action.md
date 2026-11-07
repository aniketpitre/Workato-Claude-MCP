---
url: 'https://docs.workato.com/en/connectors/baserow/search-records-action.md'
description: >-
  Look up rows in a table with pagination, keyword search, sorting, or
  field-level filters.
---

# Baserow - Search records action

The **Search records** action retrieves a list of rows from a table in Baserow, with support for pagination, sorting, and filtering.

## Input

The following are a representative set of input fields. Refer to the Baserow [Database API](https://baserow.io/docs/apis/rest-api) documentation for a list of input fields.

| Input field | Description |
| --- | --- |
| Object type | Select the object type, such as **Row**. |
| Table ID | Select the table to search. |
| Page | Optional. Enter the page of rows to return. The default is `1`. |
| Size | Optional. Enter the number of rows to return per page. The default is `100`. The maximum is `200`. |
| Search | Optional. Enter a query. Only rows that match this query are returned. |
| Order by | Optional. Enter comma-separated field names to sort by, for example, `Name,-Status`. Prepend `-` for descending order. The default is `id`. |
| Filters | Optional. Enter a JSON filter tree, for example, `{"filter_type":"AND","filters":[{"field":"Name","type":"equal","value":"test"}]}`. **Filter type** and **Field filters** are ignored when this filter is set. |
| Field filters | Optional. Add field, operator, and value combinations to filter by, for example, field `Name`, operator `equal`, value `test`. This filter is ignored if **Filters** is set. |
| Filter type | Optional. Select **AND** to require rows to match all filters, or **OR** to require at least one. This filter only applies with two or more filters. The default is **AND**. |
| Include | Optional. Enter comma-separated field names to include, for example, `Name,Status`. All fields are included by default. |

## Output

| Output field | Description |
| --- | --- |
| Count | The total number of rows that match the search. |
| Next | The URL of the next page of results, if any. |
| Previous | The URL of the previous page of results, if any. |
| Results | The matching rows, one entry per row. Row fields dynamically generate based on the table you select. |

---
