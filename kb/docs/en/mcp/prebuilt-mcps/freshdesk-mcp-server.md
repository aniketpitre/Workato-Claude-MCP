---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/freshdesk-mcp-server.md'
description: >-
  Use the Freshdesk MCP server to let LLMs search, create, and update support
  tickets, monitor SLAs, and reply through conversation.
---

# Freshdesk MCP server

The Freshdesk MCP server enables LLMs to manage and explore support tickets in Freshdesk through natural conversation. It provides tools to search tickets, retrieve ticket details and conversation threads, monitor agent queues and service level agreement (SLA) compliance, create new tickets, update ticket fields, and add replies or internal notes without requiring direct interaction with the Freshdesk interface.

## Uses

Use the Freshdesk MCP server to perform the following actions:

- Retrieve full details for specific tickets
- View conversation threads including replies and notes
- Search for tickets by keyword across subjects and descriptions
- List tickets with filters for company, requester, status, priority, and assignee
- View tickets assigned to you
- Monitor overdue tickets and SLA compliance
- Find unassigned tickets for triage
- Create new support tickets
- Update ticket fields such as status, priority, and assignee
- Add public replies or private notes to tickets

### Example prompts

- `What's the status of ticket #12345?`
- `Show me the conversation on ticket #789.`
- `Find tickets about login failures.`
- `Show me open tickets for Acme Corp.`
- `What's in my queue?`
- `Which tickets are overdue?`
- `What tickets are unassigned?`
- `Create a ticket for Acme Corp about their billing issue.`
- `Set ticket #456 to high priority.`
- `Reply to the customer on ticket #789 confirming the fix.`

## Freshdesk MCP server tools

