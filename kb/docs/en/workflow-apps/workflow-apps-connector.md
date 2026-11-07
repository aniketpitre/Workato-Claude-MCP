---
url: 'https://docs.workato.com/en/workflow-apps/workflow-apps-connector.md'
description: >-
  Use the Workflow apps by Workato connector to add user steps to your workflows
  and manipulate app data and the Workflow apps portal.
---

# Workflow apps by Workato connector

Use the **Workflow apps by Workato** connector to add user steps to your workflows and manipulate your application data and the Workflow apps portal.

You can define Workflow stages in [App settings](/en/workflow-apps/builder-experience#app-settings).

![Workflow apps actions](/assets/workflow-apps-actions.RzsZtRM2.png)_Available actions_

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-trigger.md
description: >-
  Configure the New component event trigger to run a recipe when a Run recipe
  action is invoked and return data to a Workflow app component.
---

# New component event trigger

The **New component event** trigger runs when a [Run recipe action](/en/workflow-apps/component-actions/run-recipe) is invoked in the Workflow apps portal. Use this trigger in combination with the **Return data to component** action to send data back to a page component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Output schema | Specify output fields to send data obtained in this recipe back to your Workflow apps page. |

* * *

## Output

| Output field | Description |
| --- | --- |
| Context | The context object contains information about the Workflow apps user using the page, including app-user details and group membership. |
| Workflow apps user | This object is nested within the `Context` object and contains the following available attributes: `User ID`: The ID of the user., `User name`: The user's name., `User email`: The user's email address., `Status`: The user's status., `Groups`: An object nested within the `Workflow apps user` object and contains information about user group membership. |
| Parameters | The parameters object is nested within the `Context` object and contains input parameters defined in the trigger. This object is empty if you haven't defined any input parameters. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-drop-down-trigger.md
description: >-
  Configure the New component event (drop-down) trigger to populate Workflow app
  drop-down components with data from a third-party app.
---

# New component event (drop-down) trigger

The **New component event (drop-down)** real-time trigger runs when a drop-down component is opened in a Workflow app. This trigger enables you to populate drop-down components with data from a third-party app. Use this trigger in combination with the **Return data to component** action to send data back to a drop-down component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Use recipe to find search results? | Select `Yes` and use the Search Query datapill in the recipe to enable typeahead search in drop-down components. Select `No` if the drop-down contains fewer than 1,000 options and all records can be retrieved at once. |
| Minimum search characters to trigger the recipe | Specify the minimum number of characters to trigger the recipe. The default value is `3`. Alternatively, enter `0` to trigger recipe immediately when the drop-down opens without requiring user input. |

## Output

| Output field | Description |
| --- | --- |
| Context | This object contains information about the Workflow apps user accessing the page, including app-user details and group membership. |
| Workflow apps user (Context) | An object nested within the `Context` object containing information about the user who accesses the application. |
| User ID (Workflow apps user) | The user's unique identifier. |
| User name (Workflow apps user) | The user's name. |
| User email (Workflow apps user) | The user's email address. |
| Status(Workflow apps user) | The user's status, such as `active` or `inactive`. |
| Groups (Workflow apps user) | An object nested within the `Workflow apps user` object containing information about the user's group membership. |
| Parameters | Contains input parameters defined in the trigger. This object is empty if you haven't defined any input parameters. |
| Search query | The search term used in the drop-down component on the Workflow apps page. Map this datapill into other actions if you are using the recipe to find search results. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-component-event-table-trigger.md
description: >-
  Configure the New component event (Table widget) trigger to send data back to
  a table component when a Workflow app page loads.
---

# New component event (Table widget) trigger

The **New component event (Table widget)** trigger runs when a page is loaded in a Workflow app. Use this trigger in combination with the **Return data to component** action to send data back to a table component in a Workflow app.

## Input

| Input field | Description |
| --- | --- |
| Input parameters | Use input parameters to receive data from the Workflow apps page for use in your recipe. For example, you can use page data to search for relevant records in a third-party app. |
| Table schema | Enter fields to define the table's schema. |

## Output

| Output field | Description |
| --- | --- |
| Context | This object contains information about the Workflow apps user accessing the page, including app-user details and group membership. |
| Workflow apps user (Context) | An object nested within the `Context` object containing information about the user who accesses the application. |
| User ID (Workflow apps user) | The user's unique identifier. |
| User name (Workflow apps user) | The user's name. |
| User email (Workflow apps user) | The user's email address. |
| Status(Workflow apps user) | The user's status, such as `active` or `inactive`. |
| Groups (Workflow apps user) | An object nested within the `Workflow apps user` object containing information about the user's group membership. |
| Parameters | Contains input parameters defined in the trigger. This object is empty if you haven't defined any input parameters. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-request-trigger.md
description: >-
  Configure the New request trigger to run a recipe in real time when a new
  request is created in a Workflow app or its data table.
---

# New request trigger

The **New request** (real-time) trigger runs when there is a new request in a Workflow app.

This trigger also runs when a user creates a new record manually in a workflow app's corresponding [data table](/en/data-tables).

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose a Workflow app to check for new requests. |
| When first started this recipe should pick up events from | Get new requests since a particular date/time. Leave empty to get new requests since one hour ago. Once the recipe has been run or tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

You can also toggle **Set trigger condition** to only process trigger events matching conditions you specify.

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Change ID | The ID number that corresponds to the Workflow app's corresponding data table. |
| Request | This JSON object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Created by (Request) | A nested JSON object within the Request object. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested JSON object within the Created by object. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested JSON object within the Request object. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/new-updated-request-trigger.md
description: >-
  Configure the New/updated request trigger to run a recipe when a Workflow app
  request, task, or data table record is created or updated.
---

# New/updated request trigger

This real-time trigger runs when there is a New/updated request in a Workflow app.

It also runs when the following events occur:

- When a new task in a Workflow app is created.
- When a user completes a task or a task expires.
- When a task is reassigned from one app user to another app user.
- When a user creates/updates a record manually in a Workflow app's corresponding [data table](/en/data-tables).

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose a Workflow app to check for new requests. |
| When first started this recipe should pick up events from | Get new requests since a particular date/time. Leave empty to get new requests since one hour ago. Once the recipe has been run or tested, you cannot change this value. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |

You can also toggle **Set trigger condition** to only process trigger events matching conditions you specify.

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

### Request object

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |
| Change ID | The ID number that corresponds to the Workflow app's corresponding data table. |

### Old request object

| Output field | Description |
| --- | --- |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's data table. |
| Assigned task (Old request) | A nested object within the `Old request` object. Empty if no active task is associated with the request. |
| Task ID (Assigned task) | Task ID of the assigned task. |
| Task name (Assigned task) | Name of the assigned task. |
| Status (Assigned task) | Status of the assigned task. |
| Due date (Assigned task) | Due date of the assigned task. |
| Task URL (Assigned task) | URL of the assigned task. |
| Assigned user (Assigned task) | A nested object within the `Assigned task` object. Empty if task is assigned to a group. |
| User ID (Assigned user) | User ID of the assigned user. |
| User name (Assigned user) | Name of the assigned user. |
| Email (Assigned user) | Email of the assigned user. |
| Status (Assigned user) | Status of the assigned user. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/change-workflow-stage-action.md
description: >-
  Configure the Change workflow stage action to transition a request through
  stages in a Workflow app, such as marking it Done or Invalid.
---

# Change workflow stage action

**Change workflow stage** is an action you can use to transition a request in a Workflow app through the workflow.

Typical use cases for this action include the following scenarios:

- If the input provided does not pass validation, mark the request as **Invalid**.
- If the request does not need user approval, mark it as **Done** automatically.
- If the manager approval task is approved, mark the request as **Completed**.

* * *

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select an App from the list of available Apps. |
| Record ID | The ID of the record whose workflow stage you plan to change. You can map this in using a datapill from a trigger or action from the Workato Data Tables or Workflow apps connector. |
| Workflow stage | The new workflow stage for the record. Select one of the stages defined in your [application settings](/en/workflow-apps/interface#pages-assign). |

## Output

There is no output for this action.

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/create-request-action.md
description: >-
  Configure the Create request action to create a new request in a Workflow app,
  with input fields based on the app and its data table.
---

# Create request action

Use this action to create a request in a Workflow app.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to create a new request. |
| New request fields | Fill in the fields for the new request. The available fields are determined by the Workflow app you select. |

### Additional input fields

Additional input fields are variable. They are determined by the Workflow app you select and the columns present in its corresponding data table.

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |

---

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

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/complete-workflow-task-programmatically-action.md
description: >-
  Configure the Complete workflow task programmatically action to approve,
  reject, or complete a Workflow app task with an optional status label.
---

# Complete workflow task programmatically

Use this action to complete a workflow task programmatically. For example, you can use it to perform a workflow task in a different UI (including Workbot for Slack or Microsoft Teams), or to close a task that is no longer valid.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to complete a task. |
| Record ID | Choose a request (identified by its **Record ID**) to update. Use a datapill or enter the exact ID. Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Task status | Complete a task by approving, rejecting, or completing it. |
| Custom status label | _Optional_. Provide a custom task status label to customize what users see when a task is approved, rejected, or completed in the portal. For example, you can use a custom task status such as `sent for rework` to accompany a `rejected` status. This communicates clearly the reason the request was rejected and enables you to configure conditional logic to customize how your workflow handles requests assigned custom task status labels. When left empty, the label appears the same as the task status. |
| Email address | _Optional_. Provide the email address of the assignee you plan to complete the task. If this field is left empty, Workato defaults to the currently assigned user. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

### Completed task object

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

### Request object

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/delete-request-action.md
description: >-
  Configure the Delete request action to remove a request from a Workflow app by
  its record ID using the Workflow apps connector.
---

# Delete request

Delete a request from a Workflow app.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to delete a request. |
| Record ID | The ID of the record you plan to delete. You can map this in using a datapill from a trigger or action from the Workflow apps connector. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Success | Whether the record is deleted successfully. Available values include `True` or `False`. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/get-activity-history-action.md
description: >-
  Configure the Get activity history (batch) action to retrieve a full audit
  trail of request creation, task assignments, status updates, and comments.
---

# Get activity history (batch) action

Use the **Get activity history (batch)** action to retrieve a complete activity history for requests, including creation, task assignments, status updates, and user comments. This provides a full audit trail to track all activities related to the requests.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose the workflow app you plan to get activity history for. |
| Record ID | Specify the request to get activity history for. Use a datapill or enter the exact ID. |
| Activity type | Choose activity types to search for. |
| Performed by | Enter an email address of a specific user to show only activities performed by a specific user. |
| Activities from | Retrieve activities that occurred on or after this date. |
| Activities to | Retrieve activities that occurred on or before this date. |
| Sort direction | Select the order in which activities are retrieved. Default is oldest to newest. |
| Next page token | Get activity records starting from this offset. |

## Output

| Output field | Description |
| --- | --- |
| Activity records | This object contains details about the activities requested. |
| Activity ID (Activity records) | A unique identifier for the activity performed. |
| Request record ID (Activity records) | The ID of the request record associated with the activity. |
| Activity type (Activity records) | The type or category of the activity (for example, comment or status change). |
| Comment text (Activity records) | The content of a comment, if the activity involved one. |
| Activity summary (Activity records) | A brief description of what the activity entailed. |
| Performed at (Activity records) | The date and time when the activity was executed. |
| List size (Activity records) | The total number of items in the list (if part of a paginated response). |
| List index (Activity records) | The position of the current item within the list. |
| Performed by (Activity records) | An object nested within the `Activity records` object containing details about the user who performed the activity. |
| User ID (Performed by) | The user's ID. |
| Email (Performed by) | The user's email address. |
| Status (Performed by) | The user's status. |
| List size | The size of the list. |
| List index | The position in the list. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/get-user-data-action.md
description: >-
  Configure the Get user data (batch) action to retrieve user details from the
  Workflow apps portal by email, user group, and sort options.
---

# Get user data action (batch)

Get user data from the Workflow apps portal.

## Input

| Input field | Description |
| --- | --- |
| Email address | Provide the user email to retrieve the user data. |
| User groups | Select user groups from the list to retrieve user data for all users in each group. |
| Sort by | Specify how to sort the results. Available options include `Name`, `Email`, and `Status`. |
| Sort direction | Determine whether to sort the results in `Ascending` or `Descending` order. |
| Entries per page | Limit the number of users returned in this action. The default value is 500 and the maximum value is 500. |
| Next page token | Get users starting with the given offset. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Users | An object containing information about the user. |
| User ID (Users) | The ID of the user. |
| User name (Users) | The user's name. |
| User email (Users) | The user's email address. |
| Status (Users) | The user's status. |
| Groups (Users) | An object nested within the `Users` object. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Continuation token | The token used to paginate through entries. |
| Entries per page | The number of entries per page. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/invite-user-action.md
description: >-
  Configure the Invite user action to send an email invitation to the Workflow
  apps portal and add the user to one or more user groups.
---

# Invite user

Invite a user by email to the Workflow apps portal. The user must accept the invitation before using the portal.

## Input

| Input field | Description |
| --- | --- |
| Name | The name of the user you plan to invite to the portal. |
| Email address | Provide the email address to send the invite to. |
| User groups | Add the user to one or more user groups. If left blank, the user is added to the **Everyone** group by default. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Users | An object containing information about the user. |
| User ID (Users) | The ID of the user. |
| User name (Users) | The user's name. |
| User email (Users) | The user's email address. |
| Status (Users) | The user's status. |
| Groups (Users) | An object nested within the `Users` object. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Continuation token | The token used to paginate through entries. |
| Entries per page | The number of entries per page. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/return-data-component-action.md
description: >-
  Configure the Return data to component action to send data back to a Workflow
  app component, paired with a New component event trigger.
---

# Return data to component action

Use the **Return data to component** action to return data back to a component in a Workflow app. This action must be used in combination with the **New component event**, **New component event (Table widget)**, or **New component event (drop-down)** trigger. The recipe job stops immediately after this action.

## Input

| Input field | Description |
| --- | --- |
| Consider action as successful? | Use the **Consider action as successful?** drop-down to determine whether the action was completed successfully. |
| Output | Map in recipe datapills to return data to a page component. The fields in this section are dynamic and determined by the **Output schema** defined in the trigger. |
| Successful toast message | Optional. Provide a successful toast message to display to end-users if the action completes successfully. If left blank, no toast message is displayed to users. |
| Error message | Optional. Provide a custom error message to display to end-users if the action fails. If left blank, no error message is displayed to users. |

## Output

| Output field | Description |
| --- | --- |
| Successful toast message | The message that displays to end-users when the action completes successfully. |
| Error message | The message that displays to end-users when the action fails. |
| Output | The data returned to the Workflow app component. This object is dynamic and the output depends on the datapills mapped into the action input. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/remove-user-action.md
description: >-
  Configure the Remove user action to remove a user from the Workflow apps
  portal by email using the Workflow apps connector.
---

# Remove user action

Remove a user from the Workflow apps portal. Refer to the [App-user and group management](/en/workflow-apps/app-user-groups) guide to manage app-users in the UI.

## Input

| Input field | Description |
| --- | --- |
| User email | Provide the email of the user you plan to remove from the Workflow apps portal. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Success | Whether the user is deleted successfully. Available values include `True` or `False`. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/search-requests-action.md
description: >-
  Configure the Workflow apps connector search requests action to find requests
  matching filters, sort criteria, and result quotas.
---

# Search requests action

Search requests in a Workflow app matching criteria you specify.

## Input

| Input Field | Description |
| --- | --- |
| Workflow app | Select the Workflow app from which you plan to retrieve lists. |
| Filters | Add one or more filters to the query. All filters must contain `Column name`, `Operand`, and `Value`. All filters are chained using `AND`. |
| Column name | Available column names depend on the Workflow app you select and the columns available in its corresponding data table. |
| Operand | Available operands depend on the Workflow app and column types. Operands by data type include: Short text Equals, Is not equal to, Is null, Is not null ; Long text Equals, Is not equal to, Is null, Is not null ; Integer Equals, Is not equal to, Is less than, Is greater than, Is less or equals, Is greater or equals, Is null, Is not null ; Decimal Equals, Is not equal to, Is less than, Is greater than, Is less or equals, Is greater or equals, Is null, Is not null ; Boolean Is true, Is false, Is null, Is not null ; Date Equals, Is not equal to, Is before, Is after, Is on or before, Is on or after, Is null, Is not null ; DateTime Equals, Is not equal to, Is before, Is after, Is on or before, Is on or after, Is null, Is not null |
| Value | The value you enter must match the data type of the column and the operand you select. |
| Sort by | Organize search results by `Column name`. Options depend on the Workflow app and its data table. |
| Sort direction | Order search results in `Ascending` or `Descending` order. |
| Limit | Determine how many records to fetch. The default is 100 and the maximum is 200 records. |
| Next page token | Get records starting from the specified offset. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |
| Next page token | Get records starting from the specified offset. |
| List size | Size of the list. |
| List index | Index of the list. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/share-request-action.md
description: >-
  Use the Share request action to share a request from a Workflow app with a
  user or user group.
---

# Share request action

Use the **Share request** action to share a request from a Workflow app with a user or user group. You can use this action to:

- Share the request with approvers. This enablers approvers to see the request after approval. Requests disappear from an approver's view after approval by default if you don't share the request.
- Share the request with a group of observers who need to monitor certain requests without participating in the approval workflow.
- Add participants to the request for communication purposes. Participants can leave comments and stay informed about request progress.

Users with whom you share the request have the same view as the requester. Users can see the request, access the **View details** page, and leave comments when you share a request. Sharing a request doesn't allow users to make decisions to tasks that aren't assigned to them.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Choose the Workflow app to share the request from. |
| Record ID | Choose a request to share with one or more additional participants. You can map in a datapill or enter the exact ID of a request. |
| Share to | Specify the user group or individual user to share the request with. You can select a user group from the list, provide a user group ID, or enter a user's email address. You can share a request with a maximum of 20 users or user groups. |

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Shared with (Record) | A nested object within the `Record` object containing information about the user group or user the request is shared with. |
| ID (Shared with) | The ID of the user group who the request is shared with. |
| Name (Shared with) | The name of the user or user group who the request is shared with. |
| Email (Shared with) | The email address of the user who the request is shared with, if applicable. Emails don't display for user groups. |
| Type (Shared with) | Indicates whether the request was shared with a user or user group. |
| Record | This object represents a record in a Workflow app. |
| Record ID (Record) | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Application (Record) | This object represents a Workflow app. It contains columns from a request and approval app's primary data table. The exact output varies based on the columns present in your app's data table. |
| Created by (Record) | A nested object within the `Record` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Created by) (Groups) | The ID of the group this task is assigned to. |
| Group name (Created by) (Groups) | The name of the group this task is assigned to. |
| List size (Created by) (Groups) | The size of the list. |
| List index (Created by) (Groups) | The list index. |
| Guest user (Created by) | Indicates whether the request was submitted by an anonymous user. |
| Stage (Created by) | A nested object within the `Request` object containing stage details. |
| Stage ID (Created by) (Stage) | The ID of the group this task is assigned to. |
| Stage name (Created by) (Stage) | The name of the stage this task is assigned to. |
| Created at (Record) | The date the record was created. |
| Updated at (Record) | The date the record was most recently updated. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/update-request-action.md
description: >-
  Configure the Workflow apps connector update request action to change request
  fields, workflow stage, and assignee by record ID.
---

# Update request action

Update a request in a Workflow app. You must specify the values of all request fields you plan to update.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select a Workflow app in which to update the request. |
| Record ID | Choose a request (identified by its `Record ID`) to update. Use a datapill or enter the exact ID. Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. Workato requires the Record ID to perform certain Workflow apps connector actions, including update record and delete record actions. |
| Workflow stage | Use the **Choose a value** drop-down to update the request's workflow stage to update. If left empty, the stage will remain unchanged. |
| Assignee | Use the **Choose a value** drop-down to assign the task to a user group. |
| Update request fields for the specified request | Fill in the fields for the specified request. You must fill in the fields you plan to update. Fields that are not specified are not updated. The fields that appear here depend on the request you plan to update. |

* * *

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Request | This object represents a record in a Workflow app. It includes metadata and links to related objects. |
| Record ID | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Active task (Request) | A nested object within the `Request` object. Empty if there is not an active task associated with the request. |
| Task ID (Active task) | The ID of the task. |
| Task name (Active task) | The name of the task. |
| Status (Active task) | The task's status. |
| Due date (Active task) | The due date of the task. |
| Task URL (Active task) | The URL for the task. |
| Assigned user (Active task) | A nested object within the `Active task` object containing information about the task assignee. Empty if the task is assigned to a group. |
| User ID (Assigned user) | The ID of the user assigned to the task. |
| User name (Assigned user) | The name of the user assigned to the task. |
| Email (Assigned user) | The email of the user assigned to the task. |
| Status (Assigned user) | The status of the user assigned to the task. |
| Assigned group (Active task) | A nested object within the `Active task` object containing information about the assigned group. Empty if the task is assigned to an individual user. |
| User ID (Assigned group) | The ID of the user assigned to the task. |
| User name (Assigned group) | The name of the user assigned to the task. |
| Email (Assigned group) | The email of the user assigned to the task. |
| Status (Assigned group) | The status of the user assigned to the task. |
| Created by (Request) | A nested object within the `Request` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Groups) | The ID of the group this task is assigned to. |
| Group name (Groups) | The name of the group this task is assigned to. |
| List size (Groups) | The size of the list. |
| List index (Groups) | The list index. |
| Stage (Request) | A nested object within the `Request` object containing stage details. |
| Stage ID (Stage) | The ID of the group this task is assigned to. |
| Group name (Stage) | The name of the group this task is assigned to. |
| Created at | The date the record was created. |
| Updated at | The date the record was most recently updated. |

