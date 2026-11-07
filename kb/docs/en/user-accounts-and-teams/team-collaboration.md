---
url: 'https://docs.workato.com/en/user-accounts-and-teams/team-collaboration.md'
description: >-
  Manage who can build, edit, and run integrations in a Workato workspace by
  inviting collaborators and assigning roles and access controls.
---

# Workspace collaborators

Workspace collaborators enables you to manage who can build, edit, and manage integrations within a workspace. Workato supports collaborative development while maintaining security, governance, and flexible membership controls.

You can invite collaborators, assign roles, and manage pending invitations from **Workspace admin > Access control**.

This guide covers the following:

- [Collaborator features](#collaborator-features)
- [Manage collaborators](#manage-collaborators)
- [Switch between workspace accounts](#switch-between-workspace-accounts)
- [Leave a workspace](#leave-a-workspace)
- [Track changes made by collaborators](#track-changes-made-by-collaborators)
  - [Recipe versions](#recipe-versions)
  - [Exports/imports](#exports-imports)

## Collaborator features

Workspace collaborators enable teams to develop integrations collaboratively while maintaining security and governance. Admins can use the following features to manage access and control workspace activity:

- [**Role-based access control (RBAC)**](/en/user-accounts-and-teams/role-based-access/): Assign [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles), [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles), and [custom roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles) to control what collaborators can view and manage.
  
- **Support for multiple workspaces**: Use a single account to join multiple workspaces. This setup makes it easier for admins or experts to collaborate across departments and business units.
  
- [**Single Sign-On (SSO)**](/en/user-accounts-and-teams/single-sign-on): Integrate SAML-based SSO with providers like Okta or OneLogin to manage user access centrally. Workato also supports [Just in time provisioning](/en/user-accounts-and-teams/just-in-time-provisioning) for custom roles.
  
- **Track changes with audit trails**: Use [Auto-versioning](#track-changes-made-by-collaborators) to monitor collaborator activity and restore previous versions without losing work.
  
- **Maintain recipe ownership:** Recipes created within a workspace belong to the workspace. Contributions remain intact when collaborators leave or change roles.
  

## Manage collaborators

You can manage workspace collaborators from **Workspace admin** in the side navigation bar. These settings enable you to perform the following actions:

- [Invite and manage collaborators](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators)
- View pending invitations
- [Manage collaborator roles and permissions](/en/user-accounts-and-teams/role-based-access/)
- Configure workspace settings, including [SSO](/en/user-accounts-and-teams/single-sign-on)

> **ACCESS REQUIREMENTS**
> 
> You must have one of the following to manage workspace collaborators:
> 
> - The **Environment admin** role or legacy [Admin](/en/roles#system-roles) collaborator role
> - A custom environment role with the [Workspace admin privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#admin-privileges)

## Switch between workspace accounts

You can use the workspace switcher to view and access other workspaces you belong to:

1. Click the current workspace name to open the workspace switcher.
   
   ![Workspace Switch with Okta](/assets/team-switch.PCml5bld.png)_Open the workspace switcher by clicking on your profile icon on the top left_
   
2. Select a workspace from the drop-down menu to switch to a different workspace.
   

## Leave a workspace

When you leave a workspace, Workato revokes all access to that workspace. You can't switch back to the workspace [with the workspace switcher](#switch-between-workspace-accounts). Any recipes, connections, and assets you contributed remain in the workspace and stay accessible to other collaborators.

Workato also notifies the workspace admin by email when a collaborator leaves.

Complete the following steps to leave a workspace:

1. Sign in to your Workato account.
   
2. Go to your personal account by clicking your user icon and selecting **Profile settings** from the drop-down menu.
   
   ![Go to Profile Settings](/assets/navigate-profile-settings.B6ket8sz.png)_Go to **Profile Settings**_
   
3. Go to **Workspace membership**.
   
4. Click **Leave** next to the workspace you plan to leave.
   

## Track changes made by collaborators

Workato tracks changes made by collaborators to recipes and exports/imports, creating an audit trail. This helps you manage your workspace effectively and confirm that updates follow your organization’s security and governance policies.

### Recipe versions

The **Versions** tab logs all recipe changes and attributes them to the collaborator who made the update. In the new permissions model, restoring previous recipe versions depends on your project role privileges. Collaborators with project roles that grant **Edit** or **Full access** to recipes, such as **Project admin**, **Advanced builder**, or **Builder**, can restore earlier versions.

### Exports/imports

Workato tracks all exports and imports during [recipe lifecycle management](/en/recipe-development-lifecycle). You can review these activities on the export/import history pages for each manifest and import folder.

![Recipe export history](/assets/recipe-export-history.CDp_5581.png)_Recipe export history_

---
