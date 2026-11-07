---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/assign-task-to-users-action.md
description: >-
  Reference for the Workflow apps Assign task to users action, covering input
  fields, output objects, and task assignment behavior.
---

# Assign task to users action

The **Assign task to users** action creates and assigns a workflow task to a user or group. It pauses the recipe job until the task reaches completion or expires. This action enables workflows that require user intervention, such as reviews, approvals, and rejections. Workato creates the task using the configured **Task name**, **Assignee**, and **Record ID**.

When the recipe reaches this step, Workato creates the task and sends an email notification to the assignee(s) if the **Send email notification to assignee** parameter is enabled. App-users can access the task through the email link, the [Workflow apps portal homepage](/en/workflow-apps/portal-homepage), or the **Go to task** option on the [application page](/en/workflow-apps/application-page). Assignees can complete the task in the portal or use the [Complete workflow task programmatically](/en/workflow-apps/workflow-apps-connector/complete-workflow-task-programmatically-action) action. Tasks not completed within the specified timeframe expire, and the recipe resumes with the task marked as **Expired**.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose the workflow app where Workato assigns the task. |
| Record ID | Specify the request to create the user task for. Use a datapill or enter the exact ID. |
| Workflow stage | Choose the workflow stage to switch to while the task is active. Select one of the stages defined in your [application settings](/en/workflow-apps/interface#pages-assign) or leave this field blank to keep the current stage. |
| Task name | Provide a description for the task. This name appears in email subject lines and helps users identify the task. Use datapills to personalize it. |
| Assignee | Assign the task to a user or user group. Assignees can access the task and receive an email if the **Send email notification to assignee** parameter is enabled. |
| Page | Select or create a page for assignees to complete the task. The page must include a button configured with the [Complete task](/en/workflow-apps/component-actions/complete-task) component action. |
| Number of days to complete task | Specify the timeframe for task completion by either selecting from the list or entering a custom value. The maximum allowed value is 365 days. Tasks expire automatically if not completed within this timeframe. |
| Send email notification to assignee | Choose whether to notify the assignee through email. This field defaults to **Yes**. |
| Allow assignee to reassign task | Choose whether assignees can reassign the task. Managers can still reassign tasks even if this option is disabled. |
| Allow user who completes the task to access the request after the task is complete | Use the drop-down menu to select `Yes` or `No`. When yes, the user who completes the task has persistent access to the request, even after it's completed. |

> **REQUIRED CONFIGURATION**
> 
> The selected page must include a button configured with the [Complete task](/en/workflow-apps/component-actions/complete-task) component action. Without it, Workato can't register task completion and the recipe job stays paused until the task expires.

## Output

The output from the **Assign task to users** action includes two main objects. The **Task** object provides consistent details about the task created by the action, such as its ID, name, status, custom status label, and timestamps. The **Record** object dynamically reflects data from the Workflow app’s corresponding [data table](/en/data-tables). Attributes in the **Record** object vary depending on the Workflow app configuration and its data table.

### Task object

| Output field | Description |
| --- | --- |
| Task ID | Workato automatically generates a unique ID for each task in a `Task` object. |
| Task name | The name of the task. |
| Status | The task's status. Available values include: `Approved`, `Rejected` and `Expired`. |
| Custom status label | The custom status label applied to the task. |
| Is approved | Whether the task was completed with `Approved` status. |
| Is rejected | Whether the task was completed with `Rejected` status. |
| Is expired | Whether the task was completed with `Expired` status. |
| Created at | The date the task was created. |
| Completed at | The date the task was completed. |
| Completed by (Task) | A nested object within the `Task` object describing the user that completed the task. Empty if the task is expired. |
| User ID (Completed by) | The user's ID. |
| Task name (Completed by) | Name of the task. |
| Email (Completed by) | The user's email address. |

### Record object

| Output field | Description |
| --- | --- |
| Record ID | A unique identifier for the record. |
| Created by (Record) | An object nested within the `Record` object containing details about the user who created the record. |
| User ID (Created by) | The unique identifier for the user. |
| User name (Created by) | The name of the user. |
| Email (Created by) | The user's email address. |
| Status (Created by) | The current status of the user. |
| Groups (Created by) | A nested object containing the details about the groups the user is assigned to. |
| Guest user (Created by) | Whether the user is an anonymous user. |
| Stage | A nested object containing details on the current stage or status in the workflow. |
| Stage ID (Stage) | The unique identifier for the stage. |
| Stage name (Stage) | The name of the stage. |
| Created at | The date and time when the record was created. |
| Updated at | The date and time when the record was last updated. |
