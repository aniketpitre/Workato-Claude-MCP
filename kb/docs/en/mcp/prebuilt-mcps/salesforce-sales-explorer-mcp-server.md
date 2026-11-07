---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/salesforce-sales-explorer-mcp-server.md
description: >-
  Use the Salesforce Sales Explorer MCP server to connect your LLM to Salesforce
  with a curated set of tools to search for records, retrieve details, create
  new entries, and update existing information.
---

# Salesforce Sales Explorer MCP server

The Salesforce Sales Explorer MCP server enables LLMs to work with leads, accounts, contacts, opportunities, tasks, events, and products in Salesforce. It provides tools to search for records, retrieve details, create new entries, and update existing information through natural conversation.

## Uses

Use the Salesforce Sales Explorer MCP server when you plan to perform the following actions:

- Search for leads, accounts, contacts, opportunities, tasks, and products
- Retrieve detailed information about specific sales records
- Create new leads, accounts, contacts, opportunities, tasks, and events
- Update existing sales records with new information or status changes
- Add product line items to opportunities
- Execute SOQL queries for custom data retrieval
- Retrieve schema information for Salesforce objects

### Example prompts

Use the following example prompts to invoke Salesforce Sales Explorer MCP server tools:

- `Find all qualified leads from last month.`
- `Show me opportunities closing this quarter over $100k.`
- `Get details on the Acme Corp account.`
- `Create a lead for Jane Smith at TechCo.`
- `Update the Acme renewal opportunity to Negotiation stage.`
- `Schedule a call with the customer for tomorrow at 2pm.`
- `Add the Enterprise subscription product to this opportunity.`
- `What are my high-priority tasks due this week?`

## Salesforce Sales Explorer MCP server tools