The Freshdesk MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_ticket](#get-ticket-tool) | Retrieves full details for a specific Freshdesk ticket by ticket ID. |
| [get\_ticket\_conversations](#get-ticket-conversations-tool) | Retrieves the full conversation thread for a Freshdesk ticket, including replies and notes. |
| [search\_tickets](#search-tickets-tool) | Searches Freshdesk tickets by keyword across subjects and descriptions. |
| [list\_tickets](#list-tickets-tool) | Retrieves Freshdesk tickets with flexible filters including company, requester, status, priority, assignee, and date range. |
| [list\_my\_tickets](#list-my-tickets-tool) | Lists tickets assigned to the authenticated user with optional status and priority filters. |
| [list\_overdue\_tickets](#list-overdue-tickets-tool) | Retrieves tickets that have breached or are approaching SLA deadlines. |
| [list\_unassigned\_tickets](#list-unassigned-tickets-tool) | Retrieves tickets with no assigned agent for triage workflows. |
| [create\_ticket](#create-ticket-tool) | Creates a new support ticket in Freshdesk. |
| [update\_ticket](#update-ticket-tool) | Updates fields on an existing Freshdesk ticket. |
| [add\_ticket\_note](#add-ticket-note-tool) | Adds a public reply or private note to an existing Freshdesk ticket. |

## Install the Freshdesk MCP server

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
    

## Freshdesk connection setup

View Freshdesk connection setup steps

Ensure you complete the following steps before using the Freshdesk connector in Workato:

- [Download Freshdesk from the community](#community-download)
- [Retrieve API key in Freshdesk](#retrieve-api-key-in-freshdesk)

### Download Freshdesk from the community

View Download Freshdesk from the community steps

Complete the following steps to install the connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Retrieve API key in Freshdesk

View Retrieve API key in Freshdesk steps

Complete the following steps to retrieve your Freshdesk API key:

1. Sign in to the [Freshdesk](https://login.freshworks.com/email-login/) portal.
   
2. Go to **Profile Settings** and click **View API Key**.
   
   ![Freshdesk View API Key](/assets/view-api-key.B1-bgSFd.png)_Freshdesk View API Key_
   
3. Copy the **API Key** and store it securely for later use.
   

### Connect to Freshdesk on Workato

View Connect to Freshdesk on Workato steps

Complete the following steps to connect your Freshdesk account to Workato:

1. Click **Create > Connection**.
   
2. Search for and select `Freshdesk` as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![Freshdesk Connection](/assets/freshdesk-connection.BdgfXr9U.png)_Freshdesk\_Connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the Freshdesk **API key**. Refer to [Retrieve API key in Freshdesk](#retrieve-api-key-in-freshdesk) to obtain this value.
   
6. Enter your Freshdesk instance subdomain in the **Helpdesk name** field.
   
7. Click **Connect**.
   

## How to use Freshdesk MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_ticket tool

The **get\_ticket** tool retrieves full details for a specific Freshdesk ticket by ticket ID. Your LLM uses this tool to check the status, priority, assignee, or other details of a specific ticket.

**Try asking**:

- `What's the status of ticket #12345?`
- `Tell me about ticket 67890.`
- `Get the details for ticket #456.`
- `Who is assigned to ticket #789?`

### get\_ticket\_conversations tool

The **get\_ticket\_conversations** tool retrieves the full conversation thread for a Freshdesk ticket, including replies and notes. Your LLM uses this tool to view conversation history, review customer communications, or check internal notes on a ticket.

**Try asking**:

- `Show me the conversation on ticket #789.`
- `What notes are on this ticket?`
- `Read the conversation thread for ticket #456.`
- `What has been discussed on ticket #12345?`

### search\_tickets tool

The **search\_tickets** tool searches Freshdesk tickets by keyword across subjects and descriptions. Your LLM uses this tool to find tickets by topic, keyword, error message, or description content.

**Try asking**:

- `Find tickets about login failures.`
- `Search for tickets mentioning SSO timeout.`
- `Look for tickets about billing errors.`
- `Find tickets containing 'password reset'.`

### list\_tickets tool

The **list\_tickets** tool retrieves Freshdesk tickets with flexible filters including company, requester, status, priority, assignee, and date range. Your LLM uses this tool to see tickets matching structured criteria such as company, status, or assignee.

**Try asking**:

- `Show me open tickets for Acme Corp.`
- `What high-priority tickets are assigned to Marco?`
- `List tickets created this week.`
- `Show me all pending tickets from jade@acme.com.`

### list\_my\_tickets tool

The **list\_my\_tickets** tool retrieves tickets assigned to you with optional status and priority filters. Your LLM uses this tool to see your work queue or check what tickets are assigned to you.

**Try asking**:

- `What's in my queue?`
- `What's assigned to me?`
- `Show me my open tickets.`
- `What should I work on next?`

### list\_overdue\_tickets tool

The **list\_overdue\_tickets** tool retrieves tickets that have breached or are approaching SLA deadlines. Your LLM uses this tool to monitor SLA compliance, identify at-risk tickets, or prioritize work based on urgency.

**Try asking**:

- `Which tickets are overdue?`
- `What's about to breach SLA?`
- `Show me at-risk tickets.`
- `What tickets need immediate attention for SLA compliance?`

### list\_unassigned\_tickets tool

The **list\_unassigned\_tickets** tool lists tickets with no assigned agent for triage workflows. Your LLM uses this tool when you need to see unassigned work, identify tickets that need to be picked up, or manage triage queues.

**Try asking**:

- `What tickets are unassigned?`
- `Show me tickets that need to be picked up.`
- `What came in that nobody's handling?`
- `What tickets need triage?`

### create\_ticket tool

The **create\_ticket** tool creates a new support ticket in Freshdesk. Your LLM uses this tool to create, log, or file a new support ticket from customer communications or reported issues.

**Try asking**:

- `Create a ticket for Acme Corp about their billing issue.`
- `Log a bug report from the customer call.`
- `File a ticket for jade@acme.com about login problems.`
- `Create a new support ticket for the SSO timeout error.`

### update\_ticket tool

The **update\_ticket** tool updates fields on an existing Freshdesk ticket including status, priority, assignee, and custom fields. Your LLM uses this tool to change ticket properties, reassign work, or update status as issues progress.

**Try asking**:

- `Set ticket #456 to high priority.`
- `Assign ticket #789 to Josh.`
- `Close ticket #123.`
- `Change the status of ticket #456 to pending.`

### add\_ticket\_note tool

The **add\_ticket\_note** tool adds a public reply or private note to an existing Freshdesk ticket. Your LLM uses this tool to respond to customers, document internal updates, or add context to tickets.

**Try asking**:

- `Reply to the customer on ticket #789 confirming the fix.`
- `Add a private note to ticket #456 saying we're waiting on logs.`
- `Post an update to ticket #123 for the customer.`
- `Add an internal note about the troubleshooting steps we tried.`

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
