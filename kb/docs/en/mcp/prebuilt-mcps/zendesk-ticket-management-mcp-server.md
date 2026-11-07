---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/zendesk-ticket-management-mcp-server.md
description: >-
  Use the Zendesk Ticket Management MCP server to let LLMs find, create, and
  update Support tickets, manage queues, and monitor SLAs.
---

# Zendesk Ticket Management MCP server

The Zendesk Ticket Management MCP server enables LLMs to manage and explore Zendesk Support tickets across their full lifecycle through natural conversation. It provides tools to find, create, and update support tickets, manage queues, and monitor SLAs without requiring direct interaction with the Zendesk interface.

## Uses

Use the Zendesk MCP server to perform the following actions:

- Search for tickets using keywords or structured filters
- Retrieve full details for specific tickets
- View conversation history and comments on tickets
- Retrieve information about ticket requesters and agents
- List tickets in your personal queue or team queues
- Find unassigned tickets for triage
- Monitor overdue tickets and SLA compliance
- Check when tickets entered specific statuses
- Create new support tickets
- Update ticket fields such as status, priority, and assignee
- Add public replies or internal notes to tickets

### Example prompts

Use the following example prompts to invoke Zendesk Ticket Management MCP server tools:

- `What's the status of ticket #12345?`
- `Show me the conversation on ticket #789.`
- `Find tickets about login failures.`
- `List my open tickets.`
- `What tickets are unassigned?`
- `Which tickets are overdue?`
- `When was ticket #4560 solved?`
- `Create a ticket for Acme Corp about their billing issue.`
- `Set ticket #7892 to high priority.`
- `Reply to the customer on ticket #1432 with the solution.`

## Zendesk MCP server tools

