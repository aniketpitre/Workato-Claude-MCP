---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/highspot-mcp-server.md'
description: >-
  Use the Highspot MCP server to let LLMs discover, share, and track sales
  content and access battle cards by chat.
---

# Highspot MCP server

The Highspot MCP server enables LLMs to manage, discover, share, and track sales content in Highspot through natural conversation. It provides tools to access decks and battle cards, track pitch engagement, and get instant answers without requiring direct interaction with the Highspot interface.

## Uses

Use the Highspot MCP server to perform the following actions:

- Search for sales enablement content by keyword or content type
- Get detailed information about specific content items
- View pitches you've created and their engagement metrics
- Get AI-generated answers to questions from Highspot content
- Browse available Spots (content collections)
- Track content engagement and pitch activity
- Access battle cards, case studies, and presentations

### Example prompts

- `Find competitive battle cards in Highspot.`
- `Show me details about this sales deck.`
- `Show me my recent pitches and their engagement.`
- `What's our pricing model for enterprise customers?`
- `What Spots are available for product content?`
- `Find presentations about our AI platform.`

## Highspot MCP server tools

The Highspot MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_content](#search-content-tool) | Searches Highspot content items by keyword with optional sorting. |
| [get\_content\_details](#get-content-details-tool) | Retrieves full metadata for a Highspot content item you specify. |
| [list\_my\_pitches](#list-my-pitches-tool) | Lists pitches created by the current user with engagement summary data. |
| [get\_instant\_answer](#get-instant-answer-tool) | Returns an AI-generated answer to a natural language question with source citations from Highspot content. |
| [list\_spots](#list-spots-tool) | Lists available Spots in Highspot. |

## Install the Highspot MCP server

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
    

## Highspot connection setup

View Highspot connection setup steps

The Highspot connector uses API key authentication.

This authentication method requires the following access and values:

- Admin access to your Highspot instance
- API credentials from Highspot

### Highspot API key authentication setup

View Highspot API key authentication setup steps

Complete the following steps to retrieve your API credentials from Highspot:

1. Sign in to your Highspot account.
   
2. Click your profile image and select **Settings**.
   
3. Go to **Developer > Basics**.
   
4. Copy and save the following values for use in Workato:
   
   - **URL**: Your Highspot API instance URL. For example, `https://api-su2.highspot.com`.
   - **Key**: Your API client key.
   - **Secret**: Your API client secret.

### Connect to Highspot with API key authentication

View connect to Highspot with API key authentication steps

Complete the following steps to connect to Highspot in Workato:

1. Click **Create > Connection**.
   
2. Search for `Highspot` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Highspot](/assets/connect.BQtF6-s_.png)_Connect to Highspot_
   
4. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
5. Enter the **API key** and **API secret**.
   
6. Enter the **Instance name**. For example, `https://api-su2.highspot.com`.
   
7. Enter the **API version** you plan to use. For example, `0.5`.
   
8. Click **Connect**.
   

## How to use Highspot MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_content tool

The **search\_content** tool searches Highspot content items by keyword with optional sorting. Your LLM uses this tool to find, search for, or locate sales enablement content in Highspot, including requests for decks, presentations, playbooks, battle cards, case studies, one-pagers, whitepapers, videos, or other sales content.

**Try asking**:

- `Find competitive battle cards in Highspot.`
- `Search for presentations about our AI platform.`
- `Show me all our case studies.`
- `Find the latest product one-pagers.`

### get\_content\_details tool

The **get\_content\_details** tool retrieves full metadata for a Highspot content item you specify. Your LLM uses this tool to provide detailed information about a content item you specify.

**Try asking**:

- `Show me details about this sales deck.`
- `When was this battle card last updated?`
- `Get the full information for this presentation.`
- `Tell me more about that case study.`

### list\_my\_pitches tool

The **list\_my\_pitches** tool lists pitches you've created with engagement summary data. Your LLM uses this tool to view your pitches, shared content, Digital Sales Rooms, or pitch engagement metrics.

**Try asking**:

- `Show me my recent pitches.`
- `What have I sent to prospects?`
- `Has anyone viewed my pitch to Acme Corp?`
- `Get my pitch engagement data.`

### get\_instant\_answer tool

The **get\_instant\_answer** tool returns an AI-generated answer to a natural language question with source citations from Highspot content. Your LLM uses this tool to provide answers from Highspot content rather than a list of documents, such as product questions, process questions, or competitive positioning.

**Try asking**:

- `What's our pricing model for enterprise customers?`
- `How do we handle objections about security?`
- `What are the key differentiators vs Competitor X?`
- `What's our ROI story for manufacturing companies?`

### list\_spots tool

The **list\_spots** tool lists available Spots in Highspot. Your LLM uses this tool to understand how content is organized in Highspot, see available content collections or channels, or identify Spot names for context when searching content.

**Try asking**:

- `What Spots are available in Highspot?`
- `Show me the content collections.`
- `List all content channels.`
- `What Spots exist for product content?`

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
