---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/discord-mcp-server.md'
description: >-
  Use the Discord MCP server to let AI assistants read, post, and reply to
  channel messages, manage threads, and moderate members.
---

# Discord MCP server

The Discord MCP server enables AI assistants to read messages from Discord channels and threads, post or reply to messages, create discussion threads, search recent message history, pin or delete individual messages, and apply temporary timeouts to members using a configured Discord bot.

## Uses

Use the Discord MCP server when you plan to perform the following actions:

- View which Discord servers your bot has access to
- List channels within a Discord server
- Read recent messages from channels or threads
- Post new messages to channels or threads
- Reply to specific messages with conversational context
- Search for recent mentions of specific topics or terms
- Create threads from existing messages
- List active and archived threads in a channel
- Pin or unpin important messages for visibility
- Delete specific messages when explicitly instructed
- Apply temporary timeouts to members for moderation
- Get community context and server information

### Example prompts

- `What Discord servers is my bot in?`
- `Show me the channels in the Gaming Community server.`
- `Read the recent messages in the #general channel.`
- `Post an announcement in #announcements about the upcoming event.`
- `Reply to that message thanking them for the feedback.`
- `Search for recent mentions of 'bug report' in #support.`
- `Create a thread from that message to discuss the feature request.`
- `What threads are active in #development?`
- `Pin the message with the meeting link.`
- `Delete that spam message.`

## Discord MCP server tools

