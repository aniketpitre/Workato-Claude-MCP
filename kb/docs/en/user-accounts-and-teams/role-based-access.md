---
url: 'https://docs.workato.com/en/user-accounts-and-teams/role-based-access.md'
description: >-
  Manage who can access your Workato workspace, environments, and projects using
  role-based access control across both permissions models.
---

# Manage your workspace collaborators with role-based access control

Role-based access control (RBAC) in Workato enables you to manage who can access what across your workspace, environments, and projects. Your available roles depend on which [permissions model](#understand-permissions-models) your workspace uses.

> **PERMISSION REQUIREMENTS**
> 
> You must meet one of the following requirements to perform the tasks in this guide:
> 
> - Sign in using the workspace root login
> - Have the **Environment admin** system role or legacy [Admin system role](/en/roles#system-roles)
> - Have a custom role with [Workspace access privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#workspace-access)

## Understand permissions models

Workato supports two permissions models. The features and role types you see depend on which model is enabled in your workspace.

- [New permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2): Manage access using environment roles, project roles, and collaborator groups. This is the default for all workspaces.
- [Legacy permissions model](/en/roles): Uses workspace-level roles only and doesn't support collaborator groups or project-level permissions.

> **DEPRECATION NOTICE**
> 
> The legacy permissions model will be deprecated at the end of August 2026. Workato recommends that you migrate to the new permissions model before this date. Refer to the [Migrate to the new access control model](/en/user-accounts-and-teams/role-based-access/migrate-roles) guide for step-by-step instructions.

## How role-based access control works

RBAC secures your organization's data by assigning roles that define what collaborators can view, create, and manage. In the new permissions model, you control access at the environment and project level:

- [Environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles): Manage access to an entire environment and define what collaborators can do within it.
- [Project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles): Control access inside individual projects, including recipes, assets, folders, and connections.
- [Custom roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles): Define granular privileges within environments or projects to match your organization's needs.

> **LEGACY SYSTEM ROLES**
> 
> In workspaces using the legacy permissions model, [legacy system roles](/en/roles) such as **Admin** and **Operator** remain visible but aren't used in the new permissions model. If your workspace has migrated, manage access using [environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) and [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) instead.

## Add environment or project roles

You must create environment roles or project roles instead of collaborator roles for the permissions model. These roles let you define granular privileges and control access across environments and projects.

> **FEATURE AVAILABILITY**
> 
> The custom collaborator role feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.

> **LEGACY ROLES**
> 
> Custom roles remain visible in the **Collaborator roles** tab even if your workspace has the permissions model enabled, but you haven't migrated your custom roles. However, you can't create new collaborator roles. Workato prompts you to migrate to the new permissions model to manage access using environment and project roles instead.

### Add an environment role

Complete the following steps to add an environment role:

1. Go to **Workspace admin > Access control > Environment roles**.
   
2. Click **\+ Add environment role**.
   
   ![Add an environment role](/assets/add-env-role.De7kone4.png)_Add an environment role_
   
3. Click **Edit** (pencil icon) next to **New environment role** to name the environment role, and click **✓ Save** to confirm your changes.
   
   ![Name environment role](/assets/name-env-role.Cicxri1l.png)_Name environment role_
   
4. Assign privileges to the role from the available options. Refer to the [Environment privileges reference](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#environment-privileges) for more details about each privilege.
   
   > **ASSIGNING PRIVILEGES**
   > 
   > Consider the following when you assign privileges:
   > 
   > - Some privileges require dependencies. For example, the **Edit File Storage** permission requires **View File Storage**.
   >   
   > - When a privilege has dependencies, they appear when you hover over the privilege. Selecting or deselecting them adjusts the related permissions automatically.
   >   
   > 
   > ![Additional role access to features](/assets/interdependent-privileges.CNoJCY3E.gif)_Autoselecting interdependent privileges_
   
5. Click **Save changes** when finished.
   

### Add a project role

Complete the following steps to add a project role:

1. Go to **Workspace admin > Access control > Project roles**.
   
2. Click **\+ Add project role**.
   
   ![Add project role](/assets/add-proj-role.CQp2OurZ.png)_Add a project role_
   
3. Click **Edit** (pencil icon) next to **New project role** to name the collaborator role, and click **✓ Save** to confirm your changes.
   
   ![Name collaborator role](/assets/name-proj-role.DnAoj7p7.png)_Name project role_
   
4. Assign privileges to the role from the available options. Refer to the [Project privileges reference](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-privileges) for more details about each privilege.
   
   > **ASSIGNING PRIVILEGES**
   > 
   > Consider the following when you assign privileges:
   > 
   > - New project roles include default permissions. By default, new project roles have **View** privileges for recipes, Genies and folders. Clear these privileges if they aren't required.
   >   
   > - Some privileges require dependencies. For example, **View folders** is required to view recipes and connections stored in those folders.
   >   
   > 
   > ![Additional role access to features](/assets/interdependent-privileges.CNoJCY3E.gif)_Autoselecting interdependent privileges_
   > 
   > Hovering over a privilege displays its requirements, and related permissions adjust automatically.
   
5. Click **Save changes** when finished.
   

## Assign roles to team collaborators

You can assign roles to collaborators when you [invite them to the workspace](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators#inviting-collaborators). You can also [update roles at any time](/en/user-accounts-and-teams/role-based-access/managing-team-collaborators#changing-a-collaborator-s-role).

Watch a quick video overview

[Video](https://www.youtube.com/embed/Z7gema4ml_s?rel=0&rel=0)

## Clone roles

Cloning a role creates a copy you can modify without affecting the original.

> **CLONE ROLES PROGRAMMATICALLY**
> 
> You can clone roles programmatically through the [Workato API](/en/workato-api/roles).

### Clone an environment role

Complete the following steps to clone an environment role in Workato:

1. Go to **Workspace admin > Access control > Environment roles** in your Workato account.
   
2. Click the environment role you plan to clone. This opens the **Edit environment role** page.
   
3. Click **Clone role**.
   
   ![Clone role](/assets/clone-role.CZkGxQJn.png)_Clone role_
   
4. Rename and modify the copy of the role as needed.
   
5. Click **Save changes**.
   

### Clone a project role

Complete the following steps to clone a project role in Workato:

1. Go to **Workspace admin > Access control > Project roles** in your Workato account.
   
2. Click the project role you plan to clone. This opens the **Edit project role** page.
   
3. Click **Clone role**.
   
   ![Clone role](/assets/clone-role.CZkGxQJn.png)_Clone role_
   
4. Rename and modify the copy of the role as needed.
   
5. Click **Save changes**.
   

## Delete roles

We recommend that you reassign collaborators to new roles before you delete a role to prevent access issues.

> **SYSTEM ROLES CAN'T BE DELETED**
> 
> You can't delete [system environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) or [system project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles).

Access changes based on the role type when you delete a role:

- **Environment roles**: Deleting an environment role revokes a collaborator's access to that specific environment. For example, a collaborator has access to **DEV** and **TEST** environments. In **DEV**, they're assigned the **HR - Dev** role, and in **TEST**, the **Tester** role. If you delete the **HR - Dev** role, the collaborator loses access to the **DEV** environment until you assign them a new environment role. Their access to **TEST** remains unaffected.
  
- **Project roles**: Deleting a project role revokes a collaborator's access to projects with that role assigned to them. Other projects remain unaffected as long as the collaborator has roles assigned there.
  

Complete the following steps to delete a role:

**Delete an environment role**

1. Go to **Workspace admin > Access control > Environment roles**.
   
2. Click the environment role you plan to delete. This opens the **Edit environment role** page.
   
3. Click the **Delete** button.
   
   ![Delete environment role](/assets/delete-env-role.C5DN4t2u.png)_Delete environment role_
   

**Delete a project role**

1. Go to **Workspace admin > Access control > Project roles**.
   
2. Click the project role you plan to delete. This opens the **Edit project role** page.
   
3. Click the **Delete** button.
   
   ![Delete project role](/assets/delete-proj-role.B1HYRb3Z.png)_Delete project role_

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/access-control-v2.md
description: >-
  Learn how the Workato role-based access control model uses environment roles,
  project roles, custom roles, and collaborator groups.
---

# Manage workspace collaborators with the new role-based access control model

The Workato role-based access control (RBAC) system separates environment-level and project-level permissions. This model replaces legacy system roles (Admin, Analyst, Operator) with flexible role assignments that define access precisely and scale with your team's needs.

Environment roles manage high-level privileges across environments, while project roles control access and actions within specific projects. You can also define custom roles and use collaborator groups to grant project access to multiple users at once.

> **LEGACY ROLES**
> 
> The new permissions model is generally available and is the default for all workspaces. Older workspaces that still use legacy system roles (**Admin**, **Analyst**, **Operator**) can continue using them until they migrate. Legacy collaborator roles will be deprecated at the end of August 2026.
> 
> We recommend that you migrate to environment roles and project roles to take full advantage of this new access control. You can migrate manually, using the built-in wizard, or at scale using APIs, depending on the number of custom roles in your workspace.
> 
> Refer to the [Migrate to the new access control model](/en/user-accounts-and-teams/role-based-access/migrate-roles) guide for step-by-step instructions to upgrade before the deprecation deadline.

## Prerequisites

Ensure the following before you enable the new permissions model:

- The home assets (root) folder must be empty. If your workspace still contains assets in the home assets folder, you must migrate them into a project. Refer to the [Home assets project](https://docs.workato.com/en/projects.html#home-assets) documentation for more information.

> **MIGRATION SUPPORT**
> 
> Workato provides automatic migration that performs the following:
> 
> - Converts home assets into a standard project in each environment.
> - Retains the same `folder_id` and `project_id`.
> - Prevents users from adding new assets to the root folder.

## How the model works

Collaborators can hold one environment role per environment and one or more project roles per project. Environment roles don't grant access to project content, and project roles don't grant access to environment settings.

You can assign roles based on a collaborator's responsibilities. For example, you can allow an IT admin to manage security settings in all environments without viewing project content, or allow a developer to build recipes in one project without accessing other teams' work.

You can control privileges using the following:

- [System environment roles](#environment-roles): Predefined roles with environment-wide privileges
- [System project roles](#project-roles): Predefined roles with project-level privileges
- [Custom roles](#custom-roles): Tailored privilege sets for specific needs
- [Collaborator groups](#collaborator-groups): Collections of collaborators that share the same project roles

## Collaborators

Collaborators are individual workspace users. You can invite them, assign environment roles, and manage their project access from **Workspace admin**.

Go to the **Collaborators** tab to view a summary of each user's environment roles. These roles define their access level in each environment.

![Collaborator view](/assets/collaborator-view.aFXYkIOr.png)_Collaborator view_

### Invite a collaborator

Complete the following steps to invite a collaborator and assign environment roles:

1. Go to **Workspace admin > Access control > Collaborators**.
   
2. Click **\+ Invite collaborator**.
   
   ![Invite collaborator](/assets/collaborator-view.aFXYkIOr.png)_Invite collaborator_
   
3. Enter the collaborator's **Name**.
   
   ![Invite collaborator](/assets/enter-collaborator-name.LWrbmqRk.png)_Enter the collaborator's name_
   
4. Enter the collaborator's **Email address**.
   
5. Assign an [Environment role](#environment-roles) for each environment. If the workspace has only one environment, assign a role to the default environment.
   
6. Optional. Add the collaborator to one or more **Collaborator groups**.
   
7. Click **Send invitation**.
   

### Manage collaborator details

Click a collaborator's name to open their details page. You can update their environment roles and view project-level access from this page.

The **Environment access** section displays the collaborator's assigned role for each environment. The **Project access** section lists the projects the collaborator can access in each environment, along with their assigned [project roles](#project-roles).

![Manage collaborator details](/assets/manage-collaborator-details.Dc1NuDDM.png)_Manage collaborator details_

You can also update the collaborator's **Collaborator groups**. Changes to group memberships take effect immediately.

![Manage collaborator group access](/assets/collaborator-group-manage.BbNUyV48.png)_Manage collaborator group access_

## Key roles

Workato's role-based access control system includes the following role types:

- [**Environment roles**](#environment-roles) define permissions to manage projects, configure environment settings, and control access across environments.
- [**Project roles**](#project-roles) define permissions to build, deploy, and manage content within specific projects.

Assign roles based on a user's responsibilities within an environment or project. For example, an IT admin can manage security settings across all environments without accessing project content, while a developer can build recipes in one project without viewing other teams' work in another project.

You can use [custom roles](#custom-roles) to define more granular permissions based on your organization's needs. Use [collaborator groups](#collaborator-groups) to scale access control as teams grow.

## Environment roles

An environment role defines a collaborator's permissions in a specific environment. Workato provides the following system-defined environment roles:

- **Environment admin**: Full control over workspace-wide and environment settings.
- **Environment manager**: Full control over environment settings, but no workspace-wide permissions.
- **Member**: View-only access to environment settings.

You can [assign different roles](#assign-environment-roles-to-users) to a user in different environments based on their responsibilities.

Environment roles don't grant access to project content. Collaborators, including environment admins, need a [project role](#project-roles) to open a project and view, edit, or manage project assets.

Workato doesn't grant implicit access through environment roles. Assigning a project role makes access explicit and visible in the audit log, which is important for sensitive or restricted projects.

Refer to the system [Environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) page to learn more about the permissions included in each role.

> **PROJECT VISIBILITY**
> 
> Only users with the **Manage projects** permission in their environment role can view a list of all projects in that environment and manage project access. While they don't need a project role to see project names, they can't open or edit project content without one. Other users can see project names only if they have direct access to those projects.

### Assign environment roles to users

Collaborators with the **Environment admin** role can assign roles to individual users. A user can have different roles in each environment. For example, you can assign a DevOps engineer as an **Environment admin** in Development, a **Member** in Testing, and **No access** in Production.

Complete the following steps to assign or update environment roles:

1. Go to **Workspace admin > Access control > Collaborators**.
   
   ![Collaborator view](/assets/collaborator-view.aFXYkIOr.png)_Collaborator view_
   
2. Select a collaborator.
   
3. Assign environment roles in the **Environment access** section.
   
   ![Assign environment roles](/assets/assign-environment-roles.CFVOOz3W.png)_Assign environment roles_
   
   If multiple environments are enabled, assign the collaborator a role for each environment. If the workspace includes only one environment, choose a role from the available options.
   
4. Click **Save** to apply your changes.
   

Collaborator settings are updated immediately after you assign a role. The **No access** role removes the user's ability to view or switch into the environment.

> **ACCESS LOSS WHEN CHANGING YOUR OWN ROLE**
> 
> You lose access to the **Collaborators** page and workspace settings if you assign yourself the **No Access** role or a role without admin privileges in the **DEV** environment.
> 
> Review your **DEV** environment role carefully before you save changes to your own access.

## Project roles

Project roles control which actions a collaborator can perform in a project. These roles include permissions to build recipes, manage connections, deploy content, and view project assets.

Workato provides four system-defined project roles:

- **Project admin**: Full access to all project content and settings, including user management and deletion.
- **Advanced builder**: Full access to build and deploy, without access to manage settings or user permissions.
- **Builder**: Can build recipes and submit deployment requests when review and approval is enabled for the workspace. Builders can't review, approve, or deploy projects.
- **Project operator**: Can view all project content and run or stop recipes.

You can assign project roles to individuals or [collaborator groups](#collaborator-groups). Each project requires a separate role assignment. This separation allows teams to control access and responsibilities across projects. For example, a developer may be a **Builder** in one project and a **Project operator** in another.

Collaborators must have a project role to view or manage project content. Environment roles don't grant project access.

Refer to the system [Project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) page to learn more about the permissions included in each role.

> **PROJECT CREATION**
> 
> Users with an environment role that includes the **Create** project privilege automatically receive the **Project admin** role for any project they create. Other collaborators with the Manage projects permission can edit the creator's project role after the project is created.

### Manage project access and roles

You can manage project access directly in each project's settings. To give collaborators or groups project access, explicitly assign them project roles. Alternatively, you can set [default access](#default-access-for-all-collaborators) for all workspace users.

Only a **Project admin** or users with environment roles that grant the **Manage projects** permission can manage project access.

#### Add users or groups to a project

Complete the following steps to assign project roles:

1. Open the project in Workato.
   
2. Go to **Settings > Project access**.
   
   ![Go to project access](/assets/project-access-settings.gE2JRq7F.png)_Go to project access_
   
3. Click **Add collaborators**.
   
4. Choose a **Project role** for the collaborators or group.
   
5. Select one or more collaborators or groups to add.
   
   ![Add collaborators to project](/assets/add-collaborators-project.PEHQdkQz.png)_Add collaborators to project_
   
6. Click **Add**. The user or group appears in the project access list with the assigned role.
   

When you assign a group to a project, its members receive access according to the group's role. For example, if you assign a data team group the **Project operator** role, each group member can view project content and run or stop recipes. You can assign multiple collaborators or groups to a project.

> **EFFECTIVE PERMISSIONS ACROSS GROUPS**
> 
> If a user belongs to multiple groups, their effective permissions combine across all assigned roles. Refer to the [How Workato resolves permission conflicts](#resolve-permission-conflicts) section for more information.

#### Remove collaborator access

Choose one of the following options to revoke project access:

- Set the collaborator's role to **No access** in the project access list. This blocks the collaborator from accessing the project content.
- Click the delete icon next to the collaborator's name to remove their project role assignment entirely.

### Default access for all collaborators

The default access setting defines a project role for every workspace collaborator who doesn't have an explicit individual or group assignment. Workato applies the default access setting through the **Everyone else** entry on the **Project access** page. This setting applies separately to each project and environment.

![Default access setting](/assets/default-access-setting.CoWzKthf.png)_Default access setting_

The default project access setting is **No access**. You can change this setting to any available project role, such as **Project operator** or **Builder**, to grant general access without assigning users individually.

For example, setting the default role to **Project operator** grants all collaborators view access and the ability to run or stop recipes in projects within the environment, unless they have a different role through an individual or group assignment.

### Assign project roles during deployment

When a user deploys a project to a new environment for the first time and no project with the same name exists, Workato creates a new project in that environment. The user must have an environment role that includes the **Create** project permission in the target environment and the **Deploy** permission for the project in the source environment. Workato assigns the user the **Project admin** role in the newly created project. The **Project admin** can manage access for other collaborators in the new environment.

If a project with the same name already exists in the target environment, the user must have the **Deploy** permission in both the source and target environments to complete the deployment.

Workato also detects collaborators with project roles in the original environment and suggests assigning the same roles in the new environment. You can accept, modify, or reject the suggestions.

## Custom roles

Workato supports custom roles at both the [environment](#create-a-custom-environment-role) and [project](#create-a-custom-project-role) levels. Use custom roles when system-defined roles don't meet your access requirements. You can create these roles by selecting privileges from a predefined list.

### Create a custom environment role

Custom environment roles define who can create projects, manage users, or configure environment settings:

1. Go to **Workspace admin > Environment roles**.
   
2. Click **\+ Add environment role**.
   
   ![Add environment role](/assets/add-env-role.De7kone4.png)_Add environment role_
   
3. Select the required privileges and save the role.
   

Refer to the [Environment privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#environment-privileges) reference for a complete list of available privileges and their descriptions.

### Create a custom project role

Custom project roles define who can build recipes, deploy content, or manage project assets:

1. Go to **Workspace admin > Project roles**
   
2. Click **\+ Add project role** to create a new role.
   
   ![Add project role](/assets/add-proj-role.CQp2OurZ.png)_Add project role_
   
3. Select the required privileges and save the role.
   

Refer to the [Project privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-privileges) reference for a complete list of available privileges and their descriptions.

## Collaborator groups

Collaborator groups simplify access management. Each group acts as a single unit that includes multiple users. You can assign a project role to the group to grant access to all members automatically.

![Collaborator groups](/assets/collaborator-groups.id4PdREi.png)_Collaborator groups_

> **INDIVIDUAL ASSIGNMENT REQUIRED**
> 
> You can't grant environment roles through collaborator groups. You must assign environment access to each user individually, even if they belong to a group.

Use collaborator groups to organize users by team or function, such as QA testers or marketing teams. Collaborators can belong to multiple groups, but group nesting isn't supported.

Refer to the [Collaborator groups](/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups) guide for more information.

## AHQ moderators and OEM customer managers

Workato supports dedicated user accounts for AHQ moderators and OEM customer managers to support Embedded and managed workspaces. These users follow different access rules from standard collaborators.

### Group membership

AHQ moderators and OEM customer managers aren't included in the [default access setting](#default-access-for-all-collaborators) that applies to standard workspace collaborators. You must assign and manage their access separately.

### Role assignment

The new access control model requires workspace admins to assign both an environment role and a project role when they add a moderator or customer manager. This replaces the previous workflow where a single collaborator role controlled all access. The environment role applies across all environments, and the project role applies across all projects in the customer or managed workspace. Customer managers or moderators can't be added to any collaborator groups.

### Inherited roles

AHQ admins and Embedded partners can create custom, inheritable roles. These roles automatically appear in all managed workspaces as non-editable roles. Inheritable roles apply across all managed workspaces without project scope restrictions.

### How Workato resolves permission conflicts

Workato combines permissions when a user belongs to multiple collaborator groups that hold different roles in the same project.

The user receives all permissions granted by any of the assigned roles. Workato merges permission sets instead of prioritizing or overriding roles.

For example, if a user belongs to one group with the **Project operator** role and another group with the **Builder** role in the same project, Workato merges both sets of permissions. The user can view and build recipes. If any assigned role grants a permission, the user receives it.

### Key limitations

Workato supports environment role assignment only at the individual user level. Collaborator groups control project roles but can't grant environment access. Admins should define all required environment roles in advance to prevent access issues during login.

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles.md
description: >-
  Reference for Workato environment roles, including Environment admin,
  Environment manager, and Member, and the privileges each role grants.
---

# Environment roles

Environment roles define a collaborator's permissions within a specific environment. These roles control access to platform tools, environment settings, and administrative functions, but don't grant access to project content.

You can assign different environment roles to the same collaborator in different environments. For example, a DevOps engineer can have **Environment admin** in Development, **Member** in Testing, and **No access** in Production.

> **PROJECT ACCESS**
> 
> Environment roles don't include project access. Assign a project role to allow collaborators to view, edit, or manage project content.

Workato provides the following default environment roles:

| Type | Description |
| --- | --- |
| Environment admin | Full control over workspace-wide and environment settings. |
| Environment manager | Full control over environment settings, but no workspace-wide permissions. |
| Member | View-only access to environment settings. |

Use the following guides to review the full set of privileges for each role:

- [Environment admin](#environment-admin)
- [Environment manager](#environment-manager)
- [Member](#member)

## Environment admin

The **Environment admin** role grants full administrative access within a specific environment. Assign this role to collaborators who manage projects, configure platform features, and control access within the environment.

Environment admins can perform the following actions in their assigned environment:

- [Create and manage](#project-management) projects in the environment
- [Manage project membership](#project-management), including adding or removing collaborators and assigning project roles
- [Configure tools](#tools) like Workbot, Logs, and Message templates
- Manage shared features such as data storage, the API platform, Apps portal, and Insights
- [Assign environment roles](#workspace-access) to other users

Environment admins can't access or edit the contents of a project, such as recipes or assets, unless also assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) that explicitly grants those permissions.

The following tables list the full set of privileges included in the **Environment admin** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ✔ | ✔ | ✔ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Custom OAuth profiles | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Message templates | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Event streams | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Recipe lifecycle management | ✔ |  |  |  |  |  |  |
| Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Enterprise Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Runtime user connections | ✔ | ✔ | ✔ |  | ✔ |  |  |
| Logs | ✔ |  |  |  |  |  |  |
| File Storage | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Workato GO | ✔ | ✔ | ✔ |  |  |  | ✔ |

#### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ✔ | ✔ | ✔ | ✔ | ✔ |
| Connection - on-prem files | ✔ |  |  |  |  |
| Connection - command line scripts | ✔ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ✔ |
| Users and groups | ✔ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Environment properties | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Configurable data retention | ✔ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, logs, and the ability to build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ✔ |  |  |  |  |
| Collections & endpoints | ✔ | ✔ | ✔ | ✔ | ✔ |
| Client & access profiles | ✔ | ✔ | ✔ | ✔ | ✔ |
| Policies | ✔ | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ✔ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ✔ | ✔ | ✔ | ✔ | ✔ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ✔ |
| Collaborator roles (non-system) | ✔ |
| Collaborator SAML SSO auth | ✔ |
| Developer API | ✔ |
| SCIM provisioning | ✔ |
| Workspace settings | ✔ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ✔ |
| Audit log replication | ✔ |
| Debug, Log and Security | ✔ |
| Manage locked projects | ✔ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ✔ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ✔ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ✔ |
| End users and groups | ✔ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ✔ | ✔ | ✔ | ✔ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ✔ |  |  | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ | ✔ | ✔ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ✔ | ✔ | ✔ |

## Environment manager

The **Environment manager** role provides administrative control over environment-level settings and platform tools, but excludes workspace-wide privileges and project-level access. Assign this role to collaborators who maintain environment configurations and create new projects, without needing full administrative control.

Environment managers can perform the following actions in their assigned environment:

- [Create new projects](#project-management) in the environment
- [Configure platform tools](#tools) such as Workbot and OAuth profiles
- Manage shared features such as data storage, the API platform, Apps portal, and Insights

Environment managers can't configure workspace settings or manage users across environments. They also can't access or edit project content, such as recipes or assets, unless also assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) that explicitly grants those permissions.

The following tables list the full set of privileges included in the **Environment manager** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ❌ | ✔ | ❌ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Custom OAuth profiles | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Message templates | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Event streams | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Recipe lifecycle management | ❌ |  |  |  |  |  |  |
| Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Enterprise Workbot | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Runtime user connections | ✔ | ✔ | ✔ |  | ✔ |  |  |
| Logs | ❌ |  |  |  |  |  |  |
| File Storage | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |
| Workato GO | ❌ | ❌ | ❌ |  |  |  | ❌ |

#### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ✔ | ✔ | ✔ | ✔ | ✔ |
| Connection - on-prem files | ✔ |  |  |  |  |
| Connection - command line scripts | ✔ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ✔ |
| Users and groups | ✔ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Environment properties | ✔ | ✔ | ✔ | ✔ | ✔ |  |
| Configurable data retention | ❌ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, logs, and the ability to build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ✔ |  |  |  |  |
| Collections & endpoints | ✔ | ✔ | ✔ | ✔ | ✔ |
| Client & access profiles | ✔ | ✔ | ✔ | ✔ | ✔ |
| Policies | ✔ | ✔ | ✔ | ✔ | ✔ |
| Settings | ✔ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ✔ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ✔ | ✔ | ✔ | ✔ | ✔ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ❌ |
| Collaborator roles (non-system) | ❌ |
| Collaborator SAML SSO auth | ❌ |
| Developer API | ❌ |
| SCIM provisioning | ❌ |
| Workspace settings | ❌ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ❌ |
| Audit log replication | ❌ |
| Debug, Log and Security | ❌ |
| Manage locked projects | ❌ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ❌ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ❌ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ❌ |
| End users and groups | ❌ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ❌ | ❌ | ❌ | ❌ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ❌ |  |  | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ | ❌ | ❌ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ❌ | ❌ | ❌ |

## Member

The **Member** role grants limited, view-only visibility in an environment. Assign this role to users who need visibility into an environment without permission to make changes.

Members can perform the following actions:

- View basic environment information.
- Reference shared assets for context.

Members can't edit, create, or delete tools or settings at the environment level. They also can't access project content unless assigned a [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles).

The following tables list the full set of privileges included in the **Member** role. Each section describes the tools or features the privileges control.

### Platform tools privileges

The following privileges control environment-level tools and features shared across multiple projects. They include configuration access for core tools, project management, and on-prem systems.

#### Project management

These privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

| Privilege | Full access | Create | Access control |
| --- | --- | --- | --- |
| Manage projects | ❌ | ❌ | ❌ |

#### Tools

These privileges control access to shared environment-level tools and resources used across recipes. They include configuration access for components such as OAuth profiles, lifecycle management, and event streams.

| Privilege | Full access | View | Edit | Create | Delete | View history | Manage access |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Common data models | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Custom OAuth profiles | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Message templates | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Event streams | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| Recipe lifecycle management | ❌ |  |  |  |  |  |  |
| Workbot | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Enterprise Workbot | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Runtime user connections | ❌ | ❌ | ❌ |  | ❌ |  |  |
| Logs | ❌ |  |  |  |  |  |  |
| File Storage | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |
| Workato GO | ❌ | ❌ | ❌ |  |  |  | ❌ |

### On-premise

These privileges control access to on-premise features, including agent management, file-based connections, and command line scripts.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| On-prem groups & agents | ❌ | ❌ | ❌ | ❌ | ❌ |
| Connection - on-prem files | ❌ |  |  |  |  |
| Connection - command line scripts | ❌ |  |  |  |  |

#### Apps portal

These privileges control group management and access to related workspace settings through the apps portal.

| Privilege | Full access |
| --- | --- |
| Settings | ❌ |
| Users and groups | ❌ |

#### Data storage

These privileges control access to environment-level data, including lookup tables and environment properties.

| Privilege | Full access | View | Edit records | Create | Delete | Modify structure |
| --- | --- | --- | --- | --- | --- | --- |
| Lookup tables | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Environment properties | ❌ | ❌ | ❌ | ❌ | ❌ |  |
| Configurable data retention | ❌ |  |  |  |  |  |

#### API platform

These privileges control access to API platform features such as endpoint management, API clients, and logs. These privileges control who can build and manage APIs within the environment.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Dashboard & logs | ❌ |  |  |  |  |
| Collections & endpoints | ❌ | ❌ | ❌ | ❌ | ❌ |
| Client & access profiles | ❌ | ❌ | ❌ | ❌ | ❌ |
| Policies | ❌ | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ |  |  |  |  |

#### Connector SDK

These privileges control access to develop and manage custom SDK connectors and use them in recipes.

| Privilege | Full access |
| --- | --- |
| Connector SDK | ❌ |
| Use in recipes | ✔ |

#### Insights

These privileges control access to Insights dashboards to monitor recipe usage, errors, and performance.

| Privilege | Full access | View | Edit | Create | Delete |
| --- | --- | --- | --- | --- | --- |
| Insights | ❌ | ❌ | ❌ | ❌ | ❌ |

### Admin privileges

These privileges control administration at the workspace and environment level, including access to user roles, APIs, and security configurations that extend beyond individual projects.

#### Workspace access

These privileges control access to manage collaborators, workspace-level settings, and API clients that can modify workspaces.

| Privilege | Full access |
| --- | --- |
| Collaborators | ❌ |
| Collaborator roles (non-system) | ❌ |
| Collaborator SAML SSO auth | ❌ |
| Developer API | ❌ |
| SCIM provisioning | ❌ |
| Workspace settings | ❌ |

#### Environment settings

These privileges control access to environment-level security settings and audit logs. They include visibility into all team activity in the environment, regardless of platform tools or project access.

| Privilege | Full access |
| --- | --- |
| Activity audit | ❌ |
| Audit log replication | ❌ |
| Debug, Log and Security | ❌ |
| Manage locked projects | ❌ |

#### Billing & usage

These privileges control access to the Billing & Usage dashboard.

| Privilege | Full access |
| --- | --- |
| Usage dashboard | ❌ |

### Automation HQ privileges

This privilege grants access to the Automation HQ console for managing enterprise automation programs and initiatives.

| Privilege | Full access |
| --- | --- |
| Automation HQ | ❌ |

### Solutions access

These privileges control authentication, end-user groups, and identity management for solutions such as Workato GO, Genies, and Low Code App. They include configuration of authentication methods, SSO, and user/group assignments.

| Privilege | Full access |
| --- | --- |
| Authentication settings and SSO | ❌ |
| End users and groups | ❌ |

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

| Privilege | Full access | View | Edit | Create |
| --- | --- | --- | --- | --- |
| Version | ❌ | ❌ | ❌ | ❌ |

#### Curation

| Privilege | Full access | View | Edit | Delete | Publish/Distribute | Review | Share |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Packages | ❌ |  |  | ❌ | ❌ | ❌ | ❌ |
| Settings | ❌ | ❌ | ❌ |  |  |  |  |

#### Consumption

| Privilege | Full access | View | Install |
| --- | --- | --- | --- |
| Verified Packages | ❌ | ❌ | ❌ |

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles.md
description: >-
  Reference for Workato project roles, including Project admin, Advanced
  builder, Builder, and Project operator, and the access each provides.
---

# Project roles

Project roles control what a user or group can access and manage inside a specific project. You can assign these roles per project to define responsibilities across build, deploy, and review tasks. The following table lists system project roles and the access they provide:

| Type | Description |
| --- | --- |
| Project admin | Grants full access to all project content and settings, including user management and deletion. |
| Advanced builder | Grants full access to build and deploy, without access to manage settings or user permissions. |
| Builder | Allows users to modify folders, recipes, Workato apps, and data tables. This role also allows test automation but not deployment. |
| Project operator | Grants read-only access to project content and the ability to run and stop recipes. |

Use the following guides to review the full set of privileges for each role:

- [Project admin](#project-admin)
- [Advanced builder](#advanced-builder)
- [Builder](#builder)
- [Project operator](#project-operator)

## Project admin

The **Project admin** role provides full control over all content and settings within a project. This includes recipe development, resource configuration, deployments, and access management. Assign this role to collaborators who manage project assets without requiring environment-level administrative access.

Project admins can perform the following actions in their assigned project:

- Build and manage recipes, folders, and connections.
- Approve and review deployments.
- Manage project access and assign roles to collaborators.
- View and manage data tables, test automation, and network trace.

Project admins can access every recipe, connection, and asset in a project. This role doesn't include access to environment or workspace-level settings.

### Privileges

The following tables list the full set of privileges included in the **Project admin** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  |  |
| Event streams | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Resources | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Knowledge bases | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| Custom chat interface | ✔ | ✔ | ✔ | ✔ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ✔ |  | ✔ |  |  | ✔ | ✔ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ✔ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ✔ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ✔ | ✔ | ✔ |

## Advanced builder

The **Advanced builder** role provides full access to build, test, and deploy project assets. This role doesn't include access to project administration or user management.

Advanced builders can perform the following tasks:

- View, edit, and manage project assets.
- Perform deployments across environments.
- Manage test automation and workflow apps.

They can't rename or delete projects, or manage project access. Assign this role to users who handle project development and deployment without administrative control.

### Privileges

The following tables list the full set of privileges included in the **Advanced builder** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  |  |
| Event streams | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Resources | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ | ✔ |
| Knowledge bases | ✔ | ✔ | ✔ | ✔ | ✔ |  |  |  |
| Custom chat interface | ✔ | ✔ | ✔ | ✔ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ✔ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ✔ | ❌ |

## Builder

The **Builder** role provides access to develop recipes and manage key assets within a project. Builders don't have access to deployments or project administration.

Builders can perform the following actions in their assigned project:

- Create and test recipes and folders, and view connections
- Manage project properties and review deployments
- Configure workflow apps, manage access, and publish them

Builders can't deploy project assets or manage project-level access. Assign this role to collaborators who build and test project components without administrative access.

### Privileges

The following tables list the full set of privileges included in the **Builder** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Recipes | ✔ | ✔ | ✔ |  | ✔ | ✔ | ✔ | ✔ |  |  |
| Decision models | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Data Pipelines | ❌ | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |  |  |
| Event streams | ❌ | ✔ | ✔ |  | ✔ | ❌ |  |  |  | ✔ |
| Data tables | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |  | ✔ |  |
| Folders | ✔ | ✔ | ✔ |  | ✔ | ✔ |  |  |  |  |
| Blueprints | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Resources | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
|  |  |  |  |  |  |  |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ❌ | ✔ | ✔ | ✔ | ❌ | ✔ | ❌ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Knowledge bases | ❌ | ❌ | ❌ | ❌ | ❌ |  |  |  |
| Custom chat interface | ❌ | ❌ | ❌ | ❌ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ✔ | ✔ |  | ✔ | ✔ | ✔ |  |
| Approve deployment | ❌ |  |  |  |  |  |  |
| Review deployment | ✔ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ✔ |  |  |
| App access and role management | ✔ | ✔ | ✔ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ✔ | ✔ | ✔ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ❌ | ❌ |

## Project operator

The **Project operator** role provides limited access to view and run content within a project. Assign this role to users who need visibility into project activity and permission to test recipes, but not edit or deploy content.

Project operators can perform the following actions in their assigned project:

- View recipes and folders
- Access job history
- Test, start, and stop recipes

They can't create, edit, or deploy content. They also can't view connections or manage project settings or user access.

### Privileges

The following tables list the full set of privileges included in the **Project operator** role. Each section outlines what actions the role can perform within a project.

#### Project assets

The following privileges control access to recipe-building features and shared project resources:

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Test/ Start/Stop | Job history | Modify structure | View history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Connections | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Recipes | ❌ | ✔ | ❌ |  | ❌ | ❌ | ✔ | ✔ |  |  |
| Decision models | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Data Pipelines | ❌ | ✔ | ❌ |  | ❌ | ❌ | ❌ |  |  |  |
| Event streams | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  | ✔ |
| Data tables | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |  | ❌ |  |
| Folders | ❌ | ✔ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Blueprints | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |
| Resources | ❌ | ❌ | ❌ |  | ❌ | ❌ |  |  |  |  |

#### MCP servers

The following privileges control access to create and manage MCP servers:

| Privilege | Full access | View | Edit | Create | Delete | Manage access | Publish/Unpublish |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MCP servers | ❌ | ✔ | ❌ | ❌ | ❌ | ❌ | ❌ |

#### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

| Privilege | Full access | View | Edit | Create | Delete | Start/ Stop | Test | Conversation history |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Genies | ❌ | ✔ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Knowledge bases | ❌ | ✔ | ❌ | ❌ | ❌ |  |  |  |
| Custom chat interface | ❌ | ✔ | ❌ | ❌ |  |  |  |  |

#### Project settings

The following privileges control project-level administration, such as access control, project properties, and deployment approvals:

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

| Privilege | Full access | View | Edit | Edit records | Create | Delete | Access control |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Project administration | ❌ |  | ❌ |  |  | ❌ | ❌ |
| Project properties | ❌ | ❌ |  | ❌ | ❌ | ❌ |  |
| Approve deployment | ❌ |  |  |  |  |  |  |
| Review deployment | ❌ |  |  |  |  |  |  |

#### Low-code apps

The following privileges control access to workflow apps, including app configuration and approval steps:

> **ACCESS DEPENDENCY**
> 
> Access to workflow apps also depends on data table privileges.

| Privilege | Full access | Manage access and role | Go live/Take offline |
| --- | --- | --- | --- |
| App development | ❌ |  |  |
| App access and role management | ❌ | ❌ | ❌ |

#### Test automation

The following privileges control access to recipe test cases. Full access includes **View**, **Create**, **Edit**, **Run**, and **Delete** actions. Test automation management also depends on [recipe privileges](#project-assets) such as **View**, **Test**, and **Job History**.

| Privilege | Full access | View | Manage (Create, Edit, Delete, Run) |
| --- | --- | --- | --- |
| Test automation | ❌ | ✔ | ❌ |

#### Debug jobs

The following privileges control access to job-level network traces:

| Privilege | Full access |
| --- | --- |
| Network trace | ❌ |

#### Secrets management

The following privileges control access to security-related secrets within the project:

| Privilege | Full access | View | Edit |
| --- | --- | --- | --- |
| Secrets management | ❌ | ❌ | ❌ |

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/collaborator-groups.md
description: >-
  Learn how collaborator groups in Workato assign project roles to sets of users
  at once and how stacked group permissions are applied.
---

# Collaborator groups

Collaborator groups simplify access management by letting you assign project roles to a set of collaborators at once. You can group collaborators based on team structure, such as QA testers, marketing, or engineering teams.

![Collaborator groups](/assets/collaborator-groups.id4PdREi.png)_Collaborator groups_

## How collaborator groups manage project permissions

Collaborator groups organize collaborators under shared project-level roles. After you create a group and add members, you can grant project access to entire groups instead of managing individual assignments.

Collaborators with the **Collaborators** admin privilege manage these groups and control their membership. Collaborators can belong to multiple groups, but each group can include only individual users. Group nesting isn't supported.

> **INDIVIDUAL ASSIGNMENT REQUIRED**
> 
> You can't grant environment roles through collaborator groups. You must assign environment access to each user individually, even if they belong to a group.

### How group-based permissions are applied

When you assign a collaborator group to a project, all members of the group inherit the assigned project role.

Collaborators who belong to multiple groups receive the highest level of access granted by any group. Permissions from multiple groups stack and don't conflict. For example, when one group grants the **Project admin** role in a project and another grants the **Builder** role in the same project, the collaborator inherits **Project admin** permissions.

Changes to collaborator groups take effect immediately after you refresh the page. The system immediately revokes any access granted through that group when you remove a collaborator from a group.

If your workspace uses SAML role sync / SCIM for passing in the workato\_user\_groups parameter, this serves as the source of truth and any manual updates will be overwritten.

## Create a collaborator group

Complete the following steps to create and manage a collaborator group:

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Click **\+ Create collaborator group**.
   
3. Enter a **Group name**.
   
   ![Create collaborator group](/assets/create-collaborator-group.C5qAEaer.png)_Create collaborator group_
   
4. Optional. Add a **Description**. The quota is 350 characters.
   
5. Select **Collaborators** to add to the group. Use the search bar to filter by name or email.
   
6. Click **Create**.
   

> **ADD COLLABORATORS TO GROUPS DURING INVITATION**
> 
> You can also add collaborators to groups when you invite them to the workspace. The **Invite collaborator** dialog in **Workspace admin > Access control > Collaborators** includes an optional **Collaborator groups** field. This allows you to assign group membership during the invitation process instead of adding the collaborator to a group separately.

## Manage group collaborators

After you create a collaborator group, you can manage its members directly:

**Add collaborators to an existing group**

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Select the group to manage.
   
3. Click **\+ Add collaborators**.
   
   ![Add collaborators](/assets/add-collaborators-group.BauZOWsY.png)_Add collaborators_
   
4. Search for collaborators by name or email, then select members to add.
   
5. Click **Add**.
   
   ![Click add](/assets/click-add.CUtY7JIU.png)_Click **Add**_
   

**Remove collaborators from a group**

1. Go to **Workspace admin > Access control > Collaborator groups**.
   
2. Select the group to manage.
   
3. Click the checkbox next to the group members you plan to remove.
   
4. Click **Remove member**.
   
   ![Remove member](/assets/remove-member.7B-4g-aE.png)_Remove member_
   

**View project access for a group**

1. Open the group page from **Workspace admin > Access control > Collaborator groups**.
   
2. Select the **Project access** tab.
   
3. View a list of all projects where the group has access.
   
   ![Project access](/assets/project-access.Cu45WI8s.png)_Project access_
   
   If the group has no access to any project, the page displays **No project access is given to this group**.
   
   ![No project access](/assets/no-project-access.CTzsH4N7.png)_No project access_
   

## Assign project access to collaborator groups

Collaborators with the Manage project access privilege can assign project roles to individual collaborators or entire collaborator groups.

1. Go to **Projects > \[Project name\] > Settings > Project access**.
   
2. Click **\+ Add collaborators**.
   
   ![Project access](/assets/add-collaborators-group-project.ChJlu_uA.png)_Add collaborators to project_
   
3. Select a **Project role** from the drop-down menu.
   
4. Search for collaborators or collaborator groups by name or email, then select the checkboxes next to the collaborators or groups you plan to add.
   
   ![Project access](/assets/select-collaborator-groups.DLL3kbVu.png)_Choose collaborators_
   
5. Click **Add** to apply the selected project roles.

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference.md
description: >-
  Reference for Workato environment-level and project-level privileges, covering
  what each controls and its dependencies for custom roles.
---

# Privileges

This page lists all available privileges in Workato. Use this reference when creating or editing custom roles. Each entry describes what the privilege controls, where it applies, and any dependencies to consider.

Privileges fall into two scopes:

- [Environment-level privileges](#environment-privileges): Apply across the entire environment
- [Project-level privileges](#project-privileges): Apply within a specific project

## Environment privileges

Environment-level privileges control access across entire environments. They cover administrative tools, configuration options, and features shared across multiple projects, such as lifecycle settings, OAuth profiles, or project creation.

Workspaces may include multiple environments, and collaborators can have different environment roles across each one.

### Platform tools

The **Platform tools** privileges tab controls access to shared tools and features that operate across projects within the environment. This tab includes the following privilege access:

- [Project management](#project-management)
- [Tools](#tools)
- [On-premise](#on-premise)
- [Apps portal](#apps-portal)
- [Data storage](#data-storage)
- [API platform](#api-platform)
- [Connector SDK](#connector-sdk)
- [Insights](#insights)

#### Project management

The following privileges control whether a collaborator can create projects and manage access to all projects in the environment. When a user creates a project, Workato automatically assigns them the [Project admin](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles#project-admin) role for that project.

- Manage projects
  
- Controls access to create projects and manage collaborator access across all projects in the environment.
  
  - Full access
    
  - Includes project creation and the ability to manage collaborator access for all projects in the environment.
    
  - Create
    
  - Grants the ability to create new projects. The creator is automatically assigned the **Project admin** role for that project.
    
  - Access control
    
  - Grants permission to manage collaborator roles and access across all projects in the environment.
    

#### Tools

The following privileges control access to shared environment-level tools and resources used across recipes:

- Common data models
  
- Controls access to create and manage common data models that standardize schema across recipes.
  
  - Full access
    
  - Grants all permissions to common data models.
    
  - View
    
  - View common data models in the workspace.
    
  - Edit
    
  - Edit common data models in the workspace.
    
  - Create
    
  - Create common data models in the workspace.
    
  - Delete
    
  - Delete common data models in the workspace.
    

- Custom Oauth profiles
  
- Controls access to manage custom OAuth profiles used for authentication across recipes and connectors in the environment.
  
  - Full access
    
  - Grants all Custom OAuth profile permissions.
    
  - View
    
  - View Custom OAuth Profiles and Enterprise Workbots.
    
  - Edit
    
  - Edit Custom OAuth Profiles and Enterprise Workbots.
    
  - Create
    
  - Create Custom OAuth Profiles and Enterprise Workbots.
    
  - Delete
    
  - Delete Custom OAuth Profiles and Enterprise Workbots.
    

- Message templates
  
- Controls access to manage message templates used in recipes.
  
  - Full access
    
  - Grants all message templates permissions.
    
  - View
    
  - View message templates in the workspace.
    
  - Edit
    
  - Edit message templates in the workspace.
    
  - Create
    
  - Create message templates in the workspace.
    
  - Delete
    
  - Delete message templates in the workspace.
    

- Event streams
  
- Controls access to event streams.
  
  - Full access
    
  - Grants full access to all event streams permissions.
    
  - View
    
  - View Event topics in the workspace.
    
  - Edit
    
  - Edit Event topics in the workspace.
    
  - Create
    
  - Create Event topics in the workspace.
    
  - Delete
    
  - Delete Event topics in the workspace.
    
  - View history
    
  - View the message content in the Event topics messages list.
    

- Recipe lifecycle management
  
- Controls access to the Recipe lifecycle management feature.
  
  - Full access
  - Grants full access to the Recipe lifecycle management (RLCM) feature. This includes the ability to create manifests and view and interact with all assets included in manifests.

- Workbot
  
- Controls access to manage Workbot configurations.
  
  - Full access
    
  - Grants full access to all Workbot permissions.
    
  - View
    
  - View installed Workbots in the workspace.
    
  - Edit
    
  - Edit installed Workbots in the workspace.
    
  - Create
    
  - Create Workbots in the workspace.
    
  - Delete
    
  - Delete installed Workbots in the workspace.
    

- Enterprise Workbot
  
- Controls access to manage Enterprise Workbot configurations.
  
  - Full access
    
  - Grants full access to all Enterprise Workbot permissions.
    
  - View
    
  - View installed Enterprise Workbots in the workspace.
    
  - Edit
    
  - Edit installed Enterprise Workbots in the workspace.
    
  - Create
    
  - Create Enterprise Workbots in the workspace.
    
  - Delete
    
  - Delete installed Enterprise Workbots in the workspace.
    

- Runtime user connections
  
- Controls access to runtime user connections.
  
  - Full access
    
  - Grants all runtime connection permissions.
    
  - View
    
  - View runtime connections in the workspace.
    
  - Edit
    
  - Edit runtime connections in the workspace.
    
  - Delete
    
  - Delete runtime connections in the workspace.
    

- Logs
  
- Controls access to system logs that track platform activity at the environment level.
  
  - Full access
  - Grants full access to available logs.

- File Storage
  
- Controls access to the FileStorage feature.
  
  - Full access
    
  - Grants full access to FileStorage permissions.
    
  - View
    
  - View files and directories in the FileStorage interface.
    
  - Edit
    
  - Edit files and directories in the FileStorage interface.
    
  - Create
    
  - Create files and directories in the FileStorage interface.
    
  - Delete
    
  - Delete files and directories in the FileStorage interface.
    

- Workato GO
  
- Controls access to manage [Workato GO](/en/agentic/workato-go).
  
  - Full access
    
  - Grants full access to all Workato GO permissions.
    
  - View
    
  - View Workato GO configurations.
    
  - Edit
    
  - Edit Workato GO configurations.
    
  - Manage access
    
  - Manage user access to Workato GO.
    

#### On-premise

The following privileges control access to on-premise features, including agent management, file-based connections, and command line scripts:

- On-prem groups & agents
  
- Controls access to set up, configure, and manage on-premise agents and agent groups.
  
  - Full access
    
  - Grants full access to permissions for on-prem groups and agents.
    
  - View
    
  - View on-prem groups and agents.
    
  - Edit
    
  - Edit on-prem groups and agents.
    
  - Create
    
  - Create on-prem groups and agents.
    
  - Delete
    
  - Delete on-prem groups and agents.
    

- Connection - on-prem files
  
- Controls access to create and manage connections to local file systems through the on-prem agent. These connections enable recipes to interact with the file system of the machine where the agent is installed.
  
  - Full access
  - Grants full access to permissions for on-prem groups and agents. Grants permission to create, edit, and delete on-prem file connections, including secondary connections. Note that global connection settings may override this permission.

- Connection - command line scripts
  
- Controls access to create and manage on-premise connections that execute command-line scripts on machines where the on-prem agent is installed. These connections enable recipes to run local shell commands as part of automated workflows.
  
  - Full access
  - Grants permission to create, edit, and delete command-line script connections. Note that global connection settings may override this permission.

#### Apps portal

The following privileges control access to the Workflow Apps portal. These permissions control portal-level settings and identity group access. Creating or editing a Workflow app requires Workflow app privileges. Access to a Workflow app's data depends on data table permissions.

- Settings
  
- Controls access to manage settings for the Workflow Apps portal. This includes workspace-level branding, authentication methods, login experience, and other global configurations for end-user apps.
  
  - Full access
  - Grants full access to all Workflow Apps portal settings.

> **ACCESS CONTEXT**
> 
> Workflow app creation is controlled by Workflow app permissions. Access to a Workflow app's data is controlled by data table privileges.

- Users and groups
  
- Controls access to manage groups and user assignments in the Workflow Apps portal.
  
  - Full access
  - Grants permission to view, add, remove, and modify users and their group memberships in the Apps portal.

#### Data storage

The following privileges control access to environment-level data storage features such as lookup tables and environment properties:

- Lookup tables
  
- Controls access to the lookup tables interface. These permissions apply only to tables the user can already access. This includes tables scoped to All projects, and project-scoped tables if the user also has access to that project.
  
  - Full access
    
  - Grants full to lookup tables permissions.
    
  - View
    
  - View all tables and their records.
    
  - Edit records
    
  - Add, edit, or delete records for all lookup tables in the lookup tables interface.
    
  - Create
    
  - Create new tables in the Lookup tables interface.
    
  - Delete
    
  - Delete tables in the Lookup tables interface.
    
  - Modify structure
    
  - Edit the schema, such as adding, removing, or editing columns for any table.
    

> **CONNECTOR ACCESS**
> 
> Users can still add, update, or delete records using the Lookup Tables connector in recipes, as long as they have access to the table. This works independently of the “Edit records” UI permission.

- Environment properties
  
- Controls access to environment-level configuration values used across recipes.
  
  - Full access
    
  - Grants full to environment properties permissions.
    
  - View
    
  - View all Environment properties.
    
  - Edit records
    
  - Add, edit, or delete environment properties.
    
  - Create
    
  - Create new environment properties.
    
  - Delete
    
  - Delete environment properties.
    

- Configurable data retention
  
- Controls access to environment-level data retention settings.
  
  - Full access
  - Configure and manage data retention policies for the environment.

#### API platform

The following privileges control access to the API platform, including endpoints, policies, and related configurations:

- Dashboard & logs
  
- Controls access to API dashboards and logs.
  
  - Full access
  - Grants full access to view, configure, and manage API dashboards and logs.

- Collections & endpoints
  
- Controls access to API collections and endpoints.
  
  - Full access
    
  - Grants all permissions for managing API collections and endpoints.
    
  - View
    
  - View existing API collections and endpoints.
    
  - Edit
    
  - Edit API collections and endpoints.
    
  - Create
    
  - Create new API collections and endpoints.
    
  - Delete
    
  - Delete API collections and endpoints.
    

- Client & access profiles
  
- Controls access to client profiles and access credentials for API usage.
  
  - Full access
    
  - Grants full access to manage client profiles and access credentials.
    
  - View
    
  - View client profiles and access credentials.
    
  - Edit
    
  - Edit client profiles and access credentials.
    
  - Create
    
  - Create client profiles and access credentials.
    
  - Delete
    
  - Delete client profiles and access credentials.
    

- Policies
  
- Controls access to manage API policies that govern usage and security.
  
  - Full access
    
  - Grants all API policy permissions.
    
  - View
    
  - View API policies.
    
  - Edit
    
  - Edit API policies.
    
  - Create
    
  - Create new API policies.
    
  - Delete
    
  - Delete API policies.
    

- Settings
  
- Controls access to API platform settings.
  
  - Full access
  - Grants complete control of API platform settings.

#### Connector SDK

The following privileges control access to custom SDK connectors and their usage in recipes:

- Connector SDK
  
- Controls access to develop and manage SDK-based connectors within the environment.
  
  - Full access
  - Grants full access to create, edit, publish, and manage custom SDK connectors. Note that this doesn't include permissions for recipe-level use.

- Use in recipes
  
- Controls whether users can use SDK connectors in recipes.
  
  - Full access
  - Grants full access to using custom SDK connectors in recipes across any accessible project.

#### Insights

The following privileges control access to Insights dashboards:

- Insights
  
- Controls access to Insights dashboards and their underlying data.
  
  - Full access
    
  - Grants full access to the Insights feature and permissions.
    
  - View
    
  - View all accessible Insights dashboards and their metrics.
    
  - Edit
    
  - Edit existing Insights dashboards.
    
  - Create
    
  - Create new Insights dashboards.
    
  - Delete
    
  - Delete Insights dashboards.
    

### Admin privileges

The **Admin privileges** tab controls access to administrative features at the workspace and environment level. The following privileges affect collaborator roles, workspace configuration, API access, and security visibility.

This tab includes the following privilege categories:

- [Workspace access](#workspace-access)
- [Environment settings](#environment-settings)
- [Billing & usage](#billing-usage)

#### Workspace access

The following privileges control access to workspace-wide configuration and collaborator management. Use these privileges to assign roles, manage users, and configure workspace settings:

- Collaborators
  
- Controls access to manage collaborators in the workspace.
  
  - Full access
  - Grants full control over collaborator management, including viewing, adding, updating, and removing users.

- Collaborator roles (non-system)
  
- Controls access to create and manage custom roles within the workspace. This applies to both environment and project-level roles, but does not include system-defined roles like Environment admin or Project admin.
  
  - Full access
  - Grants permission to define, edit, and delete custom roles.

- Collaborator SAML SSO auth
  
- Controls access to configure SAML single sign-on authentication for collaborators.
  
  - Full access
  - Grants permission to configure and manage collaborator SAML SSO settings.

- Developer API
  
- Controls access to manage the Developer API settings in the workspace.
  
  - Full access
  - Grants permission to view and update Developer API settings.

- SCIM provisioning
  
- Controls access to configure SCIM-based user provisioning for the workspace.
  
  - Full access
  - Grants permission to configure and manage SCIM provisioning settings.

- Cross-workspace sharing
  
- Controls access to manage [cross-workspace grants](/en/cross-share-streams) that share Event streams topics with other workspaces in your Automation HQ organization.
  
  - Full access
  - Grants permission to create, view, edit, and delete cross-workspace grants.

- Workspace settings
  
- Controls access to update global workspace-level settings.
  
  - Full access
  - Grants permission to view and update all workspace settings.

#### Environment settings

The following privileges control access to environment-level logs, debug tools, and security configurations:

- Activity audit
  
- Controls access to view activity audit logs for the environment.
  
  - Full access
  - View all activity audit logs for the environment
- Audit log replication
  
- Controls access to configure and manage audit log replication for the environment.
  
  - Full access
  - Configure audit log replication settings and manage replication targets.
- Debug, Log and Security
  
- Controls access to view team activity and security settings for the environment.
  
  - Full access
  - Grants permission to view and edit the workspace's [environment-specific settings](/en/workspace#environment-related-settings), including error alerts, network trace, data retention, and AWS IAM information.
- Manage locked projects
  
- Controls access to manage locked projects in the environment
  
  - Full access
  - Unlock projects and manage project lock state within the environment.

#### Billing & usage

The following privileges control access to the Billing & Usage dashboard:

- Usage dashboard
  
- Controls access to view the workspace's billing and usage dashboard.
  
  - Full access
  - Grants full access to view the Billing & Usage dashboard.

### Manage customers privileges

- Customers & customer managers
  
- Controls access to the **Customers** and **Customer managers** tabs of the Embedded Admin console.
  
  - Full access
    
  - Grants all [customers](/en/oem/admin-console/customers) and [customer managers](/en/oem/admin-console/customer-managers) permissions to view, add, update, and delete customers and customer managers.
    
  - View
    
  - Grants permission to view customers and customer managers.
    
  - Manage
    
  - Grants permission to add customers and assign customer managers.
    
  - Delete
    
  - Grants permission to delete customers and customer managers.
    

- Shared connectors
  
- Controls access to **Shared connectors** tab of the Embedded Admin console.
  
  - Full access
    
  - Grants all [shared connectors](/en/oem/admin-console/shared-connectors) permissions to view, manage, and delete shared connectors.
    
  - View
    
  - Grants permission to view shared connectors.
    
  - Manage
    
  - Grants permission to manage shared connectors.
    
  - Delete
    
  - Grants permission to delete shared connectors.
    

- Usage metrics & settings
  
- Controls access to usage metrics and settings in the Embedded Admin console.
  
  - Full access
    
  - Grants all [usage metrics](/en/oem/admin-console/usage-metrics) and [settings](/en/oem/admin-console/settings) permissions, including viewing and managing usage metrics and settings.
    
  - View
    
  - Grants permission to view usage metrics and settings.
    
  - Manage
    
  - Grants permission to manage audit log streaming and branding settings.
    

> **WHO CAN USE THIS FEATURE?**
> 
> The **Manage customers** interface only appears for [Embedded](/en/oem) collaborators with permission to create or modify collaborator roles.

### Automation HQ privileges

The **Automation HQ privileges** tab controls access to Automation HQ.

- Automation HQ
  
- Controls access to the Automation HQ interface.
  
  - Full access
  - Allows users to access and use all features within Automation HQ.

### Solutions access

The **Solutions access** tab controls permissions to manage end users, user groups, and authentication for Workato solutions such as Workato ID, Workato GO, Genies, and the Low Code App.

- Authentication settings and SSO
  
- Controls access to configure authentication methods and single sign-on (SSO) for Workato solutions.
  
  - Full access
  - Grants permission to configure authentication settings, enable or disable SSO, and manage identity providers.

- End users and groups
  
- Controls access to manage end users and user groups for Workato solutions.
  
  - Full access
  - Grants permission to add, remove, and update end users and groups.

### XChange

The **XChange** tab controls permissions to create, curate, and consume packages in [XChange](/en/xchange), Workato's package management and distribution platform.

#### Package creation

The following privileges control access to create and submit packages to XChange:

- Version
  
- Controls access to manage package versions submitted to XChange.
  
  - Full access
    
  - Grants all package version permissions.
    
  - View
    
  - View existing package versions.
    
  - Edit
    
  - Edit package versions.
    
  - Create
    
  - Create new package versions.
    

#### Curation

The following privileges control access to approve, manage, and distribute packages in XChange:

- Packages
  
- Controls access to review and distribute submitted packages.
  
  - Full access
    
  - Grants all package curation permissions.
    
  - Delete
    
  - Delete packages from XChange.
    
  - Publish/Distribute
    
  - Publish and distribute packages to XChange.
    
  - Review
    
  - Review submitted packages.
    
  - Share
    
  - Share packages with other workspaces.
    

- Settings
  
- Controls access to configure XChange curation settings.
  
  - Full access
    
  - Grants all XChange settings permissions.
    
  - View
    
  - View XChange settings.
    
  - Edit
    
  - Edit XChange settings.
    

#### Consumption

The following privileges control access to browse and install packages from XChange in the private library:

- Verified Packages
  
- Controls access to browse and install verified packages from XChange.
  
  - Full access
    
  - Grants all verified package permissions.
    
  - View
    
  - View verified packages in the private library.
    
  - Install
    
  - Install verified packages from XChange.
    

## Project privileges

The following privileges control what users can access and manage within a specific project. Assign these permissions when creating custom project roles to define what collaborators can build, deploy, or view.

Project-level privileges are grouped into the following categories:

- [Project assets](#project-assets)
- [MCP servers](#mcp-servers)
- [Genie building](#genie-building)
- [Project settings](#project-settings)
- [Low-code apps](#low-code-apps)
- [Test automation](#test-automation)
- [Debug jobs](#debug-jobs)
- [Secrets management](#secrets-management)

### Project assets

The following privileges control access to build and manage core project components such as recipes, folders, and connections. Each asset type has its own set of granular permissions.

- Connections
  
- Controls access to manage connections that recipes use to integrate with external systems.
  
  - Full access
    
  - Grants all connection permissions.
    
  - View
    
  - View existing connections in the project.
    
  - Edit
    
  - Update connection configurations.
    
  - Create
    
  - Create new connections in the project.
    
  - Delete
    
  - Remove existing connections from the project.
    

- Recipes
  
- Controls access to create, manage, and operate recipes in the project.
  
  - Full access
    
  - Grants all recipe-related permissions.
    
  - View
    
  - View existing recipes.
    
  - Edit
    
  - Update recipe configurations.
    
  - Create
    
  - Build new recipes.
    
  - Delete
    
  - Remove existing recipes from the project.
    
  - Test/Start/Stop
    
  - Start, stop, and test recipes.
    
  - Job history
    
  - View a recipe's job history in the **Jobs** tab.
    

> **POTENTIAL SENSITIVE DATA EXPOSURE**
> 
> Admins should consider disabling Job history for certain users to prevent access to raw inputs and outputs that may contain sensitive data when using genies. Genies ingest knowledge and context through knowledge bases and skills. The raw inputs and outputs for knowledge bases and skills can be accessed through recipe Job history.

- Decision models
  
- Controls access to create and manage decision models.
  
  - Full access
    
  - Grants all decision model permissions.
    
  - View
    
  - View decision models and decision tables.
    
  - Edit
    
  - Edit decision models and decision tables.
    
  - Create
    
  - Create decision models and decision tables.
    
  - Delete
    
  - Delete decision models and decision tables.
    

- Data Pipelines
  
- Controls access to create, manage, and test Data Pipelines.
  
  - Full access
    
  - Grants all Data Pipeline permissions.
    
  - View
    
  - View Data Pipelines.
    
  - Edit
    
  - Update existing Data Pipeline configurations.
    
  - Create
    
  - Build new Data Pipelines.
    
  - Delete
    
  - Remove existing Data Pipelines.
    
  - Test/Start/Stop
    
  - Start, stop, and test Data Pipelines.
    

- Data tables
  
- Controls access to create and manage data tables.
  
  - Full access
    
  - Grants all Data Table permissions.
    
  - View
    
  - View Data Tables.
    
  - Edit records
    
  - Update existing records within a data table.
    
  - Create
    
  - Add new data tables.
    
  - Delete
    
  - Remove existing data tables.
    
  - Modify structure
    
  - Change the schema of a data table, including adding, updating, or removing columns.
    

- Folders
  
- Controls access to project folders used to organize recipes and assets.
  
  - Full access
    
  - Grants all folder permissions.
    
  - View
    
  - View folders and sub-folders in the project.
    
  - Edit
    
  - Update folder properties.
    
  - Create
    
  - Add new folders and sub-folders.
    
  - Delete
    
  - Remove existing folders and sub-folders.
    

- Blueprints
  
- Controls access to manage [Blueprints](/en/airo/blueprints), AIRO-generated implementation plans that scaffold the assets needed for a project.
  
  - Full access
    
  - Grants all Blueprint permissions.
    
  - View
    
  - View existing Blueprints in the project.
    
  - Edit
    
  - Update Blueprint configurations.
    
  - Create
    
  - Create new Blueprints in the project.
    
  - Delete
    
  - Remove existing Blueprints from the project.
    

### MCP servers

The following privileges control access to create and manage MCP servers:

- MCP servers
  
- Controls access to create and manage MCP servers.
  
  - Full access
    
  - Grants all MCP server-related permissions.
    
  - View
    
  - View existing MCP servers.
    
  - Edit
    
  - Update MCP server configurations.
    
  - Create
    
  - Build new MCP servers.
    
  - Delete
    
  - Remove existing MCP servers.
    
  - Manage access
    
  - Manage which users and roles can access an MCP server.
    
  - Publish/Unpublish
    
  - [Publish or unpublish](/en/mcp/manage-mcp-registry#publish-an-mcp-server) an MCP server to or from the MCP server registry.
    

> **SKILL ACCESS FOR GENIES AND MCP**
> 
> Users with either the **Workato Genies** privilege or the **MCP servers** privilege can view and manage [skills](/en/agentic/skills) built with the [Workato Skill connector](/en/agentic/agent-studio/connectors/workato-skill-connector/workato-skill-connector). This lets builders on Business MCP and Enterprise MCP plans create and manage skills without an Agent Studio license.

### Genie building

The following privileges control access to the core assets used to build genies, including the knowledge bases that power genies, and custom chat interfaces where end users interact with genies:

- Genies
  
- Controls access to create and manage genies.
  
  - Full access
    
  - Grants all genie-related permissions.
    
  - View
    
  - View existing genies.
    
  - Edit
    
  - Update genie configurations.
    
  - Create
    
  - Build new genies.
    
  - Delete
    
  - Remove existing genies.
    
  - Start/Stop
    
  - Start and stop genies in a project.
    
  - Test
    
  - Grants access to Test mode.
    
  - Conversation history
    
  - Grants access to the Conversations tab with historical genie conversations.
    

- Knowledge Bases
  
- Controls access to manage Knowledge Bases used for storing and retrieving structured content.
  
  - Full access
    
  - Grants all Knowledge Base permissions.
    
  - View
    
  - View Knowledge Bases in the project.
    
  - Edit
    
  - Update Knowledge Base configurations.
    
  - Create
    
  - Add new Knowledge Bases.
    
  - Delete
    
  - Remove existing Knowledge Bases.
    

- Custom chat interface
  
- Controls access to manage a genie's [custom chat interface](/en/agentic/agent-studio/chat-interface/headless-api) and genie clients.
  
  - Full access
    
  - Grants full access to all custom chat interface permissions.
    
  - View
    
  - View a genie's custom chat interface configuration and genie clients.
    
  - Edit
    
  - Edit a genie's custom chat interface configuration, including regenerating, detaching, and deleting genie clients.
    
  - Create
    
  - Create and attach genie clients for a genie's custom chat interface.
    

- Event streams
  
- Controls project-level access to event streams. Collaborators must also be members of the project that contains the event streams.
  
  - Full access
    
  - Grants all Event streams permissions.
    
  - View
    
  - View event streams in the project.
    
  - Edit
    
  - Edit event streams in the project.
    
  - Create
    
  - Create event streams in the project.
    
  - Delete
    
  - Delete event streams in the project.
    
  - View history
    
  - View the message content in the event stream messages list.
    

> **PERMISSION MIGRATION**
> 
> Access control for event streams is transitioning to the project level because event streams are now assets. Workato migrates existing access automatically by creating new user groups and project roles named **Topics manager**, **Topics editor**, and **Topics viewer**, which provide collaborators equivalent project-level permissions to their pre-migration access. Workato skips environment roles without any collaborators, and environment roles with the same access level share one project role.
> 
> You can access event stream access through either [project-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) or [environment-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#tools) privileges during the [transition period](/en/event-streams#event-streams-as-project-assets). You must use the project-level privilege after the transition period.

### Project settings

The following privileges control access to manage project-level configurations, deployments, and collaborator permissions. These settings define who can administer the project, modify properties, and approve or review deployments.

> **ENABLE DEPLOYMENT**
> 
> You must enable deployment in both the source and target environments.

- Project administration
  
- Controls access to core administrative actions within a project.
  
  - Full access
    
  - Grants all project administrative permissions.
    
  - Edit
    
  - Update the project's name and description.
    
  - Delete
    
  - Delete the entire project.
    
  - Access control
    
  - Manage collaborator access and assign roles within the project.
    

- Project properties
  
- Controls access to manage project-level metadata and related configurations.
  
  - Full access
    
  - Grants all permissions to configure project properties.
    
  - View
    
  - View project properties such as the name, description, and metadata.
    
  - Edit records
    
  - Update existing project property records.
    
  - Create
    
  - Add new project property records.
    
  - Delete
    
  - Remove existing project property records.
    

- Approve deployment
  
- Controls the ability to approve deployments when deployment approval workflows are enabled.
  
  - Full access
  - Grants permission to approve deployment requests.

- Review deployment
  
- Controls the ability to review deployment details before approving or rejecting.
  
  - Full access
  - Grants permission to view and review deployment configurations.

### Low-code apps

The following privileges control access to Workflow apps, such as the ability to create apps and manage settings for Workflow apps on an individual basis. These permissions only apply to the web interface and don't affect access to the Workflow apps connector. Access to the Workflow apps portal is determined by Workflow apps portal permissions. Access to a Workflow app's corresponding data table is determined by data tables permissions.

- App development
  
- Controls access to build and edit the workflow app's structure and logic.
  
  - Full access
  - Grants full Workflow app development permissions.

- App access and role management
  
- Controls access to manage who can use and manage the workflow app.
  
  - Full access
    
  - Grants full access to Workflow apps and role management permissions.
    
  - Manage access and role
    
  - Manage the users of your Workflow app.
    
  - Go live / Take offline
    
  - Allows users to publish a Workflow app in the Workflow apps portal or take an app offline.
    

### Test automation

The following privileges control access to [Test Automation](/en/test-automation):

- Test automation
  
- Grants access to all test automation privileges.
  
  - Full access
    
  - Grants all test automation permissions.
    
  - View
    
  - View [test case](/en/test-automation/test-case) details, including mock data and checks.
    
  - Manage (Create, Edit, Delete, Run)
    
  - Manage (create, edit, run, delete) test cases for recipes.
    

### Debug jobs

The following privileges control access to the network trace within job history:

- Network trace
  
- Manage access to network tracing information in job histories.
  
  - Full access
  - View [network traces](/en/recipes/job-debug-tracing#viewing-job-debug-tracing) in job histories.

### Secrets management

The following privileges control access to manage security-related settings, including viewing, editing, and configuring secrets:

- Secrets management
  
- Controls access to create, view, and update secrets in the workspace.
  
  - Full access
    
  - Grants all permissions to manage secrets, including viewing and editing.
    
  - View
    
  - View existing secrets and their configurations.
    
  - Edit
    
  - Update or modify existing secrets.

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/permission-model-faqs.md
description: >-
  Answers to common questions about the new Workato permission model, including
  environment roles, project roles, and default system roles.
---

# Role-based access control FAQs

Learn more about Workato's new permission model with these frequently asked questions.

## Overview

What can I do with the permission model?

The [new permission model](/en/user-accounts-and-teams/role-based-access/access-control-v2#manage-workspace-collaborators-with-role-based-access-control) enables the following capabilities:

- **Project-level access control**: Assign different roles per project within the same environment. Collaborators no longer share the same permissions across all projects in their environment.
- **User group-based permissions**: Grant project access to collaborator groups. Members inherit access automatically, making permission management scalable and consistent.
- **Enhanced role lifecycle management**: Use APIs and SAML/SCIM to manage roles and assignments programmatically.

How does the permissions model work with existing permissions?

The permissions model separates a collaborator's permissions into two types:

- [Environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles): Define permissions per environment. These roles govern platform settings, admin capabilities, and AHQ console access. Assign the necessary permissions in the **Dev** environment to access admin features or AHQ. Permissions in **Test** or **Prod** don't apply at the workspace level.
- [Project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles): Define permissions within individual projects. These include access to folders, connections, recipes, deployments, and admin rights.

What system project roles are provided by default?

Workato provides [four default project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles):

- **Project operator**: View-only access with recipe run and stop capabilities.
- **Builder**: Create recipes but can't deploy them.
- **Advanced builder**: Create and deploy recipes.
- **Project admin**: Full access to all project assets and settings.

You can also create unlimited custom roles with tailored permissions.

## Prerequisites

What are the requirements before enabling the permission model?

The [home assets](/en/projects#home-assets) (root) folder must be empty before you enable the model. You must store all assets within dedicated projects to meet the access control system requirement.

What happens if I have assets in the home assets folder?

You must migrate the assets into a [project](/en/projects#projects). Workato provides a migration script that performs the following actions:

- Converts **Home Assets** into a standard project in each environment.
- Retains the same `folder_id` and `project_id`.
- Enforces validation to block users from adding new assets to the root.

How do I migrate home assets?

Contact your Workato representative to confirm readiness. They run the migration script after confirmation. Complete this step before you enable the [permission model](/en/user-accounts-and-teams/role-based-access/access-control-v2).

## Compatibility with the existing role model

What happens with collaborator roles when the permission model is enabled in my workspace?

The platform prevents users from creating new [collaborator roles](/en/roles). It hides roles without assigned members in the UI but ensures that all roles remain accessible through the API. The platform assigns the role and displays it in the UI again when a user with that role logs in through SAML or SCIM.

Can I still access legacy roles through the API after migration?

Yes. The API provides full access to all roles, including [legacy roles](/en/roles). You can retrieve the full list and assign legacy roles to collaborators using API endpoints. Roles without collaborators assigned to them are hidden in the UI.

> **DEPRECATION**
> 
> Legacy roles are supported in the API only for backward compatibility. Workato plans to deprecate this access in a future release. Migrate to the new permission model and collaborator groups, and avoid assigning legacy roles through the API.

What should early adopters do before enabling the permission model?

Create a complete record of all [collaborator roles](/en/roles) before you enable the permission model. Take screenshots or use the API to export the list. Some roles may disappear from the UI after migration.

Can old and new permission models work together during migration?

Yes. The platform supports both models at the same time. Some collaborators can use [legacy roles](/en/roles) while others use [environment and project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#key-roles). Each collaborator must use one model per environment. The platform doesn't allow mixing legacy and new roles within a single environment.

## Legacy role migration

What happens if I don't migrate before the deprecation deadline?

Legacy collaborator roles continue to function normally until the deprecation date at the end of August 2026. Workato recommends that you complete your [migration](/en/user-accounts-and-teams/role-based-access/migrate-roles) before this date to ensure uninterrupted access for all collaborators.

After August 31, 2026, you can no longer migrate your workspace yourself. Workato manages all remaining migrations and rolls them out by data center during the first two weeks of September 2026. Legacy roles continue to function throughout this period with no loss of permissions.

Workato sends you a report of all changes made to your workspace during the managed migration. The report includes the following information:

- The environment and project roles created from your existing roles
- The collaborator groups created from users who held the same role within an environment
- The collaborator group and project role assignments based on your previous project access

Does migrating roles in a parent workspace migrate child or customer workspaces?

The behavior depends on your workspace structure:

- **Automation HQ**: Migrating [inheritable roles](/en/user-accounts-and-teams/role-based-access/migrate-roles#ahq-inheritable-roles) in the Automation HQ workspace applies to every downstream workspace where the role is assigned. Downstream collaborator assignments update automatically. Custom collaborator roles created directly in a child workspace don't migrate automatically. Each child workspace admin must run the migration wizard in their workspace.
- **Embedded**: Migrating [inheritable roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#inherited-roles) in the Embedded partner workspace applies to every customer workspace where the role is assigned, matching Automation HQ behavior. Custom roles created directly in a customer workspace don't migrate automatically. Migrate inheritable roles first, then migrate each customer workspace individually using the Embedded API or the in-app migration wizard. Refer to **How do I migrate Embedded customer workspaces?** in this section for more information.

How do I migrate my legacy collaborator roles?

Use the bulk-migration tool in **Workspace admin > Access control > Collaborator roles**. You must have **Workspace admin** access. The tool follows a two-step process:

- Generate and review a staged report that lists the new environment role each collaborator receives, the collaborator groups they join, and the project roles they hold for each project.
- Run the full migration. The wizard creates the new roles and collaborator groups and preserves equivalent access levels across your workspace.

Refer to the [Migrate to the new access control model](/en/user-accounts-and-teams/role-based-access/migrate-roles) guide for step-by-step instructions.

I manage roles through SAML or SCIM. What must I do before the managed migration?

Role attributes passed from your identity provider continue to manage environment access after migration. Project permissions can be managed in the Workato UI, or from your identity provider through the `workato_user_groups` attribute.

Configure the `workato_user_groups` attribute before the migration if you plan to manage project permissions from your identity provider. Refer to [SAML role sync](/en/user-accounts-and-teams/saml-role-sync) for configuration steps. No other action is required if you plan to manage project permissions in the UI.

How do I migrate child workspaces in Automation HQ?

Migrate [inheritable roles](/en/user-accounts-and-teams/role-based-access/migrate-roles#ahq-inheritable-roles) in the Automation HQ workspace. The migration applies to every downstream workspace where the role is assigned, and downstream collaborator assignments update automatically.

Child workspaces that have their own custom collaborator roles must initiate a separate bulk migration independently. Each child workspace admin must run the migration wizard in their workspace to migrate locally created custom roles.

How do I migrate Embedded customer workspaces?

Migrate [inheritable roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#inherited-roles) from the Embedded partner workspace first. The migration applies to every customer workspace where the role is assigned.

Then, migrate each customer workspace's remaining roles with the [Embedded API](/en/oem/oem-api/role-migration):

- Use the `POST /api/v2/managed_users/:managed_user_id/roles_migration/system_roles` endpoint to migrate a customer workspace's system roles.
- Use the `POST /api/v2/managed_users/:managed_user_id/roles_migration/custom_role` endpoint to migrate a custom role from a customer workspace.

Set the `dry_run` parameter to `true` to preview the changes in a JSON response without migrating roles. The endpoints migrate one customer workspace at a time. You can create a recipe to repeat the process across customer workspaces.

Alternatively, you can run the [in-app migration wizard](/en/user-accounts-and-teams/role-based-access/migrate-roles) in each customer workspace.

The migration splits each legacy collaborator role into a project role and an environment role and introduces collaborator groups. You may need to refactor your integration if your embedded UI displays or manages roles, or if your API calls create or assign collaborator roles. Contact your Customer Success Manager to align on a migration path and timeline if you expect a large impact on your customers.

What is the difference between Automation HQ and the Embedded Admin console?

[Automation HQ](/en/automation-hq) provides central control over your organization's managed workspaces. Use it to represent business units as workspaces, share assets, control apps and quotas, and create inheritable roles from the HQ workspace.

The [Embedded Admin console](/en/oem/admin-console) is the central hub for Embedded partners to manage, monitor, and provision customer workspaces. You can access it from the navigation bar by selecting **Manage customers** or **Admin > Manage customers**.

Use Automation HQ if you manage workspaces for teams inside your organization. Use the Admin console if you are an Embedded partner managing workspaces created for your customers.

## Role migration process

What happens during role migration?

The migration prompts you to name the new [environment](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) and [project](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) roles. Both the environment and project roles use the name of the legacy collaborator role by default.

You can choose to:

- Add the **Manage projects** permission to the environment role.
- Add the **Control project access** permission to the project role.

The system generates an HTML summary report before the migration starts. It includes the following information:

- Number of collaborators assigned to the role
- List of new permissions
- Side-by-side comparison of current and updated permissions
- List of affected collaborators

The process then creates the new roles and automatically reassigns collaborators. All existing project access and permissions remain unchanged.

Can I preview changes before migrating a role?

Yes. The system provides a downloadable summary report that displays all changes before [migration](/en/user-accounts-and-teams/role-based-access/migrate-roles#migrate-system-roles). This lets you review the updates without applying them.

What happens to collaborators assigned to a migrated role?

The system automatically reassigns these collaborators to the [new project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles). Collaborators retain the same project access and receive equivalent permissions.

Can I migrate roles one at a time?

Yes. The migration process works on a role-by-role basis. You can [migrate roles](/en/user-accounts-and-teams/role-based-access/migrate-roles) individually to support a gradual transition and testing.

Can I migrate multiple roles at once?

Yes. Use the [bulk-migration tool](/en/user-accounts-and-teams/role-based-access/migrate-roles#bulk-migrate-all-collaborator-roles) to consolidate and migrate all collaborator roles at scale. You can also use the [Embedded](/en/oem/oem-api/role-migration) or [Developer](/en/workato-api/role-migration) API to migrate a role and create a recipe to repeat the process for other roles.

How do I manage centralized permissions across multiple workspaces using Automation HQ?

Automation HQ supports [inheritable](/en/user-accounts-and-teams/role-based-access/access-control-v2#inherited-roles) environment and project roles:

- Admins in the parent workspace create roles based on the company's security policies.
- Child workspaces inherit these roles. Collaborators in child workspaces can use these role but can't modify them.
- Admins in the parent workspace prevent custom role creation when they exclude the **Custom roles** permission from child workspaces.

## Collaborator groups

How do collaborator groups work with the permission model?

[Collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) are sets of collaborators that receive project roles as a unit. You must create a group and assign members before you can grant project access to the entire group instead of individuals.

What happens if a collaborator belongs to multiple groups?

The platform [combines all permissions](/en/user-accounts-and-teams/role-based-access/access-control-v2#ahq-moderators-and-oem-customer-managers) from the groups. The collaborator receives the highest level of access granted by any group. Permissions increase with additional group memberships and don't conflict or cancel each other.

How does session management work when group membership changes?

Group changes apply immediately after the page refreshes. Your identity provider reasserts group membership and overwrites any interim updates if the collaborator logs out and then back in through [SAML](/en/user-accounts-and-teams/saml-role-sync) or [SCIM](/en/scim).

## Project-access permissions

What is the Manage projects – Access control permission?

This environment-level permission allows administrators to perform the following actions:

- View the names of all [projects](/en/projects) in an environment, even without direct access.
- Add themselves to any project by selecting a role.
- Supervise project access across the workspace.

What is the Project administration – Access control permission?

This project-level permission allows collaborators to manage access control for a specific [project](/en/projects). All collaborators with this permission have equal privileges and can modify each other's access within the project.

This permission supports delegated project-level administration. It doesn't allow users to invite new collaborators, create collaborator groups, or define new roles. It limits access control to existing users, groups, and roles within the project.

How does this admin access model differ from the old one?

The [permission model](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborators) introduces explicit access tracking and improves control:

- **Old model**: Admins had default read-only access to all projects. No logs captured when or where access occurred.
- **New model**: Admins can view all project names but must explicitly join a project to access it. The platform logs this action in the audit log.

This change improves visibility and restricts silent access to sensitive content such as finance or HR data.

## System roles and system collaborator group

What system environment roles are provided by default?

The platform provides [four default environment roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles):

- **No access**: Blocks all access to the environment.
- **Member**: Grants minimal access without platform tool permissions or admin privileges.
- **Environment manager**: Grants full access to platform tools but excludes workspace admin privileges.
- **Environment admin**: Grants full access to all permissions in the environment.

What system project roles are provided by default?

The platform provides [four default project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles):

- **Project operator**: Grants read-only access and the ability to run and stop recipes.
- **Builder**: Allows users to modify folders, recipes, Workato apps, and data tables. This role also allows test automation but not deployment.
- **Advanced builder**: Includes all builder permissions plus the ability to approve and deploy projects to other environments.
- **Project admin**: Grants full control over the project, including the ability to delete it.

Customers can create unlimited custom project roles to meet specific access needs.

How do I use the All collaborators system group for project access?

All projects deny access to the **All collaborators** group by default. A project admin can [change this setting](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) to assign baseline access to all collaborators who have environment access. This setup works well for shared projects that require general read access.

When should I use All collaborators instead of group assignment?

Use the **All collaborators** group to apply baseline access to everyone. Use [specific groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) when different teams need distinct access. Consider the following guidelines:

- **All collaborators**: Assign permissions that every user in the workspace should have, such as read access to shared resources.
- **Group assignment**: Assign access for teams that need specialized roles or responsibilities.

## SAML and SCIM integration for role sync

What is the new SAML/SCIM parameter?

The SAML/SCIM parameter is `workato_user_groups`. It complements the following existing attributes:

- `workato_role`
- `workato_role_test`
- `workato_role_prod`

The platform applies the permission model with [environment](/en/user-accounts-and-teams/role-based-access/access-control-v2#environment-roles) and [project](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) roles when it detects the `workato_user_groups` parameter during login. The system defaults to the legacy role assignment logic if the parameter is missing.

For example:

```text
workato_role: "WorkspaceAdmin"
workato_role_test: "TestEnvAdmin"
workato_role_prod: "ProdEnvAdmin"
workato_user_groups: "HR developers, Marketing Admin"
```

What happens if a collaborator logs in through SAML or SCIM but the configuration isn't updated?

The platform assigns the collaborator a [legacy role](/en/roles). SAML continues to act as the source of truth for role assignment. The system applies the following behavior if the `workato_user_groups parameter` is missing:

- Assigns legacy roles to collaborators during login.
- Keeps new environment and project roles visible to admins.
- Displays both role models in the system until SAML migration completes.

> **UI-ASSIGNED ROLES ARE REMOVED**
> 
> The platform deletes UI-created role assignments the next time the collaborator logs in through [SSO](/en/user-accounts-and-teams/single-sign-on#prerequisites) when the SAML configuration is active.

What happens when a SAML parameter includes a non-existent role?

The platform's behavior depends on the presence of the `workato_user_groups` [parameter](/en/user-accounts-and-teams/role-based-access/access-control-v2#saml-and-scim-integration). It applies the following logic:

- **If absent**: The system uses the legacy model and assigns the default **Operator** role when the specified role doesn't exist.
- **If present**: The system uses the permission model and assigns the **No access** role when the specified role doesn't match any defined roles.

This behavior prevents excessive permissions caused by typos and helps admins detect configuration errors early.

> **CASE SENSITIVITY**
> 
> The values in `workato_user_groups` are case-sensitive. For example, `HR Developer` and `hr developer` are treated as different groups.

What happens when a collaborator has an empty collaborator group value in SAML?

The platform assigns no project access to collaborators when `workato_user_groups` [is empty](/en/user-accounts-and-teams/role-based-access/access-control-v2#behavior-when-group-data-is-empty). These users see an empty workspace with no accessible projects.

Admins can configure the **All collaborators** system group with default project access to ensure visibility for new users.

How do I assign multiple collaborator groups to a single collaborator in SAML?

[Separate the values](/en/user-accounts-and-teams/role-based-access/access-control-v2#behavior-when-group-data-includes-values) in the `workato_user_groups` attribute with commas. For example:

```text
HR developer, Marketing Admin
```

Group names are case-sensitive.

Why does the system assign the Member role instead of Environment admin during SSO login?

The platform defaults to the **Member** role if it detects a mismatch or missing context during SSO login. If you use the `workato_role` attribute to assign the **Environment admin** role, you must also include the `workato_user_groups` parameter.

Without `workato_user_groups`, the platform treats `workato_role` as a custom role. The system falls back to the default **Member** role if `workato_role` doesn't match any defined roles.

## Common use cases

How can I give production support access to specific projects only?

You can use the permissions model with the following steps:

1. Create [collaborator groups](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) for each support team, such as **Finance App Support** or **HR App Support**.
   
2. Define custom project roles with deployment and production support permissions.
   
3. Assign each group to their respective projects in the **Prod** environment.
   
4. Use environment roles to manage access to the **Prod** environment.
   

How can I enable teams to manage their own deployments without giving full workspace access?

You can assign [project roles with deployment permissions](/en/user-accounts-and-teams/role-based-access/access-control-v2#assign-project-roles-during-deployment) only to the required projects. This configuration enables teams to do the following:

- Deploy their own recipes without IT intervention.
- Choose which recipes to deploy from their projects.
- Avoid modifying other teams' projects or shared services.
- Maintain deployment control within their team's scope.

How can I provide read-only access to sensitive projects for specific business units?

Create a [collaborator group](/en/user-accounts-and-teams/role-based-access/access-control-v2#collaborator-groups) for the business unit and assign a custom **Read Only** project role to the required projects. This setup restricts access to specific content and prevents exposure to other projects or unnecessary permissions.

How do I handle collaborators who work across multiple teams or projects?

Assign the collaborator to multiple groups. The platform [aggregates all permissions](/en/user-accounts-and-teams/role-based-access/access-control-v2#resolve-permission-conflicts) and grants the highest level from any group. For example:

- Member of marketing team: Assigned the **Project operator** role for the **Marketing** project.
- Member of advanced developers: Assigned the **Advanced builder** role for the **Marketing** project.

In this case, the collaborator receives the combined permissions from both roles for the **Marketing project**.

How can I set up shared projects that everyone can access?

Use the **All collaborators** group to [assign baseline access](/en/user-accounts-and-teams/role-based-access/access-control-v2#default-access-for-all-collaborators). Apply the following configuration:

1. Open the project's **Project access** settings.
   
2. Set **Everyone else in this environment** to a base level such as **Read Only**.
   
3. Allow all collaborators with environment access to inherit this baseline permission.
   
4. Use group assignments to grant higher access to specific teams.
   

How do I prevent unauthorized access while delegating project management?

Use the **Project administration – Access control** permission to delegate [project-level access management](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles). Project owners can manage access only to their assigned projects. They can't invite new collaborators, create roles, or define new groups. Project owners can only assign existing roles and groups. The platform logs changes in the audit log.

How can I give a collaborator builder access in Dev/Test but read-only with deploy access in Prod?

Create two [custom project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#custom-roles) to manage access across environments. Define a **Power User** role that grants full project access along with deploy permissions, including review, if enabled. Define a **CI/CD Operator** role that grants read-only access with deploy permissions.

Assign a basic environment role, such as a **Member** in all environments to provide minimal platform access.

Apply project roles per environment:

- **Dev**: Assign the **Power User** role.
- **Test**: Assign the **CI/CD Operator** role.
- **Prod**: Assign the **CI/CD Operator** role.

This configuration gives the collaborator full access in **Dev**, and read-only access with deploy permissions in both **Test** and **Prod**.

What happens if the target project doesn't exist in the destination environment during deployment?

The platform [automatically creates the project](/en/user-accounts-and-teams/role-based-access/access-control-v2#assign-project-roles-during-deployment) if it doesn't exist, which can introduce a security risk:

- The collaborator must have the **Create projects** permission in their environment role.
- The collaborator receives **Project admin** access by default when the deployment creates a new project.

This overrides intended restrictions and grants full project-level permissions.

We recommend that an administrator with the **Create projects** permission create empty projects in **Test** and **Prod**, and assign the appropriate project roles such as **CI/CD Operator** before the first deployment.

How do deployment permissions work across environments?

Deployment permissions rely on [project roles](/en/user-accounts-and-teams/role-based-access/access-control-v2#project-roles) in both the source and target environments. A collaborator needs the following permissions to complete a deployment:

- Deploy permission in the source environment (**Dev**).
- Deploy permission in the target environment, such as **Test** or **Prod**.
- Create projects permission in the target environment to initialize the project during a first-time deployment.

This setup supports different deployment roles across environments and allows tighter access control.

## API and automation

How do API keys work with the permission model?

[API keys](/en/api-mgmt/api-client-mgmt#api-keys) are environment-specific. You must use a separate API key for each environment (Dev, Test, Prod) to manage project access because permissions are tied to individual environments.

The platform handles API endpoints differently depending on what they access:

- Endpoints for collaborators and legacy collaborator roles work only in the **Dev** environment for backward compatibility.
- Endpoints for collaborator groups and environment/project roles return the same responses regardless of the environment.

Are there tools to help with bulk project permission management?

Yes. You can use the Embedded or Developer API with the Workato app to build tools that simplify permission management. For example, you can select a source project and copy its project access matrix to multiple target projects. Refer to the following API documentation for additional information:

**Developer API:**

- [Legacy roles](/en/workato-api/roles): Manage roles that use the old permissions model.
- [Role migration](/en/workato-api/role-migration): Migrate roles from the old permissions model to the new model.
- [Environment roles](/en/workato-api/environment-roles): Manage roles that control access at the environment level.
- [Project roles](/en/workato-api/project-roles): Manage roles that control access at the project level.
- [Collaborator groups](/en/workato-api/collaborator-groups): Use groups to standardize and manage permissions for multiple collaborators at a time.
- [Project grants](/en/workato-api/project-grants): Manage project roles assignments.
- [Workspace collaborators](/en/workato-api/team): Manage collaborators and their privileges.

**Embedded API:**

- [Legacy roles](/en/oem/oem-api/roles): Manage roles that use the old permissions model.
- [Role migration](/en/oem/oem-api/role-migration): Migrate roles from the old permissions model to the new model.
- [Environment roles](/en/oem/oem-api/environment-roles): Manage roles that control access at the environment level.
- [Project roles](/en/oem/oem-api/project-roles): Manage roles that control access at the project level.
- [Collaborator groups](/en/oem/oem-api/collaborator-groups): Use groups to standardize and manage permissions for multiple collaborators at a time.
- [Project grants](/en/oem/oem-api/project-grants): Manage project roles assignments.
- [Customer workspace collaborators](/en/oem/oem-api/team): Invite collaborators to a customer workspace.
- [Manage customers](/en/oem/oem-api/managed-users): Manage customers and their workspace collaborators.

## Troubleshooting

A collaborator reports they lost access after SAML changes. What should I check?

Check the following in order:

- The [SAML configuration](/en/user-accounts-and-teams/role-based-access/access-control-v2#saml-and-scim-integration) includes the `workato_user_groups` parameter.
- The group names match exactly. These values are case-sensitive.
- The environment role names are correct in the `workato_role`, `workato_role_test`, and `workato_role_prod` parameters.
- The collaborator has logged in through SSO again after the configuration changes.

---

---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/migrate-roles.md
description: >-
  Migrate legacy collaborator roles to the new Workato access control model
  using the bulk-migration tool to create environment and project roles.
---

# Migrate to the new access control model

Workato's new access control model replaces collaborator roles with environment roles and project roles. This separation improves flexibility, clarity, and project-specific access control.

> **DEPRECATION NOTICE**
> 
> Legacy collaborator roles will be deprecated at the end of August 2026. Workato recommends that you complete your migration before this date to ensure uninterrupted access for all collaborators.

Using the bulk-migration tool follows a two-step process. The tool first generates a staged report at an individual-collaborator level that lists the new environment role each user receives, the collaborator groups they join, and the project roles they hold for each project. After you review the report, you can run the full migration.

The migration wizard analyzes all legacy collaborator roles, consolidates their permissions into new environment and project roles, and creates collaborator groups that reflect existing access patterns. It supports bulk migration, generates a summary report, and preserves equivalent access levels across your workspace.

## Bulk migrate all collaborator roles

Before you begin, verify that you have **Workspace admin** access.

Complete the following steps to migrate all of your roles in bulk:

1. Go to **Workspace admin > Access control > Collaborator roles**.
   
2. Click **Upgrade all** in the banner to open the migration wizard.
   
   ![Upgrade roles](/assets/upgrade-roles.BTEwLKX7.png)_Upgrade roles_
   
3. Review the overview of changes. The wizard demonstrates how the old model combines workspace, environment, and project privileges, and how the new model separates them into environment and project roles.
   
   ![Review new access control model](/assets/review-control-model.C91nOk0K.png)_Review new access control model_
   
4. Click **Next**.
   
5. Click **Generate report** to analyze your workspace's roles and collaborators.
   
   ![Generate summary report](/assets/generate-report.C3pgadOJ.png)_Generate summary report_
   
   Workato evaluates existing access patterns and emails you when the report is ready.
   
6. Click **Download report** to review the generated report. It provides a complete view of how your existing roles and collaborators map to the new model, including the following:
   
   - All legacy roles mapped to new environment and project roles
   - Newly created collaborator groups
   - Any custom role mappings preserved from the old model
   - Project-level assignments showing which groups manage which projects
   
   ![Review summary report](/assets/review-report.dv5yDJ0U.png)_Review summary report_
   
   You can also click **Regenerate** if you made permission changes.
   
   Refer to [How the migration wizard determines new roles and groups](#how-the-migration-wizard-assigns-new-roles-and-groups) to learn more about how roles and groups are mapped.
   
7. Click **Next** to proceed.
   
8. Review the following key reminders before you upgrade:
   
   - All collaborators maintain their current access levels.
   - You can adjust permissions and project access after migration.
   - The process typically takes 5–10 minutes.
9. Click **Upgrade**.
   
   ![Upgrade roles](/assets/upgrade-roles-2.lsWuZzlz.png)_Upgrade roles_
   
   Workato processes the upgrade in the background. You can leave the page and will receive an email notification when the upgrade completes.
   

A confirmation message appears when the migration completes. New collaborator groups appear under **People > Collaborator groups**.

## What changes after you migrate

Migration replaces your legacy collaborator roles with environment roles and project roles. The following behaviors change after you complete the migration.

### AHQ moderator assignment

You must select both an environment role and a project role when you create a new Automation HQ moderator. The environment role applies across all environments, and the project role applies across all projects in the managed workspace. This replaces the previous workflow where a single collaborator role controlled all access.

Refer to the [AHQ moderators and OEM customer managers](/en/user-accounts-and-teams/role-based-access/access-control-v2#ahq-moderators-and-oem-customer-managers) section for more information.

### Project access management

Collaborators no longer receive project access through their collaborator role. You manage project access through direct project role assignments or collaborator group memberships on the **Project settings > Project access** page.

### Collaborator groups

The migration wizard creates collaborator groups automatically based on shared access patterns. These groups centralize project-level permissions. You can rename, modify, or create additional groups after migration to match your team's organizational structure.

## Post migration

After migration, review your updated roles and collaborator groups to confirm that your workspace remains clear and organized. Rename duplicate role names or collaborator groups with similar access patterns to reduce confusion and improve ongoing access management.

### Update identity provider attributes

Update your identity provider if your organization uses SCIM or SAML role sync. The new access control model requires changes to the following SAML attributes:

- `workato_role`: Update this attribute to reference the new environment role name for your default environment. The value must match an existing environment role in your workspace.
- `workato_role_test`: Update this attribute to reference the environment role name for your test environment, if applicable.
- `workato_role_prod`: Update this attribute to reference the environment role name for your production environment, if applicable.
- `workato_user_groups`: Add this attribute to map collaborators to collaborator groups in Workato. The value must be a comma-separated string of group names. Workato replaces the user's group memberships with those listed in this attribute during each login or provisioning event.

Confirm that your SAML application passes these updated attributes and that the values match the role and group names in your Workato workspace. Refer to your identity provider-specific guide for detailed configuration steps:

- [Okta](/en/saml-role-sync-okta)
- [Microsoft Entra ID](/en/saml-role-sync-azure)
- [OneLogin](/en/saml-role-sync-onelogin)

### Inheritable roles in Automation HQ

If your organization uses inheritable roles created and shared through **Automation HQ**, you must migrate those roles in the Automation HQ workspace. The migration applies to every downstream workspace where that role is assigned. Downstream collaborator assignments update automatically to align with the new access control model.

> **CHILD WORKSPACE MIGRATION**
> 
> Child workspaces that have their own custom collaborator roles must initiate a separate bulk migration independently. Migrating roles in the Automation HQ workspace updates only inheritable roles. It doesn't migrate custom roles that were created directly in a child workspace. Each child workspace admin must run the migration wizard in their workspace to migrate locally created custom roles.

## How the migration wizard assigns new roles and groups

Workato's migration wizard automatically analyzes existing collaborator roles, permissions, and project access patterns. It uses this data to translate your legacy access model into the new environment and project structure while keeping permissions equivalent.

### Environment roles

The wizard compares each collaborator's permissions across the workspace and assigns one of the new environment roles:

| Legacy access pattern | New environment role | Description |
| --- | --- | --- |
| Full workspace-level permissions | Environment admin | Has full administrative control of the workspace. |
| Limited workspace access | Environment manager | Can manage most environment resources but not user access. |
| Recipe or project only permissions | Member | Can use resources in assigned projects only. |

Custom or cloned roles are preserved as equivalent custom environment roles with the same permission scope.

### Project roles

The wizard analyzes what collaborators could do in each project (for example, edit recipes, manage folders, run jobs). These permissions are converted into project-level roles that represent equivalent access:

| Legacy role | New project role | Description |
| --- | --- | --- |
| Admin | Project admin | Full control over the project, including managing collaborators and resources. |
| Analyst | Advanced builder | Can build, edit, and test recipes within the project. |
| Operator | Project operator | Can monitor and run recipes but not edit or manage settings. |

Each collaborator group receives one or more project roles per project. Collaborators inherit those permissions automatically through their group membership, ensuring they retain equivalent access after migration.

### Collaborator groups

The wizard creates collaborator groups automatically by analyzing which collaborators share the same access patterns across projects. These groups centralize project-level permissions and reduce ongoing maintenance.

Groups are named based on the new project role assigned to the group and the projects it can access. We recommend that you rename groups using the following syntax:

```text
{{Project}} | {{Project role}} | {{Environment}}
```

For example, `Reusable Assets | Viewers | DEV TEST`

The wizard creates numbered variants such as **Project admin (2)** when multiple legacy roles share identical permission levels but differ in project-scoped access.

Workato auto-generates a description for each group based on how the group formed during migration. For example, `Created during migration privilege group: DevOps Viewer.`

Each group's membership reflects the collaborators who previously shared the same project-level access, ensuring they retain equivalent permissions after migration.

## Best practices

Consider the following best practices when you migrate from legacy roles to the new access control model.

### Start with low-risk changes

Begin with low-impact or internal roles before you migrate sensitive or complex ones. This approach helps you validate role mappings and access behavior without disrupting critical projects.

### Review before you apply changes

Use the preview step in the migration wizard to confirm role assignments and project access before you apply any updates.

### Manage workspace-level access through DEV

Assign workspace-level admin privileges in the **DEV** environment. These permissions don't apply when assigned only in **TEST** or **PROD**. Treat **DEV** as the primary environment for global administration.

### Clean up and verify after migration

Review all environment and project roles after migration, consolidate duplicates, and verify collaborator access using the audit log.

---
