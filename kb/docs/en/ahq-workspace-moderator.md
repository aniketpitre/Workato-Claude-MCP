---
url: 'https://docs.workato.com/en/ahq-workspace-moderator.md'
description: >-
  Learn how workspace moderators in Automation HQ administer managed workspaces,
  support collaborators, and use environment and project roles.
---

# Workspace moderators

A workspace moderator is a member of your HQ workspace with permissions to administer and manage workspaces. Moderators guide and support collaborators, manage memberships, adjust usage and billing quotas, and monitor workspace activity and system health.

Workspace admins must assign both an [environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) and a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) when adding a moderator. These roles define the moderator's access:

- Environment roles control access across all environments in managed workspaces.
- Project roles control access within all projects in managed workspaces.

> **LEGACY ROLES**
> 
> In workspaces that still use the legacy permissions model, existing moderators may display legacy roles (**Admin**, **Analyst**, **Operator**). However, when you add new moderators, you must assign environment and project roles instead.

HQ admins can also create [inheritable roles](/en/automation-hq#inheritable-roles) that automatically appear in all managed workspaces. Admins can assign these roles to moderators when needed.

If someone appears in a workspace both as a collaborator and as a workspace moderator, their assigned environment and project roles as a collaborator take precedence over the moderator's roles. You can use this behavior to fine-tune permissions in specific workspaces.

> **ADDING COLLABORATORS**
> 
> You can only add collaborators in the HQ workspace as workspace moderators. Learn how to [add collaborators to your workspace](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators).

The **Workspace moderators** interface displays each moderator's name and email address, their assigned **Environment role** and **Project role**, and the **Workspaces** they can access.

![Workspace moderators table](/assets/workspace-moderator-table.B2-_l97V.png)_Workspace moderators_

> **FURTHER READING**
> 
> To explore the various sections of Automation HQ, see these articles:
> 
> - [Assign a workspace moderator](/en/ahq-workspace-moderator-assign)
> - [Edit or remove a workspace moderator](/en/ahq-workspace-moderator-edit)
> - [Environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin)
> - [Project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles)
> - [Privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference)

---
