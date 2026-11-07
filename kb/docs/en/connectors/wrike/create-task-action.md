---
url: 'https://docs.workato.com/en/connectors/wrike/create-task-action.md'
description: >-
  The Create task action in the Wrike connector creates a single task in a
  specified folder or project to help organize your work.
---

# Wrike - Create task action

This action creates a single task in a specified Wrike folder/project. To create a main task, select **Root** as the parent folder.

![Create task action](/assets/create-task-action.eDdBLd3N.png)_Create task action_

## Input

| Input field | Description |
| --- | --- |
| Folder | Select a parent folder to create this task in. To use folder ID, toggle "Enter a folder ID". |
| Title | The title of the task. |
| Description | The description of the task. |
| Importance | The importance of the task. Permitted values are `High`, `Normal`, and `Low`. |
| Assignee | Select users who will be assigned to this task. You can define users with a source list or manually input their user ID. |
| Priority after | The newly created task will be put after this task in the task list. |
| Priority before | The newly created task will be put before this task in the task list. |
| Follow | Select `True` if this is a follow task, otherwise select `False`. |
| Share task with users | Select users who will share this task. You can define tasks with a source list or manually input their user ID. |
| Add parent folders | Select folders to be marked as parent folders. You can define folders with a source list or manually input their folder ID. |
| Followers | Select users who will be marked as task followers. You can define users with a source list or manually input their user ID. |
| Super tasks | The newly created task will be marked as a subtask to this task. You can define tasks with a task list or manually input their task ID. |
| Date | The start and due dates of this task. If left blank, a `backlog` task will be created.
<table><tbody><tr><td>Start date</td><td>The start date of this task.</td></tr><tr><td>Due date</td><td>The due date of this task.</td></tr></tbody></table>

 |
| Custom status | Select a custom status to describe this task. To use custom status ID, toggle "Enter a custom status ID". |
| Status | Select the status of the task. Permitted values are `New`, `In progress`, `Completed`, `On hold`, and `Canceled`. Ignore this field if you are using custom statuses. |
| Custom fields | Provide data for the custom fields. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | The ID of the task. |
| Account ID | The ID of the account. |
| Title | The title of the task. |
| Description | The description of the task. Will be blank if not specified. |
| Brief description | A brief description of the task. |
| Parent folder | The list of parent folders of this task.
<table><tbody><tr><td>Folder ID</td><td>The folder ID of the parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of parent folders retrieved.</td></tr></tbody></table>

 |
| Super parent folder | The list of super parent folder to this task.

<table><tbody><tr><td>Folder ID</td><td>The folder ID of the super parent folder.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of super parent folders retrieved.</td></tr></tbody></table>

 |
| List of users who share task | The list of users who share the task.

<table><tbody><tr><td>User ID</td><td>The ID of the user who shares this task.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Assignees | The list of users who are assigned to the task.

<table><tbody><tr><td>User ID</td><td>The ID of the user who shares this task.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Status | The status of the task. |
| Importance | The importance of the task. Permitted values are `High`, `Normal`, and `Low`. |
| Created date | The date this task was created. |
| Updated date | The date this task was updated. |
| Completed date | The date this task was completed. |
| Dates | The tasks dates.

<table><tbody><tr><td>Type</td><td>The type of task. Permitted values are <code>Backlogged</code>, <code>Milestone</code>, and <code>scheduled</code>.</td></tr><tr><td>Duration</td><td>Mandatory for <code>Planned</code> tasks. The duration in minutes.</td></tr><tr><td>Start date</td><td>The start date of this task. <code>Backlogged</code> tasks do not have start dates.</td></tr><tr><td>Due date</td><td>The due date of this task. <code>Backlogged</code> tasks and <code>Milestone</code> tasks do not have due dates.</td></tr><tr><td>Work on weekends</td><td>Indicates if weekends are included in task scheduling.</td></tr></tbody></table>

 |
| Scope | The scope of the task. |
| Author | The list of users who are assigned as authors of the task.

<table><tbody><tr><td>User ID</td><td>The ID of the user.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Custom status ID | The custom status ID of the task. |
| Custom status | The custom status of the task.

<table><tbody><tr><td>Name</td><td>The name of the custom status.</td></tr><tr><td>List size</td><td>The custom status ID of the task.</td></tr></tbody></table>

 |
| Has attachments | Indicates if the folder has attachments. |
| Permalink | The link to open the task in a web workspace. This is only accessible if the user has the appropriate access. |
| Priority | The ordering key that defines the task order in a task list. |
| Followed by me | Indicates if the task is followed by the Wrike user registered on Workato. |
| Followers | The users who follow this task.

<table><tbody><tr><td>Follower ID</td><td>The ID of the user who follows this task.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of users retrieved.</td></tr></tbody></table>

 |
| Super task | The list of tasks that are marked as super tasks.

<table><tbody><tr><td>Super task ID</td><td>The ID of the task that is marked as a super task.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of tasks retrieved.</td></tr></tbody></table>

 |
| Subtask | The list of tasks that are marked as subtasks.

<table><tbody><tr><td>Super task ID</td><td>The ID of the task that is marked as a subtask.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of subtasks retrieved.</td></tr></tbody></table>

 |
| Dependency | The list of tasks that are marked as dependencies.

<table><tbody><tr><td>Dependency ID</td><td>The ID of the task that is marked as a dependency.</td></tr><tr><td>List size</td><td>The size of the list, corresponding to the number of tasks retrieved.</td></tr></tbody></table>

 |
| Metadata | The metadata of this task. The metadata list size corresponds to the number of metadata entries retrieved. |
| Custom fields | Includes data from custom fields. |

---
