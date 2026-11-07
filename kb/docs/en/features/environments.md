---
url: 'https://docs.workato.com/en/features/environments.md'
description: >-
  Environments let your team plan, test, and deploy automation projects across
  development, test, and production with built-in change management.
---

# Environments

Environments enable your team to easily plan, test, and deploy automation projects. This feature simplifies applying Software Development Lifecycle (SDLC) best practices to your automation.

> **FEATURE AVAILABILITY**
> 
> Environments are available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> Learn more about [enablement for Embedded partners](/en/features/environments#how-do-i-get-it) and [Environments for Embedded customers](/en/oem/embedded-environments).

* * *

## Environment basics

### What is it?

The **Environments** feature simplifies the project lifecycle process by integrating dedicated environments into your Workato workspace. With Environments, you have built-in access to development, test, and production environments. Each environment includes a set of assets, members, and projects. Projects can include recipes, connections, lookup tables, and other asset types.

Projects can be quickly and easily deployed from one environment to another, ensuring the focus is on collaboration and recipe quality, not maintenance.

### What's included in Environments?

- **Robust change management** - Builders can safely create and experiment in your **Development (DEV)** environment, and QA teams can review and test in your **Test (TEST)** environment. Once you've tested your changes, deploy them to **Production (PROD)** with confidence.
- **Compliance and auditability** - Manage who can build, test, and deploy automations with [collaborator roles](#collaborator-access). View a complete deployment history and roll back to a previous deployment at any time.
- **Business-friendly user experience** - Manage change entirely within the Workato platform. No need for JSON manifests, git, or scripting tools.
- **CI/CD compatibility** - Use Workato's [platform APIs](/en/workato-api/projects) to integrate Workato into any existing CI/CD process.

### What environments will I have?

Workspaces with the Environments feature enabled will have the following environments automatically provisioned:

| Environment | Description |
| --- | --- |
| **Development (DEV)** | Used for recipe development; Used to deploy projects to other environments, including PROD; Used to maintain teams and the account, including collaborator roles, projects, folders, etc. |
| **Test (TEST)** | Used to test recipes in development |
| **Production (PROD)** | Used to run recipes that have been tested, reviewed, and approved |

> **DEFAULT ENVIRONMENT SETTING**
> 
> When you enable the Environments feature, your existing workspace automatically becomes a **Development (DEV)** environment by default. To set your existing workspace as a **Production (PROD)** or **Test (TEST)** environment, contact your Customer Success Manager before enabling this feature.
> 
> After enabling Environments, use [deployments](/en/features/environments/deploying-projects-to-an-environment) to make your recipes available in different environments and follow the recipe development lifecycle.

Refer to the [Environment structure section](#environment-structure-and-planning) for more info.

### How will environments affect my usage?

Usage is calculated across all environments in your account and includes billable recipes, tasks, or a combination of the two.

Using the [Dashboard and Subscription plan pages](#how-do-i-monitor-my-usage), you can view usage by environment or across all environments.

### How do I monitor my usage?

There are two ways you can check your usage:

- **Using the Dashboard:** Navigate to the **Operations hub** page to view metrics for the current environment and a high-level usage summary across all environments. When viewing this page, note that:
  
  - The **Plan usage** section summarizes your usage across all of your environments
  - All other sections and graphs reflect usage in the current environment
- **Using the Subscription plan page**: This page, available only in the Development environment, summarizes your usage across all environments over time. Navigate to [**Settings > Subscription plan**](https://app.workato.com/users/current/edit/subscription?utm_source=docs&utm_medium=referral&utm_campaign=back-to-app&utm_content=environments) to access this page.
  

### How do I get it?

The Environments feature is available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more. How the feature is enabled depends on whether you're a new or existing Workato customer:

- **If you're a new customer** after December 22, 2021, Environments will be automatically enabled in your workspace.
- **If you're an existing customer**:
  - With multiple existing workspaces, contact your Customer Success Manager to initiate a migration request.
  - Purchasing new workspaces, Environments are automatically enabled in the new workspaces.

* * *

## Environment structure and planning

A typical software lifecycle uses three environments: One for development, one for staging and testing, and one for live production use.

Workato Environments uses separate but linked environments in your workspace to create a similar structure for recipe development:

![Structure of standard environments in a workspace: Dev, Test, and Production](/assets/environments-structure.CPhsUs9H.png)

Projects and assets are deployed to other environments from the **Development** environment. Changes to automations should only be made in the **Development** environment to ensure modifications are captured and tracked accurately. Although you can change automations in the **Test** environment, we recommend changing automations in the **Development** environment only due to SDLC best practices.

For example: A recipe in the **Development** environment is ready for testing. It's deployed to the **Test** environment where the recipe runs and is tested. Issues are reported as needed and addressed in the **Development** environment.

To create a structured and predictable lifecycle management process, we recommend that you:

- **Define the criteria for promoting automations through the process.** For example: What tests must be completed before assets can be moved to **Production**?
- **Identify the teams participating in the process.** What roles and responsibilities do these teams have? For example: Who will develop recipes? Who will test or deploy them?

* * *

## Collaborator access

Access to each environment [must be granted individually](/en/user-accounts-and-teams/role-based-access/managing-environment-access). **Note**: A collaborator must have access to at least one environment.

Where collaborators land when they sign into the workspace depends on the environments they have access to:

- If they have access to **Development**, they'll land in **Development** regardless of other environment access.
- If they have access to **Test** but not **Development**, they'll land in **Test**.
- If they have access to **Production** but not **Development** or **Test**, they'll land in **Production**.

After they sign in, collaborators can switch between the environments they have access to by opening the side nav and clicking the name of the environment.

Refer to the [Managing environment access](/en/user-accounts-and-teams/role-based-access/managing-environment-access) documentation for more information.

* * *

## Deploying assets

In Workato, deployment is a process that pushes projects and assets from one environment in a workspace to another environment as part of the recipe development lifecycle (RDLC).

Recipes are typically developed in **Development**, moved to **Test** when they're ready for review, and then finally moved to **Production** after testing and approval.

> **WHO CAN PERFORM DEPLOYMENTS?**
> 
> Collaborators must have the [deployment privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-settings) enabled in both the Development environment and the target environment (Test or Production) to deploy assets. For more information, refer to the [Understanding project deployment with environments](/en/features/environments/deployment) documentation.

Refer to the [Understanding project deployment with environments](/en/features/environments/deployment) documentation for more information. In Workato Environments, you can either deploy projects and assets from **Development** to **Test**, or from **Development** to **Production**. If you want to deploy your projects and assets in a different way, see [Export: packaging recipes and dependencies](/en/recipe-development-lifecycle/export).

* * *

## What's next?

Ready to dive into Environments? Check out these resources to get started:

- [Environments best practices](/en/features/environments/best-practices)
- [Learn about deploying assets](/en/features/environments/deployment)
- [Learn about collaborator access](/en/user-accounts-and-teams/role-based-access/managing-environment-access)

---
