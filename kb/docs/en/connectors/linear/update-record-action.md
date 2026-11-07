---
url: 'https://docs.workato.com/en/connectors/linear/update-record-action.md'
description: >-
  The Update record action enables you to update the details of a specific
  record in Linear.
---

# Linear - Update record action

The **Update record** action enables you to update the details of a specific record in Linear.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to retrieve a list of records. Fields load dynamically based on the object you select. |

For example, if you select **Project** as your object, the following input schema becomes available:

| Input field | Description |
| --- | --- |
| Select fields to retrieve | Select all fields (including the nested object fields) to return in the response. |
| ID | Provide the ID of the project to update. |
| Status ID | Provide the ID of the project status. |
| Name | Enter the project name. |
| Description | Enter the project description. |
| Content | Provide the project content as Markdown. |
| Converted from issue ID | Provide the ID of the issue from which that project is created. |
| Last applied template ID | Provide the ID of the previous template applied to the project. |
| Icon | Provide the icon of the project. |
| Color | Provide the color of the project. |
| Team IDs | Provide the IDs of the teams this project is associated with. |
| Project update reminders paused until at | Provide the time until which project update reminders are paused. |
| Update reminder frequency in weeks | Provide the n-weekly frequency at which to prompt for updates. |
| Update reminder frequency | Provide the frequency at which to prompt for updates. |
| Frequency resolution | Provide the frequency resolution. |
| Update reminders day | Provide the day on which to prompt for updates. |
| Update reminders hour | Provide the hour at which to prompt for updates. |
| Lead ID | Provide the ID of the project lead. |
| Member IDs | Provide the IDs of the members of this project. |
| Start date | Provide the planned start date of the project. |
| Start date resolution | Provide the resolution of the project's start date. |
| Target date | Provide the planned target date of the project. |
| Target date resolution | Provide the resolution of the project's estimated completion date. |
| Completed at | Specify the date when the project was completed. |
| Canceled at | Specify the date when the project was canceled. |
| SLA new issue | Indicate whether to send new issue notifications to Slack. |
| SLA issue comments | Indicate whether to send new issue comment notifications to Slack. |
| SLA issue statuses | Indicate whether to send issue status update notifications to Slack. |
| Sort order | Provide the sort order for the project in shared views. |
| Priority sort order | Provide the sort order for the project within shared views when ordered by priority. |
| Trashed | Indicate whether the project has been trashed. |
| Priority | Specify the priority of the project. |
| Label IDs | Provide the IDs of the project labels associated with this project. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, if you select **Project** as your object, the following output schema becomes available. Use the **Select fields to retrieve** input field to specify the fields (including nested object fields) to return in the response.

| Output field | Description |
| --- | --- |
| Last sync ID | The ID of the last sync operation. |
| Success | Indicates whether the operation was successful. |

---
