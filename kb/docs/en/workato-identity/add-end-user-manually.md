---
url: 'https://docs.workato.com/en/workato-identity/add-end-user-manually.md'
description: >-
  Manually add end users to Workato Identity and configure environment access
  and group memberships.
---

# Add an end user manually

You can manually add end users without SSO configuration. Manually adding end users is suitable for development and testing phases. Workato recommends that you use SAML-based SSO for scalable end user management. You can define the user's environment access and user group membership when you manually add a user.

Users are automatically added to the default `Everyone` group when you provision access to an environment.

Complete the following steps to manually add an end user:

1. Sign in to Workato.
   
2. Click **Workspace admin** in the sidebar. The **Access control** page displays by default.
   
3. Click the **End users** in the sidebar.
   
4. Click **\+ Add end user**
   
5. Enter the user's name in the **Full name** field.
   
6. Enter the user's email in the **Email address** field.
   
   > **UNIQUE EMAIL REQUIRED**
   > 
   > The email address you enter must be unique. An error message displays if the system detects an existing email that matches the email you entered.
   
7. Go to the **Environment access** section and select the checkboxes for the environments the user can access. Options are `DEV`, `TEST`, and `PROD`.
   
   > **ENVIRONMENT AVAILABILITY**
   > 
   > Workspaces without [Environments](/en/features/environments) provisioned only have one environment available.
   
   ![Select environment access](/assets/add-a-user-environment-access.B5Lt1JuQ.png)_Select environment access_
   
8. Use the **Select a group** drop-down menu for each environment to select the environment-specific user groups where you plan to add the user. The **Select a group** drop-down menu is only active after you select the environment checkbox.
   
   ![Add the user to environment-specific groups](/assets/select-environment-groups.DPQBZgIx.png)_Add the user to environment-specific groups_
   
9. Click **Add**.

---
