---
url: 'https://docs.workato.com/en/connectors/monday/update-record-action.md'
description: >-
  The Update record action enables you to update the details of a specific
  record on Monday.
---

# Monday - Update record action

The **Update record** action enables you to update the details of a specific record in Monday.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object that contains the record to update. Fields load dynamically based on the object you select. |
| Item ID | Enter the unique identifier of the item to update. |
| Clear column | Indicates whether to clear all column values. |
| Select fields to retrieve | Select fields to return in the response, including nested object fields. |

Additional input fields are available based on the object you select. Refer to the [Monday](https://developer.monday.com/api-reference/reference/about-the-api-reference) documentation for a complete list of input fields.

## Output

| Output Field | Description |
| --- | --- |
| ID | The unique identifier of the item. |
| Created at | The item's creation date. |
| Creator ID | Unique identifier of the item’s creator. Returns `null` if the board created the item by default. |
| Email | The item's email. |
| Name | The item's name. |
| Relative link | The item's relative path. |
| State | The item's state. |
| Updated at | The date the item was last updated. |
| URL | The item's creation date. |

---