The Discord MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_guilds](#list_guilds-tool) | Retrieves a list of Discord servers or guilds where the bot is installed. |
| [list\_channels](#list_channels-tool) | Retrieves a list of text-based channels within a Discord server you specify. |
| [get\_channel\_metadata](#get_channel_metadata-tool) | Retrieves descriptive metadata for the Discord text-based channel you specify. |
| [read\_messages](#read_messages-tool) | Retrieves recent messages from the Discord text channel or thread you specify. |
| [post\_message](#post_message-tool) | Posts a new message to the Discord text channel or thread you specify. |
| [reply\_message](#reply_message-tool) | Posts a reply to an existing Discord message while preserving conversational context. |
| [search\_messages](#search_messages-tool) | Searches recent messages within the Discord text channel or thread you specify. |
| [list\_threads](#list_threads-tool) | Retrieves active and archived threads within the Discord text channel you specify. |
| [create\_thread](#create_thread-tool) | Creates a new thread in a Discord text channel from an existing message. |
| [get\_pinned\_messages](#get_pinned_messages-tool) | Retrieves a list of currently pinned messages in the Discord text channel you specify. |
| [pin\_message](#pin_message-tool) | Pins or unpins a Discord message in a channel. |
| [delete\_message](#delete_message-tool) | Deletes a Discord message. |
| [timeout\_member](#timeout_member-tool) | Applies a temporary timeout (mute) to the Discord server member you specify. |
| [get\_community\_context](#get_community_context-tool) | Retrieves basic community context information for the Discord server you specify. |

## Install the Discord MCP server

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
    

## Discord connection setup

View Discord connection setup steps

The Discord connector uses OAuth2 authentication.

### Install Discord from the community library

View install Discord from the community library steps

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
   

### Minimum and default scopes

View minimum and default scopes

These are the minimum required scopes to establish a connection. If you don't select these scopes, they're automatically added to your requested scopes.

- `Bot`
- `Identify`

### Discord setup for OAuth2 authentication

View Discord setup for OAuth2 authentication steps

Complete the following steps to retrieve credentials from Discord:

1. Go to the Discord [Applications](https://discord.com/developers/applications) page.
   
2. Click your application. To create a new application, refer to the Discord [Step 1: Creating an app](https://docs.discord.com/developers/quick-start/getting-started#step-1-creating-an-app) guide.
   
3. Click the **OAuth2** page under the **Overview** tab.
   
4. Copy and save the **Client ID** and **Client Secret** for use in Workato.
   
   > **SAVE YOUR SECRET**
   > 
   > The client secret only displays once. If you lose it, you must reset it.
   
5. Click **Add Redirect** under the **Redirect** section.
   
6. Add the following URI:
   
   ```html
   https://www.workato.com/oauth/callback
   ```
   
7. Click **Save Changes**.
   
8. Click the **Bot** page.
   
9. Click **Reset Token** to generate a new token.
   
10. Copy and save the **Token** for use in Workato.
    
    > **SAVE YOUR TOKEN**
    > 
    > The token only displays once. If you lose it, you must reset it.
    

### Connect to Discord with OAuth2 authentication

View connect to Discord with OAuth2 authentication steps

Complete the following steps to connect to in Workato:

1. Click **Create > Connection**.
   
2. Search for and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Discord connection setup](/assets/discord-connection-setup.DaFj6OAG.png)_Discord connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Client ID**. Refer to [Discord setup for OAuth2 authentication](#discord-setup) for instructions on how to retrieve the **Client ID**, **Client secret**, and **Bot token**.
   
6. Enter the **Client secret**.
   
7. Enter the **Bot token**.
   
8. Optional. Use the **Requested permissions (Oauth scopes)** drop-down menu to select the scopes you plan to add to this connection. Refer to [Minimum and default scopes](#scopes) for more information.
   
9. Optional. Use the **Bot permissions** drop-down menu to select the bot permissions you plan to include for this connection. This setting defaults to **Administrator** if left blank.
   
10. Click **Connect**.
    
11. Authorize access to the account.
    

## How to use Discord MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_guilds tool

The **list\_guilds** tool retrieves a list of Discord servers or guilds where your bot is installed. Your LLM uses this tool when you need to know which Discord servers are available or when server context hasn't been established yet.

**Try asking**:

- `What Discord servers is my bot in?`
- `Show me all the guilds where my bot is installed.`
- `List the Discord communities my bot can access.`
- `Which servers can I interact with?`

### list\_channels tool

The **list\_channels** tool retrieves a list of text-based channels within a specified Discord server that your bot can view. Your LLM uses this tool when you need to know about channels in a server or select a channel before message or thread operations.

**Try asking**:

- `Show me the channels in the Gaming Community server.`
- `What channels are available in this Discord server?`
- `List all text channels in the server.`
- `What channels can my bot access?`

### get\_channel\_metadata tool

The **get\_channel\_metadata** tool retrieves descriptive metadata for a Discord text-based channel. Your LLM uses this tool when you need to understand a channel's purpose, topic, type, or recent activity before posting messages or taking actions.

**Try asking**:

- `What is the #general channel used for?`
- `Show me the metadata for #announcements.`
- `What's the topic of the #support channel?`
- `Get details about the #development channel.`

### read\_messages tool

The **read\_messages** tool retrieves recent messages from the Discord text channel or thread you specify. Your LLM uses this tool when you need to review or summarize recent conversation, gather context before responding, or check discussion history.

**Try asking**:

- `Read the recent messages in #general.`
- `Show me what's been discussed in #support today.`
- `Summarize the recent conversation in the feature-requests thread.`
- `What have people been saying in #announcements?`

### post\_message tool

The **post\_message** tool posts a new message to a Discord text channel or thread. Your LLM uses this tool when you need to post, send, or announce a message that isn't a reply to a specific existing message.

**Try asking**:

- `Post an announcement in #announcements about the upcoming maintenance.`
- `Send a message to #general welcoming new members.`
- `Announce the event details in #events.`
- `Post the meeting summary in #team-updates.`

### reply\_message tool

The **reply\_message** tool posts a reply to an existing Discord message while preserving conversational context by linking the new message as a reply. Your LLM uses this tool when you need to respond directly to a specific message and maintain reply context.

**Try asking**:

- `Reply to that bug report thanking them for the details.`
- `Respond to Sarah's question in #support.`
- `Reply to the feature request with an acknowledgment.`
- `Answer that question about the API documentation.`

### search\_messages tool

The **search\_messages** tool searches recent messages within the Discord text channel or thread you specify. Your LLM uses this tool when you need to locate recent mentions of specific terms, topics, or phrases without retrieving all recent context.

**Try asking**:

- `Search for recent mentions of 'bug report' in #support.`
- `Did anyone mention the new feature in #general recently?`
- `Find messages about 'API keys' in #development.`
- `Search for discussions about the event in #planning.`

### list\_threads tool

The **list\_threads** tool retrieves active and archived threads within the Discord text channel you specify. Your LLM uses this tool when you need to discover threads before reading or posting messages.

**Try asking**:

- `What threads are active in #development?`
- `Show me the threads in #support.`
- `List all discussion threads in #feature-requests.`
- `What archived threads exist in #general?`

### create\_thread tool

The **create\_thread** tool creates a new thread in a Discord text channel from an existing message. Your LLM uses this tool when you need to move a discussion into a thread or start a thread from a specific message.

**Try asking**:

- `Create a thread from that feature request to discuss implementation.`
- `Start a thread from Josh's message about the bug.`
- `Make a discussion thread from that question.`
- `Create a thread to organize the conversation about the API changes.`

### get\_pinned\_messages tool

The **get\_pinned\_messages** tool retrieves a list of currently pinned messages in a Discord text channel. Your LLM uses this tool when you need to review or reference important or highlighted messages.

**Try asking**:

- `What messages are pinned in #announcements?`
- `Show me the pinned messages in #general.`
- `List the pinned content in #rules.`
- `What important messages are highlighted in #support?`

### pin\_message tool

The **pin\_message** tool pins or unpins a Discord message in a channel. Your LLM uses this tool when you need to pin or unpin important messages for visibility, such as announcements or solutions.

**Try asking**:

- `Pin the message with the meeting link.`
- `Pin that announcement about the server rules.`
- `Unpin the old event announcement.`
- `Highlight that helpful solution by pinning it.`

### delete\_message tool

The **delete\_message** tool deletes a Discord message. Your LLM uses this tool only when you explicitly instruct it to delete a specific message, such as spam or inappropriate content.

**Try asking**:

- `Delete that spam message.`
- `Remove the inappropriate content in #general.`
- `Delete the duplicate announcement.`
- `Remove that test message.`

### timeout\_member tool

The **timeout\_member** tool applies a temporary timeout (mute) to a Discord server member. Your LLM uses this tool when you explicitly ask to temporarily mute or timeout a member due to disruptive behavior.

**Try asking**:

- `Timeout that user for 10 minutes for spamming.`
- `Temporarily mute the member causing disruption.`
- `Apply a 1-hour timeout to that user.`
- `Mute that member for violating server rules.`

### get\_community\_context tool

The **get\_community\_context** tool retrieves basic community context information for a Discord server. Your LLM uses this tool when you need high-level community context such as server size or basic structure before selecting channels or deciding where to post messages.

**Try asking**:

- `What's the size of the Gaming Community server?`
- `Give me an overview of this Discord server.`
- `How many members are in the server?`
- `Show me the community context for this guild.`

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

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/docusign-esignature-mcp-server.md
description: >-
  Use the Docusign MCP server to connect your LLM to Docusign with tools to send
  agreements for signature, track progress, retrieve signed documents, and
  manage in-progress agreements through natural language.
---

# Docusign MCP server

The Docusign MCP server enables LLMs to manage the lifecycle of agreements sent for electronic signature within Docusign through natural conversation. It provides tools to create agreements from templates, send agreements for signature, track the progress of agreement documentation, and retrieve completed documents without requiring direct interaction with the Docusign interface.

## Uses

Use the Docusign MCP server to perform the following actions:

- List and search envelopes filtered by status, date range, sender, or recipient
- Retrieve summary details and status for a specific envelope
- Check recipient-level signing status to identify who has signed or is pending
- List documents attached to an envelope
- List available templates and retrieve template structure and required fields
- Create a draft envelope from a template
- Send a draft envelope to recipients for signature
- Cancel an in-progress envelope
- Resend signing notifications to remind recipients

### Example prompts

Use the following example prompts to invoke Docusign MCP server tools:

- `Show me all agreements awaiting signature.`
- `List envelopes sent to this recipient in the last 30 days.`
- `Get the status of this agreement.`
- `Who still needs to sign this envelope?`
- `List the documents attached to this envelope.`
- `What templates are available for sending agreements?`
- `Show me the required fields for this template.`
- `Create a draft agreement from the NDA template.`
- `Send this draft envelope to the recipients.`
- `Cancel this in-progress agreement.`
- `Remind the recipients who haven't signed yet.`

## Docusign MCP server tools

The Docusign MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_envelopes](#list-envelopes-tool) | Lists envelopes filtered by status, date range, sender, or recipient. |
| [get\_envelope](#get-envelope-tool) | Retrieves summary details and status for an envelope you specify. |
| [get\_envelope\_recipients](#get-envelope-recipients-tool) | Retrieves recipient-level signing status for an envelope. |
| [get\_envelope\_documents](#get-envelope-documents-tool) | Lists documents attached to an envelope. |
| [list\_templates](#list-templates-tool) | Lists available templates for agreement creation. |
| [get\_template](#get-template-tool) | Retrieves structure and required fields for a template. |
| [create\_envelope\_from\_template](#create-envelope-from-template-tool) | Creates a draft envelope using a selected template. |
| [send\_envelope](#send-envelope-tool) | Sends a draft envelope to recipients for signature. |
| [void\_envelope](#void-envelope-tool) | Cancels an in-progress envelope. |
| [resend\_envelope](#resend-envelope-tool) | Resends signing notifications for an envelope. |

## Install the Docusign MCP server

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
    

## Docusign connection setup

View Docusign connection setup steps

The Docusign connector supports the following authentication types:

- [JWT Grant](#jwt-token)
- [OAuth 2.0 (Authorization Code Grant)](#oauth-2-0)

> **AUTHENTICATION AND SENDING**
> 
> **JWT Grant** authentication uses the Docusign `impersonation` scope to send documents from the email address of the user you connect with, without requiring that user to sign in. The impersonated user, or their account admin, must grant consent before you can connect.
> 
> **OAuth 2.0** (Authorization Code Grant) sends all documents from the email address of the user who signs in to authorize the connection.

> **ROLES AND PERMISSIONS**
> 
> Users who can sign in to Docusign can connect it to Workato. Users have the same permissions and capabilities to view, manage, and send envelopes on Workato as in Docusign. Refer to the Docusign [Permission Profiles](https://support.docusign.com/en/guides/ndse-admin-guide-permission-sets) documentation for more information.

The Docusign connector works with the following Docusign plans:

- Personal
- Standard
- Business Pro

View JWT Grant authentication setup steps

Use JWT Grant authentication to connect to Docusign with a private key for server-to-server authentication. This method sends documents from the email address of the User ID you connect with, using the Docusign user impersonation. That user, or their account admin, must grant consent before you can connect. Refer to [Retrieve your User ID](#retrieve-your-user-id) for more information.

#### JWT Grant setup

Complete the following to set up JWT Grant authentication:

- [Retrieve your User ID](#retrieve-your-user-id)
- [Create an integration key](#create-an-integration-key)
- [Generate an RSA keypair](#generate-an-rsa-keypair)
- [Add the redirect URI](#add-the-redirect-uri)
- Optional: [Obtain consent for user impersonation](#obtain-consent-for-send-on-behalf-of)

##### Retrieve your User ID

View retrieve your User ID steps

Complete the following steps to retrieve your User ID in Docusign:

1. Sign in to Docusign.
   
2. Go to **Admin > Apps and Keys**.
   
3. Copy and save the **User ID** for use in Workato.
   

##### Generate an integration key

View generate an integration key steps

You must create an app to generate an integration key.

Complete the following steps to generate an integration key in Docusign:

1. Go to the **Apps and Keys** page and click **Add App and Integration Key**.
   
2. Enter a name for your application, such as `Workato Integration`.
   
3. Click **Create App**.
   
4. Copy and save the **Integration Key** (also known as the Client ID) for use in Workato.
   

##### Generate an RSA keypair

View generate an RSA keypair steps

Complete the following steps to generate an RSA keypair in Docusign:

1. Go to the **Service Integration** section in your newly created app settings.
   
2. Click **Generate RSA** to create a new RSA keypair.
   
3. Copy the **Private Key** and save it in a secure location. This value is required to establish the connection in Workato.
   
   > **SAVE YOUR PRIVATE KEY**
   > 
   > The private key is only displayed once. After you close this dialog, you won't be able to retrieve it again. If you lose it, you must generate a new keypair.
   
4. Click **Close** to save the keypair to your integration.
   

##### Add the redirect URI

View add the redirect URI steps

Complete the following steps to add the redirect URI in Docusign:

1. Go to the **Additional settings > Redirect URIs** section in your newly created app settings.
   
2. Click **\+ Add URI**.
   
3. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field.
   
4. Click **Save**.
   

##### Obtain consent for user impersonation

View obtain consent for user impersonation steps

JWT Grant authentication sends envelopes from the email address of the user you connect with, using Docusign's user impersonation. Connecting as that user requires consent, which comes in two forms:

- [Admin consent](#obtain-admin-consent) for the JWT app (one-time setup for the organization)
- [Individual user consent](#obtain-individual-user-consent) for the user you connect as

###### Obtain admin consent

View obtain admin consent steps

Use the Docusign Admin panel to grant consent to your JWT app on behalf of all users within your organization's claimed domains. This authorization grants app access to all domain users, with access limited by the permissions you specify. This is a one-time configuration.

> **PREREQUISITES FOR ADMIN CONSENT**
> 
> - Your organization must have the Docusign Admin feature enabled.
> - Your organization must have at least one claimed domain. Refer to the Docusign [Claim a domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256_1.html) documentation.
> - You must have created an [integration key](#create-an-integration-key) for your app.

Complete the following steps to obtain admin consent:

1. Sign in to Docusign as an organization administrator.
   
2. Open your [Organization](https://apps-d.docusign.com/admin/organization/) home page in Docusign Admin.
   
3. Select **Connected Apps** from the navigation pane.
   
4. Select **Authorize Application** and choose your application from the drop-down menu. This menu lists every integration key by name (for example, `Workato Integration`).
   
5. Enter `signature impersonation` in the **Permissions** field of the **Add New Application** dialog.
   
   These permissions apply to every user who's a member of the organization's claimed domains.
   
6. Click **Add** to confirm and authorize the application.
   

Refer to the Docusign [How to obtain admin consent for internal applications](https://developers.docusign.com/platform/auth/consent/obtaining-admin-consent-internal/) documentation for more information.

###### Obtain individual user consent

View obtain individual user consent steps

Each user you plan to connect as must grant individual consent to your JWT app. This allows the app to act on their behalf when sending envelopes.

> **INTEGRATION KEY AND REDIRECT URI**
> 
> Ensure you complete the [integration key](#create-an-integration-key) and [redirect URI](#add-the-redirect-uri) steps from the JWT Grant setup section before you set up individual consent.

Complete the following steps to obtain individual user consent:

**For administrators**

1. Construct the individual consent URL using the following format:
   
   **For production accounts:**
   
   ```
   https://account.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=YOUR_INTEGRATION_KEY&redirect_uri=https://www.workato.com/oauth/callback
   ```
   
   **For demo/sandbox accounts:**
   
   ```
   https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=YOUR_INTEGRATION_KEY&redirect_uri=https://www.workato.com/oauth/callback
   ```
   
   Replace `YOUR_INTEGRATION_KEY` with your integration key (Client ID).
   
2. Provide the consent URL to each user who needs to grant consent. Users can open this URL in their web browser.
   

**For users**

1. Open the consent URL provided by your administrator in a web browser.
   
2. Sign in to Docusign.
   
3. Review the consent screen and click **Accept** to grant consent. You won't be prompted again unless consent is revoked.
   

  

> **CONSENT DURING CONNECTION**
> 
> Docusign prompts you to grant consent when you [connect with JWT Grant authentication](#jwt-token). This grants individual consent for the user who authenticates the connection. You only need to follow the steps above to pre-authorize consent for users who won't personally set up the connection, for example, so an admin can grant consent ahead of time for another user's connection.

Refer to the Docusign [How to obtain individual consent](https://developers.docusign.com/platform/auth/consent/obtaining-individual-consent/) documentation for more information.

#### Connect to Docusign with JWT Grant authentication

View connect to Docusign with JWT Grant authentication steps

Complete the following steps to set up a JWT Grant connection to Docusign in Workato:

1. Click **Create > Connection**.
   
2. Search for `Docusign` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Docusign JWT Grant connection](/assets/jwt-grant-connection.D5bvWRRz.png)_Docusign JWT Grant connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Auth type** drop-down menu to select **JWT Grant**.
   
6. Use the **Demo** drop-down menu to indicate if this is a demo Docusign account. Select **Yes** for demo/sandbox accounts or **No** for production accounts.
   
7. Enter the [integration key](#create-an-integration-key) from your Docusign application in the **Client ID** field.
   
8. Enter the [User ID](#retrieve-your-user-id) from the [JWT Grant setup](#jwt-token-setup) steps in the **User ID** field.
   
9. Enter the [RSA private key](#generate-an-rsa-keypair) from the [JWT Grant setup](#jwt-token-setup) steps in the **Private key** field. Enter the complete private key including the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----` headers.
   
10. Optional. Enter the **Account ID** to specify a Docusign account when you have multiple accounts. You can find the account ID by navigating to **Admin > Apps and Keys > API Account ID**. The connection selects your first Docusign account by default.
    
11. Optional. Enter the Connect key in the **Connect key** field to validate your webhook requests. Refer to the Docusign [Add HMAC keys for your app](https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/) documentation for more information.
    
12. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
13. Click **Connect**. Workato redirects you to Docusign to authorize the connection.
    
14. Click **Allow Access** to grant the Workato integration permission to access your account.
    
    ![JWT consent screen](/assets/jwt-consent.C2zP7euJ.png)_JWT consent screen_
    

View OAuth 2.0 (Authorization Code Grant) setup steps

### OAuth 2.0 (Authorization Code Grant)

Use OAuth 2.0 (Authorization Code Grant) to connect to Docusign by signing in and granting access through Docusign's authorization flow. All documents are sent from the email address of the user who authorized the connection.

#### Connect to Docusign with OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 authentication connection to Docusign in Workato:

1. Click **Create > Connection**.
   
2. Search for `Docusign` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Docusign OAuth 2.0 (Authorization Code Grant) connection](/assets/oauth-2.NAxc7mKJ.png)_Docusign OAuth 2.0 (Authorization Code Grant) connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Demo** drop-down menu to indicate if this is a demo Docusign account. Select **Yes** for demo/sandbox accounts or **No** for production accounts.
   
7. Optional. Enter the **Account ID** to specify a Docusign account when you have multiple accounts. You can find the account ID by navigating to **Admin > Apps and Keys > API Account ID**. The connection selects your first Docusign account by default.
   
8. Optional. Enter the Connect key in the **Connect key** field to validate your webhook requests. Refer to the Docusign [Add HMAC keys for your app](https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/) documentation for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

## How to use Docusign MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_envelopes tool

The **list\_envelopes** tool lists envelopes filtered by status, date range, sender, or recipient. Your LLM uses this tool to search and surface agreements matching the criteria you provide.

**Try asking**:

- `Show me all agreements awaiting signature.`
- `List envelopes sent to this recipient in the last 30 days.`
- `Show me completed agreements from this month.`
- `Find envelopes sent by this team member.`

### get\_envelope tool

The **get\_envelope** tool retrieves summary details and status for an envelope you specify. Your LLM uses this tool to return its current state, sent date, and recipient summary.

**Try asking**:

- `Get the status of this agreement.`
- `Show me the details for this envelope.`
- `What's the current state of this agreement?`
- `Pull up the summary for this envelope.`

### get\_envelope\_recipients tool

The **get\_envelope\_recipients** tool retrieves recipient-level signing status for an envelope. Your LLM uses this tool to return each recipient's current status, identifying who has signed and who is still pending.

**Try asking**:

- `Who still needs to sign this envelope?`
- `Show me the signing status for each recipient on this agreement.`
- `Which recipients have completed signing?`
- `Who is holding up this agreement?`

### get\_envelope\_documents tool

The **get\_envelope\_documents** tool lists documents attached to an envelope. Your LLM uses this tool to return available documents.

**Try asking**:

- `List the documents attached to this envelope.`
- `What documents are included in this agreement?`
- `Show me the files associated with this envelope.`
- `What documents are available for this completed agreement?`

### list\_templates tool

The **list\_templates** tool lists available templates for agreement creation. Your LLM uses this tool to match template references and help select the right starting point before creating an envelope.

**Try asking**:

- `What templates are available for sending agreements?`
- `Show me all Docusign templates I can use.`
- `Find a template for an NDA.`
- `List available templates before I create a new agreement.`

### get\_template tool

The **get\_template** tool retrieves the structure and required fields for a template. Your LLM uses this to provide required roles and fields before creating an envelope from the template.

**Try asking**:

- `Show me the required fields for this template.`
- `What roles and fields does the NDA template require?`
- `Get the structure of this template before I create an agreement.`
- `What information do I need to fill in for this template?`

### create\_envelope\_from\_template tool

The **create\_envelope\_from\_template** tool creates a draft envelope using a template you select. Your LLM uses this tool to apply the template structure and the recipient and field information you provide to build the draft before sending.

**Try asking**:

- `Create a draft agreement from the NDA template.`
- `Set up a new envelope using the MSA template for this recipient.`
- `Draft an agreement from this template with these signer details.`
- `Create an envelope from the SOW template before I send it.`

### send\_envelope tool

The **send\_envelope** tool sends a draft envelope to recipients for signature. Your LLM uses this tool to send an envelope to the recipients you specify.

**Try asking**:

- `Send this draft envelope to the recipients.`
- `Deliver this agreement for signature.`
- `Send the NDA I just created to this contact.`
- `Dispatch this envelope now that it's ready.`

### void\_envelope tool

The **void\_envelope** tool cancels an in-progress envelope. The tool uses the envelope ID to stop the agreement and notify recipients that it has been voided. This tool is only used when you explicitly ask to cancel or stop an agreement.

**Try asking**:

- `Cancel this in-progress agreement.`
- `Void this envelope — we're using a different version.`
- `Stop this agreement from being signed.`
- `Cancel and void this envelope.`

### resend\_envelope tool

The **resend\_envelope** tool resends signing notifications for an envelope. Your LLM uses this tool to re-notify recipients who haven't completed signing.

**Try asking**:

- `Remind the recipients who haven't signed yet.`
- `Resend the signing notification for this envelope.`
- `Send a reminder to the pending signers on this agreement.`
- `Nudge the recipients who are holding up this agreement.`

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
