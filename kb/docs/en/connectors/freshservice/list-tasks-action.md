---
url: 'https://docs.workato.com/en/connectors/freshservice/list-tasks-action.md'
description: 'Lists the tasks of a ticket in Freshservice based on ticket ID. '
---

# Freshservice - List tasks action

The **List tasks** action lists the tasks of a ticket in Freshservice based on ticket ID.

## Input

| Input field | Description |
| --- | --- |
| Ticket ID | Provide ID of the ticket to which the task is assigned |

## Output

| Output field | Description |
| --- | --- |
| Task ID | Select the ticket ID under which you wish to create a task from the drop-down menu. |
| Agent ID | Provide the title of the task. |
| Status | Select the status of task from the drop-down menu. |
| Due date | Provide the due date of the task. |
| Notify before | Time in seconds before which notification is sent prior to due date. Select the time from the drop-down menu. |
| Title | The title of the task. |
| Description | The description of the task. |
| Created at | The timestamp when the task was created. |
| Updated at | The timestamp when the task was last updated. |
| Closed at | The timestamp when the task was closed. |
| Group ID | The unique ID fo the group the task is assigned to. |
| Deleted | Indicates whether the task has been deleted. |
| Workspace ID | The unique identifier of the workspace where the task belongs. |
| Custom fields | Additional attributes defined for the task. |
| Stack rank | The priority ranking of the task within a list of tasks. |
| Planned start date | Provide planned start date in timestamp format. |
| Planned end date | Provide planned end date in timestamp format. |
| Planned effort | Provide planned efforts in this field. |

---

---
url: >-
  https://docs.workato.com/en/connectors/freshservice/list-ticket-form-fields-action.md
description: 'Returns a list of ticket form fields in Freshservice. '
---

# Freshservice - List ticket form fields action

The **List ticket form fields** action returns a list of ticket form fields in Freshservice.

## Input

This action doesn’t require any input fields.

## Output

| Output field | Description |
| --- | --- |
| Field ID | Unique ID of the field. |
| Label | Display name of the field. |
| Description | Description of the field. |
| Field type | Type of the field. |
| Created at | Timestamp when the field was created. |
| Updated at | Timestamp when the field was last updated. |
| Position | Order in which the field appears. |
| Required for closure | Indicates if the field is mandatory for ticket closure. |
| Name | Internal name of the field. |
| Default field | Indicates whether this is a default system field. |
| Required for agents | Indicates if the field is mandatory for agents. |
| Customers can edit | Specifies if customers can edit the field. |
| Label for customers | Display label for customers. |
| Required for customers | Indicates if the field is mandatory for customers. |
| Displayed to customers | Specifies if the field is visible to customers. |
| Belongs to section | Specifies if the field is part of a section. |
| Choices | List of selectable values (if applicable). |
| Nested fields | Sub-fields associated with this field. |
| Sections | Sections where this field is used. |
| Workspace ID | Unique ID of the workspace the field belongs to. |

---
