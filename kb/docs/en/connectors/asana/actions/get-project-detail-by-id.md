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
