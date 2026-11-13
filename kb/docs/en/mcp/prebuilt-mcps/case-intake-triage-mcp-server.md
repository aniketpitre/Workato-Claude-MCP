---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/case-intake-triage-mcp-server.md'
description: >-
  Use the Case Intake & Triage MCP server to connect your LLM to Jira Service
  Desk, Salesforce, Confluence, and PagerDuty to triage a ticket end-to-end,
  from customer context to priority, routing, and escalation.
---

# Case Intake & Triage MCP server

The Case Intake & Triage MCP server enables LLMs to interact with Jira Service Desk, Salesforce, Confluence, and PagerDuty for end-to-end support ticket triage through natural conversation. It provides tools to fetch a ticket, enrich it with customer context, apply a priority matrix, and write the resulting priority and routing back to the ticket, without requiring direct interaction with the Jira Service Desk, Salesforce, Confluence, and PagerDuty interfaces.

## Uses

Use the Case Intake & Triage MCP server to perform the following actions:

- Triage a ticket by pulling its classification fields, enriching it with Salesforce customer context, and applying a priority matrix
- Write the resulting priority and routing, or a specific assignee, back to the ticket
- Look up a ticket's customer tier and active entitlements without changing anything
- Search configured Confluence spaces for a runbook matching a ticket's issue
- Notify the on-call PagerDuty responder when a ticket is triaged as P1
- List the agents eligible for assignment to a ticket
- Reassign a ticket to a different agent with a fresh triage write
- Re-triage a ticket after its classification changes and get the resulting SLA state

### Example prompts

Use the following example prompts to invoke Case Intake & Triage MCP server tools:

- `Triage HELPDESK-1234`
- `What tier is the customer on ticket HELPDESK-1234?`
- `Prioritize this ticket and page on-call if it's P1`
- `Find a runbook that matches this ticket`
- `Who could work on HELPDESK-1234?`
- `Reassign HELPDESK-1234 to a different agent`
- `What's the current severity and impact on HELPDESK-5678?`
- `Search Confluence for a runbook about database timeouts`
- `Re-triage HELPDESK-1234 now that the impact has changed`

## Case Intake & Triage MCP server tools