The Zendesk MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_ticket](#get-ticket-tool) | Retrieves full details for a Zendesk ticket by ticket ID. |
| [get\_user](#get-user-tool) | Retrieves basic profile information for a Zendesk user by user ID. |
| [list\_ticket\_comments](#list-ticket-comments-tool) | Retrieves conversation comments for a Zendesk ticket. |
| [search\_tickets](#search-tickets-tool) | Searches Zendesk tickets using keyword queries. |
| [list\_tickets](#list-tickets-tool) | Lists Zendesk tickets using structured filters. |
| [list\_my\_tickets](#list-my-tickets-tool) | Lists tickets assigned to the authenticated user. |
| [list\_unassigned\_tickets](#list-unassigned-tickets-tool) | Lists Zendesk tickets without an assigned agent. |
| [list\_overdue\_tickets](#list-overdue-tickets-tool) | Lists tickets that are overdue or approaching SLA deadlines. |
| [get\_ticket\_status\_transition\_timestamp](#get-ticket-status-transition-timestamp-tool) | Retrieves the timestamp when a ticket most recently entered a status you specify. |
| [create\_ticket](#create-ticket-tool) | Creates a new Zendesk support ticket. |
| [update\_ticket](#update-ticket-tool) | Updates fields on an existing Zendesk ticket. |
| [add\_ticket\_comment](#add-ticket-comment-tool) | Adds a public reply or internal note to a Zendesk ticket. |

## Install the Zendesk MCP server

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
    

## Zendesk connection setup

View Zendesk connection setup steps

The Zendesk connector uses OAuth 2.0 authentication.

> **DEPRECATED AUTHENTICATION METHODS**
> 
> Effective March 31, 2026, you can no longer create new Zendesk connections using Basic authentication or Custom OAuth profiles. This change is required by [Zendesk Developer Terms](https://www.zendesk.com/company/agreements-and-terms/zendesk-developer-terms/).
> 
> Existing connections using these authentication methods will continue to work until **April 30, 2027**. On this date, Zendesk connections still using Basic authentication or a Custom OAuth profile will be terminated, and recipes relying on these connections will stop functioning.

Complete the following steps to connect to Zendesk in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Zendesk` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Zendesk with OAuth 2.0](/assets/oauth2.CJ5g3KV-.png)_Connect to Zendesk with OAuth 2.0_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Zendesk subdomain in the **Subdomain** field. For example, your subdomain is `acme` if your Zendesk URL is `https://acme.zendesk.com`.
   
6. Click **Connect**.
   
7. Sign in to Zendesk using your credentials to authorize Workato.
   

### Project property configuration

You must configure the **ZENDESK\_SLA\_VIEW** for your Zendesk Ticket Management MCP server at the project level. **ZENDESK\_SLA\_VIEW** is used for the `list_overdue_tickets` tool. You can configure this setting to operate in deterministic or efficient mode. Deterministic mode scans for `SLA-breached` tickets while efficient mode scans for `SLA-nearing tickets`. Zendesk admins must configure Zendesk View IDs for SLA-breached or SLA-nearing tickets. The `list_overdue_tickets` tool queries the View IDs directly when you set the project property in Workato and View IDs are configured and accessible in Zendesk.

The `list_overdue_tickets` tool scans unsolved tickets using Search API with SLA sideloading and filters results by SLA metrics if you don't set the **ZENDESK\_SLA\_VIEW** project property. This fallback is bounded by page and record caps and may return partial results in large accounts.

Complete the following steps to configure your SLA view:

View Project property configuration steps

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the **ZENDESK\_SLA\_VIEW** property and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-sla-view-project-property.CmKKHSw3.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and enter your Zendesk SLA view. For example, `SLA-Breached Tickets` or `SLA-nearing tickets`.
   

## How to use Zendesk MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_ticket tool

The **get\_ticket** tool retrieves full details for a Zendesk ticket by ticket ID. Your LLM uses this tool to retrieve details for a ticket ID you provide.

**Try asking**:

- `What's the status of ticket #4234?`
- `Get the details for ticket 7890.`
- `Show me ticket #4561.`
- `Tell me about ticket 1432.`

### get\_user tool

The **get\_user** tool retrieves basic profile information for a Zendesk user by user ID. Your LLM uses this tool to provide information about a ticket requester or agent, or when additional user context is required after retrieving a ticket.

**Try asking**:

- `Who is the requester for this ticket?`
- `What organization is this customer part of?`
- `Get information about the agent assigned to this ticket.`
- `Tell me about user 9876.`

### list\_ticket\_comments tool

The **list\_ticket\_comments** tool retrieves conversation comments for a Zendesk ticket. Your LLM uses this tool to view replies, notes, or conversation history, or when deeper context is required after retrieving a ticket.

**Try asking**:

- `Show me the conversation on ticket #7890.`
- `What replies are on ticket #4562?`
- `Get the comment history for this ticket.`
- `What notes are on ticket #4325?`

### search\_tickets tool

The **search\_tickets** tool searches Zendesk tickets using keyword queries. Your LLM uses this tool to search with keywords, phrases, or error descriptions to find relevant tickets.

**Try asking**:

- `Find tickets about login failures.`
- `Search for tickets mentioning SSO timeout.`
- `Look for tickets about billing errors.`
- `Find tickets containing 'password reset'.`

### list\_tickets tool

The **list\_tickets** tool lists Zendesk tickets using structured filters. Your LLM uses this tool when you specify structured attributes such as status, assignee, group, or tags.

**Try asking**:

- `Show me open tickets for Acme Corp.`
- `List high-priority tickets assigned to Mei.`
- `Get all pending tickets from this week.`
- `Show me tickets tagged with 'billing'.`

### list\_my\_tickets tool

The **list\_my\_tickets** tool lists Zendesk tickets assigned to you. Your LLM uses this tool to view your work queue or check what tickets are assigned to you.

**Try asking**:

- `What's in my queue?`
- `Show me my open tickets.`
- `What tickets are assigned to me?`
- `What should I work on next?`

### list\_unassigned\_tickets tool

The **list\_unassigned\_tickets** tool lists Zendesk tickets without an assigned agent. Your LLM uses this tool to view unassigned tickets for triage or to identify work that needs to be picked up.

**Try asking**:

- `What tickets are unassigned?`
- `Show me tickets that need to be picked up.`
- `What's in the triage queue?`
- `What tickets haven't been assigned yet?`

### list\_overdue\_tickets tool

The **list\_overdue\_tickets** tool lists tickets that are overdue or approaching SLA deadlines. Your LLM uses this tool to monitor SLA compliance or identify at-risk tickets.

**Try asking**:

- `Which tickets are overdue?`
- `Show me tickets approaching SLA deadlines.`
- `What tickets are at risk?`
- `What needs immediate attention for SLA compliance?`

### get\_ticket\_status\_transition\_timestamp tool

The **get\_ticket\_status\_transition\_timestamp** tool retrieves the timestamp when a ticket most recently entered a status you specify. Your LLM uses this tool to find when a ticket entered a specific lifecycle state, such as when it was solved.

**Try asking**:

- `When was ticket #4561 solved?`
- `When did this ticket move to pending?`
- `What time was ticket #7890 closed?`
- `When did ticket #4324 enter the open status?`

### create\_ticket tool

The **create\_ticket** tool creates a new Zendesk support ticket. Your LLM uses this tool to create a new ticket from customer communications or reported issues.

**Try asking**:

- `Create a ticket for Acme Corp about their billing issue.`
- `File a bug report for the login timeout.`
- `Create a ticket for jade@acme.com about password reset.`
- `Log a new support ticket for the API error.`

### update\_ticket tool

The **update\_ticket** tool updates fields on an existing Zendesk ticket, including status, priority, assignee, and custom fields. Your LLM uses this tool to modify ticket attributes, reassign work, or update status as issues progress.

**Try asking**:

- `Set ticket #7890 to high priority.`
- `Assign ticket #4561 to Marco.`
- `Close ticket #4324.`
- `Change the status of ticket #7890 to pending.`

### add\_ticket\_comment tool

The **add\_ticket\_comment** tool adds a public reply or internal note to a Zendesk ticket. Your LLM uses this tool to reply to customers or add internal notes. Your LLM confirms whether the comment should be public or internal before invoking the tool.

**Try asking**:

- `Reply to the customer on ticket #4324 with the solution.`
- `Add an internal note to ticket #4561 about the troubleshooting steps.`
- `Post a public update to ticket #7890.`
- `Add a private note saying we're waiting on engineering.`

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
