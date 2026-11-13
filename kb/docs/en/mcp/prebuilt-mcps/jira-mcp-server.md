---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/jira-mcp-server.md'
description: >-
  Use the Jira MCP server to connect your LLM to Jira with a curated set of
  tools to search for issues, retrieve details, review comments and activity
  history, create new issues, update status, and modify issue fields.
---

# Jira MCP server

The Jira MCP server enables LLMs to explore and manage Jira issues through natural conversation. It provides tools to search for issues, retrieve details, review comments and activity history, create new issues, update status, and modify issue fields without requiring direct interaction with the Jira interface.

The Jira MCP server lets your LLM synthesize information across multiple tickets to identify patterns, summarize comment threads, and highlight dependencies. Your LLM can aggregate customer tickets and surface critical issues for meeting preparation and compile your assignments and recent activity into coherent summaries for standup briefings.

## Uses

Use the Jira MCP server when you plan to perform the following actions:

- Check the status of a specific issue
- Create or update an issue
- Transition an issue to a new status
- Add a comment to an issue
- Get full context on an issue including comments and history
- Find issues by topic, assignee, status, or customer
- View issues assigned to you or a teammate
- Prepare for a customer call by reviewing their open issues
- Update priority status, reassign, or add labels to an issue

### Example prompts

Use the following example prompts to invoke Jira MCP server tools:

- `What's the status of API-1234?`
- `Summarize the payment timeout bug`
- `What do I need to know about API-1234 before my meeting?`
- `Who's working on the login issue?`
- `Summarize API-456`
- `What's the history on API-789?`
- `What decisions were made on API-2323`
- `What issues does Acme Corp have?`
- `Summarize Acme's recent tickets`
- `What's been escalated by Acme?`
- `Give me context before my call with Acme`

## Jira MCP server tools

