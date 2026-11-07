---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/slack-mcp-server.md'
description: >-
  Use the Slack MCP server to connect your LLM to Slack with tools to search
  messages and channels, retrieve channel history and thread context, post and
  schedule messages, explore communication spaces, and look up user profiles.
---

# Slack MCP server

The Slack MCP server enables LLMs to interact with your Slack workspace for exploring conversational content, posting messages, and discovering channels and users. It provides tools to search messages and channels, retrieve channel history and thread context, send and schedule messages, explore available communication spaces, and retrieve user profile information without switching to the Slack interface.

The Slack MCP server helps you streamline communication workflows by allowing you to find past discussions, catch up on channels, post and schedule announcements, and find the right channels or people to contact directly from your AI conversation.

## Uses

Use the Slack MCP server when you plan to perform the following actions:

- Search for discussions about a topic, project, customer, or issue across channels
- Find a channel by name or topic
- Retrieve recent messages from a channel to catch up on activity
- Get the full context of a thread conversation
- Post meeting summaries, standup updates, or announcements to channels
- Schedule a message for future delivery to a channel or direct message
- Send direct messages to team members
- Discover available public channels in your workspace
- Find private channels you're already a member of
- Get information about specific channels (purpose, member count, etc.)
- Look up user profile information including title, department, and timezone

### Example prompts

Use the following example prompts to invoke Slack MCP server tools:

- `What's been discussed about Customer Acme in the last two weeks?`
- `Is there a channel for the checkout redesign project?`
- `Catch me up on #engineering since Monday.`
- `Get the full thread for the deployment incident discussion.`
- `Post a summary of our standup to #engineering-updates.`
- `Schedule a reminder in #team-updates for Monday at 9 AM.`
- `Send a DM to Sarah letting her know the project plan is approved.`
- `What public channels are available for engineering discussions?`
- `Get details about the #product-team channel.`
- `What is Sarah's job title and department?`

## Slack MCP server tools

