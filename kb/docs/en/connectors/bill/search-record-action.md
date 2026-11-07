---
url: 'https://docs.workato.com/en/connectors/bill/search-record-action.md'
description: >-
  The Search record batch action in the BILL connector searches BILL objects in
  batches and returns the records that match your filter criteria.
---

# BILL - Search record action (batch)

The **Search record** batch action searches BILL objects in batches and returns a list of the results that fit the specified criteria.

## Input

| Field | Description |
| --- | --- |
| Object | Select the object type to search for. |
| Offset | Enter the number of objects to skip at the start of the search. |
| Limit | Enter the maximum number of objects you plan to retrieve. The maximum value is `999` and the default value is `500`. |
| Filter source list | Input a list datapill that contains the fields, operators, and values you plan to use for filtering. |
| Field | Enter the API name of the field you plan to filter by. Find a field's API name by hovering over its datapill in the **Recipe data** menu or refer to [BILL's API v2 documentation](https://developer.bill.com/v2/reference/api-reference-overview). |
| Value | Provide the value to compare against the selected **Field**. |
| Operator | Specify an operator to define how to compare the returned **Field** values against the **Value** you set. For example, `=` (equals), `!=` (not equal), `<` (less than), and `>` (greater than). |
| Include related fields | Specify whether to include related fields in the results. |

## Output

| Field | Description |
| --- | --- |
| Response status | Displays the status of the **Search record** action's API request. A value of `0` indicates success, and `1` indicates an error. |
| Response message | The response message returned from BILL's API. |
| Response data | A datatree that contains information about the objects found in BILL, such as their `ID`, `Name`, `Created` date, and `Active?` status. |

---
