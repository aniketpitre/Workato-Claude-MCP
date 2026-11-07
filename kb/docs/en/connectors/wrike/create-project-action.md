---
url: 'https://docs.workato.com/en/connectors/wrike/create-project-action.md'
description: >-
  The Create project action in the Wrike connector creates a single project in a
  specified location to organize and report on your work.
---

# Wrike - Create project action

Projects are one of the main ways to organize, manage, and report on work within Wrike. In essence, Wrike projects are folders with additional properties.

This action creates a single project in a specified location. To create a main project, select **Root** as the parent folder.

![Create project action](/assets/create-project-action.DY0gbJB1.png)_Create project action_

## Input

| Input field | Description |
| --- | --- |
| Parent folder/project | Select a parent folder/project to create this folder in. To use folder/project ID, toggle "Enter a folder/project ID". |
| Title | The title of the folder. |
| Project | Select the project properties.
<table><tbody><tr><td>Status</td><td>The status of the project.</td></tr><tr><td>User IDs of Wrike users who should own this project</td><td>Select users as project owners. You can define users with a source list or manually input their user ID.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project will end.</td></tr></tbody></table>

 |
| Description | The description of the project. |
| Users who share the project | Select users who share this project. You can define users with a source list or manually input their user ID. |
| Custom fields | Provide data for the custom fields. |

## Output

| Output field | Description |
| --- | --- |
| Project ID | The ID of the project. |
| Account ID | The ID of the account. |
| Title | The title of the project. |
| Updated date | The date this project was updated. |
| Created date | The date this project was created. |
| Description | The description of the project. Will be blank if not specified. |
| Users who share the project | The list of users who share the project.
<table><tbody><tr><td>User ID</td><td>The ID of the user who shares this project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Parent project | The list of parent projects of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the parent project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent projects retrieved.</td></tr></tbody></table>

 |
| Child project | The list of child projects of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the child project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of child projects retrieved.</td></tr></tbody></table>

 |
| Super parent project | The list of super parent project to this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the super parent project.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent projects retrieved.</td></tr></tbody></table>

 |
| Scope | The scope of the project. |
| Has attachments | Indicates if the project has attachments. |
| Permalink | The link to open the project in a web workspace. This is only accessible if the user has the appropriate access. |
| Workflow ID | The ID of the project workflow. |
| Metadata | The metadata of this project. The metadata list size corresponds to the number of metadata entries retrieved. |
| Project | The project properties of this project.

<table><tbody><tr><td>Author</td><td>The author who created the project.</td></tr><tr><td>Owner ID</td><td>The list of IDs of project owners.<table><tbody><tr><td>User ID</td><td>The user ID of the project owner.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of project owners retrieved.</td></tr></tbody></table></td></tr><tr><td>Status</td><td>The status of the project.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project was ended.</td></tr><tr><td>Created date</td><td>The date this project was created.</td></tr><tr><td>Completed date</td><td>The date this project was completed.</td></tr></tbody></table>

 |
| Custom fields | Includes data from custom fields. |

---
