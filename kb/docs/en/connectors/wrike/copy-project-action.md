---
url: 'https://docs.workato.com/en/connectors/wrike/copy-project-action.md'
description: >-
  The Copy project action in the Wrike connector selects a single project and
  copies it into a specified location in Wrike.
---

# Wrike - Copy project action

Projects are one of the main ways to organize, manage, and report on work within Wrike. In essence, Wrike projects are folders with additional properties.

This action selects a single project and copies it into a specified location. To copy the project as a main project, select **Root** as the parent project.

![Copy project action](/assets/copy-project-action.FMJUwGXI.png)_Copy project action_

## Input

| Input field | Description |
| --- | --- |
| Project to be copied | The name of the project to be copied. To use project ID, toggle "Enter a project ID". |
| Destination project/project | Select a parent project/project to copy the project into. To use folder/project ID, toggle "Enter a folder/project ID". |
| Title | The title of the project. |
| Copy description | Select `Yes` to copy the original project's description, otherwise select `No`. This will leave the field empty. |
| Copy assignee | Select `Yes` to copy the original project's task with the original task responsible list, otherwise select `No`. |
| Add assignees to copied tasks | Add users to the task responsible list in the new project. You can define users with a source list or manually input their user ID. |
| Remove assignees to copied tasks | Remove user from the task responsible list in the new project. You can define users with a source list or manually input their user ID. |
| Copy custom fields | Select `Yes` to copy the original project's custom fields, otherwise select `No`. |
| Copy custom statuses | Select `Yes` to copy the original project's custom statuses, otherwise select `No`. |
| Copy statuses | Select `Yes` to copy the original project's statuses, otherwise select `No`. This will set the status to `New`. |
| Copy parent projects/projects | Select `Yes` to copy the original project's parent projects/projects, otherwise select `No`. |
| Reschedule date | Only `New`/`In progress` tasks can be rescheduled. The date to use in task rescheduling.
> To activate and reschedule all tasks, use **Reschedule date** in combination with **Copy statuses** = `No`.

 |
| Reschedule mode | Valid only of **Reschedule date** is present. Select `Start` to set the start date of the task in the new project. Select `End` to set the end date to the task. |
| Entry quota | Choose the maximum number of tasks/projects/projects to be copied to the new project. |

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
