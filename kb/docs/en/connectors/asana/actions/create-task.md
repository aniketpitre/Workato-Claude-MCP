---
url: 'https://docs.workato.com/en/connectors/asana/actions/create-task.md'
description: The Create task action creates a task in Asana.
---

# Asana - Create task action

The **Create task** action creates a task in Asana. Tasks must be created in an Asana workspace.

You can use the [List workspaces action](/en/connectors/asana/actions/list-workspaces) to view all available workspaces for the authorized user.

## Input

| Input field | Description |
| --- | --- |
| Sample workspace | Select the workspace or project. Custom fields defined in your Asana workspace or project are listed automatically after you select the workspace or project URL. |
| Workspace ID | Enter the workspace ID. You can find the Workspace ID in the admin console URL, for example `https://app.asana.com/admin/{workspace_gid}`. |
| Projects | Expand this section to configure the projects this task is associated with. |
| Projects source list (Projects) | Input a list datapill that represents the projects that this task belongs to. |
| Project ID (Projects) | Provide the unique identifier of the project. |
| Assignee status | Select the status of the people assigned. Accepted values are `inbox`, `later`, `today`, or `upcoming`. |
| Completed | Specify whether the task is completed. |
| Due on | Enter the date when the task is due. |
| Due at | Enter the date and time when the task is due. |
| Heart this | Specify whether to add a heart to this task. |
| Task name | Enter the name of the task. |
| Description | Enter the description of the task. |
| Assignee | Expand this section to configure the people that are assigned to this task. |
| Assignee ID (Assignee) | Enter the unique identifier of the assignee. Use this field if the **Assignee status** is `today` or `inbox`. |
| Followers | Expand this section to configure the people that follow this task. |
| Followers source list (Followers) | Input a list datapill that represents the people that follow this task |
| Follower ID (Followers) | Provide the unique identifier of the follower. |
| Tags | Expand this section to configure the tags attached to this task. |
| Tags source list (Tags) | Input a list datapill that represents the tags attached to this task. |
| Tag ID (Tags) | Provide the unique identifier of the tag. |
| Start on | Enter a start date. If you provide this value, specify either the **Due on** or **Due at** field. |
| Like this | Specify whether to add a like to this task. Select `Yes` to like it through the authorized user or `No` to not. The default value is `No`. |

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
| Number of hearts | The number of hearts given to the task. |
| Hearts | Array of people who have added heart to the task. |
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
  https://docs.workato.com/en/connectors/asana/actions/get-people-details-by-id.md
description: The Get people details by ID action retrieves user details by ID in Asana.
---

# Asana - Get people details by ID action

The **Get people details by ID** action retrieves user details by ID in Asana.

## Input

| Input field | Description |
| --- | --- |
| People ID | Enter the user ID. |

## Output

| Output field | Description |
| --- | --- |
| People | Object representing the person. |
| People ID (People) | The unique identifier of the person. |
| Name (People) | The name of the person. |
| Email (People) | The email address of the person. |
| Photo (People) | Photo URLs for the person in various sizes. |
| Image 21x21 (Photo) | 21x21 pixel image URL. |
| Image 27x27 (Photo) | 27x27 pixel image URL. |
| Image 36x36 (Photo) | 36x36 pixel image URL. |
| Image 70x70 (Photo) | 70x70 pixel image URL. |
| Image 128x128 (Photo) | 128x128 pixel image URL. |
| Workspaces (People) | Array of workspaces the person belongs to. |
| Workspace ID (Workspaces) | The unique identifier of each workspace. |
| Name (Workspaces) | The name of each workspace. |

---

---
url: >-
  https://docs.workato.com/en/connectors/asana/actions/get-project-detail-by-id.md
description: >-
  The Get project detail by ID action retrieves details about an Asana project
  using the project's ID.
---

# Asana - Get project detail by ID action

The **Get project detail by ID** action retrieves details about an Asana project using the project's ID.

## Input

| Input field | Description |
| --- | --- |
| Project ID | Enter the project ID located in the URL of the projects page. |

## Output

| Output field | Description |
| --- | --- |
| Project name | The project name. |
| Project ID | The project ID. |
| Owner | The person who is the owner of the project. |
| Owner ID (Owner) | The unique identifier of the owner. |
| Name (Owner) | The name of the owner. |
| Current status | The current status of the project. |
| Due date | The date and time when the project is due. |
| Due on | The date when the project is due. |
| Start on | The start date of the project. |
| Created at | The date and time when the record was created. |
| Modified at | The date and time when the project was last modified. |
| Archived | Indicates whether the project has been archived. |
| Public (deprecated) | Indicates whether the project is public to the organization. |
| Privacy setting | The project's privacy setting. |
| Members | Array of people who are members in this project. |
| Member ID (Members) | The unique identifier of each member. |
| Name (Members) | The name of each member. |
| Followers | Array of people that follow the project. |
| Follower ID (Followers) | The unique identifier of each follower. |
| Name (Followers) | The name of each follower. |
| Color | The color assigned to the project. |
| Description | Detailed description about the project. |
| Workspace | The workspace that the project belongs to. |
| Workspace ID (Workspace) | The unique identifier of the workspace. |
| Name (Workspace) | The name of the workspace. |

> **DEPRECATED TEAM OBJECT**
> 
> Effective April 1, 2025, the `team` object returned in this action's response is deprecated. Projects can now be shared directly with multiple teams. Newly created projects will no longer be associated with a single team, and the `project.team` field will be `null`. Refer to the [Asana changelog](https://forum.asana.com/t/change-teamless-projects/929205) for more information.

---
