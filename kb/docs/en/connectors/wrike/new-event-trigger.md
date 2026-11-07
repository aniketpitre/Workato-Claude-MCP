---
url: 'https://docs.workato.com/en/connectors/wrike/new-event-trigger.md'
description: >-
  The New event trigger in the Wrike connector monitors changes to tasks,
  folders, projects, attachments, timelogs, and comments in real time.
---

# Wrike - New event trigger (real-time)

The **New event** trigger monitors changes to tasks, folders, projects, attachments, time logs, and comments in Wrike in real-time.

## Input

| Input field | Description |
| --- | --- |
| Events to monitor | Select the events that you plan to monitor. If left blank, all events are monitored. |
| Folder name | Select a folder to monitor for changes. If left blank, all folders are monitored. |
| Monitor nested subfolders, projects & tasks? | Set to **Yes** to monitor nested subfolders, projects, and tasks. Defaults to No. |

## Output

The output fields depend on the event type and Wrike object you plan to monitor. Not all fields return values for every event. Common fields may include the following:

| Output field | Description |
| --- | --- |
| Webhook ID | Unique identifier for the webhook event. |
| Event author ID | ID of the user who triggered the event. |
| Event type | Type of event that triggered the action, such as **Task created** or **Folder created**. |
| Last updated date | Timestamp indicating when the event occurred. |
| Task ID | Unique identifier for the task, if applicable. |
| Old value | Previous value before the update, if applicable. |
| Title | Name of the task, folder, or project. |
| Importance | Priority level of the task. |
| Old status | Previous status of the task or project. |
| Status | Current status of the task or project. |
| Old custom status ID | Previous custom status identifier. |
| Custom status ID | Current custom status identifier. |
| Dates | Task or project start and due dates. |
| Added parent folders | List of folders newly associated with the task or project. |
| Removed parent folders | List of folders removed from the task or project. |
| Added responsibles | Users newly assigned to the task or project. |
| Removed responsibles | Users removed from the task or project. |
| Added shared users | Users granted access to the record. |
| Removed shared users | Users whose access was revoked. |
| Custom field ID | Identifier of the custom field that changed. |
| Value | New value of the updated custom field. |
| Attachment ID | Unique identifier of the added or updated attachment. |
| Comment | Content of the comment added or updated. |
| Comment ID | Unique identifier of the comment. |
| Time tracker ID | Identifier for the time tracking entry. |
| Type | Type of tracked time entry. |
| Hours | Logged hours for the time tracking event. |
| Approval ID | Unique identifier of the approval request. |
| Decision | Approval decision, if applicable. |
| Approver IDs | List of users who reviewed the approval. |
| Folder ID | Unique identifier for the folder, if applicable. |
| Added owner IDs | IDs of users newly assigned as owners. |
| Removed owner IDs | IDs of users removed as owners. |

---
