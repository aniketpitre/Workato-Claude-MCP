---
url: 'https://docs.workato.com/en/connectors/monday/delete-record-action.md'
description: The Delete record action enables you to delete a record on Monday.
---

# Monday - Delete record action

The **Delete record** action enables you to delete a record in Monday.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object that contains the record to delete. Fields load dynamically based on the object you select. |

Additional input fields are available based on the object you select. Refer to the [Monday](https://developer.monday.com/api-reference/reference/about-the-api-reference) documentation for a complete list of input fields.

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item. |
| Created at | The item's creation date. |
| Creator ID | Unique identifier of the item's creator. Returns `null` if the board created the item by default. |
| Email | The item's email. |
| Name | The item's name. |
| Relative link | The item's relative path. |
| State | The item's state. |
| Updated at | The date the item was last updated. |
| URL | The URL to the item. |

---