The Jira MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_issue](#get-issue-tool) | Retrieves detailed information about a single Jira issue by its key or ID. |
| [get\_issue\_changelog](#get-issue-changelog-tool) | Retrieves the change history for a specified issue, showing what fields changed, change date, who made the changes, and the old and new values. |
| [get\_issue\_comments](#get-issue-comments-tool) | Retrieves all comments for Jira issue by ID. |
| [search\_issues](#search-issues-tool) | Searches for Jira issues matching the criteria you specify. |
| [create\_issue](#create-issue-tool) | Creates a new Jira issue with the fields you specify. |
| [get\_account\_id](#get-account-id-tool) | Retrieves the account ID for the user you specify. |
| [transition\_issue](#transition-issue-tool) | Transitions an issue to a new workflow status. |
| [get\_transition\_id](#get-transition-id-tool) | Retrieves the transition ID for the issue you specify. |
| [add\_comment](#add-comment-tool) | Adds a comment to an existing Jira issue. |
| [update\_issue](#update-issue-tool) | Updates an existing Jira issue with the fields you specify. |

## Install the Jira MCP server

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
    

## Jira connection setup

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

### API token

View API token steps

API tokens authenticate your Atlassian account without using a username and password. API token authentication doesn't support connections to on-premise Jira.

#### Prerequisites

You must generate an Atlassian API token for this authentication method. Refer to the Atlassian [Manage API tokens](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/) guide for more information.

#### Connect to Jira using an API token

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
    

### Service account (API token)

View Service account (API token) steps

Use this authentication method to connect Workato to Jira using an Atlassian Cloud service account. A service account is a dedicated, non-personal Atlassian account used for integrations. Service accounts aren't tied to individual users, so connections remain stable when team members leave or change roles.

Service account (API token) authentication supports Jira Cloud connections only.

#### Prerequisites

Complete the following tasks before you connect:

##### Set up the service account

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
    

#### Connect to Jira using a service account API token

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
    

### OAuth 2.0 (Cloud - Atlassian-hosted Jira)

View OAuth 2.0 (Cloud - Atlassian-hosted Jira) steps

OAuth 2.0 enables you to share specific data with an application while keeping your username, password, and other information private. OAuth 2.0 (Cloud - Atlassian-hosted Jira) supports Jira Cloud connections.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Cloud Jira](https://support.atlassian.com/jira-cloud-administration/docs/manage-webhooks/) webhook documentation for registration steps.

#### Connect to Jira using OAuth 2.0 (Cloud - Atlassian-hosted Jira)

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
    

### OAuth 2.0 (Data Center)

View OAuth 2.0 (Data Center) steps

OAuth 2.0 (Data Center) enables you to connect to an on-premise Jira Data Center instance using OAuth 2.0.

> **REAL-TIME TRIGGERS NOT SUPPORTED**
> 
> OAuth 2.0 doesn't support real-time triggers because it's incompatible with webhooks. As an alternative, you can register the [Webhooks connector](/en/connectors/workato-webhooks) in Jira to use Jira's static webhook functionality. Refer to the [Jira Data Center](https://confluence.atlassian.com/adminjiraserver/managing-webhooks-938846912.html) webhook documentation for registration steps.

#### Prerequisites

You must generate an Atlassian client ID and client secret if you plan to connect to Jira Data Center using OAuth 2.0. Refer to the Atlassian [Configure an incoming link](https://confluence.atlassian.com/adminjiraserver/configure-an-incoming-link-1115659067.html) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.

#### Connect to Jira using OAuth 2.0 (Data Center)

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
    

### Personal access tokens

View Personal access tokens steps

Personal access tokens (PATs) authenticate your Atlassian account without using a username and password. PAT authentication supports on-premise Jira connections.

#### Prerequisites

You must generate an Atlassian personal access token for this authentication method. Refer to the Atlassian [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html) guide for more information.

#### Connect to Jira using a personal access token

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
    

### Basic authentication with password

View Basic authentication with password steps

Basic authentication connects to your Atlassian account using a username and password. Basic authentication supports on-premise Jira connections.

> **DEPRECATED PASSWORD AUTHENTICATION**
> 
> Atlassian deprecated basic authentication for cloud connections in December 2018. On-premise Jira is not affected.

#### Connect to Jira using basic authentication

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
    

## How to use Jira MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_issue tool

The **get\_issue** tool retrieves the full details of a specific Jira ticket using its issue key, such as `PROJ-123`. Your LLM uses this tool to check the progress of a task, read the full requirements of a story, or see who is currently responsible for resolving a bug.

**Try asking**:

- `What is the current status of JIRA-101 and who is it assigned to?`
- `Show me the full description and priority for the 'login page' bug.`
- `Get the details for the task 'Update API documentation' and check for any linked issues.`
- `When was the ticket PROJ-45 created and are there any labels on it?`

### get\_issue\_changelog tool

The **get\_issue\_changelog** tool retrieves the history of all changes made to a specific Jira ticket. Your LLM uses this tool to track how an issue has evolved, see when its status changed, or identify who modified specific fields like priority or assignee.

**Try asking**:

- `Show me the recent history of changes for PROJ-123.`
- `When was the status of JIRA-45 changed from 'In Progress' to 'Done'?`
- `Who changed the priority on the 'API integration' task?`
- `Get the changelog for the 'mobile-app' bug to see how many times it has been reassigned.`

### get\_issue\_comments tool

The **get\_issue\_comments** tool retrieves the entire discussion history for a Jira ticket you specify. Your LLM uses this tool to catch up on team conversations, find specific decisions made regarding a task, or gather additional context that isn't in the main description.

**Try asking**:

- `Show me all the comments on JIRA-101.`
- `What have people been saying about the 'payment gateway' bug?`
- `Get the discussion history for PROJ-45 to see if there are any updates from the client.`

### search\_issues tool

The **search\_issues** tool searches for Jira issues based on keywords, filters, or criteria you specify. Your LLM uses this tool to locate tickets within a project, find all tasks assigned to a specific person, or filter for bugs with a certain priority level.

**Try asking**:

- `Find all open bugs in the 'Mobile App' project.`
- `Search for issues containing the keyword 'authentication'.`
- `What tasks are currently assigned to @Sarah in the 'Marketing' project?`
- `Search for all high-priority tickets that haven't been updated in the last week.`

### create\_issue tool

The **create\_issue** tool creates a new Jira issue with the fields you specify, including summary, description, issue type, priority, assignee, and labels. Your LLM uses this tool to capture bugs, feature requests, or tasks from your conversation and immediately create properly formatted, actionable issues without switching to the Jira interface.

**Try asking**:

- `Create a bug in PROJ for the timeout issue on the checkout page and assign it to Sarah.`
- `File a high-priority task about updating our SSL certificates.`
- `Create a story for the dark mode feature in the mobile app project.`
- `Open a new ticket for the API documentation update and label it 'documentation'.`

### get\_account\_id tool

The **get\_account\_id** tool retrieves the Jira account ID for a user you specify. Your LLM uses this tool to find the correct account identifier before assigning issues, filtering by user, or performing other operations that require a specific account ID.

**Try asking**:

- `What's Josh's account ID in Jira?`
- `Get the account ID for jade.anderson@acme.com.`
- `Find the Jira account ID for the user 'Maria Rodriguez'.`
- `Look up the account identifier for our team lead before I assign them this bug.`

### transition\_issue tool

The **transition\_issue** tool moves an issue to a new workflow status, such as from `To Do` to `In Progress` or from `In Review` to `Done`. Your LLM uses this tool to update issue status as work progresses, mark tasks complete, or move tickets through your team's workflow without manual clicks.

**Try asking**:

- `Move PROJ-123 to 'In Progress' status.`
- `Mark the authentication bug as 'Done'.`
- `Transition JIRA-456 to 'In Review' now that the code is ready.`
- `Change the status of the API task to 'Blocked'.`

### get\_transition\_id tool

The **get\_transition\_id** tool retrieves the available workflow transition IDs for a specific issue. Your LLM uses this tool to identify which status changes are possible for a ticket based on your Jira workflow configuration before attempting to transition the issue.

**Try asking**:

- `What status transitions are available for PROJ-123?`
- `Show me the valid next steps for this ticket in the workflow.`
- `What are the transition options for the 'payment bug' issue?`
- `Check what statuses I can move JIRA-789 to from its current state.`

### add\_comment tool

The **add\_comment** tool adds a comment to an existing Jira issue. Your LLM uses this tool to provide status updates, answer questions, share additional context, or document decisions directly in the ticket without leaving your conversation.

**Try asking**:

- `Add a comment to PROJ-123 saying we've completed the database migration.`
- `Comment on the login bug that we're investigating the root cause.`
- `Post an update to JIRA-456 with the latest test results.`
- `Add a note to the API task explaining the workaround we found.`

### update\_issue tool

The **update\_issue** tool updates an existing Jira issue with the fields you specify, including summary, description, priority, assignee, labels, or any custom fields. Your LLM uses this tool to modify ticket details as requirements change, update priority levels, reassign work, or adjust issue fields based on your conversation.

**Try asking**:

- `Update PROJ-123 to high priority and assign it to Josh.`
- `Change the description of the checkout bug to include the new error details.`
- `Update JIRA-456 with the label 'needs-review' and increase its priority.`
- `Modify the API task summary to reflect that it now includes authentication updates.`

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
