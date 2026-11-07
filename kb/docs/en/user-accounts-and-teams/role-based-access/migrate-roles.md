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
