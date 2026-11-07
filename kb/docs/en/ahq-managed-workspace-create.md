---
url: 'https://docs.workato.com/en/ahq-managed-workspace-create.md'
description: >-
  Create a managed workspace in Workato Automation HQ, set its name, and
  allocate billable recipe and task quotas from your organization subscription.
---

# Create a workspace in Automation HQ

[Automation HQ](/en/automation-hq) manages various aspects of its workspaces, including organization-wide settings like consolidated [audit log streaming](/en/features/activity-audit-log) and shared [custom connectors](/en/developing-connectors/sdk). Automation HQ moderators oversee and administer workspaces by setting usage quotas and managing application access within Workato.

Find out more about operating managed workspaces from the [Workspaces](/en/ahq-workspaces), [Workspace moderators](/en/ahq-workspace-moderator), [Shared connectors](/en/ahq-shared-connector), [Usage](/en/ahq-usage), and [Settings](/en/ahq-settings).

1. To create a managed workspace, select **Create Workspace** from the [HQ Workspace](/en/ahq-hq-workspace).
   
   _Create a new workspace_
   
2. The **New Workspace** interface appears.
   
3. In the interface, provide the name of the new managed workspace and the quota for both the number of billable recipes and tasks.
   
   Workato deducts usage quotas from your organization's subscription; you can update them at any time.
   
   <dl><dt>Workspace name</dt><dd>The name of the new managed workspace.</dd><dd>We suggest you choose a name that represents the organizational unit that the workspace serves. This makes it easier for users to find the various workspaces where they participate. For example, for the <strong>Recruiting</strong> department, name the workspace <strong>HR: Recruiting</strong>.</dd><dt>Billable recipe limit</dt><dd>The quota of all billable (active) recipes allocated to the managed workspace.</dd><dd>Workato guides you in choosing the recipe quota, based on your plan. For example, the following illustration states that you have "2.7k unassigned recipes". If you don't plan to set up additional workspaces, you can assign 500 recipes to this workspace. You can adjust the quotas in the future.</dd><dt>Task limit</dt><dd>The task quota for this workspace.</dd><dd>Similarly, Workato advises you of the remaining tasks available in the plan. In the following illustration, you have "23.3m unassigned tasks" remaining. Depending on expected usage, start by assigning 1,000,000 tasks to this workspace. You can adjust the quota in the future.</dd></dl>
   
   _New workspace interface_
   
4. Click **Create workspace**.
   
5. You successfully added a new managed workspace! Now the new managed workspace appears in the list of workspaces.
   

> **FURTHER READING**
> 
> - [Managed workspace](/en/ahq-managed-workspace)
> - [Automation HQ usage](/en/ahq-usage)
> - [Plan overview](/en/ahq-usage#plan-overview)
> - [Task usage](/en/ahq-usage#task-usage)
> - [Recipe usage](/en/ahq-usage#recipe-usage)

---
