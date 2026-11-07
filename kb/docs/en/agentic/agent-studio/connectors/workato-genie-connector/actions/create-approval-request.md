---
url: >-
  https://docs.workato.com/en/agentic/agent-studio/connectors/workato-genie-connector/actions/create-approval-request.md
description: >-
  Create an approval request record in a data table as the first step of a
  Business approvals workflow.
---

# Workato Genie connector - Create approval request action

The **Create approval request** action creates a new approval request record in a data table you specify. The request information is shared with the user assigned to the approval task in the subsequent [Assign task to user](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-user) action.

This action is used as part of [Business approvals](/en/agentic/agent-studio/business-approvals) workflows. Refer to that page for full setup steps and conditional outcome logic.

## Input

| Input field | Description |
| --- | --- |
| Request data table | Select the data table to store the approval request. |
| Created by | Specify the user ID of the user who initiated the request. The user must exist in [Workato Identity](/en/workato-identity). |
| Record fields | Enter values for any additional columns in the selected data table. |

## Output

| Output field | Description |
| --- | --- |
| Request ID | The ID of the created approval request. Pass the Request ID datapill to the [Assign task to user](/en/agentic/agent-studio/connectors/workato-genie-connector/actions/assign-task-to-user) action. |
| Creator ID | The user ID of the user who created the request. |
| Parameters | The request data stored in the data table. Available fields depend on how your data table is configured. |
| Record ID | The ID of the record created in the data table. |
| Created at | The timestamp when the request was created. |
| Updated at | The timestamp when the request was last updated. |
