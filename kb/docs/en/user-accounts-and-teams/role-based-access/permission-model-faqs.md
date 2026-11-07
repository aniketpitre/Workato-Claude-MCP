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
