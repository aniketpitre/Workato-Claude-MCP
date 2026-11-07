---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/gong-mcp-server.md'
description: >-
  Use the Gong MCP server to connect your LLM to Gong with a curated set of
  tools to retrieve and explore customer conversation history through recordings
  and transcripts.
---

# Gong MCP server

The Gong MCP server enables LLMs to retrieve and explore customer conversation history from Gong. This allows you to access call recordings, transcripts, and participant information, without signing in to the Gong interface.

The Gong MCP server provides raw conversation data from Gong and your LLM can synthesize the data into prep notes, deal summaries, commitment tracking, or relationship overviews.

## Uses

Use the Gong MCP server when you plan to perform the following actions:

- Prepare for upcoming customer meetings using recent call history
- Catch up on what has been discussed with a customer or account
- Review conversation context for pipeline or deal discussions
- Recall commitments, action items, or next steps from past calls
- Locate a specific past conversation based on customer, participant, or timeframe
- Provide managers or coverage owners with quick situational awareness

### Example prompts

Use the following example prompts to invoke Gong MCP server tools:

- `I have a call with Datadog tomorrow. What should I know from our recent conversations?`
- `Catch me up on what we've discussed with Stripe in the last month`
- `What did we talk about last time we met with this customer?`
- `Give me the full picture on the Figma deal—what's happened across our calls?`
- `What objections has the customer raised on this opportunity?`
- `Who from their side has been involved in our conversations?`
- `Walk me through the conversation history for this deal`
- `What did I promise to send Acme after our call last week?`
- `What were the next steps from my call with the procurement team?`
- `Did the customer say they'd get back to us on anything?`
- `What action items came out of yesterday's call with Notion?`
- `What have been the main themes in our discussions with this customer over the past 3 months?`

## Gong MCP server tools

The Gong MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_calls](#search-calls-tool) | Retrieve information about conversations and calls in the Gong application. This tool can help identify the correct call using fields like context, brief, and outline. |
| [get\_call\_details](#get-call-details-tool) | Retrieve extensive details about a call by ID. This tool can provide additional information, including parties involved, a call outline, outcomes, key points, comments, questions, interactions, speakers, topics, and trackers. |
| [get\_call\_transcript](#get-call-transcript-tool) | Use this tool after search\_calls to retrieve the full conversation content for a specific call. This tool can help extract action items, requirements, and next steps from a conversation. |

## Install the Gong MCP server

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
    

## Gong connection setup

The Gong connector uses OAuth 2.0 authentication.

View Gong OAuth 2.0 connection setup steps

### Minimum and default scopes

Workato requires the `api:users:read` scope. Refer to the [Gong API documentation](https://app.gong.io/settings/api/documentation#overview) for more detailed information about the available scopes.

### Gong setup

Complete the following steps in Gong to generate credentials:

1. Sign in to your Gong developer instance. Refer to [Request a developer instance](https://help.gong.io/docs/create-an-app-for-gong#request-a-developer-instance) for more information.
   
2. Go to **Admin center**.
   
   ![Admin center](/assets/admin-center.ynD0MeHK.png)_Admin center_
   
3. Click **API** in the **Ecosystem** section.
   
4. Click **CREATE INTEGRATIONS** in the **INTEGRATIONS** tab.
   
5. Complete the **CREATE YOUR GONG INTEGRATION** page, including name, description, and required authorization scopes. Refer to [Submit your integration details to Gong](https://help.gong.io/docs/create-an-app-for-gong?highlight=client%20secret) for more information.
   
   > **SELF-SERVICE (WORKATO FREE, WORKATO PRO, OR DEVELOPER SANDBOX) WORKSPACES**
   > 
   > If you created your workspace as a [Self-service](https://www.workato.com/developers/sandbox) user, use `https://app.trial.workato.com/oauth/callback` as the redirect URI or callback URL when you configure the OAuth integration.
   
6. Click **Save**. Your integration information appears as a new row in the list of integrations.
   
7. Copy and save the **CLIENT ID** and **CLIENT SECRET** for use in Workato.
   

### Connect to Gong with OAuth 2.0

Complete the following steps to connect to Gong in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Gong.io` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Gong](/assets/connect.B5wWXAjX.png)_Connect to Gong_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Expand the **Advanced settings** section to configure **Scopes** for your connection. Workato requests all available scopes by default. You can select granular scopes from the multi-select list to limit access.
   
6. Enter the **Client ID** and **Client secret**. Refer to [Gong setup](#gong-setup) for more information.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to Gong using your credentials when prompted.
   
10. Click **Allow** to provision access to Workato.
    

### Project property configuration

You must configure the default timezone for your Gong MCP server at the project level.

Complete the following steps to configure your timezone:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the **MCP\_DEFAULT\_TIMEZONE** property and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/edit-timezone.CiilJ_dZ.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and enter your timezone. For example: `US/Pacific`, `Australia/Sydney`, `Asia/Kolkata`, or `Europe/London`.
   

## How to use Gong MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_calls tool

The **search\_calls** tool retrieves a list of recorded calls associated with a specific customer or account. Your LLM uses this tool to find recent meetings, check the duration of a specific conversation, or see who participated in a call with a client.

**Try asking**:

- `Find recent calls with the 'Acme Corp' account.`
- `Search for any meetings with 'Global Industries' from last month.`
- `What calls have we had with 'John Smith' lately?`
- `Show me the metadata for the most recent calls with 'Starlight Ventures'.`

### get\_call\_details tool

The **get\_call\_details** tool retrieves the complete metadata for a Gong call you specify. Your LLM uses this tool to get a full list of attendees and their email addresses, verify the call duration, and see which sales opportunities or accounts are linked to the conversation.

**Try asking**:

- `Get the full details and participant list for the call titled 'Quarterly Business Review'.`
- `Who were the external participants in my last meeting with 'Acme Corp'?`
- `What was the duration of the 'Acme Corp' call from yesterday?`
- `What are the email addresses of the people who attended the 'Initial Discovery' call?`

### get\_call\_transcript tool

The **get\_call\_transcript** tool retrieves the word-for-word text of a specific call. Your LLM uses this tool to review exactly what was said during a meeting, identify specific quotes from a client, or search for key technical details mentioned during a conversation without re-listening to the audio.

**Try asking**:

- `Get the full transcript for the 'Product Demo' call.`
- `What exactly did the client say about the budget in call #54321?`
- `Show me the transcript for my last meeting with 'Acme Corp' with speaker labels.`
- `Read the transcript of the 'Technical Discovery' call to find the database requirements mentioned.`

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
