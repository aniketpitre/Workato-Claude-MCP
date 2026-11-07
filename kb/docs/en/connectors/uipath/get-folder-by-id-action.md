---
url: 'https://docs.workato.com/en/connectors/uipath/get-folder-by-id-action.md'
description: >-
  The Get folder by ID action retrieves the details of a specific folder by its
  ID in UiPath Orchestrator.
---

# UiPath - Get folder by ID action

The **Get folder by ID** action retrieves the details of a specific folder by its ID in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Folder ID | Provide the ID of the folder to retrieve. |

## Output

| Output field | Description |
| --- | --- |
| ID | Unique identifier of the folder. |
| Key | Unique key value associated with the folder. |
| Display name | Human-readable name assigned to the folder. |
| Fully qualified name | Full path of the folder including parent hierarchy. |
| Description | Optional text describing the folder’s purpose or content. |
| Folder type | Indicates whether the folder is of type `Modern` or `Classic`. |
| Is personal | Boolean value indicating if the folder is a personal workspace. |
| Provision type | Specifies how the folder was provisioned. |
| Permission model | Defines the folder’s permission structure, such as inherited or custom. |
| Parent ID | Unique identifier of the parent folder, if applicable. |
| Parent key | Key value of the parent folder. |
| Feed type | Specifies the package feed type associated with the folder. |
| Fully qualified name orderable | A normalized version of the fully qualified name, useful for sorting. |
| Is active | Boolean value indicating whether the folder is currently active. |
| Reserved options | Contains system-reserved properties related to folder configuration. |

---
