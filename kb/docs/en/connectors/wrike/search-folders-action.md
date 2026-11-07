---
url: 'https://docs.workato.com/en/connectors/wrike/search-folders-action.md'
description: >-
  The Search folder action in the Wrike connector retrieves up to 100 folders
  that match your search criteria from your Wrike instance.
---

# Wrike - Search folder action

Folders are one of the main ways to organize and manage information on Wrike.

This action retrieves a list of folders that matches your search criteria. Only records in your Wrike instance that match all the criteria will be returned. A maximum of 100 folders can be retrieved per job.

![Search folder action](/assets/search-folder-action.CnCXnKyE.png)_Search folder action_

## Input

| Input field | Description |
| --- | --- |
| Custom field list | Select a custom field to open the corresponding input field. This will be blank by default. |
| Metadata | The metadata details to use in your search. You can define metadata with a metadata source list or manually input the `Key`/`Value` pair information. |
| Permalink | The link to open the folder in a web workspace. This is only accessible if the user has the appropriate access. |
| Descendants | Select `Yes` to add all descendant folders to search scope, otherwise select `No`. |
| Retrieve deleted folders only | Select `True` to retrieve deleted folders only, otherwise select `False`. |
| Updated date | Retrieve folders created after this date. |

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
| List size | The size of the list, corresponding to the number of folders retrieved. |

---
