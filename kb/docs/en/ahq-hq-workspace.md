---
url: 'https://docs.workato.com/en/ahq-hq-workspace.md'
description: >-
  The Automation HQ Workspace lets you manage quotas, settings, moderators, and
  monitor automations across all managed workspaces in your Workato account.
---

# HQ Workspace

You can access the Automation HQ features in the [HQ Workspace](https://app.workato.com/organization_console). The HQ Workspace enables you to manage quotas, update settings, and monitor automations across all Workspaces in your account.

## Workspaces

Get an overview of all managed workspaces in your organization at a glance. See key metrics like the number of billable recipes, task usage in the current accounting period, number of collaborators, and connected applications.

_Managed workspaces in HQ workspace_

> **FURTHER READING**
> 
> To use the **Workspaces** section of Automation HQ, see these articles:
> 
> - [Workspaces in Automation HQ](/en/ahq-workspaces)
> - [Create a workspace](/en/ahq-managed-workspace-create)
> - [Managed workspaces](/en/ahq-managed-workspace)

## Workspace moderators

To help your teams set up the managed workspaces, assign workspace moderators. Workspace moderators have access to all workspaces in your organization.

Only members in the HQ workspace can be assigned as workspace moderators.

![Workspace moderators table](/assets/workspace-moderator-table.B2-_l97V.png)_Workspace moderators_

> **FURTHER READING**
> 
> To use the **Workspace moderators** section of Automation HQ, see these articles:
> 
> - [Workspace moderators](/en/ahq-workspace-moderator)
> - [Assign a workspace moderator](/en/ahq-workspace-moderator-assign)

## Shared connectors

Build and maintain [custom connectors](/en/developing-connectors/sdk) using the Workato SDK and distribute them to the managed workspaces. Ensure that all your workspaces are using the latest version of your custom connectors.

_Shared connectors_

> **FURTHER READING**
> 
> To use the **Shared connectors** section of Automation HQ, see these articles:
> 
> - [Shared connectors](/en/ahq-shared-connector)
> - [Share a connector](/en/ahq-shared-connector-share)
> - [Version a connector](/en/ahq-shared-connector-version)
> - [Stop sharing a connector](/en/ahq-shared-connector-stop-sharing)

## Usage

Workspaces share a pooled task quota, allowing you to allocate tasks across managed workspaces and adjust as needs change.

The **Usage** section provides an overview of consumption and plan details across all workspaces. Key components include the following:

- Plan overview
  
- A consolidated report that displays plan details, total tasks used, percentage of task usage, and plan renewal date.
  
- Task usage
  
- Displays task consumption across workspaces.
  
- Recipe usage
  
- Displays recipe activity and usage data across workspaces.
  

![Workspace usage](/assets/automation-hq-workspace-usage.CbV9BwiG.png)_Workspace usage_

> **FURTHER READING**
> 
> To use the **Usage** section of Automation HQ, see these articles:
> 
> - [Automation HQ usage](/en/ahq-usage)
> - [Plan overview](/en/ahq-usage#plan-overview)
> - [Task usage](/en/ahq-usage#task-usage)
> - [Recipe usage](/en/ahq-usage#recipe-usage)

## Settings

You can set up organization-wide Audit log streaming in the [Settings](/en/ahq-settings) interface. After setup, all logs from the [HQ Workspace](#hq-workspace) and all managed workspaces stream to a single destination.

Audit log streaming is off by default. To set it up, see [Audit log streaming for Automation HQ](/en/ahq-audit-log-streaming).

_Workspace settings_

## Cross-workspace grants

You can enable [cross-workspace grants](/en/cross-share-streams) for the entire organization from the [Settings](/en/ahq-hq-workspace#settings) interface. Source workspaces can grant other managed workspaces access to their Event streams topics when enabled.

Cross-workspace grants are off by default. Refer to [Enable cross-workspace grants](/en/cross-share-streams#enable-cross-workspace-grants) to set it up.

> **FURTHER READING**
> 
> To use the **Settings** section of Automation HQ, see these articles:
> 
> - [Automation HQ Settings](/en/ahq-settings)
> - [Audit log streaming](/en/ahq-audit-log-streaming)
> - [Cross-workspace grants](/en/cross-share-streams)

---
