---
url: 'https://docs.workato.com/en/connectors/wrike/updated-project-trigger.md'
description: >-
  The New/updated project trigger in the Wrike connector picks up projects that
  are created or updated and returns the project tree data.
---

# Wrike - New/updated project triggers

Projects are one of the main ways to organize, manage, and report on work within Wrike. In essence, Wrike projects are folders with additional properties.

## New/updated project trigger

This trigger picks up projects that are created or updated and returns the project tree data. Each record is processed as a separate job.

![New/updated project trigger](/assets/updated-project-trigger.DiJ-b5eh.png)_New/updated project trigger_

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Projects created or updated after this time will be processed by the recipe. If left blank, the default will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

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
| Parent folder | The list of parent folders of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent folders retrieved.</td></tr></tbody></table>

 |
| Child folder | The list of child folders of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the child folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of child folders retrieved.</td></tr></tbody></table>

 |
| Super parent folder | The list of super parent folder to this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the super parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent folders retrieved.</td></tr></tbody></table>

 |
| Scope | The scope of the project. |
| Has attachments | Indicates if the project has attachments. |
| Permalink | The link to open the project in a web workspace. This is only accessible if the user has the appropriate access. |
| Workflow ID | The ID of the project workflow. |
| Metadata | The metadata of this project. The metadata list size corresponds to the number of metadata entries retrieved. |
| Project | The project properties of this project.

<table><tbody><tr><td>Author</td><td>The author who created the project.</td></tr><tr><td>Owner ID</td><td>The list of IDs of project owners.<table><tbody><tr><td>User ID</td><td>The user ID of the project owner.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of project owners retrieved.</td></tr></tbody></table></td></tr><tr><td>Status</td><td>The status of the task.</td></tr><tr><td>Start date</td><td>The date this project was started.</td></tr><tr><td>End date</td><td>The date this project was ended.</td></tr><tr><td>Created date</td><td>The date this project was created.</td></tr><tr><td>Completed date</td><td>The date this project was completed.</td></tr></tbody></table>

 |
| Custom fields | Includes data from custom fields. |

## New/updated project trigger (real-time)

This trigger picks up projects as soon as they are created or updated and returns the project tree data. Each record is processed as a separate job.

![New/updated project trigger(real time)](/assets/updated-project-trigger-real-time.D2kZDGok.png)_New/updated project trigger (real time)_

### Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Projects created or updated after this time will be processed by the recipe. If left blank, the default will be set to **one hour** before the recipe is first started. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

### Output

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
| Parent folder | The list of parent folders of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent folders retrieved.</td></tr></tbody></table>

 |
| Child folder | The list of child folders of this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the child folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of child folders retrieved.</td></tr></tbody></table>

 |
| Super parent folder | The list of super parent folder to this project.

<table><tbody><tr><td>Project ID</td><td>The project ID of the super parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent folders retrieved.</td></tr></tbody></table>

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
