---
url: 'https://docs.workato.com/en/connectors/linear/create-record-action.md'
description: The Create record action enables you to create a new record in Linear.
---

# Linear - Create record action

The **Create record** action enables you to create a new record in Linear.

## Input

| Input field | Description |
| --- | --- |
| Object | Specify the object to create a new record for. Fields load dynamically based on the object you select. |

For example, if you select **Issue** as your object, the following input schema becomes available:

| Input field | Description |
| --- | --- |
| Select fields to retrieve | Select all fields (including the nested object fields) to return in the response. |
| ID | Provide the ID in UUID v4 format. If none is provided, the backend generates one. |
| Title | Provide the title of the issue. |
| Description | Provide the issue description in Markdown format. |
| Description data | Provide the issue description as a Prosemirror document. |
| Assignee ID | Provide the user ID to assign to the issue. |
| Parent ID | Provide the ID of the parent issue. |
| Priority | Specify the priority of the issue. |
| Estimate | Provide the estimated complexity of the issue. |
| Subscriber IDs | Provide the IDs of the users subscribing to this ticket. |
| Label IDs | Provide the IDs of the issue labels associated with this ticket. |
| Team ID | Provide the team ID associated with the issue. |
| Cycle ID | Provide the cycle ID that is related to the issue. |
| Project ID | Provide the project ID that is related to the issue. |
| Project milestone ID | Provide the project milestone that is associated with the issue. |
| Last applied template ID | Provide the ID of the previous template applied to the issue. |
| State ID | Provide the state ID of the issue. |
| Reference comment ID | Provide the comment that the issue is referencing. |
| Source comment ID | Provide a source comment ID on where the issue was created. |
| Source pull request comment ID | Provide the pull request comment ID for the issue that was created. |
| Sort order | Provide the position that the issue is related to other issues. |
| Priority sort order | Provide the position of the issue relative to other issues when ordered by priority. |
| Sub issue sort order | Provide the position of the issue in the parent's sub-issue list. |
| Due date | Provide the date by which the issue is due. |
| Create as user | Provider user name. |
| Display icon URL | Provide the external user avatar URL. |
| Preserve sort order on create | Indicate whether the passed sort order should be preserved. |
| Created at | Provide the date when the issue was created. |
| SLA breaches at | Provide the timestamp at which an issue will be considered in breach of the SLA. |
| SLA started at | Provide the timestamp at which the issue's SLA was started. |
| Template ID | Provide the ID of the template the issue should be created. |
| Completed at | Provide the date when the issue was completed. |
| SLA type | Provide the SLA day count type for the issue. |

## Output

The output fields are determined by the object selected in the input. Map the relevant datapill from the datatree to subsequent steps.

For example, if you select **Project** as your object, the following output schema becomes available. Use the **Select fields to retrieve** input field to specify the fields (including nested object fields) to return in the response.

| Output field | Description |
| --- | --- |
| Last sync ID | The ID of the last sync operation. |
| Success | Indicates whether the operation was successful. |

---
