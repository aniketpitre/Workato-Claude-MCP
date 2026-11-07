---
url: 'https://docs.workato.com/en/connectors/airtable.md'
description: >-
  Connect Airtable to Workato to automate workflows with your cloud-based
  relational database platform.
---

# Airtable

[Airtable](https://www.airtable.com/) is a cloud-based platform that allows you to link records from one table to another, creating an easy-to-share relational database. Airtable provides pre-built templates for different industries and use cases, including project management, event planning, customer relationship management, and more.

## API version

The Airtable connector uses Airtable's REST-based [API v1](https://airtable.com/developers/web/api/introduction).

## Connection setup

The Airtable connector supports the following authentication types:

- [Personal access token](#personal-access-token)
- [OAuth 2.0](#oauth2)

### Personal access token

Use personal access token authentication to connect to Airtable with a token generated from your Airtable account.

> **API KEY DEPRECATION**
> 
> Airtable deprecated API keys for authentication at the end of January 2024. API keys no longer work on the platform. Migrate to personal access tokens to maintain API access to Airtable. Personal access tokens provide granular, secure API access to your Airtable data.

#### Create a personal access token

Refer to [Creating personal access tokens](https://support.airtable.com/docs/creating-and-using-api-keys-and-access-tokens) in the Airtable documentation.

#### Connect to Airtable using personal access token

Complete the following steps to set up a personal access token connection to Airtable in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Airtable** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Airtable connection setup](/assets/connection-setup-pat.DaJdezj7.png)_Airtable connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
6. Enter your [personal access token](#pat-create-token) in the **Personal access token** field.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   

### OAuth 2.0

Use OAuth 2.0 to connect to Airtable by signing in and granting access through Airtable's authorization flow.

#### Minimum and default scopes

The scopes `data.records:read` and `schema.bases:read` are requested automatically. The connection defaults to `data.records:read`, `schema.bases:read`, `data.records:write`, and `schema.bases:write` if no additional scopes are selected.

Ensure that any additional scopes you select are supported by your Airtable plan. Selecting unsupported scopes may result in a connection error. For example, the scope **View metadata about workspaces, bases, and views including collaborators** corresponds to `workspacesAndBases:read`, which is available only on the Business and Enterprise Scale plans.

Refer to the Airtable documentation for more information on [Airtable OAuth scopes and associated plans](https://airtable.com/developers/web/api/scopes).

#### Connect to Airtable using OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Airtable in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Airtable** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Airtable connection setup](/assets/connection-setup-oauth.Ce6bMao1.png)_Airtable connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Expand **Advanced settings** and use the **Requested permissions (OAuth scopes)** drop-down menu to select the scopes for this connection.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to Airtable when prompted and click **Allow** to grant Workato access.

---
