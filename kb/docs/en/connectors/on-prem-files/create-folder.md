---
url: 'https://docs.workato.com/en/connectors/on-prem-files/create-folder.md'
description: >-
  The Create folder action in the On-prem files connector lets you create a new
  folder in your on-prem directory at a path you specify.
---

# On-prem files - Create folder action

The **Create folder** action creates a folder in your on-prem directory. If a folder with the same name already exists in the destination, the action returns a success.

You can use this action with the [upload file](/en/connectors/on-prem-files/upload-file-action) action to upload files into a new folder.

## Input

| Input field | Description |
| --- | --- |
| Parent folder | Select or manually enter the [relative path](/en/connectors/on-prem-files#relative-path) of the destination to create the new folder in. |
| Folder path | Enter the path of the folder to create, relative to the path defined in the **Parent folder** field. Folders are created automatically if they don't already exist within the specified file path. |

## Output

| Output field | Description |
| --- | --- |
| Folder path | The [relative path](/en/connectors/on-prem-files#relative-path) to the newly created folder. For example: `/my-profile/path/newly-created-folder`. |

---
