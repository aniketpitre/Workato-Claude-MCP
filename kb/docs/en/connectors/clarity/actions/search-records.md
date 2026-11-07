---
url: 'https://docs.workato.com/en/connectors/clarity/actions/search-records.md'
description: >-
  The Search records action in the Clarity connector lets you search records of
  a selected object type using filter criteria and sorting.
---

# Clarity - Search records action

The **Search records** action searches for records in your Clarity instance based on specified criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the type of record to search. |
| Fields to retrieve | Select specific fields to return in the results. ID and timestamp fields are included by default. |
| Limit | Specify the maximum number of records to return. |
| Offset | Enter the starting position for record retrieval to enable pagination. |
| Sort | Define the sort order using field names. For example, `name`, `lastUpdatedDate desc`. Default is ascending. |
| Filter criteria | Enter filter expressions using Clarity query syntax. Each expression must be in parentheses. Date format is `"YYYY-MM-DD"`. Examples: `(transactionDate >= "2024-01-01")` or `(status = "ACTIVE")`. |

Additional fields may load based on the object you select.

## Output

| Output field | Description |
| --- | --- |
| Total count | The total number of records matching the search criteria. |
| Page size | The maximum number of records per page. |
| Records returned | The actual number of records returned in this response. |
| Next page URL | URL to retrieve the next page of results. |
| Previous page URL | URL to retrieve the previous page of results. |
| Self URL | URL of the current result set. |
| Results | Array containing the matching records. |

Additional fields in the Results array depend on the object type selected and the fields specified in the input.

---
