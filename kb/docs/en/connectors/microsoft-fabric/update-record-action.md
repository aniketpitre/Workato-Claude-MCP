---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/update-record-action.md
description: >-
  The Update record action enables you to update the specified record in
  Microsoft Fabric.
---

# Microsoft Fabric - Update record action

The **Update record** action enables you to update the specified record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to update its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item is located. |
| Lakehouse ID | Select or enter the ID of the lakehouse to update. |
| Display name | Enter the name of the lakehouse. |
| Description | Enter the description for the lakehouse. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. To take an example of the **Lakehouse** object, the following are the output fields.

| Output field | Description |
| --- | --- |
| Description | Description of the lakehouse. |
| Display name | Name of the lakehouse. |
| Folder ID | ID of the folder where the lakehouse is created. |
| ID | ID of the lakehouse. |
| Properties | Properties of the lakehouse include the following data. Type, Default schema, One lake files path, One lake tables path, SQL endpoint properties, Connection string, ID, Provisioning status. |
| Item tag | The list of tags attached to the lakehouse is any. |
| Type | Type of the item. Lakehouse in this case. |
| Workspace ID | ID of the workspace where the Lakehouse was created. |
| Status | Status of provisioning of the lakehouse. |
