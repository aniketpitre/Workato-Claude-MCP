---
url: 'https://docs.workato.com/en/connectors/clickup/create-record-action.md'
description: >-
  The **Create record** action creates a record in ClickUp, such as a task.
  Select the object to create, then provide the data for creating the record.
---

# ClickUp - Create record action

The **Create record** action creates a record in ClickUp, such as a task. Select the object to create, then provide the data for creating the record.

## Input

Input fields load dynamically based on the object selected. For example, if you select the **Chat view comment** object, the following input fields are available.

| Input field | Description |
| --- | --- |
| View ID | Provide the view ID to create a record in. |
| Comment text | Enter the comment text. |
| Notify all | Select the boolean value from the drop-down menu. |

## Output

The output schema loads dynamically based on the object selected when configuring the action. For example, if you select the **Chat view comment** object, the following output schema is generated.

| Output field | Description |
| --- | --- |
| Chat view ID | The unique ID of the chat view. |
| History ID | The unique ID to track the history of the comment. |
| Date | The date of a **Chat view comment** using unix time in milliseconds. |

---
