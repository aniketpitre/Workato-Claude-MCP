---
url: 'https://docs.workato.com/en/features/common-data-model.md'
description: >-
  Learn how the common data model defines a standard schema in Workato so
  integrations build on a canonical structure instead of individual apps.
---

# Common data model

The common data model, also known as the canonical data model or the abstract data model, is a standard schema that organizations define to simplify data flow and interaction between the different applications they use across the organization. This enables integrations to be built based on the common data model instead of being based on the application - and as a result, minimizes impact on organizations when they add, edit, or remove integrations and applications.

Refer to the following connector documentation for common data model use cases:

- [Java messaging service connector](/en/connectors/jms)
- [Mapper connector](/en/connectors/mapper)
- [Confluent Cloud](/en/connectors/confluent-cloud)
- [Kafka](/en/connectors/kafka)

## Access common data models

Go to **Tools > Common data models** to access common data models.

![Shared schema management](/assets/shared-schema-management.D9g2Y3hM.png)_Create and manage data models_

You can define a common data model manually or using JSON. Open an existing common data model and click **Edit Schema** to update the data structure.

![Edit a data model](/assets/editing-schema.DsgHP9R3.png)_Edit a data model_

## Common data models as project assets

Common data models are transitioning to [project assets](/en/projects#assets-page). Each common data model belongs to a folder or project and appears in the **Assets** view, similar to recipes and connections. This enables you to organize, tag, and manage common data models together with the assets that rely on them. Common data model names only need to be unique within a folder, so the same name can exist in different projects.

The **Default Common Data Models** project is the default storage location for existing common data models and for new common data models created without a specified location. Workato creates this project the first time it's needed and migrates common data models to it without recipe downtime. You don't need to preserve the **Default Common Data Models** project because Workato recreates the project as needed. Common data model creation is briefly blocked while its workspace is migrating.

> **DELETING A PROJECT WITH COMMON DATA MODELS**
> 
> Deleting a project or folder also deletes the common data models inside it.

Manage common data model assets using the following features:

### Access control

[Environment-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#tools) privileges control access to common data models before migration. [Project-level](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) privileges control access after migration.

How Workato migrates existing access depends on your workspace's permission model:

**Environment roles**

**Environment roles** ([RBAC 2.0](/en/user-accounts-and-teams/role-based-access/access-control-v2)): Workato creates a collaborator group and a project role for each access level, then assigns that project role on the **Default Common Data Models** project. Workato names these groups **Common Data Models user group {N}**, where `{N}` enumerates each group, and names the project roles based on their privilege level:

- **Common Data Models manager**: View, create, edit, and delete access
- **Common Data Models editor**: View, create, and edit access
- **Common Data Models viewer**: View access
- **Common Data Models: {privileges}**: Privilege sets not covered by the **manager**, **editor**, or **viewer** roles. For example: **Common Data Models: read, create**.

Workato skips environment roles without any collaborators, and environment roles with the same access level share one project role. Name clashes get a numbered suffix, for example: **Common Data Models viewer (2)**.

Built-in [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) also include the **Common data models** permission:

- **Advanced builder** and **Project admin**: View, create, edit, and delete access
- **Builder**: View, create, and edit access
- **Project operator**: View access

**Legacy roles**

**Legacy roles** ([RBAC 1.0](/en/roles)): Collaborators keep access through the migrated **Default Common Data Models** project and the new project-level **Common data models** permission. You must update permissions to maintain collaborator access if you move a common data model out of the **Default Common Data Models** project.

#### Customer managers and workspace moderators

This migration applies to all collaborator types, including [customer managers](/en/oem/admin-console/customer-managers) and AHQ [workspace moderators](/en/ahq-workspace-moderator).

A customer manager's or workspace moderator's existing project role gains the permission directly if every user assigned to that role has the same access level. Workato doesn't update a role directly if it contains multiple access levels, is used for project access grants, is built-in, or was migrated from a legacy role. Workato instead creates a copy of the role with the permission added. For example: **Project admin (Common Data Models)**.

### Deployment

Packages include common data models and their storage location. This allows you to move common data models between folders and environments. Workato stores a common data model exported before this migration in the **Default Common Data Models** project during import into the root. Refer to [Importing assets](/en/recipe-development-lifecycle/import) for more information.

### API endpoints

The following endpoints no longer return the environment-level **Common data models** privilege in their response after a workspace migrates to project-level permissions:

- [Developer API](/en/workato-api/environment-roles) and [Embedded API](/en/oem/oem-api/environment-roles) environment roles endpoints: The `workato_schema` key disappears from the `config` object.
- [Developer API](/en/workato-api/team#get-privileges) and [Embedded API](/en/oem/oem-api/managed-users#get-list-of-customer-privileges) **Get privileges** endpoints: The **Common data models** key disappears from each environment's `privileges` object for environment roles.

### Activity tracking

The [activity audit log](/en/features/activity-audit-log-reference#common-data-model-activities) records common data model actions, such as when a common data model moves between projects.

---
