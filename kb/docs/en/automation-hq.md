---
url: 'https://docs.workato.com/en/automation-hq.md'
description: >-
  Automation HQ gives you central control over managed workspaces, so you can
  provision team hierarchies, share assets, and govern usage and quotas.
---

# Automation HQ

[Video](https://www.youtube.com/embed/S3TuAh_JQsI)

As Workato scales within your organization, the number of workspaces grows, and the need for both oversight and more granular control becomes critical. **Automation HQ** provides central control over all your [managed workspaces](/en/ahq-managed-workspace), without diminishing the ability to specialize for the unique business needs modeled by each workspace.

With Automation HQ, you can easily represent your company's business units as workspaces, provision these hierarchies, and maintain a high level of visibility into the operational success of Workato-enabled processes. In the [HQ workspace](/en/ahq-hq-workspace), you have visibility into all managed workspaces to provide guidance and assistance, ensure compliance, share resources, and manage your organization's Workato subscription.

_Automation HQ Architecture_

## Create independent workspaces for teams

With Automation HQ, administrators can create and manage independent workspaces for different teams with unique needs, keeping control over usage and organization-wide rules that apply to each team.

## Share assets

Share custom connectors with teams so that they can use them in their workspaces.

## Control apps and quotas

Control what apps are available in different workspaces, and set tasks and recipe quotas for teams.

## Centralize Audit log streaming

With a central place for all logs in your company, you can easily configure Audit log streaming for the entire organization, and not depend on individual team's effort to set up logs.

## Feature inheritance

All newly created workspaces get all the features of HQ workspace, by default.

## Inheritable roles

AHQ admins can create custom roles and mark them as inheritable. These roles automatically appear in all managed workspaces as non-editable roles. Inheritable roles apply across all managed workspaces without project scope restrictions.

### Create an inheritable environment role

Complete the following steps to create an inheritable environment role:

1. Go to **Workspace admin > Access control > Environment roles**.
   
2. Click **\+ Add environment role**.
   
3. Enable the **Make this role available in all other workspaces as a non-editable role** toggle.
   
   ![Configure an inheritable environment role](/assets/inheritable-roles-environment.CBpCvEcb.png)_Configure an inheritable environment role_
   
4. Configure the role privileges. Inheritable roles automatically receive access to all projects. You can't apply project access rules.
   
5. Click **Save changes**.
   

You can now assign this role to collaborators in any managed workspace. The role appears as non-editable and applies consistently across all workspaces.

### Create an inheritable project role

Complete the following steps to create an inheritable project role:

1. Go to **Workspace admin > Access control > Project roles**.
   
2. Click **\+ Add project role**.
   
3. Enable the **Make this role available in all other workspaces as a non-editable role** toggle.
   
   ![Configure an inheritable project role](/assets/inheritable-roles-project.ChFovoH2.png)_Configure an inheritable project role_
   
4. Configure the role privileges for project-level access.
   
5. Click **Save changes**.
   

You can now assign this role to collaborators in any managed workspace. The role appears as non-editable and applies consistently across all workspaces.

## Automation HQ sections

Automation HQ provides visibility and control over your entire organization.

> **FURTHER READING**
> 
> To explore the various sections of Automation HQ, see these articles:
> 
> - [Automation HQ workspaces](/en/ahq-workspaces)
> - [Automation HQ moderators](/en/ahq-workspace-moderator)
> - [Automation HQ shared connectors](/en/ahq-shared-connector)
> - [Automation HQ usage](/en/ahq-usage)
> - [Automation HQ settings](/en/ahq-settings)

---
