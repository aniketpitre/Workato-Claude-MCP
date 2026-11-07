---
url: >-
  https://docs.workato.com/en/connectors/cornerstone-hr/search-records-using-odata-query-action.md
description: >-
  The Search records using OData query action returns Cornerstone records that
  match an OData query you provide.
---

# Cornerstone HR - Search records using OData query action

The **Search records using OData query** action returns Cornerstone HR records that match an OData query you provide.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object or reporting view you plan to query. For example, **User**. You can also provide the internal name of a custom object. |
| Query | Enter an OData filter condition to filter results. For example, `user_create_dt le cast('2016-08-16', Edm.DateTimeOffset) and user_id eq 78`. |
| Select fields | Select the fields to include in the response. All fields are returned if left blank. |
| Page size | Enter the maximum number of records to return. The maximum is `1000`. Default is `100`. |
| Offset | Enter the number of records to skip before returning results. |

## Output

Output fields dynamically generate based on the object you select. Refer to the [Cornerstone API documentation](https://apiexplorer.csod.com/apiconnectorweb/apiexplorer#/data-exporter-api) for a complete list of output fields.
