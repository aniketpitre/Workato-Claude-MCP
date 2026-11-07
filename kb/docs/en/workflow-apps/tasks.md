---
url: 'https://docs.workato.com/en/workflow-apps/tasks.md'
description: >-
  Learn how app-users view, filter, work on, reassign, and apply custom status
  labels to tasks in the Workflow apps portal.
---

# Manage tasks

The Workflow apps portal enables users to view, filter, manage, and engage with their tasks efficiently. The [Application page](/en/workflow-apps/application-page) displays all requests that are visible to the app-user. Managers of the application can see all requests. Members can only see the requests that they've created or the ones they are assigned to.

## Work on tasks

If an app-user is assigned a task (directly or through a group to which they belong), the task displays in their inbox and clicking the task opens the task page. App-users can also access a request by clicking the **Go to task** button in the details panel.

The builder of the application configures the page and typically allows app-users to move the request through the workflow (approve, reject, and complete) and/or modify the data.

![Process requests](/assets/image13.BWAn9kmB.png)_Process requests_

## Reassign tasks

Managers and assignees can reassign the request to another user by clicking the **Reassign** link in the right panel.

![Reassign task](/assets/image25.Dl8NtlPB.png)_Reassign task_

Additionally, Workflow apps builders can determine whether task assignees have the ability to reassign tasks by configuring the [Assign tasks to users](/en/workflow-apps/workflow-apps-connector/assign-task-to-users-action#input) action to allow assignees to reassign tasks. Managers can reassign tasks regardless of whether this setting is enabled.

## Custom task status labels

Workflow apps support custom task status labels, which enable app users to provide more information on why a task was approved, rejected, or completed. For example, you can use a custom task status label `sent for rework` to accompany a `rejected` status. This clearly communicates the reason the request was rejected and indicates that a revision is required. When left empty, the label is the same as the task status.

![Custom task status label in portal](/assets/portal-custom-status-label.E1Wve_DC.png)_The custom task status label `sent for rework` is reflected in the portal_

When configured, the custom task status label is reflected in the **Activities** section of the task details panel on the request page and on specific request pages. Custom task status labels are also visible in your recipes in the **Complete workflow task programmatically** action.

You can configure a custom task status label using one of the following methods:

- In the page editor, by pairing a [button component](/en/workflow-apps/page-components#button) with the [Complete workflow task programmatically](/en/workflow-apps/workflow-apps-connector/complete-workflow-task-programmatically-action#input) action and setting a custom status label.
  
- Programmatically in your recipe using the [Complete workflow task programmatically](/en/workflow-apps/workflow-apps-connector/complete-workflow-task-programmatically-action#input) or [assign task to users](/en/workflow-apps/workflow-apps-connector/assign-task-to-users-action) actions. You can also use conditional logic to customize how your workflow handles requests with custom task status labels.

---
