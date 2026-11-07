---
url: 'https://docs.workato.com/en/control-plane/add-end-users.md'
description: >-
  Add end users to Control plane and configure environment access and group
  memberships.
---

# Add an end user manually

You can manually add end users without SSO configuration. Manually adding end users is suitable for development and testing phases. Workato recommends that you use SAML-based SSO for scalable end user management. You can define the user's environment access and user group membership when you manually add a user.

Users are automatically added to the default `Everyone` group when you provision access to an environment.

Complete the following steps to manually add an end user:

1. Sign in to Workato.
   
2. Expand the workspaces menu.
   
3. Click **Control plane**. Control plane opens in a new tab by default.
   
4. Sign in using your Control plane credentials or SSO.
   
5. Click **End user access**.
   
6. Click **\+ Add end user**.
   
7. Enter the user's name in the **Full name** field.
   
   ![Add an end user](/assets/add-end-user.B2kVwZyC.png)_Add an end user_
   
8. Enter the user's email in the **Email address** field.
   
   > **UNIQUE EMAIL REQUIRED**
   > 
   > The email address you enter must be unique. An error message displays if the system detects an existing email that matches the email you entered.
   
9. Go to the **Environment access** section and select the checkboxes for the environments the user can access. Options are `Development`, `Test`, and `Production`.
   
10. Use the **Select a group** drop-down menu for each environment to select the environment-specific user groups where you plan to add the user. The **Select a group** drop-down menu is only active after you select the environment checkbox.
    
11. Click **Add**.

---
