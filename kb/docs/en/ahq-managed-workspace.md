---
url: 'https://docs.workato.com/en/ahq-managed-workspace.md'
description: >-
  Learn how managed workspaces in Workato Automation HQ organize recipes and
  assets by department, with independent environments, users, and roles.
---

# Managed workspace

In Workato, we build automations inside workspaces. While projects help to organize the automations by related use cases, workspaces organize recipes and other assets into meaningful groups for every department, level of business, or organization unit.

Each Workspace maintains a level of independence, to reflect the actual business practices for each unit of your organization.

A managed workspace exists within the Automation HQ framework, and represents a department, line of business, or organization unit, where collaborators can build automations.

Managed workspaces have the same attributes, functionality, and enablements as the workspaces that are not directly managed by Automation HQ. Each managed workspace has:

<dl><dt>Lifecycle independence</dt><dd>Workspaces have their own <a href="/en/features/environments.html">set of environments</a> (Lifecycle).</dd><dt>Operational independence</dt><dd>Workspaces automatically get the capabilities, features, shared connectors, and assets within the HQ Workspace. Additionally, they can have their own projects, recipes, connections, properties, and other assets. Each workspace has a dashboard to monitor issues and control usage, and can independently configure notification settings and everything necessary for creating automations and operational management.</dd><dt>Users, roles, and permissions</dt><dd>Invite a <a href="/en/user-accounts-and-teams/team-collaboration">different set of collaborators</a> to each workspace, and assign them to appropriate user roles for each workspace.</dd></dl>

In [Automation HQ](/en/automation-hq), we have a high-level _management view_ of workspaces. Moderators can define quotas for each workspace, set up centralized audit log streaming, control available applications and shared connectors, and so on. However, general workspace operations take place directly inside the workspace itself. See [Workspace](/en/workspace).

To create a workspace in Automation HQ, see [Create Managed Workspace](/en/ahq-managed-workspace-create).

## Workspace sections in Automation HQ

## Operations

View critical information about automation in this workspace.

### Activity report

The activity report provides the following metrics:

<dl><dt id="environment">Environment</dt><dd>Toggle between viewing the metrics for the <strong>Development</strong>, <strong>Test</strong>, and <strong>Production</strong> environments.</dd><dt>Period</dt><dd>Select the dimensions of the graph's horizontal access by choosing between <strong>Last hour</strong>, <strong>Last 24 hours</strong>, <strong>Last 7 days</strong> (default), <strong>Last 30 days</strong>, or specify a <strong>Custom range</strong> using a calendar selector.</dd><dt>KPIs</dt><dd>The key indicators for the workspace include the number of <strong>Recipes</strong>, <strong>Successful jobs</strong>, <strong>Failed jobs</strong>, and <strong>Tasks used</strong> for the specified Environment and Period.</dd><dt>Graph</dt><dd>The stacked bar chart plots both successful and failed <strong>Jobs</strong> for the selected time period, at an appropriate fractional period of time. For example, if the Period is "Last hour", the graph produces a measurement for each 5-minute interval. The chart also specifies the global time zone of these operations.</dd></dl>

### Summary

The summary provides visibility into the number of **Projects**, **On-prem agents**, and **Workbots** in the specified workspace [environment](#environment).

### Connected apps

This report communicates the names of apps connected to the workspace, and the number of connections for each app.

## Usage

View usage in this workspace across time and across all [environments](/en/features/environments).

### Plan usage

The plan usage report incorporates the following metrics:

<dl><dt>Data</dt><dd>The plan reports data either as <strong>Tasks</strong> (default), or as <strong>Recipes</strong>.You can easily toggle between the two options.</dd><dt>Period</dt><dd>Select the dimensions of the graph's horizontal access by choosing between the available time periods.</dd><dt>Environment</dt><dd>By default, the chart shows usage across all environments. You can select to show data from 1 to 3 (all) environments: <strong>Development</strong>, <strong>Test</strong>, and <strong>Production</strong>.</dd><dt>Chart view</dt><dd>A <strong>Cumulative</strong> chart plots usage as stacked areas, by default. Alternatively, you can switch to <strong>Monthly</strong> column views.</dd></dl>

### Summary

The summary for usage includes the following bar indicators:

<dl><dt>Recipes</dt><dd>Count of recipes as a portion of the allowed plan, with the corresponding bar indicator.</dd><dt>Tasks</dt><dd>A percentage of tasks used as a portion of the allowed plan, with the corresponding bar indicator.</dd><dt>Change quotas</dt><dd>Depending on your role and permissions, you may see an option to change quotas. See <a href="#usage-limits">Usage quotas</a>.</dd></dl>

## Collaborators

See who is part of this workspace.

_Collaborators of the workspace_

<dl><dt>Search</dt><dd>You can search for collaborators by <strong>name</strong>, <strong>e-mail address</strong>, or <strong>role</strong>. For example, enter "Admin" if you have to reach an administrator for assistance, and then select the person who appears logged in.</dd><dt>Name</dt><dd>All collaborators in the workspace appear here, with their email addresses. Some carry the "Workato moderator" tag, and some added their photo to their profile.</dd><dt>Latest activity</dt><dd>Latest activity for each collaborator includes their status (<strong>No activity</strong>, <strong>Accepted team invitation</strong>, <strong>Logged in</strong>, and <strong>Logged out</strong>). It also includes the timestamp or relative time period.</dd><dt>Role</dt><dd>Each collaborator has an assigned <strong>Role</strong>; these can be configured.</dd></dl>

## Settings

### Usage quotas

You can allocate your organization's usage, concurrency, and OPA capacity across managed workspaces. Every workspace draws from the same organization-wide pool, so a larger allocation for one workspace leaves less for others. The total you allocate across all workspaces can't exceed what your organization has provisioned. This quotas what you can assign, not what a workspace actually consumes.

Complete the following steps to update a usage quota:

1. Go to **Automation HQ > Workspaces**.
   
2. Select a managed workspace and go to **Settings > Usage quotas**.
   
   ![The Usage quotas page for a managed workspace](/assets/managed-workspace-setting-usage.BAKup_a9.png)_The **Usage quotas** page in a managed workspace's settings_
   
3. Enter a new value in the relevant field.
   
   - Billable recipe limit
     
   - The number of active (billable) recipes allocated to this workspace.
     
   - Task limit
     
   - The number of tasks allocated to this workspace. Actual usage can exceed this allocation.
     
   - Credits limit
     
   - The number of credits allocated to this workspace.
     
   - Additional concurrency limit
     
   - The number of concurrent recipe jobs this workspace can run beyond the default of 1.
     
   - Active OPA quota
     
   - The maximum number of active on-prem agents (OPAs) this workspace can use.
     
4. Click **Save**.
   

### Control Applications

In the **App access** central interface, you can see the apps that your workspace can access; they appear with their proper names and company logos.

Decide what applications the users in the managed workspace can access when you restrict access to an allowed list of applications. Shared custom connectors also appear here.

_App access: Apps you can use in this workspace_

**Changing app access**

To change app access, follow these steps:

1. Navigate to the **Settings** interface for the workspace, and select the **App access** screen.
   
2. Click **Edit**.
   
3. In the **Edit access to apps** modal, select new apps, or deselect currently selected apps.
   
   _Edit access to apps_
   
4. Click **Apply changes**.
   
5. The system confirms the change.
   
6. Notice the change in the display of accessible apps.
   

_App access: new applications_

---
