---
url: 'https://docs.workato.com/en/oem/admin-console/customer-managers.md'
description: >-
  Create and manage customer managers in the Embedded Admin console to give team
  members role-based access to customer workspaces.
---

# Customer managers

The customer managers feature helps Embedded partners and their team members manage their customers. This feature is available on the Embedded **Admin console** under the **Customer managers** tab.

## Who are customer managers?

Customer managers are members of the Embedded partner's team. They may be members of your customer success teams, support personnel, or recipe and connector developers who help your customers with their integrations. Customer managers can access all or some customer workspaces as determined by the Embedded partner.

Ensure that customer managers are trusted team members who have permission to view data in customer workspaces. In Workato, we manage the type and amount of data or tools users can view in customer teams through [role-based access control](/en/user-accounts-and-teams/role-based-access/).

## Create a customer manager

1. Go to the **Customer managers** tab on the Embedded admin console.
   
2. Click **\+ Assign customer manager** in the top right of the interface.
   
   ![Customer managers](/assets/customer-manager-table.D64tqHsF.png)_Customer manager interface_
   
3. Use the **Collaborator** drop-down menu to select the collaborator you plan to make a customer manager.
   
4. Use the **Environment Role** drop-down menu to select an environment role for the customer manager.
   
5. Use the **Project role** drop-down menu to select a project role for the customer manager.
   
   ![Assign roles to a customer manager](/assets/customer-manager-assign-role-env-proj.ByZXbPvt.png)_Assign an environment role and a project role to a customer manager_
   
   > **ASSIGNED ROLES**
   > 
   > The environment role and project role you assign apply to this customer manager in all customer workspaces they have access to. The same environment role applies across all three environments (Development, Test, and Production).
   > 
   > If you plan to assign different roles per environment, you must add the collaborator individually to each customer workspace, instead of designating them as a customer manager, and specify the role for each environment. You can assign these roles in the user interface or through the Workato API.
   
6. Assign the customer manager to specific customer workspaces by selecting customers from the drop-down menu, or by searching for a particular customer workspace.
   
   Alternatively, assign the customer manager to all customer workspaces by toggling **Manage all customers**.
   
7. Click **Assign customer manager**.
   

Customers who have access to their **Teams** page can see all customer managers who manage their account. This is to ensure customers are aware of all users who can access their account for security and audit purposes.

![Customer managers tag](/assets/customer-manager-customer-view.DRbUiLZy.png)_List of customer managers from within a customer workspace_

> **CUSTOMER PERMISSIONS**
> 
> Customers cannot remove or edit a customer manager on their team. Workato denotes customer managers with a unique tag within customer workspaces.

> **BEFORE YOU BEGIN**
> 
> Before you create a customer manager, consider the following issues:
> 
> - Ensure this person is a collaborator in the partner's admin team. Invite collaborators on the [Teams page](https://www.workato.com/members). Determine their [environment role](/en/user-accounts-and-teams/role-based-access/new-model/system-environment-roles) and [project role](/en/user-accounts-and-teams/role-based-access/new-model/system-project-roles) within all customer teams, as these roles define their access to recipes, jobs, and features.
> - In workspaces using the legacy permissions model, [collaborator system roles](/en/roles) (**Admin**, **Analyst**, or **Operator**) still determine access until you migrate.

## Accessing customer workspaces

After you create a customer manager, they can then access their customers' accounts from the **Teams** interface.

Customer managers can also access a customer workspace from the **Customer** page.

1. Navigate to **Admin console > Customers > Customer page**.
   
2. Click **Switch to this account**. ![Customer managers](/assets/customer-info-access.BmKGfa5o.png)_Access a customer workspace from the customer information page_
   

Both actions switch the customer manager from the current account to the selected customer. They can then perform actions in the customer workspace.

### Audit tracking

The [activity audit log](/en/features/activity-audit-log) tracks all log ins, log outs, and work performed by customer managers.

The log also tracks changes made to recipes by individual users.

To view changes to recipes made by individual users:

1. Select a recipe.
   
2. Navigate to the **Versions** interface.
   
3. View the **Modified by** column.
   
   ![Changes to recipes](/assets/recipe-versions.DEnP1ri3.png)_View changes to recipes_
   

## Edit or remove a customer manager

To edit a customer manager:

1. Navigate to the **Customer managers** interface.
   
2. Click the **more** icon.
   
   ![Edit customer manager](/assets/customer-manager-edit-or-remove._PjpGb63.png)_Edit or remove customer manager_
   
3. Select **Edit customer manager**.
   
4. Choose a new role for the user.
   
   You can also assign the user to different customer workspaces.
   
5. Click **Save**.
   

Remove this user from the list of customer managers to revoke access to all customer workspaces.

1. Navigate to the **Customer managers** interface.
   
2. Click the **more** icon.
   
3. Select **Remove customer manager**.
   
   ![Remove customer manager](/assets/customer-manager-remove.COsuIDPJ.png)_Remove customer manager_
   

When you remove a customer manager Workato prevents them from accessing customer workspaces in the future. Workato preserves all of the work they completed in customer workspaces.

## FAQ

1. **How does the customer manager feature work if I already have Embedded partner team members in my customer workspace?**
   
   **Answer:** There are two options to add Embedded partners to their customers' accounts. The first option is to invite them through the teams feature. The second option is to invite them through the customer manager feature.
   
   Both of these options can work together. Consider a situation where you already have Embedded partner team members on your customers' teams. To add them as customer managers, you must invite them to your customers' teams using the customer manager feature.
   
2. **Can my team member have two roles in a customer workspace?**
   
   **Answer:** No. If you assign a team member to a role using the team feature, this role takes precedence over roles assigned through other methods.
   
   Consider a situation where a customer team invites a user to the team as an operator and also assigns the same user to an admin role through the customer manager feature. In this scenario, the user's role in the team is operator. They cannot access this customer team as an admin.
   
   You can remove the manual invite from the workspace. Then, the user can access the customer workspace with an admin role.

---
