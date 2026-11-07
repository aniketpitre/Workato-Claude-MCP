---
url: 'https://docs.workato.com/en/workflow-apps/component-actions/complete-task.md'
description: >-
  Configure a Complete task action on button click in a Workflow app to resume a
  paused recipe job and complete a workflow request.
---

# Complete task action

Specific page components enable you to complete tasks in a workflow request in the Workflow apps portal.

> **RECIPE ACTION PAIRING**
> 
> Pair this component action with the [Assign task to users](/en/workflow-apps/workflow-apps-connector/assign-task-to-users-action) recipe action. When an assignee clicks a button configured with **Complete task**, the paused recipe job resumes.

## Compatible components

| Component | Trigger event |
| --- | --- |
| Button | Button click |

## Configure a Complete task action

Complete the following steps to configure a **Complete task** action on button click:

1. Select a **Button** component.
   
2. Go to the **Action** panel. The **Trigger** event, `Button is clicked` is pre-selected.
   
3. Use the **Action** drop-down to select `Complete task`.
   
4. Use the **Task status** drop-down to select a status to assign to the task. Available actions include `Approved`, `Completed`, and `Rejected`.
   
5. Optional. Enter a custom label in the **Custom status label** field to customize what users see when a task is completed in the portal.
   
6. Optional. Use **Additional data for table columns** to save extra data to the table row alongside the submitted page fields. Click **\+ Add column**, then map a page variable or static value to a data table column.
   
7. Use the **Redirect to** drop-down menu to choose where to redirect the user after the task is complete.
   
8. Click **Save**.
   

> **LIMITATIONS**
> 
> The **Column** drop-down menu for **Additional data for table columns** only lists compatible data table columns. You can't map the same column more than once. If a mapped page variable has no value when the user submits, the column saves as empty and doesn't block submission. Static values must match the target column's data type, or the mapping shows a validation error.

Your configuration should look as follows:

![Complete task](/assets/complete-task.BfIPf3Mw.png)_Complete task on button click_

---
