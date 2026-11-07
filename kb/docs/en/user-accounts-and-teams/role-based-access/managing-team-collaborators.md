---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/managing-team-collaborators.md
description: >-
  Invite, manage, and remove collaborators in a Workato workspace, and assign
  roles and collaborator groups to control project access.
---

# Invite and manage workspace collaborators

You can invite, manage, and delete collaborators within a Workato workspace. Invitations add a collaborator to a workspace. It isn’t possible to invite a collaborator to only a specific project. However, you can invite a collaborator to your workspace with assigned collaborator groups that configure access to specific projects. Collaborators with project access can view the recipes, connections, and folders within those projects depending on the project role you assign and its associated privileges.

> **ACCESS REQUIREMENTS**
> 
> You must have one of the following privileges or roles to invite and manage workspace collaborators:
> 
> - An [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or the legacy [Admin system role](/en/roles#system-roles)
> - A custom environment role with the [**Workspace access** privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#workspace-access)
> 
> Workspaces that haven't migrated to the new access control model may still use the legacy **Admin** system role. After migration, equivalent permissions are granted through the **Environment admin** role or a custom environment role.

## Invite collaborators

Complete the following steps to invite a new collaborator to your workspace:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Click **\+ Invite collaborator**.
   
4. Enter the **Name** and **Email address** of the collaborator.
   
5. Use the **Environment role** drop-down menu to select the [Environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) you plan to assign. If multiple environments are enabled, you must select an environment role for each environment individually.
   
6. Add the collaborator to one or more [Collaborator groups](/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups).
   
7. Click **Invite** to send the invitation.
   

> **INVITATION RATE LIMIT**
> 
> The collaborator may receive an error if you delete and resend an invitation too quickly. This occurs due to system rate limits that block repeated invitations in a short time window.
> 
> You must wait at least **20 minutes** before you resend the invitation to avoid this issue.

Users with an existing Workato account can sign in to accept the invitation. New users are prompted to create an account.

## Update a collaborator's role

You can update a collaborator’s environment role to manage their workspace-level permissions. Project-level access is managed separately within each project's settings.

> **USING ENVIRONMENTS**
> 
> If you plan to use the [Environments feature](/en/features/environments), ensure that you understand how to manage [workspace roles in environments](/en/user-accounts-and-teams/role-based-access/managing-environment-access) before changing a collaborator's role.

Complete the following steps to update an existing collaborator's role:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Click the collaborator you plan to modify. This opens the **Edit collaborator** page.
   
4. Select a new **Environmental role** from the drop-down menu.
   
5. Click **Save changes**.
   

## Manage a collaborator's project access

Project-level roles are managed separately from environment roles and are configured within each project's settings:

> **PROJECT ROLE VISIBILITY**
> 
> Environment admins can assign project roles to themselves or other collaborators, even if they aren’t members of the project yet.
> 
> However, environment admins don't automatically gain access to project content. To view recipes, connections, and folders inside a project, you must first assign yourself a project role. Once assigned, you're automatically added as a project member and gain visibility based on the role’s permissions.

1. Open the project where you plan to manage access.
   
2. Go to **Settings > Project access**.
   
3. Update an existing collaborator's role using the **Project role** drop-down menu next to their name. Their access updates immediately.
   
4. Add a new collaborator by clicking **\+ Add collaborators**. Select the collaborators or groups, choose the appropriate **Project role**, and click **Add** to grant access.
   

## Delete collaborators

You can delete a collaborator from your workspace if someone has left your organization or no longer requires access to Workato.

Deleting a collaborator revokes their access but doesn’t delete any work the collaborator created, such as recipes, connections, or projects.

Complete the following steps to delete a collaborator:

1. Sign in to your Workato account.
   
2. Go to **Workspace admin > Access control > Collaborators**.
   
3. Select the collaborator you plan to remove to open their details page.
   
4. Click the **Delete** icon.
   
5. Review the warning that their work is retained, then click **Delete** to confirm.
