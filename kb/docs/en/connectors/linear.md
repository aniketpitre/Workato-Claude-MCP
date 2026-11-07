---
url: 'https://docs.workato.com/en/connectors/linear.md'
description: >-
  The Linear connector enables you to automate project management and
  issue-tracking workflows, creating and tracking issues for software
  development teams.
---

# Linear

[Linear](https://linear.app/homepage) is a project management and issue-tracking tool for software development teams. The Linear connector allows you to automate the process of creating and tracking issues, helping your team organize and manage work more efficiently.

## Prerequisites

To establish a Linear connection in Workato, complete the steps that correspond to the authentication method you plan to use:

- If you plan to use **OAuth 2.0**, [register an OAuth application](#register-oauth-app).
- If you plan to use an **API key**, [create an API key](#create-api-key).

### Register an OAuth app

Complete the following steps to register an OAuth app in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **API** in the sidebar.
   
   ![API administration page](/assets/linear-api-administration-page.Bvz7kApz.png)_API administration page_
   
4. Click **\+ New OAuth application** to add a new OAuth application.
   
5. Enter a name for your application in the **Application name** field. For example, `Workato`.
   
   ![Registering application](/assets/linear-registering-application.DQFPXn_w.png)_Registering application_
   
6. Enter the **Developer name** and a valid **Developer URL**.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Callback URLs** field. Refer to the [Callback URL](/en/developing-connectors/registering-new-client#callback-url) documentation for more information.
   
8. Click **Create** to register the OAuth app.
   
9. Copy the **Client ID** and **Client secret** and store them in a secure location. These values are required to establish the connection in Workato.
   

### Create an API key

Complete the following steps to create an API key in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **Security & access** in the sidebar.
   
   ![Personal API keys](/assets/linear-personal-api-keys.CVZ33KIY.png)_Personal API keys_
   
4. Click **New API key**.
   
5. Enter a name for the API key in the **Key name** field.
   
6. Specify permissions for the API key in the **Permissions** field.
   
7. Click **Create** to create the API key.
   
8. Copy the API key and store it in a secure location. This value is required to establish the connection in Workato. Refer to the [Linear documentation](https://linear.app/docs/api-and-webhooks) for more information.
   

## How to connect to Linear

The Linear connector supports the following authentication methods:

- [OAuth 2.0](#oauth-2-0)
- [API key](#api-key)

### OAuth 2.0

Complete the following steps to connect to Linear in Workato using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using OAuth 2.0 authentication](/assets/linear-oauth-connection-setup.iMhSgAAT.png)_Connect to Linear using OAuth 2.0 authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **Client ID** and **Client secret** for your Linear account.
   
6. Select the necessary [OAuth scopes](https://developers.linear.app/docs/oauth/authentication) required for your integration.
   
7. Click **Connect**.
   

### API key

Complete the following steps to connect to Linear in Workato using an API key:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using API key authentication](/assets/linear-api-key-connection-setup.Cww6C7p1.png)_Connect to Linear using API key authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **API key** for your Linear account.
   
6. Click **Connect**.

---
