---
url: 'https://docs.workato.com/en/connectors/wrike/new-updated-task-trigger.md'
description: >-
  The New/updated task trigger in the Wrike connector monitors tasks that are
  created or updated in a selected folder in Wrike.
---

# Wrike - New/updated task trigger

The **New/updated task** trigger monitors tasks created or updated in Wrike.

## Input

| Input field | Description |
| --- | --- |
| Folder name | Select a folder to retrieve tasks from. |
| Custom statuses | Return tasks that match any selected custom statuses. |
| Task status | Retrieve only new or updated tasks with the selected status. |
| When first started, this recipe picks up events from | Select the start date and time to retrieve trigger events. If left blank, the trigger retrieves tasks created or updated one hour ago. You can't change this value after you run or test the recipe. |
| Fields to retrieve | Select additional fields to include in the output. If left blank, the trigger retrieves all custom fields and the following default fields: `recurrent`, `description`, `briefDescription`, `parentIds`, `superParentIds`, `sharedIds`, `responsibleIds`, `authorIds`, `hasAttachments`, `attachmentCount`, `superTaskIds`, `subTaskIds`, `dependencyIds`, `metadata`, and `customItemTypeId`. If **None** is selected, no additional fields are retrieved. |
| Convert to plaintext | Select **Yes** to convert the task description to plain text. Defaults to **No**. |

## Output

| Output field | Description |
| --- | --- |
| Task ID | Unique identifier for the task. |
| Account ID | Unique identifier for the Wrike account associated with the task. |
| Title | Name of the task. |
| Description | Task description, if applicable. |
| Brief description | Shortened version of the task description. |
| Parent folder | Folder that directly contains this task. |
| Super parent folder | Highest-level parent folder(s) in the hierarchy. |
| List of users who share task | Users who have access to the task. |
| Assignees | Users assigned to the task. |
| Status | Current status of the task. |
| Importance | Priority level of the task. |
| Created date | Timestamp indicating when the task was created. |
| Updated date | Timestamp indicating when the task was last updated. |
| Completed date | Timestamp indicating when the task was marked as completed. |
| Dates | Task start and due dates. |
| Scope | Access scope of the task. |
| Author | User who created the task. |
| Custom Status ID | Identifier for the custom status. |
| Custom status | Current custom status of the task, if applicable. |
| Has attachments | Indicates whether the task contains attachments. |
| Attachment count | Number of attachments in the task. |
| Permalink | Direct URL to the task in Wrike. |
| Priority | Priority level of the task, if applicable. |
| Super task | Identifier of the parent task, if applicable. |
| Subtask | List of sub-tasks associated with this task. |
| Dependency | List of tasks that depend on this task. |
| Metadata | Additional metadata associated with the task. |
| Custom item type ID | Identifier for the custom item type. |
| Custom fields | List of custom field values assigned to the task. |

---
