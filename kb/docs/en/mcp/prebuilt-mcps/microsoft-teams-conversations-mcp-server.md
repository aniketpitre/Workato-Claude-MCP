---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-teams-conversations-mcp-server.md
description: >-
  Use the Microsoft Teams Conversations MCP server to connect your LLM to
  Microsoft Teams with tools to search, retrieve, and participate in
  conversations across channels and chats through natural language.
---

# Microsoft Teams Conversations MCP server

The Microsoft Teams Conversations MCP server enables LLMs to search, retrieve, and participate in Microsoft Teams conversations through natural conversation. It provides tools to find topics, projects, or customers, retrieve message history, get thread context, list teams, channels, and chats, and post messages or replies without requiring direct interaction with the Microsoft Teams interface.

## Uses

Use the Microsoft Teams Conversations MCP server to perform the following actions:

- List Microsoft Teams teams the authenticated user is a member of
- List channels within a specified Microsoft Teams team
- List one-on-one, group, and meeting chats the user participates in
- Retrieve messages and thread replies from a Microsoft Teams channel or chat
- Search for messages matching a keyword across Microsoft Teams channels and chats
- Post a new message to a Microsoft Teams channel or chat
- Reply to an existing message thread in a Microsoft Teams channel

### Example prompts

Use the following example prompts to invoke Microsoft Teams Conversations MCP server tools:

- `Which Microsoft Teams teams am I a member of?`
- `What channels are available in the Sales team?`
- `Show me my recent Microsoft Teams chats.`
- `Get the last 20 messages from the #general channel.`
- `Find discussions about the Acme renewal across my Microsoft Teams conversations.`
- `Search for any messages about the Q2 launch plan.`
- `Post a message to the #announcements channel.`
- `Reply to this thread in the Engineering channel.`

## Microsoft Teams Conversations MCP server tools

