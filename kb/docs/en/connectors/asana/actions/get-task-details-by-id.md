---
url: 'https://docs.workato.com/en/connectors/asana/actions/get-task-details-by-id.md'
description: >-
  The Get task details by ID action retrieves the details of a task by ID in
  Asana.
---

# Asana - Get task details by ID action

The **Get task details by ID** action retrieves the details of a task by ID in Asana.

## Input

| Input field | Description |
| --- | --- |
| Task ID | Enter the task ID. You can find the task ID at the end of the URL of the task page. |
| Workspace ID | Enter the workspace ID. |
| Project | Select the project this task is associated with. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | The task ID. |
| Assignee | The people that are assigned to this task. |
| Assignee ID (Assignee) | The unique identifier of the assignee. |
| Name (Assignee) | The name of the assignee. |
| Assignee status | The status of the people assigned. |
| Completed | Indicates whether the task is completed. |
| Completed at | The date and time when the task was completed. |
| Created at | The date and time when this record was created. |
| Due on | The date when the task is due. |
| Due at | The date and time when the task is due. |
| Followers | Array of people that follow this task. |
| Follower ID (Followers) | The unique identifier of each follower. |
| Name (Followers) | The name of each follower. |
| Heart this | Shows whether the authorized user has hearted this task. |
| Number of hearts | The number of hearts added to the task. |
| Hearts | Array of people that have hearted this task. |
| ID (Hearts) | The unique identifier of each heart. |
| People (Hearts) | The user who added the heart. |
| People ID (People) | The unique identifier of the user. |
| Name (People) | The name of the user. |
| Start on | The start date of this task. |
| Like this | Shows whether the authorized user has liked this task. |
| Number of likes | The number of likes added to the task. |
| Likes | Array of people that have liked this task. |
| ID (Likes) | The unique identifier of each like. |
| People (Likes) | The user who added the like. |
| People ID (People) | The unique identifier of the user. |
| Name (People) | The name of the user. |
| Resource type (People) | The resource type of the user. |
| Modified at | The date and time when the task was last modified. |
| Task name | The name of the task. |
| Description | The description of the task. |
| Projects | Array of projects that this task belongs to. |
| Project ID (Projects) | The unique identifier of each project. |
| Name (Projects) | The name of each project. |
| Parent Task | The parent task for this task. |
| Task ID (Parent Task) | The unique identifier of the parent task. |
| Name (Parent Task) | The name of the parent task. |
| Workspace | The workspace that this task belongs to. |
| Workspace ID (Workspace) | The unique identifier of the workspace. |
| Name (Workspace) | The name of the workspace. |
| Memberships | Array of membership details about this task. |
| Project (Memberships) | The project associated with this membership. |
| Project ID (Project) | The unique identifier of the project. |
| Name (Project) | The name of the project. |
| Section (Memberships) | The section associated with this membership. |
| Section ID (Section) | The unique identifier of the section. |
| Name (Section) | The name of the section. |
| Tags | Array of tags attached to this task. |
| Tag ID (Tags) | The unique identifier of each tag. |
| Name (Tags) | The name of each tag. |
| Created by | The user that created this task. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the creator. |
| Resource type (Created by) | The resource type of the creator. |
| Custom fields | Custom fields associated with the workspace or project. |

---

---
url: >-
  https://docs.workato.com/en/connectors/asana/actions/list-all-tasks-with-tag.md
description: The List all tasks with tag batch action lists tasks with a tag in Asana.
---

# Asana - List all tasks with tag action (batch)

The **List all tasks with tag** batch action lists tasks with a tag in Asana.

## Input

| Input field | Description |
| --- | --- |
| Tag ID | Enter the Tag ID. |
| Limit | Enter the number of objects to return per page. The value must be between 1 and 100. |
| Offset | Enter an offset to the next page returned by the API. If you don't provide an offset, the API returns the first page of results. |

## Output

| Output field | Description |
| --- | --- |
| Tasks | Array of tasks with the specified tag. |
| ID (Tasks) | The unique identifier of each task. |
| Name (Tasks) | The name of each task. |
| Created by (Tasks) | The user who created each task. |
| ID (Created by) | The unique identifier of the creator. |
| Name (Created by) | The name of the creator. |
| Resource type (Created by) | The resource type of the creator. |
| Next page | Pagination information for the next page of results. |
| Offset (Next page) | The offset for the next page. |
| Path (Next page) | The path for the next page. |
| URI (Next page) | The URI for the next page. |

---
