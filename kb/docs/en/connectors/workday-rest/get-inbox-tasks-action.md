---
url: 'https://docs.workato.com/en/connectors/workday-rest/get-inbox-tasks-action.md'
description: >-
  The Get inbox tasks action in the Workday REST connector lets you return the
  most recent inbox task records for the connected user.
---

# Workday REST - Get inbox tasks action

This action returns all the inbox task records for the connected user. Only the first 100 tasks are returned in descending order with the latest inbox task first.

> **INTEGRATION USERS AFFECT OUTPUT**
> 
> If an integration user is used to connect, this action returns inbox tasks assigned to that integration user only.

## Input

This action has no input fields.

## Output

| Output field | Description |
| --- | --- |
| Descriptor | Title of the inbox task. |
| ID | Workday ID of the inbox task. |
| HREF | API resource URL of the inbox task. |
| Subject | Subject object. Contains descriptor and ID. |
| Overall process | Business process object. Contains descriptor and ID. |
| Status | Status object. Contains descriptor and ID. |
| Step type | Step type object. Contains descriptor and ID. |
| Assigned | Date and time of assignment. |
| Due | Due date of this inbox task. |

---

---
url: >-
  https://docs.workato.com/en/connectors/workday-rest/approve-reject-inbox-task-action.md
description: >-
  The Approve/reject inbox task action in the Workday REST connector lets you
  approve or reject an approval-type inbox task by its Workday ID.
---

# Workday REST - Approve/reject inbox task action

Use this action to approve or reject an inbox task. For this action to be successful, the inbox task must have a **Step type** (API name: stepType) descriptor of **Approval**.

![Approve/reject inbox task action](/assets/approve-reject-inbox-task.C0fGNk7U.png)_Approve/reject inbox task action_

## Input

| Input field | Description |
| --- | --- |
| Inbox task ID | Workday ID of the inbox task to approve/reject. |
| Action | Select either **Approve** or **Reject**. |

## Output

| Output field | Description |
| --- | --- |
| Descriptor | Indicates _Approval by Manager_ task. |
| ID | Workday ID of the inbox task. |
| HREF | API resource URL of the inbox task. |

---
