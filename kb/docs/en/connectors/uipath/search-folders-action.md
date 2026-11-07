---
url: 'https://docs.workato.com/en/connectors/uipath/search-folders-action.md'
description: >-
  The Search folders action allows you to retrieve a list of folders in UiPath
  Orchestrator.
---

# UiPath - Search folders action

The **Search folders** action allows you to retrieve a list of folders in UiPath Orchestrator.

## Input

| Input field | Description |
| --- | --- |
| Expand | Indicates the related entities to be represented inline. The maximum depth is 2. |
| Filter | Restricts the set of items returned. The maximum number of expressions is 100. For example, `FolderType` eq 'Standard'. Refer to the [UiPath documentation](https://docs.uipath.com/orchestrator/automation-cloud/latest/api-guide/building-api-requests#%24filter) for more information. |
| Select | Limits the properties returned in the result. |
| Order by | Specifies the order in which items are returned. The maximum number of expressions is 5, for example. |
| Top | Limits the number of items returned from a collection. The maximum value is 1000. |
| Skip | Excludes the specified number of items of the queried collection from the result. |
| Count | Indicates whether the total count of items within a collection are returned in the result. |

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
| Count | Number of records returned. |

---
