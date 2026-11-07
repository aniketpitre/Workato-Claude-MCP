---
url: 'https://docs.workato.com/en/connectors/amplify.md'
description: >-
  The Amplify connector enables you to automate strategy execution workflows,
  managing strategic projects, aligning goals, and tracking progress.
---

# Amplify

[Amplify](https://portal.amplify-now.com/hc/en-us/articles/360038262234-What-is-Amplify) is a strategy execution software that helps organizations manage strategic projects, align them with goals, and track progress through analytics and reporting.

## Prerequisites

Before using the Amplify connector, ensure you have an active account and an Amplify instance with appropriate permissions to access Amplify APIs. If you don't already have an account, contact your app administrator to create an account and an Amplify instance.

### Create an API token

Complete the following steps to create an API token in the Amplify admin console:

1. Sign in to Amplify and click **My Account**.
   
2. Go to **Administration > Authentication**.
   
3. Locate the **Access Tokens** section at the bottom of the page.
   
   ![Amplify token](/assets/amplify-token.BvQcbtEx.png)_Amplify Token_
   
4. Click **New Access Token**.
   
   ![Amplify token setup](/assets/amplify-token-setup.Dl19jkQE.png)_Amplify Token Setup_
   
5. Specify the **Owner** of the new token.
   
6. Select an expiration date for the token. We recommend allowing tokens to remain valid for one month.
   
7. Click **Create** to create the API token.
   

### Configure user permissions

To make changes to objects in Amplify using your token, you must have the necessary permissions in the associated Program.

Complete the following steps to enable user permissions:

1. Navigate to the relevant **Program**.
   
2. From the menu, navigate to **Teams & Roles > Roles & Permissions**.
   
   ![Amplify user roles](/assets/amplify-user-roles.zYscAB-v.png)_Amplify User Roles_
   
3. Create a new role for the API user, or click the edit icon on an existing role.
   
   ![Amplify user permissions](/assets/amplify-user-permissions.CuBndIk_.png)_Amplify User Permissions_
   
4. Select the appropriate objects and assign **Read**, **Update**, or **Full** permissions as needed.
   
5. If you have created a new role, navigate to **Teams** and assign the new role to the user the token was created for.
   

## How to connect to Amplify

Complete the following steps to establish an Amplify connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Amplify** as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Amplify connection setup](/assets/amplify-connection-setup.fdUthXX7.png)_Amplify Connection Setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API Token** for your Amplify account created in the previous steps.
   
6. Enter the **Subdomain** for your Amplify account instance.
   
7. Click **Connect**.

---
