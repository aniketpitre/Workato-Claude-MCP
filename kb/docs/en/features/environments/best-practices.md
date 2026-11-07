---
url: 'https://docs.workato.com/en/features/environments/best-practices.md'
description: >-
  Learn best practices for using Workato Environments, including asset
  organization, connection management, and collaborator access.
---

# Best practices for using Environments

This guide provides tips on the following topics when working with [Environments](/en/features/environments):

> **FEATURE AVAILABILITY**
> 
> This guide is applicable to accounts with the [Environments](/en/features/environments) feature enabled. Environments is available for direct and Embedded users. Learn more about [Environments for Embedded customers](/en/oem/embedded-environments).

* * *

## Asset organization

We recommend organizing assets that you want to release together - such as recipes and connections - together into projects.

As it's only possible to deploy a single project at a time, this approach reduces the likelihood of missing dependencies.

Check out the [Recipe Functions (Dependency) Management section](#recipe-function-dependency-management) for guidance on managing reusable recipe dependencies.

* * *

## Connection management

When working in the Development and Test environments, we strongly recommend using a sandbox version of your applications to create connections. Using a sandbox ensures that live data isn't altered by accident.

Workato keeps recipe logic intact between environments even after deployment. When you deploy a connection to an environment for the first time or when the connection changes, you'll be prompted to re-connect the connection in the environment.

This allows you to use test data for development and testing, ensuring production data is touched after recipes have been vetted.

* * *

## Collaborator access

One of the key benefits of environments is that it securely enables collaboration while ensuring mission-critical recipes don't change without notice.

To get this benefit, we recommend a tiered approach to collaborator access:

- **Development** access for **all** collaborators
- **Test** access for **some** collaborators
- **Production** access for a **few** collaborators

By limiting access, you can allow your team to build and collaborate without risking accidental changes to production.

Refer to the [Managing Environment access guide](/en/user-accounts-and-teams/role-based-access/managing-environment-access) for more info about granting environment access.

* * *

## Recipe function (dependency) management

While we recommend [organizing assets as a unit into top-level projects](#asset-organization), you can still develop recipes that use re-use recipes with some best practices.

If using [Recipe functions](/en/connectors/recipe-functions), we recommend organizing the recipes into their own project. This approach to organization allows you to easily manage the lifecycle of these recipes independent of the recipes that depend on them.

To deploy these assets, you can:

1. Create a project to contain all Recipe functions.
   
2. Build and develop Recipe functions within this project.
   
3. Deploy the Recipe functions project to the target environment.
   
4. Deploy the dependent projects to the same target environment. Once the dependent projects are deployed, errors from missing dependencies will be automatically resolved.
   

* * *

## Resources

- [Environments overview](/en/features/environments)
- [Managing environment access](/en/user-accounts-and-teams/role-based-access/managing-environment-access)
- [Understanding project deployment](/en/features/environments/deployment)

---

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

---