The Case Intake & Triage MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_case\_context](#get-case-context-tool) | Fetches a ticket's request state and classification fields, and establishes the workflow for the case. |
| [get\_customer\_account\_context](#get-customer-account-context-tool) | Resolves the ticket's Salesforce account and returns the customer's tier and active entitlements for the triage matrix. |
| [search\_known\_issues](#search-known-issues-tool) | Searches configured Confluence spaces for a runbook matching the ticket. |
| [apply\_triage\_to\_case](#apply-triage-to-case-tool) | Runs the ticket through the triage matrix and writes the resulting priority and routing back to it. |
| [trigger\_p1\_escalation](#trigger-p1-escalation-tool) | Notifies the on-call PagerDuty responder for a ticket triaged as P1. |
| [list\_assignable\_agents](#list-assignable-agents-tool) | Lists the users eligible for assignment to the ticket. |

## Install the Case Intake & Triage MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Case Intake & Triage connection setup

View Case Intake & Triage connection setup steps

Configure the following connections to set up the Case Intake & Triage MCP server:

- [Jira](#jira-connection-setup): Required. Reads and writes ticket priority, assignee, and routing through the core Issue API.
- [Jira Service Desk](#jira-service-desk-connection-setup): Required. Reads request state, SLA cycles, and customer-request details.
- [Salesforce](#salesforce-connection-setup): Required. Enriches a ticket with the customer's tier and active entitlements.
- [Confluence](#confluence-connection-setup): Required if runbook search is enabled.
- [PagerDuty](#pagerduty-connection-setup): Required if P1 on-call escalation is enabled.

### Jira connection setup

View Jira connection setup steps

There are six ways to connect to Jira:

- [API token](#api-token)
- [Service account (API token)](#service-account-api-token)
- [OAuth 2.0 (Cloud - Atlassian-hosted Jira)](#oauth-2-0-cloud)
- [OAuth 2.0 (Data Center)](#oauth-2-0-data-center)
- [Personal access tokens](#personal-access-tokens)
- [Basic authentication (password)](#basic-authentication-with-password)

We strongly recommend using API tokens, service account API tokens, OAuth 2.0, or personal access tokens to connect to Jira instead of basic authentication with a password.

> **LIMITATIONS**
> 
> Authentication methods for the Jira connector have the following limitations:
> 
> - OAuth 2.0 (Cloud - Atlassian-hosted Jira) and OAuth 2.0 (Data Center) don't support real-time triggers.
> - API token and service account (API token) authentication don't support on-premise Jira connections.
> - Atlassian deprecated basic authentication for cloud connections in December 2018. On-premise Jira is not affected.

#### API token

View API token steps

API tokens authenticate your Atlassian account without using a username and password. API token authentication doesn't support connections to on-premise Jira.

##### Prerequisites

You must generate an Atlassian API token for this authentication method. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide for more information.

##### Connect to Jira using an API token

Complete the following steps to connect to Jira in Workato using an API token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![API token auth](/assets/api-token-auth.CeU8zRLD.png)_API token auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **API token**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the **Email** of the Jira account to link to Workato.
   
9. Enter the **API token** for your Atlassian account. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide to generate this value.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

#### Service account (API token)

View Service account (API token) steps

Use this authentication method to connect Workato to Jira using an Atlassian Cloud service account. A service account is a dedicated, non-personal Atlassian account used for integrations. Service accounts aren't tied to individual users, so connections remain stable when team members leave or change roles.

Service account (API token) authentication supports Jira Cloud connections only.

##### Prerequisites

Complete the following tasks before you connect:

###### Set up the service account

1. Go to [Atlassian Administration](https://admin.atlassian.com/).
   
2. Select your organization.
   
3. Select **Directory > Service accounts** and click **Create a service account**.
   
4. Enter a name and description for the service account, then click **Create a service account**.
   
5. Select the apps and roles for the service account on the **Select app role for service account** page.
   
6. Add the service account to groups to grant access to specific projects or spaces.
   
7. Click **Create**.
   
8. Click **Create credentials**.
   
9. Select **API token** on the **Choose authentication type** screen.
   
10. Enter a **Name** and **Expires on** date on the **Name API token** page.
    
11. Select the scopes for your connection. At minimum, you must select `read:jira-user` to establish the connection. Select additional scopes based on the triggers and actions your recipes use. Refer to [Manage API tokens for service accounts](https://support.atlassian.com/user-management/docs/manage-api-tokens-for-service-accounts/#Create-an-API-token-with-scopes) for the full list of available scopes.
    
12. Click **Next**.
    
13. Review the scopes assigned to your token on the **Review your API token** screen.
    
14. Click **Create**.
    
15. Click **Copy** to copy your API token. Save this value for use in Workato.
    
16. Click **Done**.
    

##### Connect to Jira using a service account API token

Complete the following steps to connect to Jira in Workato using a service account API token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Service account (API token)**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the email address associated with the service account in the **Email** field.
   
9. Enter the **API token** for the service account. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide to generate this value.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

#### OAuth 2.0 (Cloud - Atlassian-hosted Jira)

View OAuth 2.0 (Cloud - Atlassian-hosted Jira) steps

OAuth 2.0 enables you to share specific data with an application while keeping your username, password, and other information private. OAuth 2.0 (Cloud - Atlassian-hosted Jira) supports Jira Cloud connections.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Cloud Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-webhooks/) webhook documentation for registration steps.

##### Connect to Jira using OAuth 2.0 (Cloud - Atlassian-hosted Jira)

Complete the following steps to connect to Jira in Workato using OAuth 2.0 (Cloud - Atlassian-hosted Jira):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 auth](/assets/oauth-2-0-auth.Cd8GQFwz.png)_OAuth 2.0 auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Cloud - Atlassian-hosted Jira)**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Optional. Use the **Scopes** drop-down menu to select the authorization scopes to request. Workato requests the following scopes by default:
   
   - `read:jira-user`
   - `write:jira-work`
   - `manage:jira-project`
   - `read:jira-work`
   - `manage:jira-webhook`
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect** and sign in to your Jira instance.
    
11. Authorize Workato's request to access your Jira instance.
    

#### OAuth 2.0 (Data Center)

View OAuth 2.0 (Data Center) steps

OAuth 2.0 (Data Center) enables you to connect to an on-premise Jira Data Center instance using OAuth 2.0.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Jira Data Center](https://confluence.atlassian.com/adminjiraserver/managing-webhooks-938846912.html) webhook documentation for registration steps.

##### Prerequisites

You must generate an Atlassian client ID and client secret if you plan to connect to Jira Data Center using OAuth 2.0. Refer to the Atlassian [Configure an incoming link](https://confluence.atlassian.com/adminjiraserver/configure-an-incoming-link-1115659067.html) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.

##### Connect to Jira using OAuth 2.0 (Data Center)

Complete the following steps to connect to Jira in Workato using OAuth 2.0 (Data Center):

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Data Center)**.
   
7. Enter the hostname of your Jira Data Center instance in the **Host name** field. For example: `jira.yourcompany.com`
   
8. Expand the **Advanced settings** section.
   
9. Enter the **Client ID** and **Client secret** from your Jira Data Center application link configuration. Refer to the [Prerequisites](#oauth-2-0-data-center-prerequisites) section to generate these values.
   
10. Optional. Use the **Scopes** drop-down menu to select the authorization scopes to request. Defaults to **READ** and **WRITE**.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
12. Click **Connect** and sign in to your Jira instance.
    
13. Authorize Workato's request to access your Jira instance.
    

#### Personal access tokens

View Personal access tokens steps

Personal access tokens (PATs) authenticate your Atlassian account without using a username and password. PAT authentication supports on-premise Jira connections.

##### Prerequisites

You must generate an Atlassian personal access token for this authentication method. Refer to the Atlassian [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) guide for more information.

##### Connect to Jira using a personal access token

Complete the following steps to connect to Jira in Workato using a personal access token:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Personal access token auth](/assets/personal-access-token-auth.CVFp-sGl.png)_Personal access token auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Personal access token**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter the **Personal access token** of the Jira account to link to Workato. Refer to the Atlassian [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) guide to generate this value.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

#### Basic authentication with password

View Basic authentication with password steps

Basic authentication connects to your Atlassian account using a username and password. Basic authentication supports on-premise Jira connections.

> **DEPRECATED PASSWORD AUTHENTICATION**
> 
> Atlassian deprecated basic authentication for cloud connections in December 2018. On-premise Jira is not affected.

##### Connect to Jira using basic authentication

Complete the following steps to connect to Jira in Workato using basic authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Basic password auth](/assets/basic-password-auth.Bp4eQ9Ja.png)_Basic password auth_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select your connection type.
   
6. Use the **Auth type** drop-down menu to select **Basic**.
   
7. Enter the URL subdomain for your Jira instance in the **Host name** field. For example: `workato.atlassian.net`
   
8. Enter your Jira **Username** and **Password**.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

### Jira Service Desk connection setup

View Jira Service Desk connection setup steps

#### Jira Service Desk API version

The Jira Service Desk connector uses the [Jira Service Desk Cloud REST API](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/).

#### Jira Service Desk supported editions and versions

The Jira Service Desk connector works with both cloud and on-prem instances 7.x and later.

The Jira Service Desk connector supports the following authentication types:

- [API token](#jira-service-desk-api-token)
- [OAuth 2.0](#jira-service-desk-oauth-2-0)
- [Basic authentication with password](#jira-service-desk-basic-authentication-with-password)

#### Jira Service Desk API token

View API token authentication steps

Use API token authentication to connect to Jira Service Desk with a token generated from your Atlassian account. Use basic authentication with password for on-prem instances.

#### Get an API token

Refer to [Manage API tokens for your Atlassian account](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) in the Atlassian documentation.

#### Connect to Jira Service Desk using an API token

Complete the following steps to set up an API token connection to Jira Service Desk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira Service Desk` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![API token auth](/assets/api-token-auth.BAbtq3je.png)_API token connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**.
   
6. Use the **Auth type** drop-down menu to select **API token**.
   
7. Enter your Jira Service Desk subdomain in the **Subdomain** field.
   
8. Enter the email address for your Jira Service Desk account in the **Email** field.
   
9. Enter your [API token](#api-token-setup) in the **API token** field.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

#### Jira Service Desk OAuth 2.0

View OAuth 2.0 authentication steps

Use OAuth 2.0 to connect to Jira Service Desk by signing in and granting access through Atlassian's authorization flow.

#### Default scopes

Workato requests the following scopes by default:

- `read:jira-user`
- `read:jira-work`
- `write:jira-work`
- `manage:jira-project`
- `manage:jira-configuration`
- `manage:jira-webhook`
- `read:servicedesk-request`
- `write:servicedesk-request`
- `manage:servicedesk-customer`

#### Connect to Jira Service Desk using OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Jira Service Desk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira Service Desk` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 auth](/assets/oauth-2-0-auth.CuhHbAN1.png)_OAuth 2.0 connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select **Cloud**.
   
6. Use the **Auth type** drop-down menu to select **OAuth 2.0**.
   
7. Enter your Jira Service Desk subdomain in the **Subdomain** field.
   
8. Optional. Expand **Advanced settings** and use the **Scopes** field to request additional scopes. Refer to [Default scopes](#oauth-2-0-scopes) for the list of scopes Workato requests by default.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect** and sign in to your Jira Service Desk instance using your account username and password when prompted.
    
11. Authorize Workato's request to access your Jira Service Desk instance.
    

#### Jira Service Desk basic authentication with password

View basic authentication steps

Atlassian deprecated basic authentication with password for Jira Service Desk (cloud only) on December 1, 2018, in favor of API tokens. On-prem Jira Service Desk connections aren't affected by this change.

#### Connect to Jira Service Desk using basic authentication

Complete the following steps to set up a basic authentication connection to Jira Service Desk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Jira Service Desk` on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Basic password auth](/assets/basic-password-auth.CtTZL-sz.png)_Basic authentication connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to specify whether this is a cloud or on-prem connection.
   
6. Use the **Auth type** drop-down menu to select **Basic**.
   
7. Enter your Jira Service Desk subdomain in the **Subdomain** field.
   
8. Enter your Jira Service Desk username in the **Username** field.
   
9. Enter your Jira Service Desk password in the **Password** field.
   
10. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
11. Click **Connect**.
    

### Salesforce connection setup

View Salesforce connection setup steps

Workato supports OAuth 2.0 authentication and JWT bearer authentication connections for Salesforce.

#### OAuth 2.0 authentication

View OAuth 2.0 authentication steps

#### Connect to Salesforce using OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 (Authorization Code Grant) connection to Salesforce in Workato:

> **OAUTH RESTRICTIONS**
> 
> As of early September 2025, Salesforce restricts the use of uninstalled Salesforce Connected Apps. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for required actions if you encounter errors when you create a new connection. These steps are required for all new Salesforce connections starting **September 17, 2025**.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_OAuth2.0 Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Optional. Expand **Advanced settings** to configure the following options:
   
   Advanced settings
   
   - **Organization/community custom domain URL**: Enter the URL to your Salesforce community's custom domain. Required for community connections with unique domains.
   - **Requested permissions**: Select [permissions](https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5) to request for this connection. Refer to [Requested scopes](/en/connectors/salesforce#oauth2-scopes) for the scopes Workato requests.
   - **Verified user access configuration**: Configure custom auth for personal connections. Refer to [Runtime user connections](/en/features/runtime-user-connections) for more information.
   
   > **REFRESH TOKEN SCOPE IS REQUIRED**
   > 
   > The **Perform requests at any time (`refresh_token`, `offline_access`)** scope is one of the scopes Workato requests for OAuth 2.0 connections, but whether Salesforce actually grants this scope depends on the Connected App's own OAuth policies, not on the Workato connection's settings. Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) if your connection later disconnects when the access token expires. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
   
9. Click **Connect**.
   
10. Optional. If your Salesforce organization or community uses a custom domain, complete the following in the sign-in modal:
    
    - Click **Use Custom Domain**.
    - Enter your **Custom domain**, then click **Continue**.
    
    ![Salesforce custom domains](/assets/connection-custom-domain.D3hJN8X8.png)_Enter your Custom domain._
    
11. Enter your Salesforce **Username** and **Password**.
    
    ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
    
12. Click **Log In** to complete the setup.
    
    > **OAUTH\_APPROVAL\_ERROR\_GENERIC**
    > 
    > If you see this error, Salesforce is restricting the Workato app because it isn't installed. A Salesforce admin must install the app in **Connected Apps OAuth Usage** or assign the Salesforce permissions. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for details.
    

#### JWT bearer authentication

View JWT bearer authentication steps

> **ACTIONS ON BEHALF OF USER**
> 
> JWT connections can perform actions on behalf of a user you specify using the **On-behalf-of-user email** field. Contact your Workato Customer Success Manager to enable this feature.

#### How it works

JWT bearer authentication connects using a digital certificate that signs a JWT request. Workato sends a JWT to the Salesforce OAuth token endpoint, where Salesforce processes the JWT and issues an access token based on prior approval of Workato in Salesforce.

Although JWT bearer skips interactive sign-in, Salesforce still evaluates every request against the permissions of the user specified in the connection and attributes any changes to that user. Use a dedicated integration user rather than a personal account.

Refer to [Required roles and permissions](/en/connectors/salesforce#roles-and-permissions-required-to-connect) for the Salesforce permissions the connected user needs.

#### Generate a private key and certificate

JWT bearer authentication requires a private key and a certificate. The following command generates both using OpenSSL. Replace the `-subj` values with your own:

```bash
openssl req -x509 -sha256 -nodes -newkey rsa:2048 \
  -keyout server.key \
  -out server.crt \
  -days 365 \
  -subj "/CN=Your App Name/O=Your Organization/C=US"
```

This generates two files:

| File | Description |
| --- | --- |
| `server.key` | Your private key for Workato. Keep this secret. |
| `server.crt` | Your public certificate for Salesforce. |

Refer to Salesforce's documentation for more information:

- [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5): Details on how Salesforce uses this certificate to sign and validate JWTs.
- [Create a Private Key and Self-Signed Digital Certificate](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm): Other ways to generate a private key and certificate.

#### Create an external client app for JWT bearer

JWT bearer authentication also requires a registered external client app in Salesforce. Complete the following steps before creating your connection in Workato. Refer to Salesforce's [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US&type=5) documentation for more information.

1. Sign in to Salesforce.
   
2. Go to **Setup > Apps > External Client Apps > External Client App Manager**.
   
3. Click **New External Client App**.
   
4. Enter a name in the **External Client App Name** field, such as `Workato`.
   
5. Enter a name in the **API Name** field that meets the following requirements:
   
   - Contains only underscores and alphanumeric characters.
   - Is unique.
   - Starts with a letter.
   - Doesn't include spaces.
   - Doesn't end with an underscore.
   - Doesn't contain consecutive underscores.
6. Enter the contact email address for your app in the **Contact Email** field.
   
7. Use the **Distribution State** drop-down menu to select either **Local** or **Packaged**.
   
8. Expand **API (Enable OAuth Settings)** and select the **Enable OAuth** checkbox. Refer to Salesforce's [Configure the External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure_external_client_app_oauth_settings.htm&language=en_US&type=5) documentation for more information.
   
9. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
10. Select your OAuth scopes in the **OAuth Scopes** field based on the actions and triggers you plan to use, then click the **Move selection to Selected OAuth Scopes** arrow to apply them.
    
    ![Configure scopes for your external client app](/assets/oauth-scopes.B-mGtuor.png)_Configure scopes for your external client app_
    
    > **REFRESH\_TOKEN SCOPE IS REQUIRED**
    > 
    > If you see the error `refresh_token scope is required and the connected app should be installed and preauthorized`, add **Perform requests at any time (refresh\_token, offline\_access)** to your OAuth scopes. If you then see an invalid session error, also add **Manage user data via APIs (api)**.
    
11. Select **Enable JWT Bearer Flow** in the **Flow Enablement** section. Refer to Salesforce's [Configure a JWT Bearer Flow](https://help.salesforce.com/s/articleView?id=xcloud.configure_oauth_jwt_flow_external_client_apps.htm&language=en_US&type=5) documentation for more information.
    
12. Upload `server.crt` as the digital certificate.
    
13. Click **Create**.
    
14. Click the **Policies** tab, then click **Edit**.
    
15. Expand the **OAuth Policies** section and set **Permitted Users** to **Admin approved users are pre-authorized**.
    
    > **USER HASN'T APPROVED THIS CONSUMER**
    > 
    > If you see this error when connecting, this step was likely missed.
    
16. Locate the **App Policies** section. Add either the [profile](https://help.salesforce.com/s/articleView?id=admin_userprofiles.htm&language=en_US&type=5) or [permission set](https://help.salesforce.com/s/articleView?id=000386289&language=en_US&type=1) assigned to the Salesforce user Workato connects as to the **Select Profiles** or **Select Permission Sets** list. Refer to Salesforce's [Preauthorize User App Access Through External Client App Policies](https://help.salesforce.com/s/articleView?id=xcloud.preauth_user_app_access_through_eca.htm&language=en_US&type=5) documentation for more information.
    
    > **USER IS NOT ADMIN APPROVED TO ACCESS THIS APP**
    > 
    > If you see this error when connecting, this step was likely missed.
    
17. Click **Save**.
    
18. Click the **Settings** tab for your external client app.
    
19. Expand the **OAuth Settings** section.
    
20. Click **Consumer Key and Secret**.
    
21. Verify your identity when prompted.
    
22. Copy the **Consumer Key**. You'll enter this as the **Issuer** when connecting in Workato.
    

#### Connect to Salesforce using JWT bearer

Complete the following steps to connect to Salesforce using JWT bearer authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce JWT Connection](/assets/salesforce-new-jwt-connection.BCDJGTAT.png)_Configure Salesforce JWT Bearer connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **JWT token**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Paste the full contents of `server.key` in the **Private key** field, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
   
8. Enter the **Consumer Key** from your external client app in the **Issuer** field.
   
9. Enter the **Subject** for the JWT connection. This is the username of the Salesforce user you want Workato to authenticate as, or a valid Experience Cloud username if you're connecting to an Experience Cloud site. You can use principal (`prn`) in place of subject (`sub`) for backward compatibility. If you specify both, Workato uses `prn`.
   
10. Enter your **Salesforce Subdomain**. For example, if your Salesforce URL is `yourInstance.salesforce.com`, the subdomain is `yourInstance`.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
    
12. Click **Connect**.
    

### Confluence connection setup

View Confluence connection setup steps

The Confluence connector supports the following authentication types:

- [Basic](#confluence-basic)
- [API token](#confluence-api-token)
- [OAuth 2.0](#confluence-oauth)

#### Basic authentication

Use basic authentication with your Confluence username and password.

View basic authentication steps

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
    

#### API token authentication

You must generate an API token to use API token authentication.

##### Confluence setup for API token authentication

View generate API token steps

Complete the following steps to generate an API token in Confluence:

1. Go to the Atlassian [API Tokens](https://id.atlassian.com/manage/api-tokens) page.
   
2. Click **Create API token**.
   
3. Enter a **Name** and select an **Expires on** date.
   
4. Click **Create**.
   
5. Copy and save the **API token** for use in Workato.
   

##### Connect to Confluence with API token authentication

View connect to Confluence with API token authentication steps

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
    

#### OAuth 2.0 authentication

You must generate a client ID and secret to use OAuth 2.0 authentication.

##### Confluence setup for OAuth 2.0 authentication

View generate client ID and secret steps

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
    

##### Connect to Confluence with OAuth 2.0 authentication

View connect to Confluence with OAuth 2.0 authentication steps

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
    

### PagerDuty connection setup

View PagerDuty connection setup steps

The PagerDuty connector uses API key authentication.

#### Create an API key

View create API key steps

You must create an API key (PagerDuty integration key) to connect to Workato. PagerDuty supports the following types of API keys:

- **General access API key**: This API key has access to all objects in your PagerDuty instance.
- **Personal API key**: This API key is restricted according to the user's permissions. This requires PagerDuty [advanced permissions](https://support.pagerduty.com/docs/advanced-permissions).

Complete the following steps to create a PagerDuty API key:

1. Go to **Integrations > Developer Tools > API Access Keys** and click **Create New API Key**.
   
   Alternatively, go to **Profile > User settings** to create a Personal API key.
   
2. Enter a description that helps identify the key, such as **Workato integration key**. Ensure that you don't select `Read-only API Key`. This connection requires read and write permissions to function properly.
   
   ![Provide the API key with write permissions](/assets/api-key-permissions.DCypS1mp.png)_Provide the API key with write permissions_
   
3. Store the API key in a secure location. Use this API key to authenticate with Workato.
   

#### Connect to PagerDuty on Workato

View connect to PagerDuty steps

Complete the following steps to connect to PagerDuty in Workato:

1. Select **Create > Connection** or press C twice.
   
2. Search for `PagerDuty` on the **New connection** page and select it.
   
3. Enter a name in the **Connection name** field.
   
   ![Connect to PagerDuty](/assets/pagerduty-connection-setup.DEV0ftqU.png)_Connect to PagerDuty_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the API key you generated in the **API key** field.
   
6. Select **Connect** to verify and save the connection. Workato displays a success message when the connection is established.
   

### Case Intake & Triage role requirements

Each tool's availability depends on the permissions of the connected account. Calling a tool without the required permission returns a `permission_denied` outcome rather than a partial result.

- **Jira Service Desk** requires the project-level **Browse Users and Groups** or **Assign Issues** permission and the following scopes at a minimum:
  
  - `read:servicedesk-request`
  - `read:jira-work`
  - `write:jira-work`
  - `read:jira-user`
  
  Refer to [Scopes for OAuth 2.0 (3LO) and Forge apps](https://developer.atlassian.com/cloud/jira/platform/scopes-for-oauth-2-3LO-and-forge-apps/) for the complete list of scopes.
  
- **Salesforce** requires read access to the following objects:
  
  - Account
  - Entitlement
  - Contact, only when [account\_match\_rule](#data-table-configuration) is `contact_email_lookup`
  - Any configured escalation object
- **Confluence** requires read access to the spaces you set in [confluence.space\_keys](#data-table-configuration).
  
- **PagerDuty** requires rights to the service set in [pagerduty.service\_id](#data-table-configuration).
  

### Data table configuration

Edit the following data tables to control triage rules, connector integration settings, escalation timing, and operational limits:

- `triage_matrix`: Define the priority matrix. Create a row for every `severity`, `impact`, and `tier` combination, including the configured `unknown_customer_tier`, with the resulting `priority` (P1–P4).
  
- `suggested_routing_map`: Map each `severity`, `impact`, and `tier` combination to a `routing_value`. Required when `jsm.assignment_mode` is `routing_field`.
  
- `suggested_assignee_map`: Map each `severity`, `impact`, and `tier` combination to an `account_id`. Required when `jsm.assignment_mode` is `specific_agent`.
  
- `severity_value_map`: Map each raw JSM severity field value (`raw_value`) to a `mapped_value` of `low`, `medium`, `high`, or `critical`. Every raw value on a ticket must have a row. An unmapped value returns `classification_required`, an outcome that blocks the triage write until someone sets the field on the ticket.
  
- `impact_value_map`: Map each raw JSM impact field value to `single_user`, `multi_user`, `department`, or `org_wide`.
  
- `routing_value_map`: Map each raw JSM routing field value to a normalized routing value.
  
- `org_mapping`: Map a customer domain or identifier pattern (`pattern`) to a Salesforce Account ID (`account_id`). Required when `salesforce.account_match_rule` is `organization_mapping_table`.
  
- `entitlement_tier_derivation`: Map a Salesforce entitlement process (`SlaProcess`) name or ID (`sla_process_key`) to this server's tier values (`tier`). Required when `salesforce.tier_source` is `active_entitlement`.
  
- `case_intake_config` contains the following keys:
  

| Key | Description |
| --- | --- |
| `jsm.cloud_id` | Enter the Atlassian cloud ID for this deployment. Used as part of the workflow-state key. |
| `jsm.default_project_key` | Enter the default Jira Service Desk project key. |
| `jsm.severity_field.id` | Enter the Jira custom field ID that carries severity. |
| `jsm.impact_field.id` | Enter the Jira custom field ID that carries impact. |
| `jsm.routing_field.id` | Enter the Jira custom field ID that drives queue placement. Required when `jsm.assignment_mode` is `routing_field`. |
| `jsm.assignment_mode` | Choose `routing_field` (default) or `specific_agent`. |
| `jsm.priority_mapping.P1` / `.P2` / `.P3` / `.P4` | Map this server's P1–P4 priorities to the JSM instance's native priority names. |
| `salesforce.tier_source` | Choose `account_field` or `active_entitlement`. |
| `salesforce.tier_field` | Enter the Account custom field that holds the customer's tier. Required when `tier_source` is `account_field`. |
| `salesforce.account_match_rule` | Choose one of `direct_account_id_field`, `contact_email_lookup`, `custom_account_domain_field`, or `organization_mapping_table`. |
| `salesforce.direct_account_id_field` | Enter the JSM custom field holding the Salesforce Account ID. Required when `account_match_rule` is `direct_account_id_field`. |
| `salesforce.custom_account_domain_field` | Enter the Account custom field holding the customer's domain. Required when `account_match_rule` is `custom_account_domain_field`. |
| `salesforce.unknown_customer_tier` | Enter the fallback tier used when no Account matches the ticket. |
| `salesforce.health_field` | Optional. Enter an Account field to surface as context. This field doesn't feed the priority matrix. |
| `salesforce.escalation_object.api_name` / `.account_relationship_field` / `.status_field` / `.open_status_values` / `.returned_fields` | Optional. Enter the values needed to surface a customer's open escalations as context. |
| `confluence.enabled` | Configure whether the `search_known_issues` tool is available. |
| `confluence.space_keys` | Enter the Confluence spaces to search for runbooks. |
| `confluence.max_results` | Specify the default number of runbook search results to return. Defaults to `5`, capped by `server_limits.max_kb_results`. |
| `pagerduty.enabled` | Configure whether P1 on-call escalation is available through the `trigger_p1_escalation` tool. |
| `pagerduty.service_id` | Enter the PagerDuty service to page for P1 escalations. |
| `pagerduty.escalation_policy_id` | Optional. Enter an escalation policy to override the service's default. |
| `pagerduty.priority_mapping.P1` | Map this server's P1 priority to a PagerDuty priority ID. |
| `pagerduty.from_email` | Enter the PagerDuty user email required by the incident's `From` header. |
| `pagerduty.approval_token_ttl_seconds` | Specify how long a P1 escalation approval token remains valid. Defaults to `120`. |
| `server_limits.max_kb_results` | Specify the hard cap on Confluence runbook search results. Defaults to `10`. |
| `server_limits.max_assignable_results` | Specify the maximum assignable-agent results returned in a single page. Defaults to `50`, subject to the Jira Service Desk 1000-user endpoint cap. |
| `server_limits.snapshot_ttl_seconds` | Specify how long a customer context snapshot remains valid. Defaults to `600`. |
| `server_limits.payload_max_chars` | Specify the field-level character caps applied when sanitizing ticket text for the PagerDuty payload. Defaults to `1000`. |
| `triage_matrix_version` | Enter a version identifier for the triage matrix. Every preview and audit record includes this value. |
| `triage_matrix_content_hash` | A hash of the current triage matrix content, written into audit records and escalation payloads to confirm which matrix version produced them. Don't set this manually. |
| `audit.log_retention_days` | Specify how many days to retain audit records. Defaults to `365`. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data tables:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Case Intake & Triage** folder.
   
4. Select the data table to update, such as `triage_matrix` or `case_intake_config`.
   
5. [Add](/en/data-tables/user-interface/edit#add-a-new-row) or [edit](/en/data-tables/user-interface/edit#edit-a-row) rows to make your changes. For example, add a row to `case_intake_config` with the key `pagerduty.service_id` and your PagerDuty service's ID as the value.
   

## How to use Case Intake & Triage MCP server tools

Refer to the following sections for detailed information on available tools.

### get\_case\_context tool

The **get\_case\_context** tool fetches a ticket's request state and classification fields, and establishes the workflow for the case. Your LLM uses this tool before any other tool in the sequence, since every downstream tool requires the `workflow_id` it returns.

**Try asking**:

- `Triage HELPDESK-1234`
- `Pull up ticket HELPDESK-1234`
- `What's the status of HELPDESK-1234?`

### get\_customer\_account\_context tool

The **get\_customer\_account\_context** tool resolves the ticket's Salesforce account and returns the customer's tier and active entitlements for the [triage matrix](#data-table-configuration). Your LLM uses this tool right after **get\_case\_context**, since **apply\_triage\_to\_case** requires the `context_snapshot_id` it returns.

**Try asking**:

- `What tier is the customer on ticket HELPDESK-1234?`
- `Does this customer have an active entitlement?`
- `Triage HELPDESK-1234`

### search\_known\_issues tool

The **search\_known\_issues** tool searches configured Confluence spaces for a runbook matching the ticket. Your LLM uses this tool to find documentation related to a ticket's issue. The server derives the search terms from the ticket's subject and description, and only adds a topic you explicitly name as a hint.

**Try asking**:

- `Find a runbook that matches this ticket`
- `Search Confluence for a runbook about database timeouts`
- `Is there a known issue for this?`

### apply\_triage\_to\_case tool

The **apply\_triage\_to\_case** tool runs the ticket through the [triage matrix](#data-table-configuration) and writes the resulting priority and routing to the ticket. Your LLM calls this tool once to preview the plan, then calls it again to apply it.

**Try asking**:

- `Triage HELPDESK-1234`
- `Prioritize this ticket`
- `Show me the triage plan before you apply it`
- `Re-triage HELPDESK-1234 now that the impact has changed`

### trigger\_p1\_escalation tool

The **trigger\_p1\_escalation** tool notifies the on-call PagerDuty responder for a ticket triaged as P1. Your LLM only uses this tool when the committed priority is P1. It calls the tool once to preview the on-call target and request a single-use approval token, then calls it again with that token after you approve it to send a page.

**Try asking**:

- `Prioritize this ticket and page on-call if it's P1`
- `Page on-call for HELPDESK-1234`
- `Who's currently on-call for this escalation policy?`

### list\_assignable\_agents tool

The **list\_assignable\_agents** tool lists the users eligible for assignment to a ticket. Your LLM uses this tool to find who could work on a ticket, or to suggest an alternative to the matrix-suggested assignee.

**Try asking**:

- `Who could work on HELPDESK-1234?`
- `Reassign HELPDESK-1234 to a different agent`
- `Show me other agents who could take this ticket`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/employee-offboarding-process-mcp-server.md
description: >-
  Use the Employee Offboarding MCP server to connect your LLM to Workday, Okta,
  Google Workspace, Slack, Zoom, and ServiceNow to preview a departing
  employee's full access revocation plan, execute it after explicit
  confirmation, and track every system from a single approved Workday
  termination event.
---

# Employee Offboarding MCP server

The Employee Offboarding MCP server enables LLMs to interact with Workday, Okta, Google Workspace, Slack, Zoom, ServiceNow, Salesforce, and GitHub for cross-system access revocation when an employee leaves your organization, through natural conversation. It provides tools to resolve the departing employee, preview the full revocation plan, execute the plan after explicit confirmation, track per-system progress, retry failed steps, and cancel work that's still in progress.

## Uses

Use the Employee Offboarding MCP server to perform the following actions:

- Resolve a departing employee by name, work email, or Worker ID and review their pending Workday termination events
- Preview the full cross-system revocation plan bound to an approved Workday termination event, without committing changes
- Revoke Okta sessions and OAuth tokens, then suspend the Okta account
- Suspend the employee's Google Workspace account through the Directory
- Deactivate the employee's Slack and Zoom accounts, and Salesforce and GitHub when your deployment enables them
- Create ServiceNow tickets for the work outside automated scope, including device return, mail-forwarding follow-up, and personal access token audits
- Notify the departing employee's manager
- Schedule revocation for a future access cutoff during a notice period, or revoke immediately for an involuntary termination
- Track per-system progress, retry failed non-critical steps, and cancel scheduled or in-progress offboardings

Additionally, use the server's built-in [Employee Offboarding MCP apps](#employee-offboarding-process-mcp-apps) to review a plan before you confirm it and to track execution afterward.

## Example prompts

Use the following example prompts to invoke Employee Offboarding MCP server tools:

- `Offboard Dan Chen. The approved Workday termination event is TERM-4821.`
- `Look up Ariel Miller's pending termination events.`
- `Offboard this employee immediately. The termination is effective today.`
- `Show me the revocation plan before anything gets cut.`
- `What's the status of offboarding off_a1b2c3?`
- `Which systems failed on Jade's offboarding?`
- `Retry the Zoom deactivation step.`
- `Cancel the scheduled offboarding for Worker 100294.`
- `Show me every offboarding in flight.`
- `List the offboardings I started in the last two weeks.`

## Employee Offboarding MCP server tools

The Employee Offboarding MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [find\_employee](#find-employee-tool) | Resolves an employee from a name, email, or Worker ID and returns their identity, manager, and pending Workday termination events. |
| [execute\_offboarding](#execute-offboarding-tool) | Returns a revocation plan for your approval, then executes that specific plan when you confirm it. |
| [get\_offboarding\_status](#get-offboarding-status-tool) | Returns per-system status for an offboarding, including criticality and retry availability. |
| [retry\_offboarding\_step](#retry-offboarding-step-tool) | Retries a single failed step after a preview, without re-running earlier or later steps. |
| [cancel\_offboarding](#cancel-offboarding-tool) | Cancels an offboarding according to its current state, without reactivating any suspended account. |
| [list\_offboardings](#list-offboardings-tool) | Lists offboardings by status, initiator, employee, or date range. |

> **EVERY COMMIT NEEDS ITS OWN APPROVAL**
> 
> `execute_offboarding`, `retry_offboarding_step`, and `cancel_offboarding` each run in two stages. Your LLM calls the tool to return a preview, then calls it again only after you explicitly approve that preview.
> 
> Approval doesn't carry over. The server binds your confirmation to the specific preview that immediately precedes it, and rejects a plan that's expired or has an underlying state that's moved.

## Install the Employee Offboarding MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Employee Offboarding connection setup

Configure the following connections to set up the Employee Offboarding MCP server:

- [Workday](#workday-connection): Required. Supplies the approved termination event.
- [Okta](#okta-connection): Required. Revokes sessions and OAuth tokens, then suspends the account.
- [Google Workspace](#google-workspace-connection): Required. Suspends the employee's Directory user.
- [Slack](#slack-connection): Required. Resets sessions and deactivates the user.
- [Zoom](#zoom-connection): Required. Deactivates the user.
- [ServiceNow](#servicenow-connection): Required. Creates the device-return, mail-forwarding, and token-audit tickets, and records the manager notification.
- [Salesforce](#salesforce-connection): Required.
- [GitHub](#github-connection): Required.

> **OKTA SSO IS A DEPLOYMENT PREREQUISITE**
> 
> Enforce Okta SSO on every SaaS application you plan to use before you deploy this MCP server. The MCP server doesn't check for SSO enforcement at runtime.

### Employee Offboarding role requirements

Each tool's availability depends on the permissions of the connected account. Calling a tool without the required permission returns a `permission_denied` outcome rather than a partial result.

The MCP server separates the two identities on every audit record. The authenticated caller is recorded as `initiating_actor` and must hold the HR offboarding permission. The per-deployment service credential that performs each downstream administrative operation is recorded as `execution_identity`. HR business partners don't hold the service credentials.

- **Workday**: Requires an integration user with permission to read the termination event.
  
- **Okta**: Requires an admin API token with session management, token management, and user lifecycle management scopes.
  
- **Google Workspace**: Requires a service account with domain-wide delegation and the `admin.directory.user` scope, granted to an account holding the User Management admin role. Gmail API access isn't required, because the server only suspends the Directory user.
  
- **Slack**: Requires a Business+ or Enterprise plan for SCIM deactivation. The individual session-reset method requires Enterprise.
  
- **Zoom**: Requires a Business plan or above.
  
- **ServiceNow**: Requires write scope on the incident and request tables you configure.
  
- **Salesforce**: Requires Enterprise Edition or above and the Manage Users permission.
  
- **GitHub**: Requires GitHub Enterprise Cloud, with either SCIM provisioning through Enterprise Managed Users (EMU) or SAML SSO on member accounts.
  

#### Workday connection setup steps

View Workday REST connection setup steps

The Workato Workday connector is categorized into three distinct types: the main Workday connector, the Workday Web Services connector, and the Workday REST connector. Each type follows a similar authentication pattern but differs slightly in support capabilities and functionalities.

Workday doesn't support outbound webhooks, so the Workato Workday connector consumes termination events by polling, on a five to fifteen minute interval by default. This sets a threshold on how quickly a newly approved event becomes visible to `find_employee`. It doesn't affect the offboarding itself, which you initiate once you have the event ID.

The Workday REST API requires authentication through an OAuth client setup.

> **API CLIENTS FOR INTEGRATION NOT SUPPORTED**
> 
> Register a standard Workday API client to complete this connection. Workday API clients for Integration aren't supported in the Employee Offboarding MCP server.

##### Register a new API client in Workday

View API client setup steps

The Employee Offboarding MCP server authenticates each user individually through their own Workday login. The server doesn't use an Integration System User (ISU) like the Workday connector.

##### Register a new API client

Complete the following steps to register an API client in Workday REST:

1. Sign in to your Workday REST account.
   
2. Enter `Register API Client` to locate the **Register API Client** task.
   
3. Enter a name for your API client in the **Client Name** field.
   
4. Go to the **Client Grant Type** section and select **Authorization Code Grant**.
   
5. Go to the **Access Token Type** section and select **Bearer**.
   
6. Enter `https:www.workato.com/oauth/callback` in the **Redirection URI** field.
   
7. Enter `30` in the **Refresh Token Timeout (in days)** field.
   
8. Enter the scopes for the connection in the **Scope (Functional Areas)** field. Refer to [Workday End User MCP server Minimum permissions](/en/mcp/prebuilt-mcps/workday-end-user-mcp-server#minimum-permissions) if you're connecting to the Workday End User MCP server.
   
   ![Enter the scopes for the connection in the Scope (Functional Areas) field](/assets/api-client-rest.CIUw1iB9.png)_Enter the scopes for the connection in the **Scope (Functional Areas)** field_
   
9. Enter your client ID in the **Client ID** field.
   
10. Enter your REST API endpoint in the **Workday REST API Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
    
11. Enter your token endpoint in the **Token Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
    
12. Enter your authorization endpoint in the **Authorization Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://impl.workday.com/example/authorize`
    
13. Click **Done**.
    

##### Find your token endpoint URL

Complete the following steps to find your token endpoint URL in Workday:

1. Enter **View API Clients** into the search field in Workday.
   
2. Access the **View API Clients** report from the search results.
   
3. Save the URLs listed in the **Token Endpoint** and **Authorization Endpoint** fields. These URLs are required for the OAuth 2.0 connection.
   
   ![Save the token endpoint and authorization endpoint URLs](/assets/save-url.BkmumQyc.png)_Save the token endpoint and authorization endpoint URLs_
   

##### Complete setup in Workato

Complete the following steps to configure your Workday connection in Workato using OAuth 2.0 authentication:

View OAuth 2.0 authentication steps

1. Enter a unique **Connection name** to identify your Workday account in Workato.
   
   ![Set up your connection](/assets/workday-rest-connection.IzDCKMEG.png)_Set up your connection_
   
2. Use the **Location** drop-down to select the project or folder to store this connection.
   
3. Use the **Connection type** drop-down menu to select **Cloud**.
   
4. Enter your REST API endpoint in the **REST API endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
   
5. Enter your authorization endpoint in the **Authorization endpoint** field. You can find this value in your Workday API client details. For example: `https://impl.workday.com/example/authorize`
   
6. Enter your token endpoint in the **Token endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
   
7. Enter your client ID in the **Client ID** field.
   
8. Enter your client secret in the **Client Secret** field.
   
9. Enter your refresh token in the **Refresh token** field.
   
   > **DON'T PROVIDE A REFRESH TOKEN FOR MCP SERVERS**
   > 
   > Don't provide a refresh token if you're connecting Workday to an MCP server.
   
10. Click **Connect**.
    

#### Okta connection setup steps

View Okta connection setup steps

This deployment uses Okta's API key authentication method (an Okta API token). The token inherits the permissions of the administrator who generates it, since Okta API tokens don't support granular OAuth scopes the way Okta's authorization code grant and client credentials methods do.

#### Generate an API key

  

> **API KEY PRIVILEGES AND LIMITATIONS**
> 
> You must have administrator privileges in Okta to create an API key. Ensure that you're logged in as an administrator before you proceed.
> 
> Workato requires that the user and API key used in the connection have **Organization Administrator** or **Super Administrator** permissions. API keys inherit all permissions from the administrator who created them and can't be restricted to specific resources or operations.
> 
> Refer to [Create an API token](https://developer.okta.com/docs/guides/create-an-api-token/create-the-token/) for more information.

Complete the following steps to generate an API key in Okta:

1. Sign in to Okta.
   
2. Go to **Security > API > Token**.
   
3. Click **Create token** to generate an API key. The key inherits the permissions of the administrator who created it.
   

#### Connect to Okta using API key-based authentication

Complete the following steps to create an API key connection to Okta in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Okta** as your connection on the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Okta API key connection setup](/assets/connection-setup-api.VbvzwXfa.png)_Okta API key connection setup_
   
4. Use the **Authentication type** drop-down menu to select **API key**.
   
5. Enter your Okta domain name in the **Okta domain** field. For example, `mycompany.okta.com` or `mytest.oktapreview.com`. Ensure that the domain name you enter doesn't include `-admin`, such as `mycompany-admin.okta.com`, as this URL is used to access the Okta admin console from the UI and isn't an OAuth endpoint.
   
6. Enter the API key generated in your Okta instance.
   
7. Click **Connect**.
   

#### Google Workspace connection setup steps

View Google Workspace connection setup steps

This deployment requires service account authentication. The Google Workspace connector's OAuth 2.0 authentication method ties the connection to one employee's own Google identity, which can't suspend another employee's account.

You must enable the Google Workspace API to complete the connection setup.

> **REQUIRED SCOPE FOR SERVICE ACCOUNT AUTHENTICATION**
> 
> Ensure that you have the `admin.directory.user` scope to successfully suspend Directory users.
> 
> The service account impersonates the user based on the email address you provide during the connection setup after authentication is complete.

You must enable the Google Workspace API to complete the connection setup.

> **REQUIRED SCOPES FOR SERVICE ACCOUNT AUTHENTICATION**
> 
> Ensure that you have the following required permissions to successfully connect to Google Workspace using a service account:
> 
> - `admin.directory.user`
> - `admin.directory.orgunit`
> - `admin.directory.domain`
> - `admin.directory.group`
> - `admin.directory.group.member`
> - `admin.datatransfer`
> - `admin.directory.device.mobile.action`
> - `admin.directory.userschema`
> - `admin.reports.audit.readonly`
> - `admin.reports.usage.readonly`
> - `admin.directory.rolemanagement`
> - `admin.directory.user.security`
> 
> The service account impersonates the user based on the email address you provide during the connection setup after authentication is complete.

Complete the following steps to connect to Google Workspace using service account authentication:

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace** as your connection.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Service account**.
   
6. Enter the service account's email address in the **GCP project service account email** field.
   
   ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
   
7. Enter the **Private key** and **User email**. Retrieve the private key from the downloadable JSON. Include both the `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n`.
   
8. Click **Sign in with Google**.
   

#### Slack connection setup steps

View Slack connection setup steps

Slack deactivation and session reset each depend on your Slack plan:

| Slack plan | Deactivate through SCIM | Reset sessions |
| --- | --- | --- |
| Enterprise Grid | Supported | Supported |
| Business+ | Supported | Not available |
| Pro and Free | Not available | Not available |

The Slack step returns `skipped_plan_unsupported` when your plan doesn't support an operation.

You must authorize Workato to access your Slack organization using the OAuth 2.0 standard.

Complete the following steps to connect to Slack in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Slack` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Slack connection](/assets/slack-connection.BT6h8ZMj.png)_Slack connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand **Advanced** and use the **Is this a Classic Slack app?** drop-down menu to select `Yes` or `No`. Select `Yes` only if you haven't migrated your Slack app to granular permission scopes. Refer to [Moving to granular permission scopes](/en/connectors/slack#moving-to-granular-permission-scopes) for more information.
   
6. Optional. Use the **OAuth user scopes** drop-down menu to select the OAuth user scopes to request for your connection. Leave this field empty to request the [default scopes](/en/connectors/slack#scopes).
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Custom OAuth profiles for Slack](/en/connectors/slack/custom-oauth) for more information.
   
8. Click **Connect**.
   
9. Click **Allow** to grant Workato permission to access your account.
   

#### Zoom connection setup steps

View Zoom connection setup steps

The Zoom connector uses OAuth 2.0 authentication.

Complete the following steps to connect to Zoom in Workato with OAuth 2.0 authentication:

- [Add an API user](#add-an-api-user)
- [Create a custom OAuth profile](#create-custom-oauth-profile)
- [Connect to Zoom with OAuth 2.0 authentication](#connect)

> **RECOMMENDED SETUP**
> 
> We recommend that you set up a dedicated API user account in Zoom or create a custom OAuth profile to authorize Workato. This allows you to assign the API user to a role with only the necessary permissions.
> 
> Alternatively, you can use an existing Zoom owner or admin account if it has the required permissions. Some admin accounts may have restricted access based on their configuration.

##### Add an API user

View add an API user steps

Complete the following steps to set up a provisioned API user for Workato:

1. Sign into your [Zoom account](https://zoom.us/signin).
   
2. Go to **Admin > User Management > Users**.
   
   ![Add users](/assets/users-tab.CCrDasMU.png)_Add users_
   
3. Click **Add Users**.
   
4. Enter an appropriate email for the API user. We recommend an IT admin alias.
   
5. Enter `N/A` or make selections based on your requirements for the following fields: **Department**, **Manager**, **Job Title**, **Location**, and **User Groups**.
   
6. Click **Add**.
   
7. Go to **Admin > Roles**.
   
8. Select **Add Role**.
   
9. Provide a **Role Name** and **Description**.
   
10. Click **Add**.
    
11. Go to **Roles > Roles Settings** and add the following permissions to your Zoom role. Role permissions are required to allow the Workato Zoom connector to perform account-level actions, such as scheduling meetings or webinars on behalf of other Zoom users.
    
    - `Users: View and Edit`
    - `Role management: View and Edit`
    - `Groups: View and Edit`
    - `Recording management: View and Edit`
    - `Zoom rooms: View and Edit`
    - `Meetings: View`
    - `Webinars: View`
    - `Usage reports: View`
    - `Schedule tracking fields: View and Edit`
12. Click **Save Changes**.
    
13. Go to **User Management > Users** and locate the user you created in the preceding steps.
    
14. Click **Edit** and use the **User Role** drop-down menu to select the role you created.
    
15. Click **Save**.
    

##### Create a custom OAuth profile

View create a custom OAuth profile steps

Complete the following steps to create a custom OAuth profile for Workato:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `Zoom` and select it as your app.
   
4. Enter a name for your custom OAuth profile in the **Name** field.
   
5. Click **Create new app**.
   
6. Go to the [Zoom App Marketplace](https://marketplace.zoom.us/) and sign in to your Zoom account if you're not signed in already.
   
7. Click **Develop > Build App**.
   
   ![Build app](/assets/build-app.EiC2eXFV.png)_Build app_
   
8. Choose the kind of app to create from the following options: **General App**, **Server to Server OAuth App**, or **Webhook Only App**. If you can't select the options, you must enable the **Zoom for developers** role. Refer to the Zoom [Select general app features](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#prerequisites) page to learn how to enable the **Zoom for developers** role.
   
9. Click **Create**.
   
10. Enter a name for your app and select how the app is managed. Refer to the Zoom [Step 2: Maintain basic information](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#step-2-maintain-basic-information) page for more information.
    
11. Copy and save the **Client ID** and **Client Secret** for use in Workato.
    
    ![Copy the Client ID and Client Secret](/assets/client-id-client-secret.rM4DBfar.png)_Copy the Client ID and Client Secret_
    
12. Enter `https://www.workato.com/oauth/callback` in the **OAuth Redirect URL** field.
    
13. Optional. Configure settings in the **Access**, **Surface**, and **Embed** tabs as required.
    
14. Go to **Scopes** and click **\+ Add Scopes** to add the required scopes.
    
15. Search for and select the required scopes for your connection.
    
    **MCP server**
    
    The Zoom Meetings MCP server requires the following scopes for tool functionality:
    
    - `meeting:read:list_past_participants`
    - `user:read:user`
    - `meeting:read:list_past_instances`
    - `cloud_recording:read:meeting_transcript`
    - `cloud_recording:read:list_recording_files`
    - `meeting:read:meeting`
    - `meeting:write:meeting`
    - `meeting:update:meeting`
    - `meeting:read:list_meetings`
    
    **Connector**
    
    The Zoom connector requires the following minimum scope:
    
    `user:read:user`
    
16. Click **Done**.
    
17. Go to the **Local Test** tab and select **Preview your app listing page** to ensure your settings are properly configured.
    
18. Return to the **New custom profile** page in Workato and paste the **Client ID** and **Client secret** into their respective fields.
    
    ![Paste the client ID and client secret](/assets/enter-client-id-client-secret.BjbVOHtd.png)_Paste the client ID and client secret_
    
19. Click **Save**.
    

##### Connect to Zoom with OAuth 2.0 authentication

View connect to Zoom with OAuth 2.0 authentication steps

Complete the following steps to connect to Zoom in Workato:

1. Click **Create > Connection**.
   
2. Search for `Zoom` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Zoom Connection Setup](/assets/connection-setup-zoom.i8W0drY7.png)_Name your connection_
   
4. Optional. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to specify OAuth scopes to request for your connection.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
6. Click **Connect**.
   
7. Sign in to your Zoom account.
   

#### ServiceNow connection setup steps

View ServiceNow ITSM connection setup steps

The ServiceNow connector supports the following authentication types:

- [Username and password (Basic authentication)](#username-password)
- [OAuth 2.0 (Authorization code grant)](#oauth-2-0)
- [Password grant](#password-grant)

##### Username and password

View Username and password authentication steps

Select **Username/Password** authentication type to connect to your ServiceNow instance with your login credentials.

![Username/Password connection](/assets/basic_connection.BrtIBb_F.png)_Username/Password connection_

| Field | Description |
| --- | --- |
| Connection name | Enter a unique name that identifies which ServiceNow instance it is connected to. |
| Authentication type | Choose an authentication type for this ServiceNow connection. The ServiceNow connector supports Username/Password (Basic) authentication, OAuth 2.0 using the authorization code grant, and Password grant authentication. |
| Instance name | Provide the name of your instance. For example, if your ServiceNow URL is `https://acme.service-now.com`, the instance name is `acme`. |
| Username | Provide the username you plan to use to connect to ServiceNow. |
| Password | Provide the password you plan to use to connect to ServiceNow. |
| Custom OAuth profile | Optional. Select a custom OAuth profile for this connection. |

##### OAuth 2.0

View OAuth 2.0 authentication steps

###### Set up an OAuth 2.0 client

Complete the following steps with a ServiceNow **admin** role to configure an OAuth 2.0 client:

1. Activate the **OAuth 2.0 (com.snc.platform.security.oauth)** plugin. Refer to the ServiceNow documentation for more information on how to [activate OAuth 2.0](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/security/task/t_ActivateOAuth.html).
   
   ![Activate OAuth plugin](/assets/oauth_plugin.D0N1wSeA.png)_Activate OAuth plugin_
   
2. Create an endpoint for a client application to gain access to your ServiceNow instance. Use `https://www.workato.com/oauth/callback` as the **Redirect URL**. Refer to the ServiceNow documentation for more information on how to [create an endpoint for external clients](https://docs.servicenow.com/bundle/washingtondc-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html).
   
   ![OAuth 2.0 client](/assets/oauth_client.BNp-l2zz.png)_OAuth 2.0 client_
   
3. Use the Client ID and Client secret to create a ServiceNow connection in Workato. This triggers an OAuth authorization code grant flow that opens a new browser window requesting authorization.
   

###### Complete setup in Workato

Select the **OAuth 2.0** authentication type to connect to your ServiceNow instance without using your login credentials. This authentication type allows you to grant access to Workato by obtaining a token rather than disclosing your login credentials.

ServiceNow Istanbul and later releases support OAuth 2.0 connections that use the authorization code grant. Ensure that your ServiceNow version supports this when selecting this authentication type.

![OAuth 2.0 connection](/assets/oauth_connection.DCQBdqZY.png)_OAuth 2.0 connection_

| Field | Description |
| --- | --- |
| Connection name | Enter a unique name that identifies which ServiceNow instance it is connected to. |
| Authentication type | Choose an authentication type for this ServiceNow connection. The ServiceNow connector supports Username/Password (Basic) authentication, OAuth 2.0 using the authorization code grant, and Password grant authentication. |
| Instance name | Provide the name of your instance. For example, if your ServiceNow URL is `https://acme.service-now.com`, the instance name is `acme`. |
| Client ID | Provide the Client ID for your connection to use for authorization. Refer to the [Set up an OAuth 2.0 client](#setting-up-oauth-2-0-client) section for more information on how to set up Application Registry for an OAuth client. |
| Client secret | Provide the Client secret for this OAuth application. Click **Toggle Password Visibility** (lock icon) to reveal the secret. |
| Custom OAuth profile | Optional. Select a custom OAuth profile for this connection. |

> **INVALID REFRESH TOKEN ERROR**
> 
> You may receive an `invalid_request` or `invalid refresh token` error after your ServiceNow OAuth 2.0 connection expires. This behavior occurs because ServiceNow limits how long a refresh token remains valid. You must reauthenticate the connection when the token expires.
> 
> You can adjust the **Refresh Token Lifetime** in your ServiceNow OAuth client configuration. Go to your ServiceNow instance, click **System OAuth > Application Registry**, open your Workato OAuth client, and review the **Refresh Token Lifetime** value. The default refresh token lifetime is **100 days**.
> 
> Refer to the [ServiceNow external client](https://www.servicenow.com/docs/bundle/zurich-platform-security/page/administer/security/task/t_CreateEndpointforExternalClients.html) documentation for more information.

##### Password grant

View Password grant authentication steps

Select the **Password grant** authentication type to connect to your ServiceNow instance. This authentication type allows you to grant Workato access by providing your login credentials, which are used to obtain an access token.

![Username/Password connection](/assets/password-grant-connection.C9jkM_JE.png)_Password grant connection_

| Field | Description |
| --- | --- |
| Connection name | Enter a unique name that identifies which ServiceNow instance it is connected to. |
| Authentication type | Choose an authentication type for this ServiceNow connection. The ServiceNow connector supports Username/Password (Basic) authentication, OAuth 2.0 using the authorization code grant, and Password grant authentication. |
| Instance name | Provide the name of your instance. For example, if your ServiceNow URL is `https://acme.service-now.com`, the instance name is `acme`. |
| Username | Provide the username you plan to use to connect to ServiceNow. |
| Password | Provide the password you plan to use to connect to ServiceNow. |
| Client ID | Provide the Client ID for the connection to use for authorization. Refer to the [Set up an OAuth 2.0 client](#setting-up-oauth-2-0-client) section for more information on how to set up Application Registry for an OAuth client. |
| Client secret | Provide the Client secret for this OAuth application. Click **Toggle Password Visibility** (lock icon) to reveal the secret. |
| Custom OAuth profile | Optional. Select a custom OAuth profile for this connection. |

#### Salesforce connection setup steps

View Salesforce connection setup steps

Workato supports OAuth 2.0 authentication and JWT bearer authentication connections for Salesforce.

##### Salesforce OAuth 2.0 authentication

View OAuth 2.0 authentication steps

#### Connect to Salesforce using OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 (Authorization Code Grant) connection to Salesforce in Workato:

> **OAUTH RESTRICTIONS**
> 
> As of early September 2025, Salesforce restricts the use of uninstalled Salesforce Connected Apps. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for required actions if you encounter errors when you create a new connection. These steps are required for all new Salesforce connections starting **September 17, 2025**.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_OAuth2.0 Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Optional. Expand **Advanced settings** to configure the following options:
   
   Advanced settings
   
   - **Organization/community custom domain URL**: Enter the URL to your Salesforce community's custom domain. Required for community connections with unique domains.
   - **Requested permissions**: Select [permissions](https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5) to request for this connection. Refer to [Requested scopes](/en/connectors/salesforce#oauth2-scopes) for the scopes Workato requests.
   - **Verified user access configuration**: Configure custom auth for personal connections. Refer to [Runtime user connections](/en/features/runtime-user-connections) for more information.
   
   > **REFRESH TOKEN SCOPE IS REQUIRED**
   > 
   > The **Perform requests at any time (`refresh_token`, `offline_access`)** scope is one of the scopes Workato requests for OAuth 2.0 connections, but whether Salesforce actually grants this scope depends on the Connected App's own OAuth policies, not on the Workato connection's settings. Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) if your connection later disconnects when the access token expires. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
   
9. Click **Connect**.
   
10. Optional. If your Salesforce organization or community uses a custom domain, complete the following in the sign-in modal:
    
    - Click **Use Custom Domain**.
    - Enter your **Custom domain**, then click **Continue**.
    
    ![Salesforce custom domains](/assets/connection-custom-domain.D3hJN8X8.png)_Enter your Custom domain._
    
11. Enter your Salesforce **Username** and **Password**.
    
    ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
    
12. Click **Log In** to complete the setup.
    
    > **OAUTH\_APPROVAL\_ERROR\_GENERIC**
    > 
    > If you see this error, Salesforce is restricting the Workato app because it isn't installed. A Salesforce admin must install the app in **Connected Apps OAuth Usage** or assign the Salesforce permissions. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for details.
    

##### Salesforce JWT bearer authentication

View JWT bearer authentication steps

> **ACTIONS ON BEHALF OF USER**
> 
> JWT connections can perform actions on behalf of a user you specify using the **On-behalf-of-user email** field. Contact your Workato Customer Success Manager to enable this feature.

#### How it works

JWT bearer authentication connects using a digital certificate that signs a JWT request. Workato sends a JWT to the Salesforce OAuth token endpoint, where Salesforce processes the JWT and issues an access token based on prior approval of Workato in Salesforce.

Although JWT bearer skips interactive sign-in, Salesforce still evaluates every request against the permissions of the user specified in the connection and attributes any changes to that user. Use a dedicated integration user rather than a personal account.

Refer to [Required roles and permissions](/en/connectors/salesforce#roles-and-permissions-required-to-connect) for the Salesforce permissions the connected user needs.

#### Generate a private key and certificate

JWT bearer authentication requires a private key and a certificate. The following command generates both using OpenSSL. Replace the `-subj` values with your own:

```bash
openssl req -x509 -sha256 -nodes -newkey rsa:2048 \
  -keyout server.key \
  -out server.crt \
  -days 365 \
  -subj "/CN=Your App Name/O=Your Organization/C=US"
```

This generates two files:

| File | Description |
| --- | --- |
| `server.key` | Your private key for Workato. Keep this secret. |
| `server.crt` | Your public certificate for Salesforce. |

Refer to Salesforce's documentation for more information:

- [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5): Details on how Salesforce uses this certificate to sign and validate JWTs.
- [Create a Private Key and Self-Signed Digital Certificate](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm): Other ways to generate a private key and certificate.

#### Create an external client app for JWT bearer

JWT bearer authentication also requires a registered external client app in Salesforce. Complete the following steps before creating your connection in Workato. Refer to Salesforce's [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US&type=5) documentation for more information.

1. Sign in to Salesforce.
   
2. Go to **Setup > Apps > External Client Apps > External Client App Manager**.
   
3. Click **New External Client App**.
   
4. Enter a name in the **External Client App Name** field, such as `Workato`.
   
5. Enter a name in the **API Name** field that meets the following requirements:
   
   - Contains only underscores and alphanumeric characters.
   - Is unique.
   - Starts with a letter.
   - Doesn't include spaces.
   - Doesn't end with an underscore.
   - Doesn't contain consecutive underscores.
6. Enter the contact email address for your app in the **Contact Email** field.
   
7. Use the **Distribution State** drop-down menu to select either **Local** or **Packaged**.
   
8. Expand **API (Enable OAuth Settings)** and select the **Enable OAuth** checkbox. Refer to Salesforce's [Configure the External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure_external_client_app_oauth_settings.htm&language=en_US&type=5) documentation for more information.
   
9. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
10. Select your OAuth scopes in the **OAuth Scopes** field based on the actions and triggers you plan to use, then click the **Move selection to Selected OAuth Scopes** arrow to apply them.
    
    ![Configure scopes for your external client app](/assets/oauth-scopes.B-mGtuor.png)_Configure scopes for your external client app_
    
    > **REFRESH\_TOKEN SCOPE IS REQUIRED**
    > 
    > If you see the error `refresh_token scope is required and the connected app should be installed and preauthorized`, add **Perform requests at any time (refresh\_token, offline\_access)** to your OAuth scopes. If you then see an invalid session error, also add **Manage user data via APIs (api)**.
    
11. Select **Enable JWT Bearer Flow** in the **Flow Enablement** section. Refer to Salesforce's [Configure a JWT Bearer Flow](https://help.salesforce.com/s/articleView?id=xcloud.configure_oauth_jwt_flow_external_client_apps.htm&language=en_US&type=5) documentation for more information.
    
12. Upload `server.crt` as the digital certificate.
    
13. Click **Create**.
    
14. Click the **Policies** tab, then click **Edit**.
    
15. Expand the **OAuth Policies** section and set **Permitted Users** to **Admin approved users are pre-authorized**.
    
    > **USER HASN'T APPROVED THIS CONSUMER**
    > 
    > If you see this error when connecting, this step was likely missed.
    
16. Locate the **App Policies** section. Add either the [profile](https://help.salesforce.com/s/articleView?id=admin_userprofiles.htm&language=en_US&type=5) or [permission set](https://help.salesforce.com/s/articleView?id=000386289&language=en_US&type=1) assigned to the Salesforce user Workato connects as to the **Select Profiles** or **Select Permission Sets** list. Refer to Salesforce's [Preauthorize User App Access Through External Client App Policies](https://help.salesforce.com/s/articleView?id=xcloud.preauth_user_app_access_through_eca.htm&language=en_US&type=5) documentation for more information.
    
    > **USER IS NOT ADMIN APPROVED TO ACCESS THIS APP**
    > 
    > If you see this error when connecting, this step was likely missed.
    
17. Click **Save**.
    
18. Click the **Settings** tab for your external client app.
    
19. Expand the **OAuth Settings** section.
    
20. Click **Consumer Key and Secret**.
    
21. Verify your identity when prompted.
    
22. Copy the **Consumer Key**. You'll enter this as the **Issuer** when connecting in Workato.
    

#### Connect to Salesforce using JWT bearer

Complete the following steps to connect to Salesforce using JWT bearer authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce JWT Connection](/assets/salesforce-new-jwt-connection.BCDJGTAT.png)_Configure Salesforce JWT Bearer connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **JWT token**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Paste the full contents of `server.key` in the **Private key** field, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
   
8. Enter the **Consumer Key** from your external client app in the **Issuer** field.
   
9. Enter the **Subject** for the JWT connection. This is the username of the Salesforce user you want Workato to authenticate as, or a valid Experience Cloud username if you're connecting to an Experience Cloud site. You can use principal (`prn`) in place of subject (`sub`) for backward compatibility. If you specify both, Workato uses `prn`.
   
10. Enter your **Salesforce Subdomain**. For example, if your Salesforce URL is `yourInstance.salesforce.com`, the subdomain is `yourInstance`.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
    
12. Click **Connect**.
    

#### GitHub connection setup steps

View GitHub connection setup steps

GitHub offboarding differs across account models. Declare which model applies to your organization during deployment, so the server removes membership through the correct path and records the model in the audit record.

| GitHub account model | How the server deprovisions |
| --- | --- |
| Enterprise Managed Users (EMU) | SCIM deprovision, which also revokes personal access tokens |
| Organization or enterprise membership with SAML SSO | Membership removal and SAML credential authorization revocation |

View GitHub authentication methods

Connect to GitHub on Workato using one of the following authentication methods:

- OAuth authentication. Workato recipes act on your behalf.
- GitHub Apps. Workato recipes act as the app. Refer to [GitHub App authentication](#github-app-authentication) .
- A personal access token

Refer to the [GitHub documentation](https://docs.github.com/en/free-pro-team@latest/developers/apps/differences-between-github-apps-and-oauth-apps) for more information.

##### OAuth authentication

View OAuth authentication steps

Complete the following steps to connect your GitHub to Workato using OAuth authentication:

1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
   
2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
   
3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu and select **OAuth App**.
   
6. Optional. Click **Advanced configuration** to display the **Host name** field.
   
7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
   
8. Click **Connect**. Workato redirects you to GitHub. The OAuth App requests authorization to access your GitHub account.
   

##### GitHub App authentication

You must first [register the app](#register-your-github-app) in your GitHub account and retrieve the credentials to connect to GitHub using a GitHub App.

![GitHub app auth](/assets/github-app-view.CmRUHryh.png)_Select Authentication type as GitHub app and collect details from your GitHub App!_

###### Register your GitHub app

View step to register your GitHub App

Complete the following steps to register your GitHub App and retrieve the credentials required to connect it to Workato:

1. Complete the [steps](https://docs.github.com/en/apps/creating-github-apps/registering-a-github-app/registering-a-github-app) in the GitHub documentation to register your GitHub App.
   
2. Retrieve your **GitHub App ID** in the **General** settings page of your GitHub app.
   
   ![app id](/assets/github-app-app-id.hjpO7iTw.png)_Save this App ID and place it into your connection_
   
3. Generate a **Private key** on the same page. GitHub automatically downloads this `.pem` file to your machine.
   
   ![Generate private key](/assets/github-app-private-key.Dqjm0LL8.png)_Generate the private key_
   
4. Open the `.pem` file in a text editor. The file should look similar to the following:
   
   ```
   -----BEGIN RSA PRIVATE KEY-----
   MIIEpAIBAAKCAQEAyL/wuiSaWoH0pyf366G5E7dbzzmON1qMMrWvls8RtZtgOLjb
   FBxj6gO2aUfoGbMCMqOYRV6xCn6tK118sGYMd5U/kCFu3IRPr/2GoEtcrf0TecQG
   ON+27ijH0Vpn62o8NzGejdy0AWujrtAl6F8xGZeze0PzrGvW6h/GnAdZO1gJnp8t
   wmEqEMXqAsPOQ0hkY+r+pE8RKQVsJCe+PIanBKp7RKWDi9usPFZQdQ==
   -----END RSA PRIVATE KEY-----
   ```
   
5. Copy the entire private key, including the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----`. Use this private key when you set up the connection in Workato.
   
6. Retrieve your **Installation ID** from the organization or user where you installed your GitHub App:
   
   - Users accounts: Go to **Settings > Applications > Your GitHub App > Configure**.
   - Organizations: Go to your organization's GitHub homepage. Click **Settings > Installed GitHub Apps > Configure**.
   
   The installation ID appears in the URL. For example, if the URL is `https://github.com/settings/installations/13876669`, the installation ID is `13876669`.
   
7. Save the installation ID. Enter this ID when creating the GitHub App connection in Workato.
   

###### Configure GitHub app authentication

View steps to authenticate your GitHub app

1. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Authentication type** drop-down menu and select **GitHub App**.
   
4. Enter your **GitHub App ID**.
   
5. Enter your **Github App Private key**.
   
6. Enter your **Installation ID**.
   
7. Optional. Click **Advanced configuration** to display the **Host name** field.
   
8. Optional. Enter a **Host name** if using GitHub Enterprise Server. Use your GitHub subdomain. For example, if your host URL is `https://github.example-organisation.com`, the subdomain is `github.example-organisation.com`.
   
9. Optional. Enter a **Custom OAuth profile**. This selection ensures that all requests to the app use the specified profile.
   
10. Click **Connect**.
    

##### Personal access token authentication

Retrieve your personal access token from GitHub to connect your GitHub account to Workato using a personal access token:

View steps to retrieve your GitHub personal access token

1. Go to **Github account > Settings > Developer settings > Personal access tokens > Generate new token**.
   
2. Click **Generate new token**.
   
3. Copy the token. Enter this token in Workato to authenticate the connection.
   

###### Complete setup in Workato

View Complete setup in Workato steps

Complete the following steps to set up your GitHub connection using a personal access token:

1. Sign in to your Workato account and go to the project where you plan to add your GitHub connection.
   
2. Click **Create > Connection** (or press C twice), then select **GitHub** as your connection.
   
3. Provide a **Connection name** that identifies which GitHub instance Workato is connected to.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu and select **Personal Access Token**.
   
6. Optional. Click **Advanced configuration** to display the **Host name** field.
   
7. Optional. Enter a **Host name**. This is applicable when using Github Enterprise Server. Enter your Github subdomain. For example, if your host URL is `https://github.example-organisation.com`, your subdomain is `github.example-organisation.com`.
   
8. Enter your **Personal Access Token**.
   
9. Optional. Enter a **Custom OAuth profile**. This ensures all requests to the app use the specified profile.
   
10. Click **Connect**.
    

#### Data table configuration

Edit the following keys in the `offboarding_config` data table to control which applications this deployment deprovisions, how it escalates and routes failures, and where it sends notifications:

| Key | Description |
| --- | --- |
| `enabled_list` | Choose which optional applications this deployment deprovisions. Select `salesforce`, `github`, or both. The server skips an application that isn't on this list and doesn't create a follow-up ticket for it, even if that application is assigned to the employee in Okta. This doesn't apply to Slack or Zoom, which the server deprovisions. |
| `notifications_channel` | Choose the channel the server uses to send the manager notification. |
| `github_account_model` | Declare which GitHub account model applies to your organization. This ensures that the server deprovisions through the correct path. Required when `enabled_list` includes `github`. |
| `github_enterprise` / `github_org` | Enter your GitHub Enterprise and organization slugs. Required when `github_account_model` needs them to resolve the account. |
| `escalation_target` | Enter the identity the [Status App](#status-app) surfaces when a critical step fails. |
| `okta_app_id_slack` / `okta_app_id_zoom` / `okta_app_id_salesforce` / `okta_app_id_github` | Enter each application's Okta app ID. The server adds a deactivation step only when this app is assigned to the departing employee in Okta. Salesforce and GitHub are only deprovisioned if they're also in the `enabled_list`. |
| `snow_assignment_it` / `snow_assignment_google_admin` / `snow_assignment_app_admin` | Enter the ServiceNow assignment group for the device-return, mail-forwarding, and token-audit tickets. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data table:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Select the **offboarding\_config** data table.
   
4. [Add](/en/data-tables/user-interface/edit#add-a-new-row) or [edit](/en/data-tables/user-interface/edit#edit-a-row) rows to make your changes. For example, set the row with key `enabled_list` to `salesforce, github`, or `notifications_channel` to your HR notification channel.
   

## How to use Employee Offboarding MCP server tools

Refer to the following sections for detailed information on available tools.

### find\_employee tool

The **find\_employee** tool resolves an employee from a name, work email, or Worker ID and returns their identity, manager, and pending Workday termination events. Your LLM uses this tool when you name an employee to offboard, or when you ask about someone's termination events.

**Try asking**:

- `Look up Ariel Miller.`
- `Find the employee with Worker ID 100294.`
- `Does Dan Chen have an approved termination event?`
- `Show me dan.chen@example.com, including terminated employees.`

### execute\_offboarding tool

The **execute\_offboarding** tool returns a revocation plan when you call it in preview, and executes that plan when you confirm it. Your LLM uses this tool when you ask to offboard an employee.

**Try asking**:

- `Offboard Dan Chen. The approved Workday termination event is TERM-4821.`
- `Offboard this employee immediately, effective now.`
- `Show me the plan for Worker 100294's offboarding before anything is cut.`
- `Resume the offboarding that needs attention for Ariel Okafor.`

### get\_offboarding\_status tool

The **get\_offboarding\_status** tool returns per-system status for an offboarding. Your LLM uses this tool when you ask how an offboarding is progressing, and immediately after you confirm a plan to report initial progress.

**Try asking**:

- `What's the status of offboarding off_a1b2c3?`
- `How far along is Dan Chen's offboarding?`
- `Which systems failed on Jade's offboarding?`
- `Show me the audit records for this offboarding.`

### retry\_offboarding\_step tool

The **retry\_offboarding\_step** tool retries a single failed step. Your LLM uses this tool when you ask to retry a step that failed, and it previews the retry before running it.

**Try asking**:

- `Retry the Zoom deactivation step.`
- `The Slack step failed. Can you try it again?`
- `Show me what retrying step 4 would do.`
- `Retry the failed ServiceNow ticket for this offboarding.`

### cancel\_offboarding tool

The **cancel\_offboarding** tool cancels an offboarding according to its current state. Your LLM uses this tool when you ask to cancel, and it previews the cancellation first so you can see what can and can't be undone.

**Try asking**:

- `Cancel the scheduled offboarding for Worker 100294.`
- `Stop the offboarding for Dan Chen.`
- `What would canceling off_a1b2c3 actually undo?`
- `Cancel the remaining steps. The termination was rescinded.`

### list\_offboardings tool

The **list\_offboardings** tool lists offboardings by status, initiator, employee, or date range. Your LLM uses this tool when you ask what's in progress, when you ask about recent offboardings, or when it needs to find an offboarding ID.

**Try asking**:

- `Show me every offboarding in progress.`
- `List the offboardings I started in the last two weeks.`
- `Which offboardings completed with failures this month?`
- `Find the offboarding for Worker 100294.`

## Employee Offboarding MCP apps

The Employee Offboarding MCP server includes two [MCP apps](/en/mcp/mcp-apps) that open at the two points where a structured view reduces error. Neither app adds a confirmation step or skips a preview. Refer to [MCP Apps](/en/mcp/mcp-apps) for more information.

### Plan Review App

The Plan Review App opens after `execute_offboarding` returns a preview. It shows the employee's identity alongside the Workday event that grounds the offboarding, including the event ID, type, approval timestamp, approver, termination reason category, and position time zone, so you can catch a plan built on the wrong event.

The app groups the planned actions by criticality, such as access revocation, SaaS deactivations, ServiceNow tickets, and manager notification. Each application appears with the exact action the server takes. The tickets the MCP server creates for out-of-scope work appear explicitly.

A countdown shows how long the plan remains valid. Confirming in the app calls `execute_offboarding` with your confirmation and the plan's ID.

### Status App

The Status App opens after you confirm a plan. It shows each system as a row in a timeline, with the action, a criticality badge, a status pill, and a timestamp. Rows update as the app polls `get_offboarding_status`, and each completed step shows an audit record ID, with links to the ServiceNow tickets the server created.

A critical step failure raises a banner naming your configured escalation target and pauses the steps that depend on it. A failed non-critical row offers a retry that opens an inline preview panel first, and canceling the remaining steps opens a cancellation preview panel the same way.

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/employee-onboarding-mcp-server.md
description: >-
  Use the Employee Onboarding MCP server to connect your LLM to Workday, Slack,
  and Google Calendar to kick off onboarding, track checklists, and escalate
  issues.
---

# Employee Onboarding MCP server

The Employee Onboarding MCP server enables LLMs to interact with Workday, Slack, and Google Calendar for employee onboarding through natural conversation. It provides tools to resolve the hire, preview and commit the initial kickoff, and manage self-service onboarding for both the new hire and the manager. This server works alongside the [Access Provisioning](/en/mcp/prebuilt-mcps/access-provisioning-mcp-server), [ServiceNow ITSM](/en/mcp/prebuilt-mcps/servicenow-itsm-mcp-server), or [Confluence](/en/mcp/prebuilt-mcps/confluence-mcp-server) MCP servers if they're installed. For example, if a Confluence server is installed, it answers onboarding and policy questions, and **escalate\_or\_create\_ticket** handles issues only.

## Uses

Use the Employee Onboarding MCP server to perform the following actions:

- Resolve a new hire by name, work email, or Worker ID and confirm their approved Workday hire event, including their region and employment context
- Preview then commit the kickoff, including the initial meeting, the hire's welcome email, and a manager pre-arrival notification
- Check onboarding status for a specific hire
- Get checklist items due for either the new hire's onboarding checklist or the manager's own pre-boarding checklist
- Mark a checklist item complete or reopen it
- Schedule additional onboarding meetings after the kickoff
- Notify HR about a new hire's issue or question over Slack, or ask general policy questions when a [Confluence](/en/mcp/prebuilt-mcps/confluence-mcp-server) server isn't available as a knowledge source
- List onboardings in progress or upcoming, or cancel an onboarding

### Example prompts

Use the following example prompts to invoke Employee Onboarding MCP server tools:

- `Kick off onboarding for Jordan Lee, starting the 22nd.`
- `Does Jordan Lee have an approved hire event yet?`
- `Show me the kickoff plan before anything gets scheduled.`
- `What's my onboarding status?`
- `What do I need to do this week?`
- `Mark the benefits enrollment item as done.`
- `What's on my pre-boarding checklist for Jordan Lee?`
- `My laptop hasn't shown up yet.`
- `Show me everyone starting this month.`

## Employee Onboarding MCP server tools

The Employee Onboarding MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [find\_new\_hire](#find-new-hire-tool) | Resolves a new hire and returns their identity, hiring manager, region and employment context, and approved Workday hire event. |
| [initiate\_onboarding](#initiate-onboarding-tool) | Previews the kickoff, then schedules the initial meeting, sends the hire's welcome email, and notifies a manager. |
| [get\_onboarding\_status](#get-onboarding-status-tool) | Returns the current status of one new hire's onboarding. |
| [get\_onboarding\_checklist](#get-onboarding-checklist-tool) | Returns checklist items due, for either the new hire's onboarding checklist or the manager's own pre-boarding checklist. |
| [update\_checklist\_item\_status](#update-checklist-item-status-tool) | Marks a checklist item complete or reopens it. |
| [schedule\_onboarding\_meeting](#schedule-onboarding-meeting-tool) | Schedules an additional onboarding meeting. |
| [escalate\_or\_create\_ticket](#escalate-or-create-ticket-tool) | Notifies HR about a new hire's issue or question over Slack. |
| [list\_onboardings](#list-onboardings-tool) | Lists onboardings by status, hire, manager, or date range. |
| [cancel\_onboarding](#cancel-onboarding-tool) | Cancels a scheduled or in-progress onboarding. |

## Install the Employee Onboarding MCP server

Complete the following steps to install a prebuilt MCP server to your project:

1. Sign in to your Workato account.
   
2. Go to **AI Hub > Enterprise MCP > Custom servers**.
   
3. Click **\+ Create MCP server**.
   
4. Go to the **Start with pre-built MCP Servers using your connected apps** section and select the prebuilt MCP server you plan to use.
   
5. Click **Use this server**.
   
6. Provide a name for your MCP server in the **Server name** field.
   
7. Use the **Location** drop-down menu to select the project for the MCP server.
   
8. Go to the **Connections** section and connect to your app account.
   
9. Select the connection type you plan to use for the MCP server template.
   
   - **User's connection**: MCP server tools perform actions based on the identity and permissions of the user who connects to the application. Users authenticate with their own credentials to execute the skill.
   - **Your connection**: This option uses the connection established by the recipe builder and follows the same principles as normal app connections.
   
   ![Select your connection type](/assets/connection-type.Cor-6PJN.png)_Select your connection type_
   
   > **VERIFIED USER ACCESS AUTHENTICATION REQUIREMENTS**
   > 
   > Only app connections that use OAuth 2.0 authorization code grant are available for user's connection. Refer to [Verified user access](/en/mcp/verified-user-access) for more information.
   
10. Complete the app-specific connection setup steps in the following section.
    

## Employee Onboarding connection setup

View Employee Onboarding connection setup steps

Configure the following connections to set up the Employee Onboarding MCP server:

- [Workday](#workday-connection): Required. Provides information about approved hires.
- [Slack](#slack-connection): Required. Sends the manager pre-arrival notification as a direct message, posts escalations to the Slack user or channel configured in `escalation.hrbp_notification_target`, and serves as the Q&A fallback when [Confluence](/en/mcp/prebuilt-mcps/confluence-mcp-server) isn't available.
- [Google Calendar](#google-calendar-connection): Required. Schedules meetings.

### Employee Onboarding role requirements

Each tool's availability depends on the permissions of the connected account. Calling a tool without the required permission returns a `permission_denied` outcome rather than a partial result.

- **Workday**: The connected API client must be able to read hire events.
- **Slack**: The connected account's OAuth scopes must include `chat:write` to post the manager pre-arrival notification, Q&A fallback answers, and escalations.
- **Google Calendar**: The connected account must have permission to create events and invite attendees.

Additionally, **initiate\_onboarding** and **cancel\_onboarding** are only available to users in the server's `hr_persons` allowlist. **list\_onboardings** gives `hr_persons` members a complete view of every onboarding, scopes any other caller to onboardings where they're recorded as the hire's manager, and denies a hire's own request outright.

#### Workday connection setup steps

View Workday REST connection setup steps

The Workato Workday connector is categorized into three distinct types: the main Workday connector, the Workday Web Services connector, and the Workday REST connector. Each type follows a similar authentication pattern but differs slightly in support capabilities and functionalities.

The Workday REST API requires authentication through an OAuth client setup.

> **API CLIENTS FOR INTEGRATION NOT SUPPORTED**
> 
> Register a standard Workday API client to complete this connection. Workday API clients for Integration aren't supported in the Employee Onboarding MCP server.

##### Register a new API client in Workday

View API client setup steps

The Employee Onboarding MCP server authenticates each user individually through their own Workday login. The server doesn't use an Integration System User (ISU) like the Workday connector.

##### Register a new API client

Complete the following steps to register an API client in Workday REST:

1. Sign in to your Workday REST account.
   
2. Enter `Register API Client` to locate the **Register API Client** task.
   
3. Enter a name for your API client in the **Client Name** field.
   
4. Go to the **Client Grant Type** section and select **Authorization Code Grant**.
   
5. Go to the **Access Token Type** section and select **Bearer**.
   
6. Enter `https:www.workato.com/oauth/callback` in the **Redirection URI** field.
   
7. Enter `30` in the **Refresh Token Timeout (in days)** field.
   
8. Enter the scopes for the connection in the **Scope (Functional Areas)** field. Refer to [Workday End User MCP server Minimum permissions](/en/mcp/prebuilt-mcps/workday-end-user-mcp-server#minimum-permissions) if you're connecting to the Workday End User MCP server.
   
   ![Enter the scopes for the connection in the Scope (Functional Areas) field](/assets/api-client-rest.CIUw1iB9.png)_Enter the scopes for the connection in the **Scope (Functional Areas)** field_
   
9. Enter your client ID in the **Client ID** field.
   
10. Enter your REST API endpoint in the **Workday REST API Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
    
11. Enter your token endpoint in the **Token Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
    
12. Enter your authorization endpoint in the **Authorization Endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://impl.workday.com/example/authorize`
    
13. Click **Done**.
    

##### Find your token endpoint URL

Complete the following steps to find your token endpoint URL in Workday:

1. Enter **View API Clients** into the search field in Workday.
   
2. Access the **View API Clients** report from the search results.
   
3. Save the URLs listed in the **Token Endpoint** and **Authorization Endpoint** fields. These URLs are required for the OAuth 2.0 connection.
   
   ![Save the token endpoint and authorization endpoint URLs](/assets/save-url.BkmumQyc.png)_Save the token endpoint and authorization endpoint URLs_
   

##### Complete setup in Workato

Complete the following steps to configure your Workday connection in Workato using OAuth 2.0 authentication:

View OAuth 2.0 authentication steps

1. Enter a unique **Connection name** to identify your Workday account in Workato.
   
   ![Set up your connection](/assets/workday-rest-connection.IzDCKMEG.png)_Set up your connection_
   
2. Use the **Location** drop-down to select the project or folder to store this connection.
   
3. Use the **Connection type** drop-down menu to select **Cloud**.
   
4. Enter your REST API endpoint in the **REST API endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/api/v1/example`
   
5. Enter your authorization endpoint in the **Authorization endpoint** field. You can find this value in your Workday API client details. For example: `https://impl.workday.com/example/authorize`
   
6. Enter your token endpoint in the **Token endpoint** field. You can find this endpoint in your API client details page in Workday. For example: `https://wd2-impl-services1.workday.com/xxx/oauth2/example/token`
   
7. Enter your client ID in the **Client ID** field.
   
8. Enter your client secret in the **Client Secret** field.
   
9. Enter your refresh token in the **Refresh token** field.
   
   > **DON'T PROVIDE A REFRESH TOKEN FOR MCP SERVERS**
   > 
   > Don't provide a refresh token if you're connecting Workday to an MCP server.
   
10. Click **Connect**.
    

#### Slack connection setup steps

View Slack connection setup steps

##### API version

The Slack connector uses the [Slack Web API v1](https://api.slack.com/web) with the endpoint URL `https://slack.com/api/METHOD`.

##### Supported editions and versions

Workato connects to both Slack for teams (for single workspaces) and Slack Enterprise Grid (for multiple workspaces).

The Slack connector supports OAuth 2.0 authentication. You must log in to Slack and authorize the permissions that Workato requests.

##### Default scopes

You can customize the OAuth user scopes that Workato requests during connection setup. Workato requests the following default scopes unless you select your own in the **OAuth user scopes** field:

- `channels:read`
- `channels:write`
- `chat:write`
- `groups:read`
- `groups:write`
- `im:read`
- `im:write`
- `mpim:read`
- `mpim:write`
- `users:read`
- `users:read.email`

##### Connect to Slack using OAuth 2.0 authentication

Complete the following steps to connect to Slack in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Slack` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Slack connection](/assets/slack-connection.BT6h8ZMj.png)_Slack connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand **Advanced** and use the **Is this a Classic Slack app?** drop-down menu to select `Yes` or `No`. Select `Yes` only if you haven't migrated your Slack app to granular permission scopes. Refer to [Moving to granular permission scopes](/en/connectors/slack#moving-to-granular-permission-scopes) for more information.
   
6. Optional. Use the **OAuth user scopes** drop-down menu to select the OAuth user scopes to request for your connection. Leave this field empty to request the [default scopes](/en/connectors/slack#scopes).
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Custom OAuth profiles for Slack](/en/connectors/slack/custom-oauth) for more information.
   
8. Click **Connect**.
   
9. Click **Allow** to grant Workato permission to access your account.
   

#### Google Calendar connection setup steps

View Google Calendar connection setup steps

##### API version

The Google Calendar connector uses the [Google Calendar API v3](https://developers.google.com/calendar/api/v3/reference).

Workato supports the following types of connections to Google Calendar:

- [OAuth 2.0 authentication](#oauth)
- [Service account authentication](#service-account-authentication)
  - [Minimum scopes for service account connections](#minimum-scopes-for-service-account-connections)
  - [Set up a Google service account](#set-up-a-google-service-account)
  - [Enable the Google Calendar API](#api-setup)
  - [Complete setup in Workato](#setup)

You can use a service account to authenticate without a personal user account. Workato recommends service account authentication for consistent use.

##### OAuth 2.0 authentication

Complete the following steps to set up your Google Calendar connection using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
5. Select **OAuth 2.0** as the **Authentication type**.
   
6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
   

##### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

Service account authentication consists of the following actions:

- [Set up a Google service account](#set-up-a-google-service-account)
- [Enable the Google Calendar API](#api-setup)
- [Complete setup in Workato](#setup)

###### Minimum scopes for service account connections

The following scopes are required to connect to Google Calendar using a service account:

- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/calendar.events`
- `https://www.googleapis.com/auth/admin.directory.resource.calendar`
- `https://www.googleapis.com/auth/tasks`
- `https://www.googleapis.com/auth/userinfo.email`

A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.

Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.

###### Set up a Google service account

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

###### Enable the Google Calendar API

You must enable the Google Calendar API before you return to Workato to finish setting up your connection.

1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
   
2. Search for and select the `Google Calendar API`.
   
3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
   

###### Complete setup in Workato

Complete the following steps in Workato to set up your Google Calendar connection using a service account:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Service account** as the **Authentication type**.
   
6. Enter your service account's **Private key**.
   
7. Provide the **User email** of the account you plan to impersonate.
   
   User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Calendar. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Calendar. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
   
8. Click **Sign in with Google** to complete the setup. ![Configure Google Calendar service account connection](/assets/service-account-connection.CG2N5lxI.png)_Configure Google Calendar service account connection_
   

#### Data table configuration

Edit the following data tables to control who can use this server, checklist content, calendar and escalation defaults, and operational limits:

- `hr_persons`: Enter the names and email addresses of users to grant access to **initiate\_onboarding** and **cancel\_onboarding**, and a complete view of **list\_onboardings**.
  
- `checklist_template`: Define the checklist items for **get\_onboarding\_checklist** to return. Create a new row for each item and include whether the item belongs to the new hire or manager.
  
- `onboarding_config` contains the following keys:
  

| Key | Description |
| --- | --- |
| `calendar_id` | Required. Enter the ID of the Google Calendar for **initiate\_onboarding** and **schedule\_onboarding\_meeting** to create events on. |
| `welcome_email.template` | Enter the body text of the hire's initial welcome email. Tell the hire how to reach this server, for example by naming the Claude app or Claude Tag in Slack. |
| `onboarding_meeting.default_time_of_day` | Specify the default local time to use for the initial meeting. Defaults to `09:00`. |
| `hire_event_descriptor_prefix` | Specify the Workday business-process-event descriptor prefix for **find\_new\_hire** to match when identifying a hire event. `Rehire:` matches, regardless of this value. Defaults to `Hire:`. |
| `escalation.hrbp_notification_target` | Required for **escalate\_or\_create\_ticket**. Enter the Slack user or channel ID for **escalate\_or\_create\_ticket** to notify. |
| `server_limits.max_schedule_days_out` | Specify how far out **schedule\_onboarding\_meeting** can book a meeting. Defaults to `60` days. |
| `server_limits.max_checklist_items_per_response` | Specify how many items **get\_onboarding\_checklist** returns for `scope=all_due` in one response. Defaults to `10`. |
| `server_limits.rate_limit_calls_per_minute` | Record the intended rate limit for downstream apps. Workato doesn't enforce this limit. This field is for documentation purposes. Enforce limits directly in downstream connections. Defaults to `20`. |
| `audit.log_retention_days` | Specify how long to keep audit records before deleting them. Set this value to `0` to ensure records aren't deleted. Defaults to `365` days. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data tables:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Employee Onboarding** folder.
   
4. Open the **Data tables** folder.
   
5. Select the `hr_persons`, `checklist_template`, or `onboarding_config` data table.
   
6. Edit the table's rows to make your changes. For example, add a row to `hr_persons` with a user's name and email address, or add a row to `onboarding_config` with key `calendar_id` and your Google Calendar's ID as the value.
   

## How to use Employee Onboarding MCP server tools

Refer to the following sections for detailed information on available tools.

### find\_new\_hire tool

The **find\_new\_hire** tool finds a new hire in Workday and returns their identity, hiring manager, region and employment context, and the approved Workday hire event. This tool doesn't perform directory searches for other purposes. Your LLM uses this tool to resolve a hire you name, or to identify a new hire who gives their own name or email at the start of a self-service session.

**Try asking**:

- `Look up Jordan Lee.`
- `Find the new hire with Worker ID 100483.`
- `Does Jordan Lee have an approved hire event?`
- `Show me jordan.lee@example.com, including completed onboardings.`

### initiate\_onboarding tool

The **initiate\_onboarding** tool returns a kickoff plan for your approval, then schedules an initial meeting, sends the hire's welcome email, and notifies the manager. Your LLM uses this tool to kick off, start, or set up onboarding for a hire with an approved Workday hire event.

**Try asking**:

- `Kick off onboarding for Jordan Lee, starting the 22nd.`
- `Show me the kickoff plan before anything gets scheduled.`
- `Set up Jordan Lee's initial meeting for 9am.`

### get\_onboarding\_status tool

The **get\_onboarding\_status** tool returns the status of a hire's onboarding. It has no visibility into other MCP servers such as [Access Provisioning](/en/mcp/prebuilt-mcps/access-provisioning-mcp-server) or [ServiceNow ITSM](/en/mcp/prebuilt-mcps/servicenow-itsm-mcp-server). A new hire can only check their own status, and a manager can only check the status of their own hires. Users in `hr_persons` can query any hire's record. Your LLM uses this tool to check how onboarding is progressing, or to report initial progress right after you confirm a kickoff plan.

**Try asking**:

- `What's my onboarding status?`
- `How is Jordan Lee's onboarding going?`
- `Which step failed on this onboarding?`
- `What's the next item on my checklist?`

### get\_onboarding\_checklist tool

The **get\_onboarding\_checklist** tool returns checklist items due in either the new hire's onboarding checklist or the manager's own pre-boarding checklist. Your LLM uses this tool to show what's on a hire's or manager's checklist, what's due this week, or what to do next.

**Try asking**:

- `What do I need to do this week?`
- `What's on my pre-boarding checklist for Jordan Lee?`
- `Show me everything that's due so far.`
- `Has the benefits enrollment item come up yet?`

### update\_checklist\_item\_status tool

The **update\_checklist\_item\_status** tool marks a checklist item complete or reopens it. Your LLM uses this tool to mark a checklist item you've finished, or to reopen one you marked done by mistake.

**Try asking**:

- `Mark the benefits enrollment item as done.`
- `I finished setting up my workstation. Check that off.`
- `Reopen the IT equipment item, it's not actually done.`
- `Mark the pre-boarding desk setup item complete for Jordan Lee.`

### schedule\_onboarding\_meeting tool

The **schedule\_onboarding\_meeting** tool schedules an onboarding meeting. Your LLM uses this tool to set up time with someone during onboarding.

**Try asking**:

- `Schedule 30 minutes with IT to go over my laptop setup.`
- `Book a benefits walkthrough for next Tuesday afternoon.`
- `Show me the proposed time before you send the invite.`

### escalate\_or\_create\_ticket tool

The **escalate\_or\_create\_ticket** tool notifies HR about a new hire's issue or question over Slack. Your LLM uses this tool to escalate a problem you report or explicitly ask to escalate, and falls back on it for general onboarding or policy questions when a [Confluence MCP](/en/mcp/prebuilt-mcps/confluence-mcp-server) isn't available.

**Try asking**:

- `My laptop hasn't shown up yet.`
- `I can't log into my new account.`
- `Can you escalate this to HR?`
- `What's our policy on remote work during onboarding?`

### list\_onboardings tool

The **list\_onboardings** tool lists onboardings by status, hire, manager, or date range. Users in `hr_persons` see every onboarding matching the filters. Other callers only see onboardings where they're recorded as the hire's manager. The server directs new hires asking about onboardings to **get\_onboarding\_status** instead. Your LLM uses this tool to list onboardings in progress or coming up, or to find a specific onboarding.

**Try asking**:

- `Show me everyone starting this month.`
- `List onboardings in progress.`
- `Which onboardings are flagged for attention?`
- `Find the onboarding for Jordan Lee.`

### cancel\_onboarding tool

The **cancel\_onboarding** tool cancels a scheduled or in-progress onboarding. This performs an operational undo rather than a rehire or rescission action. It doesn't reverse anything done through the [Access Provisioning](/en/mcp/prebuilt-mcps/access-provisioning-mcp-server) or [ServiceNow ITSM](/en/mcp/prebuilt-mcps/servicenow-itsm-mcp-server) servers. Your LLM uses this tool to cancel an onboarding when an offer is rescinded, a start date changes materially, or you ask to cancel one already in flight.

**Try asking**:

- `Cancel Jordan Lee's onboarding. The offer was rescinded.`
- `Stop the onboarding for Worker 100483.`
- `What would canceling this onboarding actually undo?`
- `Cancel the remaining steps. The start date moved.`

## Getting started

View and manage your MCP server tools in the **Details** tab **Tools** section. Tool management provides the following capabilities:

- [Start tools](/en/mcp/manage-tools#start-tools)
- [Remove tools](/en/mcp/manage-tools#remove-tools)
- [Edit tools](/en/mcp/manage-tools#edit-tools)
- [Add tools](/en/mcp/manage-tools#add-tools)
- [Edit your LLM-facing MCP server description](/en/mcp/prebuilt-mcps#edit-llm-facing-mcp-server-description)

> **TOOLS MUST BE STARTED**
> 
> Your LLM can only access active tools in your MCP server connector.

---
