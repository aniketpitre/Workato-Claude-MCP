---
url: 'https://docs.workato.com/en/oem/embedded-environments/environment-roles.md'
description: >-
  Assign collaborator roles and deployment permissions for each Embedded
  Environment to control access across Development, Test, and Production.
---

# Collaborator roles and Environments

You can assign specific permissions to each collaborator and customize roles for each environment as needed after you provision Environments for a customer. A collaborator's permission level determines which elements are visible to them. There are two permissions most relevant for Environments, both of which can be independent:

- Access to an environment
- Deployment permissions within an environment

For example, a collaborator could have access to an environment without having the ability to deploy a project. The following image displays the UI for a collaborator with deployment permission for the Development and Production environments, but no deployment permission for the Test environment.

![No deploy permission](/assets/deployment-two-environments.Ba_fB57z.png)_Deployment permission in two environments_

> **CUSTOMER MANAGER ASSIGNED ROLES**
> 
> The role you assign applies to this customer manager in all customer workspaces and across all three environments (Development, Test, and Production) by default.
> 
> If you plan to provide different collaborator roles for each environment, you must add the collaborator individually to each Customer workspace (not as a Customer manager), and then specify the collaborator role for each environment. You can assign these roles in the user interface or through the Workato API.

## Deployments tab

The **Deployments** tab is only visible to collaborators that have access to two or more environments with deployment permission in at least two environments they have access to.

![No deployments tab](/assets/deployments-tab-not-visible.8Hcww8fM.png)_Deployments tab not visible_

![Deployments tab](/assets/deployments-tab.2iT_WOuC.png)_Deployments tab visible_

## Add deployment permission to a project role

Complete the following steps to grant deployment permission to a project role:

1. Log in to your Workato account and select the workspace where you plan to manage deployment permissions.
   
2. Click **Workspace admin > Access control > Project roles**.
   
3. Select an existing role or click the **Add project role** to create a new role.
   
4. Scroll down to the **Project settings** privileges and enable the appropriate permissions:
   
   - **Approve deployment**: Grants the ability to approve deployment requests.
   - **Review deployment**: Grants the ability to review deployment requests before approval.
5. Click **Save changes** when finished.
   

> **LEGACY PERMISSIONS MODEL**
> 
> In workspaces using the legacy permissions model, deployment access is granted by default to the **Admin** and **Analyst** system roles.

---

---
url: >-
  https://docs.workato.com/en/oem/embedded-environments/embedded-environments-faq.md
description: >-
  Answers to common questions about Embedded Environments, including deployment
  access, environment roles, and collaborator permissions.
---

# Embedded Environments FAQs

Get answers to frequently asked questions (FAQs) about Environments for Embedded customers.

Who can access the Deployments tab?

The **Deployments** tab is accessible for the Embedded Partner (EP) and collaborators with permission. Refer to [Embedded Environments](/en/oem/embedded-environments/environment-roles) roles for more information.

Who can access different environments?

Access to each environment can be defined for a collaborator. It is possible to assign a different role for each environment. Refer to [Embedded Environments](/en/oem/embedded-environments/environment-roles) roles for more information.

Who can make deployments to another environment?

A user must have deployment permission on both the origin and target environment to make a deployment. Refer to [Embedded Environments](/en/oem/embedded-environments/environment-roles) roles for more information.

Can a collaborator deploy to an environment they don’t have access or deployment access to?

No. A collaborator must have access to at least two environments to view the [Deployments tab](/en/oem/embedded-environments/deploy-environment), and deployment permission in both environments.

If a collaborator has deployment access on two environments, they can only choose one environment as a target. Whenever the collaborator is logged into an environment in which they do not have deployment permission, they cannot access the **Deployments** tab.

> **ENVIRONMENT ACCESS**
> 
> The Embedded Partner (EP) manages access to different environments (Development, Test, Production) within an Embedded Customer's (EC) workspace through their UI in a fully embedded environment. The EP is responsible for generating new JWT tokens to enable seamless switching between environments without compromising security. This ensures that ECs can only access the environments they are permitted to, maintaining the integrity of each environment's operations.

What happens when importing an SDK source code using RLCM in Development (package including connector)?

The connector becomes exclusively available in the current environment. It does not appear in other environments unless [deployed](/en/oem/embedded-environments/deploy-environment).

> **SHARED CONNECTORS**
> 
> We encourage partners to use shared connectors for a better and unified experience.

What occurs during a deployment from Development to Production or Test for an SDK Connector?

