---
url: 'https://docs.workato.com/en/connectors/creatio/search-record-action.md'
description: The Search records action returns results that match all your search criteria.
---

# Creatio - Search records action

The **Search records** action returns results that match all your search criteria.

![Creatio Search records action](/assets/creatio-search-record-action.CfsIf565.png)_Creatio Search records action_

## Input

| Input fields | Description |
| --- | --- |
| Object | Specify the object you plan to search for. |
| Use custom query | Select `Yes` or `No` from the drop-down. If `Yes` is selected, the **Custom query** field is dynamically loaded. |
| Custom query | Write a custom query in this field as required. |
| Filter | The filter field allows you to set the filter criteria for search action. |
| Select fields | Select the fields from the drop-down you plan to see in the result set. |
| Order by - field | Select the field name from the drop-down to order the result set. |
| Order by - Sort order | Select the sorting order of the result set. |
| Page size | Provide the number of records to be returned on each page. |
| Offset | The offset field is used for pagination and starts pulling the records after the offset record value. |

## Output

The output fields are determined by the object you select in the input. Map the relevant datapill from the data tree for downstream steps.

---
