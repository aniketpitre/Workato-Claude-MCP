---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/it-support-ticket-lifecycle-mcp-server.md
description: >-
  Use the IT Support Ticket Lifecycle MCP server to connect your LLM to Jira
  Service Desk to search a linked Confluence knowledge base and create, track,
  comment on, and close your own IT support tickets.
---

# IT Support Ticket Lifecycle MCP server

The IT Support Ticket Lifecycle MCP server enables LLMs to interact with Jira Service Desk for the employee side of the IT support ticket lifecycle through natural conversation. It provides tools to search a linked Confluence knowledge base for a grounded troubleshooting answer, and to create, track, comment on, and close IT support tickets you own, without requiring direct interaction with the Jira Service Desk portal.

## Uses

Use the IT Support Ticket Lifecycle MCP server to perform the following actions:

- Search a linked Confluence knowledge base to answer questions
- Create a new IT support ticket after validating the request type against Jira Service Desk
- Check the status of a ticket you've raised
- List your open, closed, or all tickets
- View full details for a ticket you own
- Add a comment to a ticket you own
- Close a resolved ticket you own using the close transition configured for your Jira Service Desk connection

### Example prompts

Use the following example prompts to invoke IT Support Ticket Lifecycle MCP server tools:

- `My VPN is not connecting. What should I do?`
- `How do I reset my password?`
- `Create a ticket for laptop repair.`
- `What's the status of my ticket IT-1234?`
- `Show me all my open tickets.`
- `Add a comment to IT-1234 saying I've rebooted.`
- `Close my access request, it's resolved.`
- `List my closed tickets from this month.`
- `File a ticket for a broken monitor.`
- `What tickets have I raised this month?`

## IT Support Ticket Lifecycle MCP server tools