---

---
url: >-
  https://docs.workato.com/en/workflow-apps/workflow-apps-connector/unshare-request-action.md
description: >-
  Use the Unshare request action to remove a user's or user group's access to a
  request in a Workflow app.
---

# Unshare request action

Use the **Unshare request** action to remove a user's or user group's access to a request in a Workflow app. This reverses access granted through the [Share request action](/en/workflow-apps/workflow-apps-connector/share-request-action).

This action succeeds even if the request wasn't shared with a user or user group. For example, if you share a request with a user who doesn't have access to the Workflow apps portal, the action succeeds, but the user isn't provisioned access to the request.

## Input

| Input field | Description |
| --- | --- |
| Workflow app | Select the Workflow app that contains the request. |
| Record ID | Select the request to unshare. You can map in a datapill or enter the request ID. |
| Unshare from | Specify the user group or individual user to remove access from. You can select a user group from the list, provide a user group ID, or enter a user's email address. |

## Output

Output is dynamic and may vary depending on the actions and triggers in your recipe, as well as the columns present in your Workflow app's corresponding [data table](/en/data-tables).

To use this data in downstream steps, map in the relevant [datapill](/en/recipes/data-pills-and-mapping#datapills) from the datatree.

| Output field | Description |
| --- | --- |
| Shared with (Record) | A nested object within the `Record` object containing information about users or user groups who still have access to the request. Returns an empty list if the request isn't shared with anyone. |
| ID (Shared with) | The ID of the user group who still has access to the request. |
| Name (Shared with) | The name of the user or user group who still has access to the request. |
| Email (Shared with) | The email address of the user who still has access to the request, if applicable. Emails don't display for user groups. |
| Type (Shared with) | Indicates whether the request is shared with a user or user group. |
| Record | This object represents a record in a Workflow app. |
| Record ID (Record) | Workato automatically generates a unique ID for each record in a Workflow app's corresponding data table. |
| Application (Record) | This object represents a Workflow app. It contains columns from a request and approval app's primary data table. The exact output varies based on the columns present in your app's data table. |
| Created by (Record) | A nested object within the `Record` object containing information about the user who created the request. |
| User ID (Created by) | The ID of the user who created the request. |
| User name (Created by) | The name of the user who created the request. |
| Email (Created by) | The email of the user who created the request. |
| Status (Created by) | The status of the user. |
| Groups (Created by) | A nested object within the `Created by` object containing information on group membership. |
| Group ID (Created by) (Groups) | The ID of the group this task is assigned to. |
| Group name (Created by) (Groups) | The name of the group this task is assigned to. |
| List size (Created by) (Groups) | The size of the list. |
| List index (Created by) (Groups) | The list index. |
| Guest user (Created by) | Indicates whether the request was submitted by an anonymous user. |
| Stage (Created by) | A nested object within the `Request` object containing stage details. |
| Stage ID (Created by) (Stage) | The ID of the group this task is assigned to. |
| Stage name (Created by) (Stage) | The name of the stage this task is assigned to. |
| Created at (Record) | The date the record was created. |
| Updated at (Record) | The date the record was most recently updated. |

---
