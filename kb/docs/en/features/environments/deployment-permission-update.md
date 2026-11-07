---
url: >-
  https://docs.workato.com/en/features/environments/deployment-permission-update.md
description: >-
  Learn how the Workato Deployment permission controls who can deploy projects
  across environments and how admins enable it for custom roles.
---

# Environment deployment permission update

Starting on December 12, 2023, Workato is introducing a new **Deployment** permission. The Deployment permission determines access to project [deployments](/en/features/environments/deployment) across [environments](/en/features/environments).

To deploy a project to an environment, you must have this permission enabled in both the DEV environment and the target environment.

This replaces the previous requirement of having the [Recipe lifecycle management permission](/en/privileges#recipe-lifecycle-management) enabled in the Development (DEV) environment and having any access in the target environment to deploy to it.

## Role permissions

The Deployment permission is enabled for [system roles](/en/roles#system-roles) and [custom roles](/en/roles#custom-roles) as follows:

- **Admin:** Enabled
- **Analyst:** Enabled
- **Operator:** Disabled
- **Custom:** Disabled until an admin manually enables it

> **LOSS OF ACCESS FOR CUSTOM ROLES**
> 
> All collaborators with existing custom roles _will lose access to deployment functionality_ as a result of this change. Admins can restore access for these collaborators by updating the custom role(s) to enable the Deployment permission in the appropriate environments.
> 
> If you do not have access to the **Deployments** tab for a project, ask your admin to update your permissions.

## Why is this change important?

This security enhancement provides better control over who can deploy to production or test environments by separating deployment permissions from recipe lifecycle management permissions.

## How to enable the Deployment permission for a custom role

If you are an administrator and you plan to enable the Deployment permission for a given custom role, complete the following steps:

1. Navigate to **Workspace admin > Access control** and select **Collaborator roles**.
   
2. Select the custom role you plan to update.
   
3. Select the **Recipe development** tab.
   
4. Select the **Deployment** checkbox in the **Deployment** section.
   
   ![Deployment permission](/assets/new-deployment-permission.TcXp9bFR.png) _Deployment permission_
   
5. Select **Save changes**.
