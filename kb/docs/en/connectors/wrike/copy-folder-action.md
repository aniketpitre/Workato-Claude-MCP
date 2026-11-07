---
url: 'https://docs.workato.com/en/connectors/wrike/copy-folder-action.md'
description: >-
  The Copy folder action in the Wrike connector selects a single folder and
  copies it into a specified location in Wrike.
---

# Wrike - Copy folder action

Folders are one of the main ways to organize and manage information on Wrike.

This action selects a single folder and copies it into a specified location. To copy the folder as a main folder, select **Root** as the parent folder.

![Copy folder action](/assets/copy-folder-action.Dg1D_-Bh.png)_Copy folder action_

## Input

| Input field | Description |
| --- | --- |
| Folder to be copied | The name of the folder to be copied. To use folder ID, toggle "Enter a folder ID". |
| Destination folder/project | Select a parent folder/project to copy the folder into. To use folder/project ID, toggle "Enter a folder/project ID". |
| Title | The title of the folder. |
| Copy description | Select `Yes` to copy the original folder's description, otherwise select `No`. This will leave the field empty. |
| Copy assignee | Select `Yes` to copy the original folder's task with the original task responsible list, otherwise select `No`. |
| Add assignees to copied tasks | Add users to the task responsible list in the new folder. You can define users with a source list or manually input their user ID. |
| Remove assignees to copied tasks | Remove users from the task responsible list in the new folder. You can define users with a source list or manually input their user ID. |
| Copy custom fields | Select `Yes` to copy the original folder's custom fields, otherwise select `No`. |
| Copy custom statuses | Select `Yes` to copy the original folder's custom statuses, otherwise select `No`. |
| Copy statuses | Select `Yes` to copy the original folder's statuses, otherwise select `No`. This will set the status to `New`. |
| Copy parent folders/projects | Select `Yes` to copy the original folder's parent folders/projects, otherwise select `No`. |
| Reschedule date | Only `New`/`In progress` tasks can be rescheduled. The date to use in task rescheduling.
> To activate and reschedule all tasks, use **Reschedule date** in combination with **Copy statuses** = `No`.

 |
| Reschedule mode | Valid only if **Reschedule date** is present. Select `Start` to set the start date of the task in the new folder. Select `End` to set the end date to the task. |
| Entry quota | Choose the maximum number of tasks/folders/projects to be copied to the new folder. |

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
