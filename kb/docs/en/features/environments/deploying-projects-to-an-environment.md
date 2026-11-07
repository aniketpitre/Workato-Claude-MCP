---
url: >-
  https://docs.workato.com/en/features/environments/deploying-projects-to-an-environment.md
description: >-
  Deploy a project from Development to Test or Production in Workato, customize
  the deployment, review changes, and re-establish connections.
---

# Deploy a project to an environment

You can only deploy from Development to Test and from Development to Production.

```mermaid
graph LR
    A(Development) --> B(Test)
    classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
```

```mermaid
graph LR
   A(Development) --> B(Production)
   classDef default fill:#67eadd,stroke:#b3e0e1,stroke-width:2px,color:#000;
```

This guide outlines the following steps:

- [Deployment prerequisites](#prerequisites)
- [Set up the deployment](#set-up-the-deployment)
- [Customize the deployment](#customize-the-deployment)
- [Review changes](#review-changes)
- [Add details](#add-details)
- [Review and finalize deployment](#review-and-finalize-deployment)
- [Deploy from the recipe page](#deploy-from-the-recipe-page)
- [Re-establish connections](#re-establish-connections)

> **FEATURE AVAILABILITY**
> 
> Environments are available to customers on specific pricing plans. Refer to your pricing plan and contract to learn more.
> 
> Learn more about [enablement for Embedded partners](/en/features/environments#how-do-i-get-it) and [Environments for Embedded customers](/en/oem/embedded-environments).

* * *

## Prerequisites

Ensure you have the following prerequisites to deploy a project to an environment:

- A Workato account with the [Environments](/en/features/environments) feature enabled.
- Access to the project you plan to deploy.
- The [deployment privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-settings) enabled in the main (Development) environment. You can only deploy projects from this environment.
- The [deployment privilege](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-settings) enabled in the environment where you plan to deploy the project.

> **SINGLE ENVIRONMENT ACCESS**
> 
> You cannot deploy projects if you only have access to one environment.

* * *

## Set up the deployment

Complete the following steps to set up your deployment:

1. Sign in to your Workato account.
   
2. Go to the main **DEV** environment.
   
3. Open the project you plan to deploy and click the **Deployments** tab.
   
4. Click **Deploy to**. The following options appear in the drop-down:
   
   - **TEST**
   - **PROD**
   - **Download**. This option creates a [ZIP file of the project](/en/features/environments/deployment#downloading-a-project-package).
   
   ![Deploy to environment](/assets/deploy-to.C9AQDAzg.png)_Deploy to environment_
   

Why can I only deploy from the Development environment?

You can only deploy projects from the **Development** environment because the **Test** and **Production** environments are designed for specific purposes:

- Use the **Test** environment to test recipes.
- Use the **Production** environment to run finalized recipes.

This restriction ensures consistency, prevents conflicts, and provides a complete, traceable deployment history in your project's **Deployments** tab.

* * *

## Customize the deployment

After initiating the deployment, a popup appears, allowing you to customize the deployment:

1. Choose whether to select all assets or customize the deployment by selecting individual assets.
   
2. Select or clear the checkbox next to each asset to specify which assets you plan to include in the deployment.
   
   ![Customize deployment](/assets/customize-deployment.CkYRQhZJ.png)_Customize deployment_
   
3. Select or clear the checkboxes to include or exclude test cases.
   
4. Ensure that all dependent assets are included. If any dependencies are missing, a warning displays indicating the missing dependencies.
   
5. Click **Next** to review your changes.
   

> **DEPLOYING CONNECTIONS**
> 
> When deploying connections for the first time, you must [reconnect them in the target environment](#re-establish-connections) before recipes can run, regardless of the deployment type you select.

* * *

## Review changes

Next, complete the following steps to review the changes calculated and displayed by Workato:

1. Review the list of assets added or updated in the interface.
   
   ![Deployments tab](/assets/review-changes.D0c-o57a.png)_Review changes_
   
2. Click **Customize** to go back and make further adjustments, if required.
   
3. Click **Next** to [add details](#add-details) to your deployment after reviewing the changes.
   

Refer to the [Understanding project deployment with environments](/en/features/environments/deployment#how-are-updates-made-in-the-target-environment) guide to learn more about how changes are detected.

* * *

## Add details

After reviewing the changes, you can add the necessary details for your deployment:

1. Provide a name for your deployment in the **Deployment name** field. This name is used in the deployment history tab.
   
   ![Add deployment details](/assets/add-details.j2BfRCTj.png)_Add deployment details_
   
2. Summarize the changes for this version of the project in the **Description** field.
   
3. Click **Deploy** to initiate the deployment.
   

* * *

## Review and finalize deployment

After Workato deploys the changes, complete the following steps to review and finalize the deployment:

1. Click **View project in \[ENVIRONMENT\]** to review the deployment in the relevant environment.
   
   ![View deployment](/assets/view-deployment.CbbokeYF.png)_View deployment_
   
2. Navigate to the **Deployments** tab to check the status of the deployment or to redeploy if necessary.
   
3. Use the **Deploy to** drop-down to deploy the project again to a different environment or download the package.
   
   ![Deploy again](/assets/deploy-again._3RiyxGh.png)_Deploy again_
   

* * *

## Deploy from the recipe page

You can deploy recipes directly from the recipe page with deployment permissions. This feature streamlines the deployment process and enables you to efficiently manage urgent updates.

### Prerequisites

Complete the following prerequisites before deploying from the recipe page:

- Ensure you have [deployment privileges](/en/user-accounts-and-teams/role-based-access/managing-environment-access#managing-environment-access) in both the source and target environments.

### How to deploy an asset from the recipe page

Complete the following steps to deploy directly from the recipe page:

1. Open the recipe you plan to deploy.
   
2. Click the **Deploy to** button at the top of the recipe page.
   
   ![Deploy from the recipe page](/assets/deploy-recipe-page.BRIEusH2.png)_Deploy from the recipe page_
   
3. Select the target environment from the drop-down menu. Only environments where you have deployment privileges are available.
   
4. Review the deployment popup where the current asset is pre-selected. Dependent assets are automatically selected by default.
   
   > **REVIEW DEPENDENT ASSETS**
   > 
   > Review the dependent assets and customize the selection if needed to ensure only the necessary assets are included in the deployment.
   
   ![Customize assets](/assets/customize-assets.BDs6YAzk.png)_Customize assets_
   
5. Click **Next**, [review](#review-changes) the changes, [add details](#add-details), and click **Deploy** to complete the deployment.
   

After deployment, you can click **View project in \[ENVIRONMENT\]** to [review the deployment](#review-and-finalize-deployment) in that environment.

* * *

## Re-establish connections

Deploying a project maintains [dependent relationships in recipes](/en/features/environments/deployment#how-are-recipe-dependencies-handled). However, you must reconnect connections in the target environment the first time they are deployed. Recipes won't run until you re-establish connections.

In the target environment, re-establish connections to ensure recipes run successfully.

> **SANDBOX CREDENTIALS**
> 
> Use [sandbox credentials](/en/features/environments/best-practices#connection-management) when working in a non-production environment as a best practice.

* * *

## Resolve post-deployment errors

If you encounter an error message such as `503 Service unavailable` after deploying a project to the target environment and starting a recipe, you must refresh the recipe's schema. This allows you to fix any broken external dependencies.

Complete the following steps to refresh the recipe schema:

1. Sign in to your Workato account.
   
2. Open the side panel and click your profile icon.
   
3. Select the environment you deployed the project to.
   
4. Select the project and the recipe where the error occurred.
   
5. Select **Edit recipe**.
   
6. Select **Refresh** to refresh the recipe schema.
   
   ![Select the Refresh button](/assets/refresh-schema.DpUX90Q6.png) _Select Refresh to refresh the recipe schema_
   
7. Resolve any [design-time recipe errors](/en/recipes/design-time-errors) that Workato identifies. Fields with errors are outlined in red.
   
8. Click **Save** to save your changes.
   

* * *

## Resources

- [Environments overview](/en/features/environments)
- [Environments best practices](/en/features/environments/best-practices)
- [Understanding deployment](/en/features/environments/deployment)
- [Managing environment access](/en/user-accounts-and-teams/role-based-access/managing-environment-access)
