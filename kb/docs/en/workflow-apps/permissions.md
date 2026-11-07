---
url: 'https://docs.workato.com/en/workflow-apps/permissions.md'
description: >-
  Learn how role-based access control governs who can build, manage, and
  configure Workflow apps and Workflow apps portal settings in Workato.
---

# Permissions

The ability to configure and create Workflow apps is determined by [role based access control (RBAC)](/en/user-accounts-and-teams/role-based-access/#how-role-based-access-control-works):

In the new permissions model, the following [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) have full permissions to build, manage, and configure Workflow apps and Workflow apps portal settings:

- **Project admin**
- **Advanced builder**
- **Builder**

In workspaces using the legacy permissions model, the [Admin](/en/roles#role-admin) and [Analyst](/en/roles#role-analyst) system roles provide similar full access by default.

You can also assign granular Workflow apps permissions by creating a custom role in **Workspace admin > Access control > Project roles**. This allows you to separate the permissions for building and managing Workflow apps. For example, you can create a role that allows users to create Workflow apps, but prevents them from modifying Workflow apps portal settings. This guide describes the permissions necessary to perform the following tasks:

- [Create Workflow apps pages](#minimum-permissions-create-page)
- [Create Workflow apps](#minimum-permissions-create-app)
- [Configure Workflow apps](#minimum-permissions-configure)
- [Configure Workflow apps portal settings](#portal-users-manage)
- [Configure Workflow apps users and groups](#portal-users-manage)

> **DATA TABLES PERMISSIONS**
> 
> Access to Workflow apps also depends on the type of access your role has to [data tables](/en/data-tables).

* * *

## Minimum permissions to create Workflow apps pages

Consider a situation where you plan to enable a user to create Workflow apps [pages](/en/workflow-apps/pages-create) but do not plan for them to have permission to create new Workflow apps.

In this scenario, you can create a custom role with the following minimum permissions:

**Recipe development > Projects**: View and Edit

**Recipe development > Workflow apps > App development**: Full access

* * *

## Minimum permissions to create a Workflow app

The following minimum permissions are required to create a Workflow apps:

**Recipe development > Workflow apps > App development**: Full access

**Recipe development > Recipe creation > Projects**: Create

* * *

## Minimum permissions for managing Workflow apps access

The following minimum permissions are required to manage Workflow apps access:

**Recipe development > Workflow apps > App access and role management**: Full access

**Recipe development > Data storage > Data tables**: Full access

* * *

## Permissions to configure Workflow apps portal settings

The following permission enables you to configure Workflow apps portal settings:

**Platform tools > Apps portal > Settings**: Full access

* * *

## Permissions to manage Workflow apps portal users

The following permission enables you to manage Workflow apps portal users and groups **_from the user interface_**:

**Platform tools > Apps portal > Users and groups**: Full access

* * *

> **FURTHER READING**
> 
> Read more about [environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles), [project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles), and [privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference).

---
