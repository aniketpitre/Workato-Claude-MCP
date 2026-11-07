---
url: 'https://docs.workato.com/en/workflow.md'
description: >-
  Learn how the People Task feature added human approval steps within recipes.
  This deprecated feature is replaced by Workato Workflow apps.
---

# People Task (Workflow)

The people task feature enables the addition of human approval steps within the recipe. Complex tasks requiring human judgment can be directed to an approver, then subsequently redirected based on whether the task was approved or rejected.

> **PEOPLE TASK DEPRECATION NOTICE**
> 
> Workato plans to deprecate the People Task feature in our recipes, as its functionalities now exist in [Workflow apps](/en/workflow-apps).
> 
> Deprecation follows this timeline:
> 
> - People Task is no longer available in the recipe editor.
> - Full deprecation for People Task is planned for **August 28, 2025**. On this date, existing recipes with People Task actions will stop functioning.
> 
> Workato recommends that you migrate to [Workflow apps](/en/workflow-apps), which offers a platform with enhanced capabilities for creating integrated workflow applications. Workflow apps aren't included in all pricing models, and may require changes to your plan.

## Using People Task as an admin

### People Task setup

People Task feature is enabled only for certain users. Reach out to your Customer Success Manager to learn more.

For Workato accounts with People Task feature enabled, admins are able to view the People Task option in their **Tools** page. Select **All Tools** and then click **People Task**.

![People Task option](/assets/people-task-nav.DmQpPKLC.png)_People Task tool_

#### Customize People Task subdomain

If accessing People Task for the first time, the People Task account needs to be configured. Provide a unique subdomain and customize the site for People Task approvers.

The following portrays the configuration for Workato Demo Inc. in the **People Task** setup screen. This configuration can be changed after the initial setup.

![People Task configuration screen](/assets/peopletask-config.BRi1bCGK.gif)_Configure and customize People Task site_

#### Adding People Task participants

Task requesters and approvers should be added as People Task participants. Provide their names, emails, and optionally provide an avatar for them.

![Add People Task participant](/assets/add-participant.QEHromOK.gif)_Adding a new People Task participant_

## People Task example scenario

### Recipe

The following recipe triggers on new hires in BambooHR and sends a People Task approval task from John in HR to Jill the payroll manager. An email notification should be sent to Jill to inform her about the new task pending her approval.

![People Task recipe](/assets/peopletask_bamboo_recipe.D-_I0PuB.png)_Recipe that uses People Task to approve and add sensitive data about new hires_

If the task was approved, the recipe proceeds to stage the new hire's details for uploading into ADP. If the task does not get approved, however, the recipe would stop with an error to flag this particular job for troubleshooting - as all new hires should get recorded in ADP.

### People Task step configuration

In the People Task step, there are several fields to take note of:

![People Task fields 1](/assets/peopletask_fields1.CxoAhKO_.png)![People Task fields 2](/assets/peopletask_fields2.uafYeQyQ.png)_People Task action fields configuration_

Fields:

- **Task title**

Title of the task, as viewed from the summary list of tasks.

- **Task document**

Presented as a table of relevant data for the approver in deciding whether or approve or reject the task.

- **Requester**

Select the user sending the task from a list of users.

- **Approver**

Select the user approving the task from a list of users.

- **Decision by**

Select the number of days the approver has to make a decision.

- **Requester comments**

Optional notes from the requester to the approver.

- **User data fields**

Optionally used when the requester wishes the approver to provide additional data. Fields to collect should be defined in the following format.

```
[
  {"control_type": "ssn","label": "SSN","name": "SSN","type": "string","hint": "nnn-nn-nnn"},
  {"control_type": "text","label": "Birth date","name": "birth_date","type": "date_time","format": "MM-DD-YYYY","hint": "MM-DD-YYYY"},
  {"control_type": "select","label": "Gender","name": "gender","type": "string","pick_list": [["Male","M"],["Female","F"]]}
]
```

### People Task step preview

From the approver's view, these fields will show up in the task as follows.

![Pending People Task](/assets/pending-peopletask.B_lA-49T.png)_Preview of how People Task requests display to approvers_

### Using People Task as an approver

#### Approver view

The approver has to log in to the People Task portal to view the tasks pending their approval.

![People Task login screen](/assets/peopletask-login.BzyyJwgX.png)_Customized People Task login page for People Task requesters and approvers_

Once logged in, the approver has access to the list of pending and completed tasks.

![Approver view](/assets/approver-view.CuW7jQgy.png)_List of requests that approver must review and approve/disapprove_

#### Approving tasks

As the approver, review the document sent and provide any data requested by filling in the fields. Required fields would be marked as such. All tasks will provide the approver with the option of adding an **Approver note**.

Subsequently, approve, or reject the task. The recipe will resume the job to carry out further recipe steps. Once a task has been approved or rejected, it can be found within the **Completed** tab.

![Approved People Task](/assets/approved-peopletask.lv_7JGIy.png)_Approved/Rejected request moves to Completed tab_

---