The Slack MCP server template provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_messages](#search-messages-tool) | Searches for messages across channels and DMs the user can access, returning messages that match a query. |
| [search\_channels](#search-channels-tool) | Searches for channels by name or description, returning matching public and private channels the user can access. |
| [get\_channel\_history](#get-channel-history-tool) | Retrieves recent messages from a specific channel in reverse chronological order, with thread indicators and author metadata. |
| [get\_thread](#get-thread-tool) | Retrieves all messages in a thread given the parent message's timestamp and channel. |
| [get\_channel\_info](#get-channel-info-tool) | Retrieves detailed information about a single channel by its ID. |
| [list\_member\_channels](#list-member-channels-tool) | Returns a list of private channels the user is a member of, including group chats and direct messages. |
| [list\_public\_channels](#list-public-channels-tool) | Retrieves a list of public channels the user can access. |
| [get\_user\_info](#get-user-info-tool) | Retrieves profile information for a workspace user, including display name, real name, title, department, timezone, and current status. |
| [post\_message](#post-message-tool) | Posts a new message to a specified channel or direct message conversation on behalf of the authenticated user. |
| [schedule\_message](#schedule-message-tool) | Schedules a message to be posted to a specified channel or direct message at a future time. |

## Install the Slack MCP server

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
    

## Slack connection setup

View Slack connection setup steps

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
   

### Slack permissions

Each tool operates within the authenticated user's Slack permission scope. The connected account must have access to the channels and conversations it searches or posts to, and it must be granted the OAuth scopes appropriate to the tools it runs. Refer to Slack's [OAuth scopes documentation](https://docs.slack.dev/reference/scopes) for the complete list of scope capabilities.

## How to use Slack MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_messages tool

The **search\_messages** tool searches for messages across channels and DMs the user can access and returns messages that match a query. Your LLM uses this tool to find discussions about a topic, project, customer, or issue, locate past decisions, or surface who has been discussing a subject across your workspace.

**Try asking**:

- `What's been discussed about Customer Acme in the last two weeks?`
- `Find messages about the checkout redesign in #product.`
- `Did anyone discuss the budget approval last month?`
- `Why did we decide to sunset the v1 API?`

### search\_channels tool

The **search\_channels** tool searches for channels by name or description and returns matching public and private channels you can access. Your LLM uses this tool to find a channel by name or topic, discover whether a channel exists for a subject, or identify relevant channels to monitor.

**Try asking**:

- `Is there a channel for the API migration project?`
- `Find channels related to customer success.`
- `Which channels cover engineering discussions?`
- `Search for a channel about release announcements.`

### get\_channel\_history tool

The **get\_channel\_history** tool retrieves recent messages from a specific channel in reverse chronological order, with thread indicators and author metadata. Your LLM uses this tool to catch up on a channel after time away, review recent activity, or understand what's been posted in a particular space.

**Try asking**:

- `Catch me up on #engineering since Monday.`
- `Show me the last 30 messages in #product.`
- `What was posted in #customer-success this week?`
- `Pull recent activity from the #releases channel.`

### get\_thread tool

The **get\_thread** tool retrieves all messages in a thread given the parent message's timestamp and channel. Your LLM uses this tool to get the full context of a conversation after identifying a relevant thread through **search\_messages** or **get\_channel\_history**.

**Try asking**:

- `Get the full thread for the deployment incident discussion.`
- `Show me all replies in this thread.`
- `What did people say in the thread about the pricing change?`
- `Pull the complete conversation for the Acme escalation thread.`

### get\_channel\_info tool

The **get\_channel\_info** tool retrieves detailed information about a specific Slack channel, including name, description, purpose, member count, creation date, and whether it's archived or private. Your LLM uses this tool to verify channel details before posting, understand a channel's purpose, or check membership information when coordinating team communication.

**Try asking**:

- `What is the #engineering channel used for and how many members does it have?`
- `Get the details for the customer-feedback channel.`
- `Is the #project-alpha channel archived or still active?`
- `Show me the description and member count for #sales-team.`

### list\_member\_channels tool

The **list\_member\_channels** tool retrieves the private channels you're a member of, including group chats and direct messages. Your LLM uses this tool to discover where you're already participating, find a specific conversation space, or get a view of your private Slack conversations.

**Try asking**:

- `What private channels am I a member of?`
- `Show me all the private channels I'm in.`
- `List my group chats and DMs.`
- `What group conversations do I participate in?`

### list\_public\_channels tool

The **list\_public\_channels** tool retrieves all public channels available in your workspace, including those you haven't joined yet. Your LLM uses this tool to discover channels you can join, find the right place to post information, or explore what communication spaces exist in your organization.

**Try asking**:

- `What public channels are available in our workspace?`
- `Show me all the engineering-related public channels I can join.`
- `List all public channels so I can find the right place to share this update.`
- `What channels exist for product discussions that I'm not yet a member of?`

### get\_user\_info tool

The **get\_user\_info** tool retrieves profile details for workspace members, including their job title, department, timezone, and current status. Your LLM uses this tool to identify a message author, get context on a person mentioned in a discussion, or understand someone's role before reaching out.

**Try asking**:

- `Who is Sarah Chen and what is her role on the team?`
- `What department does @Dani work in?`
- `What is @Sarah's current status and timezone?`
- `Find out who the MCP development lead is and tell me their job title.`

### post\_message tool

The **post\_message** tool sends messages to Slack channels or direct messages. Your LLM uses this tool to share summaries, post project updates, announce decisions, or send quick follow-ups without leaving your AI chat.

**Try asking**:

- `Post a summary of our meeting notes to the #marketing-team channel.`
- `Send a DM to @Sarah letting her know the project plan is approved.`
- `Announce the v2 launch in #product-announcements and tag the @engineering-lead.`

### schedule\_message tool

The **schedule\_message** tool schedules a message to post to a specified channel or direct message at a future time. Your LLM uses this tool to time reminders, schedule announcements for specific hours, or send messages to teammates in different time zones. Slack posts the message automatically at the scheduled time on your behalf.

**Try asking**:

- `Schedule a reminder in #team-updates for Monday at 9 AM.`
- `Send this announcement to #releases tomorrow morning.`
- `Schedule a standup nudge in #engineering for 8 AM Pacific.`
- `Post this update to #product at the start of next week.`

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