If the [SDK connector](/en/developing-connectors/custom-connector#connector-sdk) is selected to be included in the deployment package, the connector, along with any updates or source code changes, is successfully included in the Production or Test environment. Each environment has distinct connector IDs, indicating separate instances. The SDK connector displays under **Tools**\> connector SDK for each environment where it is available.

How does installing an SDK Connector through a sharing link affect its availability?

Installing the [SDK connector](/en/developing-connectors/custom-connector#connector-sdk) in the customer’s Development workspace through a sharing link makes it available as a private connector in Development. Without the connector, importing the package fails. The connector is not initially present in other environments after installation.

Installation with a private link makes the connector available in the current environment. Without the connector, importing a package that uses it fails. The connector is not initially present in other environments after installation.

How does editing the connector version in Development impact Production?

Modifying the version in Development does not affect the version in Production. However, [deploying a new version](/en/oem/embedded-environments/deploy-environment#deployments-workflow) from Development to Production updates the connector in Production, maintaining the same ID.

What behaviors have been observed SDK Connectors across environments?

Connectors operate independently between Development, Test, and Production. Deployment transfers connectors with updates, maintaining consistency. Additionally, using a private link for sharing the connector matches the behavior observed with [RLCM](/en/oem/oem-api/recipe-lifecycle-management#recipe-lifecycle-management) imports.

What happens to Lookup Tables when deploying a project?

[Lookup Tables](/en/oem/oem-api/lookup-tables#lookup-tables) are included in the deployment package regardless of the table scope (global or project). Lookup Table content is only included in the deployment if you choose to include this data.

How can I migrate my customers without losing data?

You can [migrate customers](/en/oem/embedded-environments/migrate-embedded-environments#migration) without data loss by using the provision button in the Workato UI. This method assigns Environments to a specific customer. Recipes continue to run as usual. Initially, your existing workspace becomes your Development environment, and you must manually move it to Production if necessary.

How will the connection-based pricing be affected?

Introducing the [Environments feature](/en/oem/embedded-environments) with Development, Test, and Production environments does not impact connection-based pricing. A connection is only counted once, regardless of whether it's authenticated in one or all three environments. This ensures our pricing remains fair by counting each connection a single time. This aligns with our commitment to straightforward and equitable billing practices.

Is the Environments feature compatible with Fully Embedded implementations?

Yes. The Environments feature is fully compatible with [Fully Embedded](/en/oem/workato-embedded#workato-fully-embedded) setups. Behind the scenes, each environment corresponds to a different `managed_user_id`. In Fully Embedded configurations, where the navigation bar is hidden, you must generate three different JWTs. Additionally, you can specify different origin URLs for each environment. This allows you tailor integration across your Development, Test, and Production stages.

How does Environments work with Embedded APIs?

Each environment is associated with a unique `managed_user_id`. You must use the appropriate `managed_user_id` in the API endpoint to interact with the [Embedded APIs](/en/oem/oem-api#authentication) for a specific environment (Development, Test, or Production). For example, you can use endpoints such `.../managed_user/:managed_user_id_dev/` or `.../managed_user/:managed_user_id_prod/` to access the corresponding environment's data and settings.

Is the Environments feature compatible with the Connection Widget?

Yes. The [Connection Widget](/en/oem/workato-embedded-implementation#connection-widget) is compatible with the Environments feature. You must specify the [correct ID](/en/oem/embedded-environments/embedded-environments-api#how-to-get-the-correct-id) and `connection_id` corresponding to the environment (Development, Test, or Production) you plan to use when you select the widget to authenticate connections.

Is the Environments feature compatible with the Admin workspace or only with Customer workspaces?

The [Environments feature](/en/oem/embedded-environments) is enabled only for Customer workspaces. Although the Admin workspace does not yet support this feature, we recommend differentiating between Build and Live workspaces as a best practice.

Can I have a mixed approach, with some customers having Environments and others not?

Yes. You can use a mixed approach. You can decide whether to provision Environments for each customer workspace. The Environments feature cannot be disabled after you provision a workspace. However, you can use [Role-Based Access Control (RBAC)](/en/user-accounts-and-teams/role-based-access/#managing-your-workspace-collaborators-with-role-based-access-control) to limit visibility, allowing collaborators to access only specific environments as required.

Can I have more than three environments?

No. The system is standardized to specifically use the Development, Test, and Production [environments](/en/oem/embedded-environments#environments). You cannot increase the number of environments.

Can I rename my environments?

No. [Environment](/en/oem/embedded-environments#environments) names are Development, Test, and Production. These names cannot be changed.

Can I have only STAGING and LIVE?

No. You cannot reduce the number of environments. However, you can adjust [Role-Based Access Control (RBAC)](/en/user-accounts-and-teams/role-based-access/#managing-your-workspace-collaborators-with-role-based-access-control) settings to limit collaborator access to only certain environments, such as Development and Production. This customizes the operational setup to functionally limit the number of environments.

How does the shared connector work with the Environments feature?

The same published version of a [shared connector](/en/oem/admin-console/shared-connectors#shared-connectors) is used across all environments (Development, Test, and Production).

How can I define different roles for customer managers in each environment (Development, Test, and Production)?

Granular Role-Based Access Control (RBAC) is available in the Embedded [Admin Console](/en/oem/admin-console#accessing-the-admin-console). The role you assign applies to this customer manager in all customer workspaces and across all three environments (Development, Test, and Production) by default.

If you plan to provide different roles or access for each environment, you must add the collaborator individually to each Customer workspace (not as a customer manager), and then specify the collaborator role for each environment. You can assign these roles in the user interface or through the Workato API.

---
