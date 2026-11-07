---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/create-record-action.md
description: >-
  The Create record action enables you to create the specified record in
  Microsoft Fabric.
---

# Microsoft Fabric - Create record action

The **Create record** action enables you to create the specified record in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create its record. Fields load dynamically based on the selected object. |

For example, if the selected object is **Lakehouse**, the input schema is as follows:

| Input field | Description |
| --- | --- |
| Workspace ID | Select or enter the ID of the workspace where the item should be created. |
| Display name | Enter the name of the lakehouse. |
| Creation payload | Enter the payload containing information for the lakehouse to be created. |
| Description | Enter the description for the lakehouse. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the data tree to subsequent steps. For example, the output for the **Lakehouse** object, includes the following fields:

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
