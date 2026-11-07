---
url: >-
  https://docs.workato.com/en/connectors/bim360/new-or-updated-issue-v2-in-a-project-trigger.md
description: >-
  The new or updated issue (V2) in a project trigger monitors a BIM 360 project
  folder you specify for newly created or updated issues.
---

# BIM 360 - New or updated issue (V2) in a project trigger

The **New or updated issue (V2) in a project** trigger monitors a BIM 360 project folder you specify for newly created or updated issues.

## Input

| Input fields | Description |
| --- | --- |
| Hub name | Select the hub that contains the project you plan to monitor. |
| Project name | Select the project you plan to monitor. |
| When first started, this recipe should pick up events from | Set the date and time to start capturing trigger events. This enables your recipe to capture past events. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

## Output

| Output fields | Description |
| --- | --- |
| Hub ID | The BIM 360 ID of the hub that contains the issue. |
| Project ID | The BIM 360 ID of the project that contains the issue. |
| ID | The BIM 360 ID of the issue. |
| Container ID | The BIM 360 ID of the container that contains the issue. |
| Display ID | A chronological and user-friendly ID for the issue. |
| Title | The issue's title. |
| Description | The issue's description. |
| Snapshot URN | The unique resource name (URN) for the snapshot associated with the issue. |
| Issue type ID | The BIM 360 ID of the issue type. |
| Issue subtype ID | The BIM 360 ID of the issue subtype. |
| Assigned to | The BIM 360 ID of the user, company, or role associated with the issue's current assignee. |
| Due date | The issue's due date. |
| Location ID | The issue's location breakdown structure (LBS) ID. |
| Location details | The issue's location in plain text. |
| Owner ID | The BIM 360 ID of the issue's owner. |
| Root cause ID | The BIM 360 ID of the issue's root cause type. |
| Issue template ID | The BIM 360 ID of the template used to create the issue. |
| Comment count | The number of comments on the issue. |
| Attachment count | The number of attachments on the issue. |
| Opened by | The BIM 360 ID of the user who opened the issue. |
| Opened at | A timestamp indicating when the issue was opened. |
| Closed by | The BIM 360 ID of the user who closed the issue. |
| Closed at | A timestamp indicating when the issue was closed. |
| Created by | The BIM 360 ID of the user who created the issue. |
| Created at | A timestamp indicating when the issue was created. |
| Updated by | The BIM 360 ID of the user who last updated the issue. |
| Updated at | A timestamp indicating when the issue was last updated. |
| Client created at | A timestamp indicating when the issue was created in the client's system. |
| Client updated at | A timestamp indicating when the issue was last updated in the client's system. |
| Status | The issue's current status, such as `draft`, `open`, or `closed`. |
| Assigned to type | Specifies whether `Assigned to` is a user, company, or role. |
| Permitted statuses | The statuses permitted for the issue. |
| Permitted attributes | The attributes permitted for the issue. |
| Permitted actions | The actions permitted for the issue. |
| Linked documents | Contains information about documents related to the issue, such as their `Type`, `Details`, and `Created at` date. |
| Official response | Contains information about the response to the issue, such as its `Responded at` date and `Response`. |
| Custom attributes | Contains information about the issue's custom attributes, such as their `Type`, `Title`, and `Attribute definition ID` . |
| Links | Contains information about the issue's associated links, such as their `Type` and `Data`. |
