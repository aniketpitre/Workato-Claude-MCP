---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/notion-databases-mcp-server.md'
description: >-
  Use the Notion Databases MCP server to let LLMs query, create, update, and
  archive database items without opening the Notion app.
---

# Notion Databases MCP server

The Notion Databases MCP server enables LLMs to interact with existing Notion databases. The Notion Database MCP server provides tools to query, create, update, and archive database items without requiring direct interaction with the Notion interface.

## Uses

Use the Notion Databases MCP server when you plan to perform the following actions:

- Discover databases accessible in your Notion workspace
- Understand database schemas including properties and relationships
- Search and retrieve database items using filters and sorting
- Get details for specific database items by identifier
- Create new items in existing databases
- Update properties of existing database items
- Archive completed or obsolete database items

### Example prompts

- `What databases do I have access to in Notion?`
- `Show me the schema for my Tasks database.`
- `Find all high-priority items in the project tracker.`
- `Get the details for the feature request item.`
- `Create a new task in my project database for the API integration.`
- `Update the status of this item to 'In Progress'.`
- `Archive the completed tasks from last sprint.`

## Notion Databases MCP server tools

The Notion Databases MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_databases](#list-databases-tool) | Retrieves databases accessible within the user's Notion workspace. |
| [get\_database\_schema](#get-database-schema-tool) | Retrieves the schema and metadata for a specified Notion database. |
| [query\_database\_items](#query-database-items-tool) | Searches and retrieves items from a Notion database using filters, sorting, and pagination. |
| [get\_database\_item](#get-database-item-tool) | Retrieves a single item from a Notion database by its identifier. |
| [create\_database\_item](#create-database-item-tool) | Creates a new item in an existing Notion database. |
| [update\_database\_item](#update-database-item-tool) | Updates properties of an existing item in a Notion database. |
| [archive\_database\_item](#archive-database-item-tool) | Archives an existing item in a Notion database. |

## Install the Notion Databases MCP server

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
    

### Notion connection setup

View Notion connection setup steps

Authenticate your Notion connection in Workato using one of the following methods:

- [OAuth 2.0](#oauth-2-0-authentication): Use this method for public integrations that require access across multiple Notion workspaces.
- [API key](#api-key-authentication): Use this method for internal integrations tied to a specific Notion workspace.

#### OAuth 2.0 authentication

View OAuth 2.0 authentication steps

Complete the following steps to set up your Notion connection using OAuth 2.0:

1. Enter a **Connection name** that identifies which Notion instance Workato is connected to.
   
2. Select **OAuth (Public integration)** in the **Authentication** field.
   
3. Enter the **Client ID** and **Client secret** for your Notion integration. Refer to Notion's [Public integration auth flow setup](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up) guide to generate these credentials.
   
4. Click **Connect** to complete the setup.
   

#### API key authentication

View API key authentication steps

Complete the following steps to set up your Notion connection using an API key:

1. Enter a **Connection name** that identifies which Notion instance Workato is connected to.
   
2. Select **API Key (Internal integration)** in the **Authentication** field.
   
3. Enter your Notion integration's **Integration Token**. Refer to Notion's [Internal integration auth flow setup](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up) guide to generate this token.
   
4. Click **Connect** to complete the setup.
   

## How to use Notion Databases MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_databases tool

The **list\_databases** tool retrieves a list of databases accessible within your Notion workspace. Your LLM uses this tool to discover what databases exist, to select an appropriate database before creating or querying items, or to retrieve available databases.

**Try asking**:

- `What databases do I have access to in Notion?`
- `Show me all my Notion databases.`
- `List the databases in my workspace.`
- `What project trackers do I have in Notion?`

### get\_database\_schema tool

The **get\_database\_schema** tool retrieves the schema and metadata for a specified Notion database. Your LLM uses this tool to understand the structure of a database before querying items, creating new records, or updating existing ones.

**Try asking**:

- `Show me the schema for my Tasks database.`
- `What properties does the project tracker have?`
- `Get the structure of the feature requests database.`
- `What fields are in my CRM database?`

### query\_database\_items tool

The **query\_database\_items** tool searches and retrieves items from a Notion database using filters, sorting, and pagination. Your LLM uses this tool to find, list, or review database items based on criteria you specify such as status, priority, dates, ownership, or keywords.

**Try asking**:

- `Find all high-priority items in the project tracker.`
- `Show me tasks assigned to me that are in progress.`
- `List feature requests created this month.`
- `Find all completed items from last sprint.`

### get\_database\_item tool

The **get\_database\_item** tool retrieves a single item from a Notion database by its identifier. Your LLM uses this tool to reference a specific item or inspect an item before updating it.

**Try asking**:

- `Get the details for item abc123 in the Tasks database.`
- `Show me the feature request item xyz789.`
- `Retrieve the information for this project tracker entry.`
- `Get the complete details for that task.`

### create\_database\_item tool

The **create\_database\_item** tool creates a new item in an existing Notion database. Your LLM uses this tool to add, log, or capture a new record such as a task, feature, issue, or note in an existing database.

**Try asking**:

- `Create a new task in my project database for the API integration.`
- `Add a feature request for dark mode support.`
- `Log a new issue in the bug tracker about the login timeout.`
- `Add a meeting note to the team database.`

### update\_database\_item tool

The **update\_database\_item** tool updates properties of an existing item in a Notion database. Your LLM uses this tool to report progress, make changes, or apply corrections to an existing database item.

**Try asking**:

- `Update the status of this task to 'In Progress'.`
- `Change the priority of the API integration task to high.`
- `Update the due date for this item to next Friday.`
- `Mark this feature request as reviewed.`

### archive\_database\_item tool

The **archive\_database\_item** tool archives an existing item in a Notion database. Your LLM uses this tool to mark tasks, records, or items as completed, obsolete, or removed from active work.

**Try asking**:

- `Archive the completed tasks from last sprint.`
- `Archive this item since it's no longer relevant.`
- `Mark this task as archived.`
- `Archive all the old feature requests.`

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