The Salesforce Sales Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_leads](#search-leads-tool) | Searches for leads matching specified criteria. |
| [search\_accounts](#search-accounts-tool) | Searches for accounts matching specified criteria. |
| [search\_contacts](#search-contacts-tool) | Searches for contacts matching specified criteria. |
| [search\_opportunities](#search-opportunities-tool) | Searches for opportunities matching specified criteria. |
| [search\_tasks](#search-tasks-tool) | Searches for tasks matching specified criteria. |
| [search\_products](#search-products-tool) | Searches for products in the Salesforce product catalog. |
| [upsert\_lead](#upsert-lead-tool) | Creates a new lead or updates an existing lead. |
| [upsert\_account](#upsert-account-tool) | Creates a new account or updates an existing account. |
| [upsert\_contact](#upsert-contact-tool) | Creates a new contact or updates an existing contact. |
| [upsert\_opportunity](#upsert-opportunity-tool) | Creates a new opportunity or updates an existing opportunity. |
| [upsert\_task](#upsert-task-tool) | Creates a new task or updates an existing task. |
| [upsert\_event](#upsert-event-tool) | Creates a new calendar event or updates an existing event. |
| [add\_opportunity\_line\_item](#add-opportunity-line-item-tool) | Adds a product line item to an existing opportunity. |
| [retrieve\_semantic\_model](#retrieve-semantic-model-tool) | Retrieves schema information for a specified Salesforce object. |
| [execute\_soql\_query](#execute-soql-query-tool) | Executes SOQL queries in Salesforce. |

## Install the Salesforce Sales Explorer MCP server

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
    

## Salesforce connection setup

View Salesforce connection setup steps

Workato supports OAuth 2.0 authentication and JWT bearer authentication connections for Salesforce Sales Explorer.

### OAuth 2.0 authentication

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
    

### JWT bearer authentication

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
    

## How to use Salesforce Sales Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_leads tool

The **search\_leads** tool searches for leads matching the criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve leads by ID, status, source, owner, company, or date ranges.

**Try asking**:

- `Find leads from last week.`
- `Show me all open leads.`
- `Find leads from Acme Corp.`
- `Show me qualified leads assigned to me.`
- `Find leads from the trade show.`
- `Show me leads created this month.`

### search\_accounts tool

The **search\_accounts** tool searches for accounts matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve accounts by ID, name, type, industry, owner, or parent account.

**Try asking**:

- `Find accounts in the technology industry.`
- `Show me all customer accounts.`
- `Find Acme Corp account.`
- `Show me prospect accounts owned by Sarah.`
- `Find child accounts of Acme Corp.`
- `Show me accounts created this quarter.`

### search\_contacts tool

The **search\_contacts** tool searches for contacts matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve contacts by ID, name, account, title, email, or owner.

**Try asking**:

- `Find contacts at Acme Corp.`
- `Find Jane Smith in Salesforce.`
- `Show me all VP-level contacts.`
- `Find contact with email jane@acme.com.`
- `Show me contacts owned by John.`
- `Get Jane Smith's contact information.`

### search\_opportunities tool

The **search\_opportunities** tool searches for opportunities matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve opportunities by ID, name, account, stage, close date, amount, or owner.

**Try asking**:

- `Find deals closing this quarter.`
- `Find the Acme Corp renewal opportunity.`
- `Show me all opportunities in negotiation stage.`
- `Find deals over $100k.`
- `Show me opportunities I'm working on.`
- `Show me deals closing next month.`

### search\_tasks tool

The **search\_tasks** tool searches for tasks matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve tasks by ID, subject, status, priority, due date, owner, or related records.

**Try asking**:

- `Find my tasks for this week.`
- `Find tasks about contract review.`
- `Show me open tasks.`
- `Show me high-priority tasks.`
- `What tasks are due today?`
- `Show me tasks for the Acme Corp account.`

### search\_products tool

The **search\_products** tool searches for products in the Salesforce product catalog. Your LLM uses this tool when you need to find, list, or retrieve products by ID, name, product code, or active status.

**Try asking**:

- `Find products in our catalog.`
- `Find the Enterprise subscription product.`
- `Find product SKU-12345.`
- `Show me software products.`
- `Show me discontinued products.`
- `What products can I add to this opportunity?`

### upsert\_lead tool

The **upsert\_lead** tool creates a new lead if it doesn't exist, or updates an existing lead if you provide the lead ID. Your LLM uses this tool when you need to create a new prospect or update lead information.

**Try asking**:

- `Create a lead for Josh Hernandez at Acme Corp.`
- `Log this person as a lead.`
- `Update the lead status to Qualified.`
- `I met Jade Anderson from TechCo at the conference - create a lead.`
- `Assign this lead to Sarah.`
- `Update the lead - they're interested in the enterprise plan.`

### upsert\_account tool

The **upsert\_account** tool creates a new account if it doesn't exist, or updates an existing account if provided with account ID. Your LLM uses this tool when you need to create a new company record or update account information.

**Try asking**:

- `Create an account for Acme Corp.`
- `Update Acme Corp's industry to Technology.`
- `Add this company to Salesforce.`
- `Update the account - their revenue is $50M.`
- `Reassign this account to John.`

### upsert\_contact tool

The **upsert\_contact** tool creates a new contact if it doesn't exist, or updates an existing contact if you provide the contact ID. Your LLM uses this tool when you need to create a new person record or update contact information.

**Try asking**:

- `Create a contact for Jane Smith.`
- `Update Jane's email address.`
- `Add John Doe as a contact at Acme Corp.`
- `Save this person's information as a contact.`

### upsert\_opportunity tool

The **upsert\_opportunity** tool creates a new opportunity if it doesn't exist, or updates an existing opportunity if you provide the opportunity ID. Your LLM uses this tool when you need to create a new sales deal or update opportunity information.

**Try asking**:

- `Create an opportunity for Acme Corp renewal.`
- `Update the Acme deal amount to $100k.`
- `Move this opportunity to Negotiation stage.`
- `Push the close date to end of quarter.`
- `Create an opportunity for what we just discussed.`

### upsert\_task tool

The **upsert\_task** tool creates a new task if it doesn't exist, or updates an existing task if you provide the task ID. Your LLM uses this tool when you need to create a to-do item or update task information, and can link tasks to leads, accounts, contacts, or opportunities.

**Try asking**:

- `Create a task to follow up with Acme Corp.`
- `Remind me to call them next week.`
- `Make a task for what we discussed.`
- `Create a task for this opportunity to send the proposal.`
- `Mark that task as completed.`
- `Push the task due date to Friday.`

### upsert\_event tool

The **upsert\_event** tool creates a new calendar event if it doesn't exist, or updates an existing event if you provide the event ID. Your LLM uses this tool when you need to schedule a meeting, call, or calendar activity with specific date and time.

**Try asking**:

- `Schedule a call with Acme Corp for tomorrow at 2pm.`
- `Put a meeting on my calendar for Friday at 10am.`
- `Move that meeting to next Tuesday.`
- `Schedule a demo for this opportunity on Wednesday.`

### add\_opportunity\_line\_item tool

The **add\_opportunity\_line\_item** tool adds a product line item to an existing opportunity. Your LLM uses this tool when you need to add products or services to a sales deal.

**Try asking**:

- `Add the Enterprise subscription to this opportunity.`
- `Add 5 licenses to the Acme deal.`
- `Add the product at $1000 per unit to this opportunity.`
- `Add the Professional Services package to the renewal deal.`

### retrieve\_semantic\_model tool

The **retrieve\_semantic\_model** tool retrieves schema information for a Salesforce object you specify, including field names, field types, field labels, relationships to other objects, and field-level permissions. Your LLM uses this tool when you need to understand object structure before building queries or creating records.

**Try asking**:

- `What fields are available on the Lead object?`
- `Show me the schema for Opportunity.`
- `What are the field types for Account?`
- `Get the object structure for Contact.`

### execute\_soql\_query tool

The **execute\_soql\_query** tool executes SOQL queries in Salesforce. Your LLM uses this tool after reviewing semantic models to build custom queries that answer specific questions about your Salesforce data.

**Try asking**:

- `Query all opportunities with amount greater than $50k closing this quarter.`
- `Find accounts in the technology industry with annual revenue over $10M.`
- `Get all contacts associated with closed-won opportunities.`
- `Query tasks due this week for my team members.`

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
