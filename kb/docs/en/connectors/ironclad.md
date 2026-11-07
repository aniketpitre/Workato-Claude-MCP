---
url: 'https://docs.workato.com/en/connectors/ironclad.md'
description: >-
  The Ironclad connector lets you automate contract lifecycle workflows: create,
  update, list, search, and delete records and trigger recipes on new events.
---

# Ironclad

[Ironclad](https://ironcladapp.com/) is a Contract Lifecycle Management (CLM) platform used by legal, sales, and business teams to automate, manage, and gain insights from digital contracts. This connector enables you to integrate Ironclad's contract management capabilities with Workato to automate contract creation, track acceptance of legal terms, and manage contract data.

## Prerequisites

To establish a connection to Ironclad, you must have an Ironclad app.

### Register your Ironclad app

Complete the following steps to create an app in Ironclad:

1. Go to your Ironclad registration page in your client application.
   
2. Click your user profile icon and select **Company settings**.
   
3. Click **API** in the sidebar.
   
4. Click **Create new app**.
   
5. Enter a **Name** for your app in the dialog.
   
6. Click **Create app**.
   
7. Copy and save the **Client ID** and **Client secret**. These values are required to complete the connection setup in Workato.
   
8. Fill out any remaining client application details.
   
9. Click **Save changes**.
   

## How to connect to Ironclad

Workato supports the following types of connections to Ironclad:

- [OAuth 2.0 Authorization code](#authentication-auth-code)
- [OAuth 2.0 Client credentials](#authentication-client-credentials)

### Authorization code grant authentication (OAuth 2.0)

To create an Ironclad connection using authorization code grant authentication, you must:

- [Verify your instance URL](#auth-code-prerequisites)
- [Request a token](#auth-code-prerequisites)
- [Complete connection in Workato](#setup)

#### Verify your instance URL and request a token

Complete the following steps to verify your instance URL and request a token:

1. Sign in to your Ironclad account and verify the **Instance URL** you plan to use. Save the **Instance URL** to use to complete setup in Workato.
   
2. Request an authorization code grant token. Refer to the [Ironclad documentation](https://developer.ironcladapp.com/reference/authorization-code-grant) for detailed instructions about requesting, refreshing, and scoping for an authorization code grant token.
   

#### Complete setup in Workato

Complete the following steps to set up your Ironclad connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Ironclad` as your connection in the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Ironclad Connection](/assets/ironclad-connection-setup.s6bU1mxU.png)_Create your Ironclad connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select `OAuth 2.0 Authorization code` as the **Authorization type** you plan to use.
   
6. Enter the **Instance URL**.
   
7. Enter the **Client ID**.
   
8. Enter the **Client secret** from your Ironclad app.
   
9. Select any **Scopes** you plan to request. The scopes must be equal to, or a subset of, the scopes of the Ironclad app.
   
10. Click **Connect**.
    

### Client credentials-based authentication (OAuth 2.0)

To create an Ironclad connection using client credentials authentication, you must:

- [Verify your instance URL](#client-credentials-prerequisites)
- [Request a token](#client-credentials-prerequisites)
- [Complete setup in Workato](#setup-client-credentials)

#### Verify your instance URL and request a token

Complete the following steps to verify your instance URL and request a token:

1. Sign in to your Ironclad account and verify the **Instance URL** you plan to use. Save the **Instance URL** to use to complete setup in Workato.
   
2. Request a client credentials grant token. Refer to the [Ironclad documentation](https://developer.ironcladapp.com/reference/client-credentials-grant) for detailed instructions about requesting, refreshing, and scoping for a client credentials grant token.
   

#### Complete setup in Workato

Complete the following steps to set up your Ironclad connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Ironclad` as your connection in the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Ironclad Connection](/assets/ironclad-connection-setup.s6bU1mxU.png)_Create your Ironclad connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select `OAuth 2.0 client credentials` as the **Authorization type** you plan to use.
   
6. Enter the **Instance URL**.
   
7. Enter the **Client ID**.
   
8. Enter the **Client secret** from your Ironclad app.
   
9. Select any **Scopes** you plan to request. The scopes must be equal to, or a subset of, the scopes of the Ironclad app.
   
10. Enter the **Impersonate user ID/email** to specify a user to impersonate.
    
11. Click **Connect**.
    

## Scopes

Any scopes you request in your Workato connection must be equal to or a subset of the Ironclad client application's registered scopes.

> **DEFAULT SCOPE**
> 
> The `scim.users.readUsers` scope is added by default in Workato. Ensure that `scim.users.readUsers` is configured in your Ironclad app to avoid connection failures.

---
