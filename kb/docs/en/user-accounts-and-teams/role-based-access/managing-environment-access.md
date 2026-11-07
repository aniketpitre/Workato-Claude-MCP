---
url: >-
  https://docs.workato.com/en/user-accounts-and-teams/role-based-access/managing-environment-access.md
description: >-
  Manage collaborator access to Workato DEV, TEST, and PROD environments by
  assigning environment and project roles with role-based access control.
---

# Manage environment access

You can manage collaborator access to environments using [role-based access control](/en/user-accounts-and-teams/role-based-access/). Roles provide maintainable and consistent access control by allowing you to configure permissions for multiple collaborators at once.

This guide covers the following topics:

- [Manage roles across environments](#manage-roles-across-environments)
- [Grant environment access](#grant-environment-access)
- [Revoke environment access](#revoke-environment-access)
- [Resources](#resources)

> **WHO CAN USE THIS FEATURE?**
> 
> This guide is applicable to accounts with the [Environments](/en/features/environments) feature enabled. Environments is available for direct and Embedded users. Learn more about [Environments for Embedded customers](/en/oem/embedded-environments).
> 
> You must have one of the following in your main workspace (**DEV**) to perform the tasks in this guide:
> 
> - The [Environment admin](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin) role or legacy [Admin](/en/roles#role-admin) system role
> - [Admin privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#admin-privileges)

* * *

## Manage roles across environments

In the new permissions model, you manage collaborator access using environment roles and project roles. Roles are assigned per environment, so the same collaborator can have different levels of access based on their responsibilities in DEV, TEST, and PROD environments.

For example, a member of the center of excellence team might need:

- **Environment admin** in the main environment (**DEV**) to access workspace management features such as SAML authentication.
- **Environment manager** in **TEST** to configure platform tools like OAuth profiles or message templates, without workspace-wide access.
- **Member** in **PROD**, since they don't need to manage any environment-level tools or settings there.

Here's how this would look in Workato for that collaborator:

![Assigning different environment roles to the same collaborator across DEV, TEST, and PROD environments.](/assets/environment-role-assignment.DgylVVEO.png)

If a role needs to be updated or deleted, you'll do so in the main environment (**DEV**). Collaborators with the **Environment admin** role in **DEV** can also see the **Workspace admin** page in **TEST** and **PROD**, regardless of their role in those environments.

* * *

## Grant environment access

Assigning a role for an environment to a collaborator also grants them access to the environment.

To grant access to an environment for a collaborator:

1. Go to [**Workspace admin > Access control > Collaborators**](https://app.workato.com/members/collaborators?utm_source=docs&utm_medium=referral&utm_campaign=back-to-app&utm_content=team) in the (**DEV**) environment of your Workato account.
   
2. Click on the collaborator you want to modify. This will open the **Edit collaborator** page.
   
3. Locate the environment you want to grant access to. For example: **TEST**
   
4. In the **Role** menu below the environment, select the collaborator's role for that environment. **To prevent or remove access to the environment**, select **No access**.
   
5. Click **Update**.
   

* * *

## Revoke environment access

To revoke access to an environment for a collaborator:

1. Go to [**Workspace admin > Access control > Collaborators**](https://app.workato.com/members/collaborators?utm_source=docs&utm_medium=referral&utm_campaign=back-to-app&utm_content=team) in the (**DEV**) environment of your Workato account.
   
2. Click on the collaborator you want to modify. This will open the **Edit collaborator** page.
   
3. Locate the environment you want to revoke access from. For example: **TEST**
   
4. In the **Role** menu below the environment, select **No access**.
   
5. Click **Update**.
   

* * *

## Resources

- [Environments](/en/features/environments)
- [Role-based access control](/en/user-accounts-and-teams/role-based-access/)
- [Environment roles](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles#environment-admin)
- [Project roles](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles)
- [Privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference)
