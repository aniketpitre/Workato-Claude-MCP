---
url: 'https://docs.workato.com/en/connectors/syncro.md'
description: >-
  The Syncro connector lets you automate business workflows by integrating with
  your Syncro account. You can create connections, manage data, and run
  operations using your API key and subdomain.
---

# Syncro

[Syncro](https://syncromsp.com/) is a business management platform built for managed service providers. It combines tools for service desk operations, remote monitoring, and customer management in one system. The Syncro connector lets you create, update, and retrieve records in Syncro.

## How to connect to Syncro

Workato requires your Syncro subdomain and a valid API key to authorize the connection. Complete the following steps to gather credentials and create the connection in Workato:

- [Step 1: Generate API credentials in Syncro](#generate-credentials)
- [Step 2: Complete the setup in Workato](#complete-setup)

## Generate API credentials in Syncro

Complete the following steps to retrieve your Syncro subdomain and API key:

1. Sign in to your Syncro account.
   
2. Locate your account's subdomain, such as `demo.syncromsp.com`.
   
3. Go to **Admin > API > API Tokens**.
   
4. Click **\+ New Token**.
   
5. Click the **Custom Permissions** tab.
   
6. Enter a **Name** for your API token.
   
7. Optional. Enter an **Expiration date**.
   
8. Select the checkboxes for the permissions you plan to enable.
   
   Refer to the [Security Permissions Reference](https://docs.syncromsp.com/security/security-perms) for more information.
   
9. Scroll down and click **Create API Token**.
   
10. Copy the token and save it securely. You can only view this value once.
    
11. Click **Done**.
    

Refer to the [Syncro API documentation](https://docs.syncromsp.com/scripting-apis/syncro-rest-api) for more information.

## Complete the setup in Workato

Complete the following steps to create a Syncro connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Syncro` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Syncro](/assets/connect-to-syncro.Bu7oV-ax.png)_Connect to Syncro_
   
4. Use the **Location** drop-down to select the project or folder to store this connection.
   
5. Enter your **Syncro Subdomain**.
   
   For example, if your Syncro instance URL is `https://demo.syncromsp.com`, enter `demo`.
   
6. Enter your **API key**.
   
   You can generate this key from your Syncro account by navigating to **Admin > API Tokens** and clicking **New API Token**.
   
7. Click **Connect**.

---
