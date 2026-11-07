---
url: 'https://docs.workato.com/en/connectors/odata/search-records-action.md'
description: The Search records action enables you to search records in OData.
---

# OData - Search records action

The **Search records** action enables you to search records in OData. The list of objects is dynamically generated based on the API endpoints found in your OData document.

## Input

| Input fields | Description |
| --- | --- |
| Object | Select the object to search records for. |
| Limit | Enter a quota for the number of records to return. |
| Offset | Enter a number of records to skip from the first record. |
| Inline count | Enter or select the inline count value to determine if the total count of records is returned. Can be all pages, none, or a custom value. Applies to OData v2 and v3 only. |
| Count | Enter or select the count value to determine if the total count of records is returned. Can be all pages, none, or a custom value. Applies to OData v4 only. |

## Output

Output fields load dynamically based on the object you select.

---
