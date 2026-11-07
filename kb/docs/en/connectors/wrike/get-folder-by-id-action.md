---
url: 'https://docs.workato.com/en/connectors/wrike/get-folder-by-id-action.md'
description: >-
  The Get folder by ID action in the Wrike connector retrieves a single folder
  that matches the folder ID you provide from your Wrike instance.
---

# Wrike - Get folder by id action

Folders are one of the main ways to organize and manage information on Wrike.

This action retrieves a single folder that matches a search by folder ID. Only results in your Wrike instance that match the criteria will be returned.

![Get folder by ID action](/assets/get-folder-by-id-action.BkQmPTQO.png)_Get folder by ID action_

## Input

| Input field | Description |
| --- | --- |
| Folder | Select a folder to retrieve. To use folder ID, toggle "Enter a folder ID". |

## Output

| Output field | Description |
| --- | --- |
| Folder ID | The ID of the folder. |
| Account ID | The ID of the account. |
| Title | The title of the folder. |
| Updated date | The date this folder was updated. |
| Created date | The date this folder was created. |
| Description | The description of the folder. Will be blank if not specified. |
| Users who share the folder | The list of users who share the folder.
<table><tbody><tr><td>User ID</td><td>The ID of the user who shares this folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Parent folder | The list of parent folders of this folder.

<table><tbody><tr><td>Folder ID</td><td>The folder ID of the parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent folders retrieved.</td></tr></tbody></table>

 |
| Child folder | The list of child folders of this folder.

<table><tbody><tr><td>Folder ID</td><td>The folder ID of the child folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of child folders retrieved.</td></tr></tbody></table>

 |
| Super parent folder | The list of super parent folder to this folder.

<table><tbody><tr><td>Folder ID</td><td>The folder ID of the super parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent folders retrieved.</td></tr></tbody></table>

 |
| Scope | The scope of the folder. |
| Has attachments | Indicates if the folder has attachments. |
| Permalink | The link to open the folder in a web workspace. This is only accessible if the user has the appropriate access. |
| Workflow ID | The ID of the folder workflow. |
| Metadata | The metadata of this folder. The metadata list size corresponds to the number of metadata entries retrieved. |
| Project | The project properties of this folder.

<table><tbody><tr><td>Author</td><td>The author who created the project.</td></tr><tr><td>Owner ID</td><td>The list of IDs of project owners.<table><tbody><tr><td>User ID</td><td>The user ID of the project owner.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of project owners retrieved.</td></tr></tbody></table></td></tr><tr><td>Status</td><td>The status of the project.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project was ended.</td></tr><tr><td>Created date</td><td>The date this project was created.</td></tr><tr><td>Completed date</td><td>The date this project was completed.</td></tr></tbody></table>

 |
| Custom fields | Includes data from custom fields. |

---
