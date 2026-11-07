---
url: 'https://docs.workato.com/en/connectors/salesloft/update-record-action.md'
description: The update object action allows you to update an object in Salesloft.
---

# Salesloft - Update record action

The **Update object** action allows you to update an object in Salesloft.

## Input

| Input field | Description |
| --- | --- |
| Object name | Select the object to be updated from the drop-down menu. |

Workato dynamically populates additional fields depending on the object you select. For example, if you select the **Note** object, fields such as **Note ID**, **Content**, and **Call ID** appear.

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, if the select object is **Note** then the output schema is as follows.

| Output fields | Description |
| --- | --- |
| Note ID | Unique identifier for the note. |
| Content | The content of the note. |
| Created at | Timestamp showing when the note was created. |
| Updated at | Timestamp showing when the note was last updated. |
| User | Object showing the details of the user who updated the note. |
| Associated with | Object showing the details of entity this note is associated to. |
| Call | Object showing the call details. |

---