The Microsoft Teams Conversations MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_teams](#list-teams-tool) | Lists teams the authenticated user is a member of. |
| [list\_channels](#list-channels-tool) | Lists team channels that you specify. |
| [list\_chats](#list-chats-tool) | Lists one-on-one or group chats the authenticated user participates in. |
| [get\_messages](#get-messages-tool) | Retrieves messages or thread replies from a Microsoft Teams channel or chat. |
| [search\_messages](#search-messages-tool) | Searches for Microsoft Teams messages matching a keyword query across channels and chats the user can access. |
| [send\_message](#send-message-tool) | Posts a new message to a Microsoft Teams channel or chat on behalf of the authenticated user. |
| [reply\_to\_message](#reply-to-message-tool) | Posts a reply to an existing message thread in a Microsoft Teams channel. |

## Install the Microsoft Teams Conversations MCP server

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
    

## Microsoft Teams connection setup

View Microsoft Teams connection setup steps

The Microsoft Teams Conversations connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials): _Only available for tenant-specific connections_

View Microsoft MFA enforcement steps

> **MICROSOFT MFA ENFORCEMENT**
> 
> Microsoft is rolling out mandatory multifactor authentication (MFA) gradually to different applications and accounts in phases. This enforcement continues throughout 2025 and beyond. Refer to the Microsoft [Mandatory multifactor authentication for Azure and admin portals](https://learn.microsoft.com/en-us/entra/identity/authentication/concept-mandatory-multifactor-authentication?tabs=dotnet) documentation for more information.
> 
> We strongly recommend enabling MFA now for all Microsoft accounts used with Workato to avoid service disruptions from short-notice enforcement changes.
> 
> Complete the following steps to maintain uninterrupted service:
> 
> 1. Enable MFA for your Microsoft organization following the Microsoft MFA setup guide. Refer to [Set up multifactor authentication for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/admin/security-and-compliance/set-up-multi-factor-authentication?view=o365-worldwide) for more information.
>    
> 2. Reconnect your Microsoft connection in Workato.
>    
> 3. Complete the OAuth flow with MFA when prompted.
>    
> 4. Test your recipes to ensure they work with the updated connection.
>    

### Minimum scopes

View minimum scopes

The Microsoft Teams connector requires the following scopes. You must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Channel.ReadBasic.All`
- `ChannelMessage.Read.All`
- `ChannelMessage.Send`
- `Chat.Read`
- `Chat.ReadWrite`
- `ChatMessage.Send`
- `Team.ReadBasic.All`
- `User.Read`
- `offline_access`

### Authorization code grant authentication (OAuth 2.0)

Use the Tenant ID/Domain value with tenant-specific account types.

#### Microsoft Teams setup for authorization code grant authentication

View Microsoft Teams setup for authorization code grant authentication steps

Complete the following steps to set up Microsoft Teams for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

##### Register the Workato app in the Azure portal

Complete the following steps to register the Workato app and assign permissions for authorization code grant connections:

View register the Workato app in the Azure portal steps

Complete the following steps to register the Workato app in the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
   
2. Select **App registrations > + New registration**.
   
3. Enter a unique name for the application.
   
4. Use the **Supported account types** drop-down menu to select an account type.
   
5. Select **Web** from the **Select a platform** drop-down menu.
   
6. Use the following URI for the **Redirect URI**:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Select **Register**.
   

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions as outlined in [Minimum scopes](#minimum-scopes).
   
4. Click **Add permissions**. Refer to [Connect Microsoft Entra ID to the Microsoft Teams connector](/en/connectors/microsoft-teams#admin-consent) if specific permissions require admin consent.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft Teams with authorization code grant authentication

View connect to Microsoft Teams with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant-specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that aren't restricted to a specific organization (tenant).
   
   ![Microsoft Teams Common connection setup](/assets/teams-connect-common.CRs_A8zB.png)_Microsoft Teams Common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection setup](/assets/teams-connect-tenant-auth-code.Dunozk1-.png)_Microsoft Teams Tenant specific connection setup_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID), or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication type requires the following values:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Microsoft Teams setup for client credentials-based authentication (OAuth 2.0)

View Microsoft Teams setup for client-credentials based authentication steps

Complete the following steps to set up Microsoft Teams for client credentials-based authentication:

- [Register the Workato App in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

##### Register the Workato app in the Azure portal

View register the Workato app in the Azure portal steps

Complete the following steps to register the Workato app in the Azure portal:

1. Sign in to the [Azure portal](https://portal.azure.com/).
   
2. Select **App registrations > + New registration**.
   
3. Enter a unique name for the application.
   
4. Use the **Supported account types** drop-down menu to select an account type.
   
5. Select **Web** from the **Select a platform** drop-down menu.
   
6. Use the following URI for the **Redirect URI**:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Select **Register**.
   

##### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions** in the navigation sidebar.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions as outlined in [Minimum scopes](#minimum-scopes).
   
4. Click **Add permissions**. Refer to [Connect Microsoft Entra ID to the Microsoft Teams connector](/en/connectors/microsoft-teams#admin-consent) if specific permissions require admin consent.
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application ID, Object ID, and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID**, **Object ID**, and **Directory (tenant) ID** for use in Workato.
   

##### Obtain the User ID from the Azure portal

View obtain the User ID from the Azure portal steps

Complete the following steps to obtain the User ID from the Azure portal:

1. Go to **Home > Users** to obtain the `User ID`.
   
   ![Users](/assets/users.CuDgSGeL.png)_Select users_
   
2. Search for and select the default user you plan to use to perform operations. This user doesn't establish the connection but is required for performing certain operations that an app can't perform. It's also required in picklists to pull user data. For example, the folder picklist populates folders belonging to the default user.
   
3. Copy and save the **User principal name**. Use this value as the **User ID** in Workato.
   

#### Connect to Microsoft Teams with client credentials-based authentication

View connect to Microsoft Teams with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection account type setup](/assets/teams-connect-tenant-client-cred.DUtPSHGJ.png)_Microsoft Teams Tenant specific connection account type setup_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the User ID from the Azure portal](#obtain-user-id), [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids), and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## How to use Microsoft Teams Conversations MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_teams tool

The **list\_teams** tool lists teams the authenticated user is a member of. Your LLM uses this tool to list teams you belong to.

**Try asking**:

- `Which Microsoft Teams teams am I a member of?`
- `Show me all the teams I have access to.`
- `What teams exist in my Microsoft Teams environment?`
- `Find the team ID for the Sales team.`

### list\_channels tool

The **list\_channels** tool lists channels within a team that you specify. Your LLM uses this tool to list channels for a team. Requires a team ID from `list_teams`.

**Try asking**:

- `What channels are available in the Sales team?`
- `List all channels in the Engineering Microsoft Teams team.`
- `Show me the channels I can access in this team.`
- `Find the channel ID for #announcements.`

### list\_chats tool

The **list\_chats** tool lists one-on-one, group, and meeting chats the authenticated user participates in. Your LLM uses this tool to provide recent chats and chat activity.

**Try asking**:

- `Show me my recent Microsoft Teams chats.`
- `List my group chats in Microsoft Teams.`
- `Find my chat with the project team.`
- `What meeting chats do I have from this week?`

### get\_messages tool

The **get\_messages** tool retrieves messages or thread replies from a Microsoft Teams channel or chat. Your LLM uses this tool to provide recent messages from a channel or chat with conversation context for catch-up or meeting preparation, and thread replies for a specific Microsoft Teams channel message.

**Try asking**:

- `Get the last 20 messages from the #general channel.`
- `Show me recent messages in the product team chat.`
- `Pull the thread replies for this message in the Engineering channel.`
- `Catch me up on what was discussed in #sales-updates today.`

### search\_messages tool

The **search\_messages** tool searches for Microsoft Teams messages matching a keyword query across channels and chats the user can access. Your LLM uses this tool to find discussions about a topic, project, customer, or keyword across your Microsoft Teams conversations, to locate a past decision or discussion, or to search broadly rather than reading a specific channel.

**Try asking**:

- `Find discussions about the Acme renewal across my Microsoft Teams conversations.`
- `Search for any messages about the Q2 launch plan.`
- `Did anyone discuss the budget approval in Microsoft Teams?`
- `Find past decisions about the API migration in my channels.`

### send\_message tool

The **send\_message** tool posts a new message to a Microsoft Teams channel or chat on behalf of the authenticated user. Your LLM presents the message content and target to you for approval before posting.

**Try asking**:

- `Post a message to the #announcements channel.`
- `Send a message to the design team chat in Microsoft Teams.`
- `Post an update to the #project-status channel.`
- `Send this summary to the Sales team channel.`

### reply\_to\_message tool

The **reply\_to\_message** tool posts a reply to an existing message thread in a Microsoft Teams channel on behalf of the authenticated user. Your LLM presents the reply content and target thread to you for approval before posting.

**Try asking**:

- `Reply to this thread in the Engineering channel.`
- `Post my response to this message in the #product channel.`
- `Reply to the latest thread in #customer-success.`
- `Add my update to this Microsoft Teams thread.`

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
