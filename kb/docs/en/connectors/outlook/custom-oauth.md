---
url: 'https://docs.workato.com/en/connectors/outlook/custom-oauth.md'
description: >-
  Create a custom OAuth profile for your Outlook connection in Workato,
  including the required Azure roles and Microsoft 365 license prerequisites.
---

# Create a Custom OAuth profile for Outlook

Complete the following steps to create a Custom OAuth profile for your Outlook connection:

> **PREREQUISITES**
> 
> The user establishing the connection (the Outlook account associated with the required credentials) must meet the following requirements:
> 
> - Hold the Application Administrator role.
> - Possess, at minimum, a Microsoft 365 Business User license.
> 
> Refer to the [Assign roles and licenses](#assign-roles-licenses) section to learn how to grant these roles and licenses to a user.

1. Go to **Tools > Custom OAuth profiles** using the navigation sidebar.
   
2. Click **\+ New custom profile**.
   
3. Select **Outlook** from the **Application** drop-down.
   
   ![Select Outlook](/assets/custom-oauth.BYAhVgKC.png)_Select Outlook_
   
4. Provide a **Name** for this account.
   
5. Click **Create new app**.
   
6. Create a new app or use an existing app.
   
   Register the Workato App in the Azure Portal
   
   Complete the following steps to register the Workato app in the Azure portal:
   
   1. Sign in to the [Azure portal](https://portal.azure.com/).
      
   2. Select **App registrations > + New registration**.
      
   3. Enter a unique name for the application.
      
   4. Use the **Supported account types** drop-down menu to select an account type.
      
   5. Select **Web** from the **Select a platform** drop-down menu.
      
   6. Use the following URI for the **Redirect URI**:
      
      ```html
      https://www.workato.com/oauth/callback
      ```
      
   7. Select **Register**.
      
   
7. Obtain the client ID
   
   1. In the [Azure portal](https://portal.azure.com/), go to **App registrations > Overview**.
      
   2. Copy the **Application (client ID)** for use in Workato.
      
   
8. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
9. Enter your **Client ID** and **Client Secret** in Workato.
   
10. Click **Save** and **Done**.
    

## Assign roles and licenses in the Azure portal

The user establishing the connection (the account associated with the required credentials) must meet the following requirements:

- Hold one of the following roles:
  - Application Administrator
  - Global Administrator
  - Cloud Application Administrator
- Possess, at minimum, a Microsoft 365 Business User license.

Complete the following steps to assign roles and licenses to a user in the [Azure portal](https://portal.azure.com/) and [Microsoft 365 Admin Center](https://admin.microsoft.com/)

1. Assign a role to your user
   
   1. Go to **Home > Users**.
      
      ![Users](/assets/users.CuDgSGeL.png)_Select users_
      
   2. Search for and select the user associated with your account.
      
   3. Select **Assigned roles** from the left sidebar.
      
      ![Assigned roles](/assets/assign-roles.Ch4rjMSV.png)_Assigned roles_
      
   4. Click **\+ Add assignments**.
      
   5. Select the **Application Administrator**, **Global Administrator**, or **Cloud Application Administrator** role from the **Role** tab.
      
   6. In the **Members** tab, assign the role to the user account associated with this connection.
      
   
   Refer to [Microsoft's documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal#step-2-open-the-add-role-assignment-page) for more information on assigning roles to your users.
   
2. Assign the Microsoft 365 Business User License
   
   1. Go to the [Microsoft 365 admin center](https://admin.microsoft.com/).
      
   2. Go to **Billing > Licenses**.
      
   3. Select the Microsoft 365 Business User license from the list.
      
   4. On the product details page, select **Assign licenses**.
      
   5. In the **Assign licenses to users** pane, start typing a name, and then choose it from the results to add it to the list. You can add up to 20 users at a time.
      
   6. Select **Turn apps and services on or off** to assign or remove access to specific items.
      
   7. Select **Assign**, then close the right pane.
      
   
   Refer to [Microsoft's documentation](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users?view=o365-worldwide) for more information on assigning licenses to your users.

---
