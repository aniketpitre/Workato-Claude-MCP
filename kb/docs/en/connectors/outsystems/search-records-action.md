---
url: 'https://docs.workato.com/en/connectors/outsystems/search-records-action.md'
description: >-
  The Search records action in the OutSystems connector searches a module for
  records that match the values you configure and returns the matching results.
---

# OutSystems - Search records action

The Search records action searches for records based on the values you configure, and returns matching results.

![Search records action](/assets/search-records-action.Zh4J3z5F.png)_Search records action_

## Input

| Input field | Description |
| --- | --- |
| Module | Select the module containing the records for which you plan to search. |
| Entity ID | Select the entity ID of the module. |
| Page number | Returns results based on the page number you specify. This value defaults to `1`. This field is optional. |
| Results per page | The number of records to return in each page. This value defaults to `100`. The maximum value allowed is `50000`. |

## Output

| Output field | Description |
| --- | --- |
| Current page | The page number for your results. |
| Results per page | The maximum results listed on each page. For example: `100`. |
| Total rows | The total rows on each page. |
| Has next page | Indicates if the results have a next page with more records. This value is `true` or `false`. |
| Records | This entry contains information specific to the record attributes and other configurations, such as `ID` and `UPLOADDATETIME`, you selected for the OutSystems object. |

---
