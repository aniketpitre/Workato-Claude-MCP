---
url: 'https://docs.workato.com/en/connectors/confluence.md'
description: >-
  The Confluence connector lets you automate knowledge management workflows:
  create pages and tasks and search for existing pages.
---

# Confluence

[Confluence](https://www.atlassian.com/software/confluence) provides a comprehensive collaboration environment designed to enhance team interaction and knowledge exchange. With Confluence, you can create, share, and collaborate on projects all in one place.

## API version

The Confluence connector uses the Confluence Cloud REST API. Refer to the Confluence [REST API](https://developer.atlassian.com/cloud/confluence/rest/v1/intro/#about) for more information.

## Connection setup

The Confluence connector supports the following authentication types:

- [Basic](#basic)
- [API token](#api-token)
- [OAuth 2.0](#oauth)

> **CLOUD EDITION REQUIRED**
> 
> Confluence Data Center edition doesn't support Confluence v2 APIs. You must use a cloud connection for the Confluence MCP server and the following actions:
> 
> - Create page
> - Create task
> - Search labels
> - Search spaces
> - Get ancestors for page
> - Get attachments for page
> - Get children for page
> - Get page by ID
> - Update page
> 
> Use a [Custom action](/en/developing-connectors/custom-actions) if you need a feature the Data Center edition doesn't support.

### Basic authentication

Use basic authentication with your Confluence username and password.

Complete the following steps to set up a basic authentication connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence basic connection](/assets/confluence-basic-connection.C9dhQeh0.png)_Basic connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **Basic**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter your Confluence **Username** and **Password**.
   
10. Click **Connect**.
    

### API token authentication

You must generate an API token to use API token authentication.

#### Confluence setup for API token authentication

Complete the following steps to generate an API token in Confluence:

1. Go to the Atlassian [API Tokens](https://id.atlassian.com/manage/api-tokens) page.
   
2. Click **Create API token**.
   
3. Enter a **Name** and select an **Expires on** date.
   
4. Click **Create**.
   
5. Copy and save the **API token** for use in Workato.
   

#### Connect to Confluence with API token authentication

Complete the following steps to set up an API token connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence API token connection](/assets/confluence-api-token-connection.U-D2amgE.png)_API token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **API token**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter your **Email** and **API token**.
   
10. Click **Connect**.
    

### OAuth 2.0 authentication

You must generate a client ID and secret to use OAuth 2.0 authentication.

#### Confluence setup for OAuth 2.0 authentication

Complete the following steps to generate a client ID and secret in Confluence:

1. Log in to the Atlassian [Developer Console](https://developer.atlassian.com/console/myapps/).
   
2. Click **Create > OAuth 2.0 integration**.
   
3. Enter a **Name**.
   
4. Agree to the terms.
   
5. Click **Create**.
   
6. Click **Authorization** and then click **Add**.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field and then click **Save changes**.
   
8. Click **Permissions**.
   
9. Click **Add** for the Confluence API.
   
10. Click **Configure**.
    
11. Click **Edit Scopes** under **Classic scopes**.
    
12. Select the following scopes:
    
    - `manage:confluence-configuration`
    - `read:confluence-groups`
    - `read:confluence-content.all`
    - `read:confluence-content.permission`
    - `read:confluence-content.summary`
    - `read:confluence-props`
    - `read:confluence-space.summary`
    - `read:confluence-user`
    - `read:page:confluence`
    - `readonly:content.attachment:confluence`
    - `search:confluence`
    - `write:confluence-content`
    - `write:confluence-file`
    - `write:confluence-groups`
    - `write:confluence-space`
13. Click **Save**.
    
14. Select **Settings**.
    
15. Copy and save the **Client ID** and **Secret** for use in Workato.
    

#### Connect to Confluence with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to Confluence in Workato:

1. Click **Create > Connection**.
   
2. Search for `Confluence` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Confluence OAuth connection](/assets/confluence-oauth-connection.Ck6ynxBz.png)_OAuth connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud** for Confluence cloud instances or the corresponding option for on-prem connections. Refer to [Connections using an on-prem agent](/en/on-prem/agents/connection) for more information.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0**.
   
7. Enter your subdomain for cloud instances in the **Confluence subdomain** field. This is typically found in the Confluence URL. For example, your subdomain is `acme` if your URL is `https://acme.atlassian.net`.
   
8. Optionally, select **Enter on-prem URI** from the drop-down menu and enter your Confluence URI in the **Confluence domain** field. This is the root URI of your on-prem Confluence host. For example, `https://confluence.intranet.acme.com:7654`. You might need to add Workato's IP address to the allowlist to connect. Refer to [IP allowlists](/en/security/ip-allowlists) for more information.
   
9. Enter the **Client ID** and **Client secret**.
   
10. Optionally, expand **Advanced settings** and select **Classic scopes** or **Granular scopes**.
    
11. Click **Connect**.
    
12. Choose a site from the **Use app on** drop-down menu. This is the Atlassian account your app accesses.
    
13. Click **Accept**.

---