The IT Support Ticket Lifecycle MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_confluence](#search-confluence-tool) | Searches the IT service desk's linked Confluence knowledge base and retrieves bounded article content for the top matches. |
| [resolve\_ticket\_metadata](#resolve-ticket-metadata-tool) | Extracts a summary, description, and request type from your request, and reports required, missing, and unsupported fields. |
| [create\_ticket](#create-ticket-tool) | Drafts a ticket, validates it against Jira Service Desk, presents a preview for your approval, then creates it. |
| [list\_my\_tickets](#list-my-tickets-tool) | Lists your tickets and filters them by status. |
| [get\_my\_ticket](#get-my-ticket-tool) | Retrieves full detail for a ticket you own, including its public comments across multiple pages. |
| [add\_comment\_to\_ticket](#add-comment-to-ticket-tool) | Drafts a comment for a ticket you own, presents a preview for your approval, then posts it. |
| [close\_my\_ticket](#close-my-ticket-tool) | Looks up the close transition for a ticket you own, presents a preview for your approval, then closes the ticket and returns the resulting status. |

## Install the IT Support Ticket Lifecycle MCP server

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
    

## IT Support Ticket Lifecycle connection setup

Refer to the following sections to connect the IT Support Ticket Lifecycle MCP server to Jira Service Desk:

View IT Support Ticket Lifecycle connection setup steps

### Jira Service Desk API version

The Jira Service Desk connector uses the [Jira Service Desk Cloud REST API](https://developer.atlassian.com/cloud/jira/service-desk/rest/intro/).

### Jira Service Desk supported editions and versions

The Jira Service Desk connector works with both cloud and on-prem instances 7.x and later.

The Jira Service Desk connector supports the following authentication types:

- [API token](#jira-service-desk-api-token)
- [OAuth 2.0](#jira-service-desk-oauth-2-0)
- [Basic authentication with password](#jira-service-desk-basic-authentication-with-password)

### Jira Service Desk API token

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
    

### Jira Service Desk OAuth 2.0

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
    

### Jira Service Desk basic authentication with password

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
    

### Jira Service Desk role requirements

Each tool's availability depends on the permissions granted to the connected account. A tool call that lacks the required permission returns a `permission_denied` outcome instead of a partial result.

The IT Support Ticket Lifecycle MCP server requires the following permissions in Jira Service Desk:

- Read and write access for customer requests
- Read access for Confluence knowledge bases

This server reaches the Confluence knowledge base entirely through the Jira Service Desk connection. No separate Confluence connection is required.

By default, only a ticket's reporter can view, comment on, or close a ticket through this server. The `ownership.allow_participants` data table key extends `list_my_tickets` to also list tickets you participate in, if the Jira Service Desk permission scheme allows participant access.

### Data table configuration

Edit the following data tables to control which request types this server supports, Confluence search behavior, ticket ownership, and operational limits:

- `supported_request_types`: Enter the allowlist of request types this server can populate. Add a row for each supported request type, with its `request_type_id`, `name`, and the `close_transition_id` that closes or resolves a customer request of that type. Allowlisted types can't have Jira Service Management Forms, user pickers, cascading selects, or asset lookups.
  
- `itsm_config` contains the following keys:
  

| Key | Description |
| --- | --- |
| `jsm.service_desk_id` | Enter the service desk ID for your Jira Service Desk connection. The server injects this ID on every request. The LLM doesn't supply the ID directly. Defaults to a placeholder value of `REPLACE_ME`, and every tool returns an error until you set this. |
| `confluence.enabled` | Configure whether the `search_confluence` tool is available. Defaults to `true`. |
| `confluence.max_results_in_search` | Enter the maximum number of Confluence articles to return for each search. Defaults to `5`, up to a maximum of `10`. |
| `confluence.max_articles_fetched_for_content` | Enter the number of top search results the server retrieves full content for. Defaults to `3`, up to a maximum of `5`. |
| `confluence.content_chars_per_article` | Enter the maximum number of characters of article content to retrieve for each article. Defaults to `4000`. |
| `taxonomy.request_type_cache_ttl_seconds` | Enter how long, in seconds, the server caches resolved request-type field metadata. Defaults to `900`. |
| `ownership.allow_participants` | Configure whether `list_my_tickets` lists tickets where you're a participant, in addition to tickets you own. This requires that the Jira Service Desk permission scheme allows participant access. This doesn't affect viewing, commenting on, or closing a ticket. Defaults to `false`. |
| `server_limits.max_query_chars` | Enter the maximum length for the natural-language query that `search_confluence` accepts. Defaults to `500`. |
| `server_limits.min_confluence_query_chars` | Enter the minimum query length `search_confluence` requires. Defaults to `3`. |
| `server_limits.max_comment_chars` | Enter the maximum length of a comment body. Defaults to `10000`. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data tables:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Data Tables** folder.
   
4. Select the data table to update, such as `supported_request_types` or `itsm_config`.
   
5. [Add](/en/data-tables/user-interface/edit#add-a-new-row) or [edit](/en/data-tables/user-interface/edit#edit-a-row) rows to make your changes. For example, set the `itsm_config` row with key `jsm.service_desk_id` to your service desk's ID.
   

## How to use IT Support Ticket Lifecycle MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_confluence tool

The **search\_confluence** tool searches the IT service desk's linked Confluence knowledge base and retrieves bounded article content for the top matches. Your LLM uses this tool first for troubleshooting or how-do-I questions, before offering to create a ticket.

**Try asking**:

- `My VPN is not connecting.`
- `How do I set up my email on my phone?`
- `Is there a guide for connecting to the office Wi-Fi?`

### resolve\_ticket\_metadata tool

The **resolve\_ticket\_metadata** tool extracts a summary, description, and request type from your request, and reports required, missing, and unsupported fields. Your LLM uses this tool after a Confluence search finds no answer, or when you explicitly ask to file a ticket.

**Try asking**:

- `Create a ticket for laptop repair.`
- `File a ticket, my monitor won't turn on.`
- `I need an access request ticket for the finance shared drive.`

### create\_ticket tool

The **create\_ticket** tool drafts a ticket, validates it against Jira Service Desk, presents a preview for your approval, then creates it. Your LLM calls this tool once to draft and validate the ticket and display the preview, then calls it again after you approve it to create the ticket.

**Try asking**:

- `Show me what this ticket will look like before you create it.`
- `Go ahead and create the ticket.`
- `Change the priority to high before you submit it.`

### list\_my\_tickets tool

The **list\_my\_tickets** tool lists your tickets and filters them by status. Your LLM uses this tool when you ask about your tickets in general terms rather than a specific ticket.

**Try asking**:

- `Show me all my open tickets.`
- `List my closed tickets from this month.`
- `What tickets have I raised?`

### get\_my\_ticket tool

The **get\_my\_ticket** tool retrieves full detail for a ticket you own, including its public comments across multiple pages. Your LLM uses this tool when you reference a specific ticket by ID or key.

**Try asking**:

- `What's the status of IT-1234?`
- `Show me the comments on my ticket IT-5678.`
- `Give me the details on my last access request.`

### add\_comment\_to\_ticket tool

The **add\_comment\_to\_ticket** tool drafts a comment for a ticket you own, presents a preview for your approval, then posts it. Your LLM calls this tool once to draft the comment and display a preview, then calls it again after you approve it to post the comment.

**Try asking**:

- `Add a comment to IT-1234 saying I've rebooted.`
- `Let IT know on my ticket that the issue is still happening.`
- `Post an update on my access request ticket.`

### close\_my\_ticket tool

The **close\_my\_ticket** tool looks up the close transition for a ticket you own, presents a preview for your approval, then closes the ticket and returns the resulting status. Your LLM calls this tool once to look up the transition and display a preview, then calls it again after you approve it to close the ticket.

**Try asking**:

- `Close my access request, it's resolved.`
- `Mark IT-1234 as done.`
- `Resolve my laptop repair ticket.`

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
