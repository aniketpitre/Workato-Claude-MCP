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
