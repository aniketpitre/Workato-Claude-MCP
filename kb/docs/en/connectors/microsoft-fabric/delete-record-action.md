---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/delete-record-action.md
description: The Delete record action enables you to delete a record in Microsoft Fabric.
---

# Microsoft Fabric - Delete record action

The **Delete record** action enables you to delete a record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to delete its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to delete. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. To take an example of the **Lakehouse** object, the following are the output fields.

| Output field | Description |
| --- | --- |
| Success | Status of the delete operation. |
