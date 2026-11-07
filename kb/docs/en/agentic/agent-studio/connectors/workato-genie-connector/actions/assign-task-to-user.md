---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-user.md
description: >-
  Assign a task to a user and wait for them to complete it before the recipe
  continues.
---

# Workato Genie connector - Assign task to user action

The **Assign task to user** action assigns a task to a user. The assignee receives a prompt in the genie's chat interface to approve or reject the request. The recipe waits until the task is completed or expires before proceeding to the next step.

This action is used as part of Business approval workflows. Refer to the [Business Approvals](/en/agentic/agent-studio/business-approvals) page for full setup steps and conditional outcome logic.

> **PREREQUISITE**
> 
> Users must be added to [Workato Identity](/en/workato-identity) before you can assign tasks to them. Refer to [Add an end user manually](/en/workato-identity/add-end-user-manually) for steps to add users individually.

## Input

| Input field | Description |
| --- | --- |
| Genie | Select the genie to process the task. |
| Request data table | Select the data table to store the approval request data. |
| Request ID | Enter or specify the ID of the approval request to create a user task for. Use the Request ID datapill from the [Create approval request](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/create-approval-request) action or enter the value directly. |
| Task name | Enter a name describing what the assignee needs to do. Use datapills to personalize the message. |
| Assignee | Specify the email address of the user to assign the task to. The user must exist in [Workato Identity](/en/workato-identity). |
| Time to complete task | Select the length of time the task is valid before it expires. The maximum value is 30 days. |
| Call ID | Enter the Call ID datapill from the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger. Links the user task back to the originating skill call. |
| Requester conversation ID | Enter the Conversation ID datapill from the [Start workflow](/en/agentic/agent-studio/connectors/workato-skill-connector/start-workflow) trigger. Enables the genie to deliver the approver's decision to the correct conversation. |
| Created by | Specify the user ID of the user who initiated the request. The user must exist in [Workato Identity](/en/workato-identity). |

## Output

| Output field | Description |
| --- | --- |
| Task | The completed task object. |
| Task ID (Task) | The unique ID of the task. |
| Task name (Task) | The name of the task as configured in the action. |
| Status (Task) | The current status of the task. |
| Is Approved (Task) | Indicates whether the task was approved. |
| Is Rejected (Task) | Indicates whether the task was rejected. |
| Is Expired (Task) | Indicates whether the task expired before completion. |
| Created at (Task) | The timestamp when the task was created. |
| Completed at (Task) | The timestamp when the task was completed. |
| Reason (Task) | The reason provided by the assignee when completing the task. |
| Completed by (Task) | The user who completed the task. |
| User ID (Completed by) | The Workato user ID of the user who completed the task. |
| User name (Completed by) | The name of the user who completed the task. |
| Email (Completed by) | The email address of the user who completed the task. |
