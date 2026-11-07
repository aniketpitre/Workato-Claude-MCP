---
url: 'https://docs.workato.com/en/connectors/eloqua/delete-record.md'
description: >-
  The Delete records action in the Eloqua connector lets you delete a standard
  or custom record by ID in Eloqua.
---

# Eloqua - Delete records action

The action `Delete record` allows you to delete a standard record or custom record in Eloqua. To begin, you will first need to select the object type of the record you want to delete.

![Select Eloqua record](/assets/record-select-record.Cz5MWZNN.png)_You can select standard or custom objects_

## Input

When you select the object you want to delete, you'll be prompted to provide the ID of the record in question.

![Get Eloqua records](/assets/delete-record-field.CrmMxtOp.png)

| Input field | Description |
| --- | --- |
| Object | The object type. This can be standard or custom objects. |
| ID | The ID of the record. |

## Output

The output to this action is a Status datapill that informs you if the delete action was successful.

![Eloqua record](/assets/delete-record-output-field.CUrw9ZcO.png)

---
