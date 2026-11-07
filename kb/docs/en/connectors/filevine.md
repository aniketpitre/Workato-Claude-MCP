---
url: 'https://docs.workato.com/en/connectors/filevine.md'
description: >-
  The Filevine connector enables you to automate legal case management workflows
  by integrating with your Filevine environment.
---

# Filevine

[Filevine](https://www.filevine.com) is a legal case management platform that helps law firms manage documents, deadlines, tasks, and communication across teams.

The Filevine connector enables you to automate legal operations by integrating Filevine objects and workflows into your recipes. You can use this connector to create or update records, retrieve record details, and trigger recipes based on real-time changes in your Filevine account.

## How to connect to Filevine

Workato requires a client ID, client secret, and an access token from Filevine to authorize the connection. Complete the following steps to generate credentials and create the connection in Workato:

- [Step 1: Generate API credentials in Filevine](#generate-credentials)
- [Step 2: Complete the setup in Workato](#complete-setup)

## Generate API credentials in Filevine

Complete the following steps to generate a client ID, client secret, and an access token in the Filevine developer portal:

1. Sign in to Filevine as an account admin.
   
2. Click your avatar or letter icon.
   
3. Select **Manage My Account** from the menu.
   
4. Go to the **Access Tokens** tab.
   
5. Click **\+ New** to create a new token.
   
6. Enter a descriptive **Name**.
   
7. Select the required **Scopes**.
   
8. Click **Create**, then copy the access token immediately. You can only view this value once.
   
9. Go to the **Client Secrets** tab.
   
10. Register your **Client ID** and **Client secret** and save the values securely.
    

Refer to the [Filevine authentication guide](https://developer.filevine.io/docs/v2-us/e0f5ad7e2c916-authentication.html) for more information.

## Complete the setup in Workato

Complete the following steps to create a Filevine connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Filevine` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Filevine](/assets/connect-to-filevine.DYSfjlAI.png)_Connect to Filevine_
   
4. Use the **Location** drop-down to select the project or folder to store this connection.
   
5. Enter your **Client ID** and **Client secret**. You can generate these credentials from the Filevine admin console.
   
6. Enter your **Token**. You can generate a token from the **Credentials** tab in Filevine.
   
7. Enter your **Org ID** and **User ID**.
   
   You can retrieve these values using the Filevine API gateway. Refer to the [Filevine API documentation](https://developer.filevine.io/docs/v2-us/e0f5ad7e2c916-authentication#3-request-the-user-id-and-org-id) for more information.
   
8. Select a **Scope** from the drop-down menu.
   
   Scopes define the level of access for this connection. Refer to the [Filevine API documentation](https://developer.filevine.io/docs/v2-us/e0f5ad7e2c916-authentication#2-request-a-bearer-token) for more information.
   
9. Click **Connect**.

---
