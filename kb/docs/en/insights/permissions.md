---
url: 'https://docs.workato.com/en/insights/permissions.md'
description: >-
  Manage Insights roles and privileges with role-based access control, including
  how to create a custom environment role with the Insights privilege.
---

# Manage roles and privileges

Permissions to access the Insights feature is determined by role-based access control (RBAC):

- In the [new permissions model](/en/user-accounts-and-teams/role-based-access/access-control-v2), collaborators with the **Environment admin** or **Environment manager** role have full access to Insights by default.
- In workspaces using the legacy permissions model, collaborators with the legacy **Admin** or **Analyst** system roles have full access by default.

Additionally, you can create a [custom environment role](/en/user-accounts-and-teams/role-based-access/access-control-v2#create-a-custom-environment-role) with the Insights privilege.

> **FEATURE AVAILABILITY**
> 
> Insights is available to customers on specific pricing plans. Additionally, access to Insights dashboards within [Workflow apps](/en/workflow-apps) is determined by whether your plan includes the Workflow apps feature. Refer to your pricing plan and contract to learn more.

## Create a custom environment role with the Insights privilege

Complete the following steps to create a custom collaborator role with the Insights privilege:

1. Go to **Workspace admin > Access control > Environment roles** and click **\+ Add environment role**.
   
2. Name the role to reflect its scope and purpose, such as `Insights builder`.
   
3. Go to **Platform tools > Insights**. ![Insights privileges](/assets/insights-privileges.CVUAmpEO.png)_Insights privileges_
   
4. Select the privileges for accessing Insights dashboards:
   
   - - Full access
     - Complete access to the Insights feature, including the ability to **View**, **Edit**, **Create**, and **Delete** Insights dashboards.
     - View
     - View existing Insights dashboards.
     - Edit
     - Edit existing Insights dashboards.
     - Create
     - Create new Insights dashboards.
     - Delete
     - Delete Insights dashboards.
   
   This setting controls the ability to access Insights in the platform. Access to Insights dashboards within [Workflow apps](/en/workflow-apps) is determined by whether your plan includes Workflow apps.
   
5. Click **Save changes**.
   
6. Assign the role to existing collaborators or invite new collaborators to your workspace with this role.
   

You can [manage privileges](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#insights) to Insights for custom roles in **Workspace admin > Access control > Environment roles** in **Platform tools > Insights**.

## How roles and privileges affect data source access

Access to the usage data source requires the [Insights](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#insights) privilege and the [Usage dashboard](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#billing-usage) privilege.

Your collaborator role and feature access determine which data sources you can use. If you don't have access to a data source, it affects what you can do with charts and filters:

- **Building a chart**: The data source isn't available as an option.
  
- **Editing a chart**: An error indicates that the data source isn't found. ![An error indicates that the data source isn't found](/assets/chart-edit-error.Djathcbe.png)_An error indicates that the data source isn't found_
  
- **Viewing a chart**: The chart doesn't display any data and shows an error instead. ![The chart displays an error if it relies on a restricted data source](/assets/chart-error.3daR8eRn.png)_The chart displays an error if it relies on a restricted data source_
  
- **Creating a filter group**: The data source isn't available when defining filters.
  
- **Using a filter group**: Filters relying on a restricted data source don't provide recommendations or picklist items.
  

Even if you don't have access to a specific data source, you may still see details about projects, recipes, or jobs in charts that use **Workspace data** as the data source type.

> **HOW DOES ENVIRONMENT ACCESS AFFECT AVAILABLE DATA?**
> 
> Environment access determines what data you can access in dashboards.
> 
> - **If you have access to all environments**:
>   
>   - You can access workspace data from all environments.
>   - Workflow app, data table, and individual recipe job history data are only available for the environment where the dashboard is created.
> - **If you don't have access to a specific environment**:
>   
>   - You can still access projects and recipes from that environment if the chart uses workspace data.
>   - However, job history data from that environment won't be available.

---
