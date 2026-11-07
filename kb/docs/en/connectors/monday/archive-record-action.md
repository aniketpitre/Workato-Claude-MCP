---
url: 'https://docs.workato.com/en/connectors/monday/archive-record-action.md'
description: The Archive Record action enables you to archive a specific record on Monday.
---

# Monday - Archive record action

The **Archive record** action enables you to archive a specific record in Monday.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object type for the record to archive. Fields load dynamically based on the object you select. |

Additional input fields are available based on the object you select. Refer to the [Monday](https://developer.monday.com/api-reference/reference/about-the-api-reference) documentation for a complete list of input fields.

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item. |
| Created at | The item's creation date. |
| Creator ID | The unique identifier of the item's creator. Returns `null` if the board created the item by default. |
| Email | The item's email. |
| Name | The item's name. |
| Relative link | The item's relative path. |
| State | The item's state. |
| Updated at | The date the item was last updated. |
| URL | The URL to the item. |

---
