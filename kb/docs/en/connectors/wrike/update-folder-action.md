---
url: 'https://docs.workato.com/en/connectors/wrike/update-folder-action.md'
description: >-
  The Update folder action in the Wrike connector updates a specific folder,
  letting you change its name, title, description, and sharing users.
---

# Wrike - Update folder action

Folders are one of the main ways to organize and manage information on Wrike.

This action updates a specific folder in Wrike. You can change the folder name, add, or modify the title and description, as well as modify sharing users.

![Update folder action](/assets/update-folder-action.CRqfQujJ.png)_Update folder action_

## Input

| Input field | Description |
| --- | --- |
| Folder | Select a folder to update. To use folder ID, toggle "Enter a folder ID". |
| Title | The new title of the folder. |
| Description | The description of the folder. |
| Users to share the folder with | Select users to share this folder with. You can define users with a source list or manually input their user ID. |
| Remove users from sharing of folder | Select the users to remove from sharing this folder. You can define users with a source list or manually input their user ID. |
| Remove parent folders/projects | Select the parent folders to remove. You cannot remove the **Root folder** or the **Recycle bin**. You can define folders with a source list or manually input the folder ID. |
| Add parent folders/projects | Select parent folders/projects to add. You can define folders/projects with a source list or manually input the folders/projects ID. |
| Restore | Select `Yes` to restore folder from recycle bin, otherwise select `No`. |
| Custom field | Provide data for the custom fields. |
| Project | Wrike projects are folders with additional properties. For more information, see the [Create project action](/en/connectors/wrike/create-project-action.html).
<table><tbody><tr><td>Status</td><td>The status of the task.</td></tr><tr><td>Add owner ID</td><td>Select users to add as project owners.</td></tr><tr><td>Remove owner ID</td><td>Select users to remove as project owners.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project will end.</td></tr></tbody></table>

 |

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
