---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/outlook-email-mcp-server.md'
description: >-
  Use the Outlook Email MCP server to let LLMs read, draft, send, and organize
  Microsoft Outlook email and manage attachments by chat.
---

# Outlook Email MCP server

The Outlook Email MCP server enables LLMs to read, organize, draft, and send email through Microsoft Outlook (Exchange Online) through natural conversation. It provides tools to find and review conversations, summarize email content, draft and send messages, organize your inbox with folders and categories, and manage attachments without requiring direct interaction with the Outlook Email interface.

## Uses

Use the Outlook Email MCP server to perform the following actions:

- Search for conversations with specific people, customers, or groups
- Find ongoing or historical discussions about topics or projects
- Read and review complete email threads and individual messages
- Compose, draft, and send new emails or replies
- Manage attachments including viewing and retrieving files
- Organize inbox with folders, categories, and flags
- Mark messages as read or unread for inbox management
- Move messages to specific folders for organization
- List and manage email drafts
- Add or remove attachments from drafts

### Example prompts

Use the following example prompts to invoke Outlook Email MCP server tools:

- `Find all email conversations with Acme Corp from the last month.`
- `Show me the conversation about the Q4 product launch.`
- `Draft a follow-up email to Mei about the meeting yesterday.`
- `What attachments were included in the contract email?`
- `Send the draft email I created earlier.`
- `Move all emails from this project to the Archive folder.`
- `Mark all unread messages from this week as read.`
- `Star the email from Josh about the budget approval.`

## Outlook Email MCP server tools

The Outlook Email MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_conversations](#search-conversations-tool) | Searches for email conversations matching criteria you specify and returns conversation identifiers with summary metadata. |
| [search\_messages](#search-messages-tool) | Searches for individual email messages matching criteria you specify and returns message identifiers with summary metadata. |
| [list\_folders](#list-folders-tool) | Retrieves the list of mail folders available in the authenticated user's mailbox. |
| [get\_conversation](#get-conversation-tool) | Retrieves all messages in a conversation identified by `conversationId`, ordered chronologically. |
| [get\_message](#get-message-tool) | Retrieves the complete contents of a single email message. |
| [list\_attachments](#list-attachments-tool) | Retrieves the list of attachments associated with a specific email message. |
| [get\_attachment](#get-attachment-tool) | Retrieves the raw payload of a specific file attachment from an email message. |
| [create\_draft](#create-draft-tool) | Creates a new email draft in the user's Drafts folder. |
| [list\_drafts](#list-drafts-tool) | Retrieves a list of email drafts with summary metadata. |
| [get\_draft](#get-draft-tool) | Retrieves the complete contents of an existing email draft. |
| [update\_draft](#update-draft-tool) | Updates the body, subject, or recipients of an existing email draft. |
| [send\_draft](#send-draft-tool) | Sends an existing email draft on behalf of the authenticated user. |
| [add\_attachments](#add-attachments-tool) | Adds one or more file or OneDrive reference attachments to an existing email draft. |
| [remove\_attachments](#remove-attachments-tool) | Removes one or more attachments from an existing email draft. |
| [mark\_message\_read\_state](#mark-message-read-state-tool) | Marks one or more email messages as read or unread. |
| [move\_to\_folder](#move-to-folder-tool) | Moves one or more email messages to a mail folder you specify. |
| [update\_categories](#update-categories-tool) | Adds or removes categories from email messages. |
| [update\_star\_state](#update-star-state-tool) | Sets or clears the star (follow-up flag) on one or more email messages. |

## Install the Outlook Email MCP server

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
    

## Outlook Email connection setup

View Outlook Email connection setup steps

The Outlook connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials): _Only available for tenant-specific connections_

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

### Authorization code grant authentication (OAuth 2.0)

View authorization code grant authentication steps

This authentication method requires the following value for tenant-specific account types:

- Tenant ID/Domain

#### Minimum and default scopes

View minimum and default scopes

The connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Mail.Send`
- `Mail.ReadWrite`
- `Mail.ReadWrite.Shared`
- `Calendars.ReadWrite`
- `Calendars.ReadWrite.Shared`
- `User.Read`
- `offline_access`

The following minimum scopes are required to establish a connection to using authorization code grant authentication:

- `User.Read`
- `offline_access`

#### Outlook setup for authorization code grant authentication

Complete the following steps to set up Outlook for authorization code grant authentication:

- [Register the Workato App in Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

#### Register the Workato app in the Azure portal

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

This step is required if you plan to use a tenant-specific account. You can skip this step if you plan to use a common, consumer, or organization account type for your connection.

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Outlook with authorization code grant authentication

View connect to Outlook with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Outlook in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Outlook` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common**, **Tenant-specific**, **Consumer**, and **Organization**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that are not restricted to a specific organization (tenant).
   
   ![Common connection](/assets/connect-common.n5OKFNtM.png)_Common connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant.Te-J1c-V.png)_Tenant specific connections_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID) or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Register the Workato app in the Azure portal](#auth-register) for more information.
   
   **Consumer**
   
   - **Consumer**: This option supports personal Microsoft accounts.
   
   ![Consumer connection](/assets/connect-consumer.DM8X7YiA.png)_Consumer connections_
   
   **Organization**
   
   - **Organization**: This option supports work or school accounts.
   
   ![Organization connection](/assets/connect-organization.BB6uVVjE.png)_Organization connections_
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Outlook custom OAuth](/en/connectors/outlook/custom-oauth) for more information.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

View client credentials-based authentication steps

This method requires the following fields:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Minimum and default scopes

View minimum and default scopes

We recommend the following scopes for client credentials connections. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Application** permissions in the Azure portal.

- `Calendars.Read`
- `Calendars.ReadWrite`
- `Contacts.Read`
- `Contacts.ReadWrite`
- `Mail.Read`
- `Mail.ReadWrite`
- `Mail.Send`

The following minimum scopes are required to establish a connection to with client credentials-based authentication:

- `Mail.Read`

#### Outlook setup for client credentials-based authentication

Complete the following steps to set up Outlook for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

##### Register the Workato app in the Azure portal

View Register the Workato app in the Azure portal steps

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

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
   

#### Connect to Outlook with client credentials-based authentication

View connect to Outlook with client credential-based authentication steps

Complete the following steps to set up a client credentials-based connection to Outlook in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Outlook` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Client credentials connection](/assets/client-credentials-connection.BNf4ndnr.png)_Client credentials connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
6. Provide your **Tenant ID/Domain**. This is the **Directory (tenant) ID** for your app. Refer to [Register an app in Azure](/en/connectors/outlook/outlook#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Register an app in Azure](/en/connectors/outlook/outlook#client-credentials-register) for more information.
   
9. Click **Sign in with Microsoft**.
   

## How to use Outlook Email MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_conversations tool

The **search\_conversations** tool searches for email conversations matching criteria you specify and returns conversation identifiers with summary metadata. Your LLM uses this tool to find conversations with specific people, locate ongoing or historical discussions about topics, identify active deal or project-related email threads, or narrow the search space before retrieving full conversation content.

**Try asking**:

- `Find all email conversations with Acme Corp from the last month.`
- `Search for conversations about the API migration project.`
- `Show me email threads with Jade Anderson that mention 'budget approval'.`
- `Find all ongoing discussions about the product launch.`

### search\_messages tool

The **search\_messages** tool searches for individual email messages matching criteria you specify and returns message identifiers with summary metadata. Your LLM uses this tool to find a specific email you sent or received, locate a message with a known subject or phrase, or identify a particular inbound or outbound message.

**Try asking**:

- `Find the email I sent to Josh yesterday about the contract.`
- `Search for messages with 'invoice' in the subject line.`
- `Locate the message from legal@acme.com about terms of service.`
- `Find the email I received from Mei with the meeting notes.`

### list\_folders tool

The **list\_folders** tool retrieves the list of mail folders available in your mailbox. Your LLM uses this tool when you refer to folders by name and available folders are unknown, when validating folder existence before moving messages, or when listing available folders for organization.

**Try asking**:

- `What folders do I have in my Outlook mailbox?`
- `Show me all my email folders.`
- `List the folders I use for project organization.`
- `What archive folders are available?`

### get\_conversation tool

The **get\_conversation** tool retrieves all messages in a conversation identified by `conversationId`, ordered chronologically. Your LLM uses this tool when complete conversation context is required, when you ask to review or summarize an email thread, or when preparing replies, follow-ups, or handoffs.

**Try asking**:

- `Show me the full conversation thread with Acme Corp.`
- `Read the entire email thread about the Q4 planning.`
- `Get the complete discussion from the contract negotiation emails.`
- `Review all messages in the thread with Marco about the budget.`

### get\_message tool

The **get\_message** tool retrieves the complete contents of a single email message. Your LLM uses this tool when a message has been identified through search and complete contents are required, or when message-level precision is needed.

**Try asking**:

- `Read the email from Jade sent on January 15th.`
- `Show me the complete message about the contract terms.`
- `Get the full contents of the meeting invitation from Mei.`
- `Read the message with the project timeline attachment.`

### list\_attachments tool

The **list\_attachments** tool retrieves the list of attachments associated with a specific email message, including OneDrive reference attachments. Your LLM uses this tool when you ask what files were attached to an email, when referencing or including existing attachments in a reply, or when preparing to retrieve an attachment payload.

**Try asking**:

- `What files were attached to the email from legal@acme.com?`
- `List the attachments in Marco's message about the proposal.`
- `Show me what documents were included in the contract email.`
- `What attachments did Josh send in the project update?`

### get\_attachment tool

The **get\_attachment** tool retrieves the raw payload of a specific file attachment from an email message. Your LLM uses this tool to download, forward, or re-attach a file.

**Try asking**:

- `Download the PDF attachment from the contract email.`
- `Get the spreadsheet that Jade attached to her message.`
- `Retrieve the presentation file from Alex's email.`
- `Download the proposal document from the legal team's message.`

### create\_draft tool

The **create\_draft** tool creates a new email draft in your Drafts folder. Your LLM uses this tool to create a draft email when you ask to write an email that may be sent now or later. **Try asking**:

- `Draft an email to Mei about tomorrow's meeting.`
- `Create a reply to Josh's message thanking them for the update.`
- `Write a follow-up email to Acme Corp about the proposal.`
- `Start a new email to the team about the project timeline.`

### list\_drafts tool

The **list\_drafts** tool retrieves a list of email drafts in your Drafts folder with summary metadata. Your LLM uses this tool when you refer to an existing draft but don't provide a draft ID, or when you ask to view, list, or select from your drafts.

**Try asking**:

- `Show me my email drafts.`
- `List all draft emails I've been working on.`
- `What drafts do I have saved?`
- `Display my unsent emails.`

### get\_draft tool

The **get\_draft** tool retrieves the complete contents of an existing email draft. Your LLM uses this tool to review, see, or confirm the current contents of a draft.

**Try asking**:

- `Show me the draft email I created earlier.`
- `Review my draft reply to Alex.`
- `What does my current draft say?`
- `Read the draft I started for the team update.`

### update\_draft tool

The **update\_draft** tool updates the body, subject, or recipients of an existing email draft. Your LLM uses this tool to change, revise, or edit an existing draft.

**Try asking**:

- `Update the draft to include the budget numbers.`
- `Revise the email draft to mention the deadline change.`
- `Edit the draft to add Marco as a CC recipient.`
- `Change the subject line of my draft email.`

### send\_draft tool

The **send\_draft** tool sends an existing email draft on your behalf. Your LLM uses this tool to send the email when a draft has been created or explicitly referenced earlier in the current conversation.

**Try asking**:

- `Send the draft email I just created.`
- `Send my reply to Sarah now.`
- `Go ahead and send that follow-up email.`
- `Send the draft about the project update.`

### add\_attachments tool

The **add\_attachments** tool adds one or more file or OneDrive reference attachments to an existing email draft. Your LLM uses this tool to attach files to an existing draft, or when attachments must be added before sending.

**Try asking**:

- `Add the roadmap.pdf file to my email draft.`
- `Attach the proposal presentation to this draft.`
- `Include the sales team spreadsheet as an attachment.`
- `Add the Q4 report to the draft email.`

### remove\_attachments tool

The **remove\_attachments** tool removes one or more attachments from an existing email draft. Your LLM uses this tool to remove, delete, or replace attachments on an existing draft, or when an attachment must be removed before sending.

**Try asking**:

- `Remove the roadmap.pdf from my email draft.`
- `Delete the proposal presentation attachment from this draft.`
- `Don't include the sales team spreadsheet.`
- `Remove all attachments from the draft email.`

### mark\_message\_read\_state tool

The **mark\_message\_read\_state** tool marks one or more email messages as read or unread. Your LLM uses this tool to mark messages as read or unread, or when to perform inbox triage actions.

**Try asking**:

- `Mark all messages from today as read.`
- `Set the unread email from Alex to read.`
- `Mark the contract email as unread so I don't forget to review it.`
- `Mark all emails in this thread as read.`

### move\_to\_folder tool

The **move\_to\_folder** tool moves one or more email messages to a mail folder you specify. Your LLM uses this tool to move, file, or organize messages into a folder you specify.

**Try asking**:

- `Move all emails from this project to the Archive folder.`
- `File the contract emails in the Legal folder.`
- `Move these messages to my Completed Projects folder.`
- `Organize the Q4 planning emails into the Planning folder.`

### update\_categories tool

The **update\_categories** tool adds or removes categories from email messages. Your LLM uses this tool to tag, categorize, reclassify, or remove categories from messages.

**Try asking**:

- `Add the 'Important' category to this email.`
- `Tag these messages with 'Project Alpha'.`
- `Remove the 'Follow-up' category from this thread.`
- `Categorize the contract emails as 'Legal Review'.`

### update\_star\_state tool

The **update\_star\_state** tool sets or clears the star (follow-up flag) on one or more email messages. Your LLM uses this tool to star, flag, mark for follow-up, unstar, or unflag messages.

**Try asking**:

- `Star the email from Mei about the budget approval.`
- `Flag the message with the contract attachment for follow-up.`
- `Unstar the email from Sarah now that I've reviewed it.`
- `Remove the flag from the completed action items.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/outreach-sales-engagement-mcp-server.md
description: >-
  Use the Outreach MCP server to connect your LLM to Outreach with tools to
  manage sequences, prospects, accounts, calls, tasks, and enrollment through
  natural language.
---

# Outreach Sales Engagement MCP server

The Outreach Sales Engagement MCP server enables LLMs to manage sales engagement data in Outreach through natural conversation. It provides tools to discover and build sequences, manage prospects and accounts, review activity, and execute enrollment operations without requiring direct interaction with the Outreach interface.

## Uses

Use the Outreach Sales Engagement MCP server to perform the following actions:

- List and search sequences with filters for status, owner, and name
- Retrieve sequence steps and structure
- Create new sequences and add steps
- Search for prospects by name, email, account, or owner
- Get detailed prospect information
- Search accounts by name or domain
- Review calls and tasks with date and type filters
- Update prospect stage, owner, or tags
- Log manual call records
- Enroll prospects in sequences
- Pause or resume sequence enrollments

### Example prompts

- `Show me all active sequences owned by Mei.`
- `Get the steps for the Q1 Enterprise sequence.`
- `Create a new outbound sequence for product demos.`
- `Find prospects at Acme Corp.`
- `Show me today's calls and tasks.`
- `Update Josh's stage to Working.`
- `Log a call with this prospect - left voicemail.`
- `Enroll Jade Anderson in the Q1 Enterprise sequence.`
- `Pause the enrollment for this prospect.`
- `Search for accounts in the technology industry.`

## Outreach Sales Engagement MCP server tools

The Outreach Sales Engagement MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_sequences](#list-sequences-tool) | Lists Outreach sequences with optional filters for status, owner, and name. |
| [get\_sequence\_steps](#get-sequence-steps-tool) | Retrieves the ordered steps for an Outreach sequence you specify. |
| [create\_sequence](#create-sequence-tool) | Creates a new Outreach sequence in draft status. |
| [create\_sequence\_step](#create-sequence-step-tool) | Adds a new step to an existing Outreach sequence. |
| [search\_prospects](#search-prospects-tool) | Searches Outreach prospects by name, email, account, or owner. |
| [get\_prospect](#get-prospect-tool) | Retrieves full details for a single Outreach prospect by ID. |
| [search\_accounts](#search-accounts-tool) | Searches Outreach accounts by name or domain. |
| [list\_calls\_and\_tasks](#list-calls-and-tasks-tool) | Lists Outreach calls and tasks with filters for date, type, prospect, or account. |
| [update\_prospect](#update-prospect-tool) | Updates stage, owner, or tags on an Outreach prospect record. |
| [log\_call](#log-call-tool) | Logs a manual outbound call record against an Outreach prospect. |
| [enroll\_prospect](#enroll-prospect-tool) | Enrolls a single prospect in an active Outreach sequence. |
| [manage\_enrollment](#manage-enrollment-tool) | Pauses or resumes a prospect's active sequence enrollment. |

## Install the Outreach Sales Engagement MCP server

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
    

## Outreach connection setup

View Outreach connection setup steps

The Outreach connector uses OAuth 2.0 authentication.

Complete the following steps to connect to Outreach in Workato:

1. Click **Create > Connection**.
   
2. Search for `Outreach` and select it as your app.
   
3. Enter a name for your connection in the **Connection** name field.
   
   ![Set up your Outreach connection](/assets/outreach-connection.DTG1YHXV.png)_Set up your Outreach connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand the **Advanced settings** section to configure **Requested permissions (OAuth scopes)** for your connection.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
   > **OAUTH PRIVILEGES**
   > 
   > The Outreach connection inherits permissions from the user who authenticates it. Workato recommends that you create an integration user for Workato on the Outreach platform. This prevents the connection from being tied to a physical user.
   
7. Click **Connect**.
   
8. Sign in to your Outreach account.
   

## How to use Outreach Sales Engagement MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_sequences tool

The **list\_sequences** tool lists Outreach sequences with optional filters for status, owner, and name. Your LLM uses this tool to view available sequences, find a specific sequence by name or owner, or review sequences by status.

**Try asking**:

- `Show me all active sequences.`
- `List sequences owned by Alex.`
- `Find the Q1 Enterprise sequence.`
- `What sequences are in draft status?`

### get\_sequence\_steps tool

The **get\_sequence\_steps** tool retrieves the ordered steps for an Outreach sequence you specify. Your LLM uses this tool to view the structure of a sequence, review what steps are configured, or understand the sequence flow before enrolling prospects.

**Try asking**:

- `Get the steps for the Q1 Enterprise sequence.`
- `Show me what's in the outbound prospecting sequence.`
- `What steps are configured in this sequence?`
- `Review the structure of the product demo sequence.`

### create\_sequence tool

The **create\_sequence** tool creates a new Outreach sequence in draft status. Your LLM uses this tool to create a new sequence with a name and optional description. New sequences are created in draft status and can't send emails until activated in the Outreach UI.

**Try asking**:

- `Create a new sequence called 'Q2 Enterprise Outbound'.`
- `Set up a sequence for product demo follow-ups.`
- `Create an outbound sequence for the new product launch.`
- `Make a new sequence for warm leads.`

### create\_sequence\_step tool

The **create\_sequence\_step** tool adds a new step to an existing Outreach sequence. Your LLM uses this tool to add email steps, call tasks, or other actions to a sequence you're building.

**Try asking**:

- `Add an email step to the Q1 Enterprise sequence.`
- `Create a call task as the next step in this sequence.`
- `Add a follow-up email to the demo sequence.`
- `Insert a LinkedIn task in this sequence.`

### search\_prospects tool

The **search\_prospects** tool searches Outreach prospects by name, email, account, or owner. Your LLM uses this tool to find prospects matching specific criteria, locate a prospect by email or name, or see all prospects in an account.

**Try asking**:

- `Find prospects at Acme Corp.`
- `Search for John Smith in Outreach.`
- `Show me prospects owned by Mei.`
- `Find the prospect with email josh@acme.com.`

### get\_prospect tool

The **get\_prospect** tool retrieves full details for a single Outreach prospect by ID. Your LLM uses this tool to find complete information about a prospect already identified from search results, or when you need to review prospect details before updating or enrolling.

**Try asking**:

- `Get the full details for this prospect.`
- `Show me complete information about prospect ID 12345.`
- `What's the current status of Jade Anderson?`
- `Review the details for this prospect before enrolling.`

### search\_accounts tool

The **search\_accounts** tool searches Outreach accounts by name or domain. Your LLM uses this tool to find accounts by company name, locate accounts by domain, or discover accounts matching search criteria.

**Try asking**:

- `Search for Acme Corp account.`
- `Find accounts with domain acme.com.`
- `Look for technology companies in our accounts.`
- `Search for accounts matching 'Enterprise'.`

### list\_calls\_and\_tasks tool

The **list\_calls\_and\_tasks** tool lists Outreach calls and tasks with filters for date, type, prospect, or account. Your LLM uses this tool to review outreach activity, view today's calls or tasks, check incomplete tasks for an account, or review call history for a prospect.

**Try asking**:

- `Show me today's calls.`
- `What tasks are incomplete for Acme Corp?`
- `List calls for this prospect this week.`
- `Show me all my tasks due tomorrow.`

### update\_prospect tool

The **update\_prospect** tool updates stage, owner, or tags on an Outreach prospect record. Your LLM uses this tool to change a prospect's stage, reassign a prospect to another owner, or update prospect tags.

**Try asking**:

- `Update Macro's stage to Working.`
- `Reassign this prospect to Sarah.`
- `Tag this prospect as hot-lead.`
- `Change the prospect stage to Qualified.`

### log\_call tool

The **log\_call** tool logs a manual outbound call record against an Outreach prospect. Your LLM uses this tool to record a call you made, document call outcomes, or track call activity.

**Try asking**:

- `Log that I called Jade Anderson and left a voicemail.`
- `Record a completed call with this prospect.`
- `Log a call - had a good conversation about pricing.`
- `Record that I spoke with the prospect about the demo.`

### enroll\_prospect tool

The **enroll\_prospect** tool enrolls a single prospect in an active Outreach sequence. Your LLM uses this tool to start a prospect on a sequence or add a prospect to an outbound campaign.

**Try asking**:

- `Enroll Josh in the Q1 Enterprise sequence.`
- `Add this prospect to my outbound sequence.`
- `Start Alex on the product demo sequence.`
- `Enroll this prospect in the warm lead follow-up sequence.`

### manage\_enrollment tool

The **manage\_enrollment** tool pauses or resumes a prospect's active sequence enrollment. Your LLM uses this tool to pause a prospect's sequence enrollment temporarily or resume outreach after a pause.

**Try asking**:

- `Pause Mei's enrollment in the sequence.`
- `Resume outreach to this prospect.`
- `Hold off on the Acme Corp sequence for now.`
- `Resume the sequence for Marco.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/quickbooks-online-ap-and-expenses-mcp-server.md
description: >-
  Use the QuickBooks Online AP and Expenses MCP server to connect your LLM to
  QuickBooks Online with tools to list, review, and record expenses, and look up
  vendors and accounts through natural language.
---

# QuickBooks Online AP and Expenses MCP server

The QuickBooks Online AP and Expenses MCP server enables LLMs to work with QuickBooks Online expense workflows through natural conversation. This MCP server supports accounts payable and expense workflows. It helps you track spending, analyze how money flows, and record transactions with accurate classification. It provides tools to list expenses, retrieve expense details, and record new expenses without interacting directly with the QuickBooks Online interface.

## Uses

Use the QuickBooks Online AP and Expenses MCP server to perform the following actions:

- List expense transactions with optional filters such as date range and account
- Retrieve detailed information for a specific expense transaction
- Record a new expense transaction using vendor and account references
- Search for vendors by name or partial identifier
- Retrieve full details for a specific vendor
- Search for accounts (categories) by name or partial identifier
- Retrieve full details for a specific account

### Example prompts

Use the following example prompts to invoke QuickBooks Online AP and Expenses MCP server tools:

- `Show me all expenses from the past 30 days.`
- `List expenses charged to the Travel account this quarter.`
- `Get the details for this expense transaction.`
- `Record a $250 expense from Office Depot for office supplies.`
- `Find the vendor record for Staples.`
- `Look up the Office Supplies account before I log this expense.`
- `Get the full details for this vendor.`
- `Retrieve the details for this account category.`

## QuickBooks Online AP and Expenses MCP server tools

The QuickBooks Online AP and Expenses MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_expenses](#list-expenses-tool) | Retrieves a list of expense transactions with optional filters, such as date range and account. |
| [get\_expense](#get-expense-tool) | Retrieves detailed information for an expense transaction you specify. |
| [record\_expense](#record-expense-tool) | Creates a new expense transaction using vendor and account references. |
| [search\_vendors](#search-vendors-tool) | Searches for vendors using a name or partial identifier. |
| [get\_vendor](#get-vendor-tool) | Retrieves full details for a vendor you specify. |
| [search\_accounts](#search-accounts-tool) | Searches for accounts or categories using a name or partial identifier. |
| [get\_account](#get-account-tool) | Retrieves full details for an account you specify. |

## Install the QuickBooks Online AP and Expenses MCP server

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
    

### QuickBooks Online connection setup

View QuickBooks Online connection setup steps

### Supported editions and versions

View Supported editions and versions

The QuickBooks connector works with the following QuickBooks Online versions:

- QuickBooks Self-Employed
- QuickBooks Simple Start
- QuickBooks Essentials
- QuickBooks Plus

Workato doesn't support QuickBooks Desktop/Enterprise versions.

### How to connect to QuickBooks on Workato

View How to connect to QuickBooks on Workato steps

Complete the following steps to establish a connection to QuickBooks Online in Workato:

1. Provide a **Connection name** that identifies which QuickBooks instance Workato is connected to.
   
   ![QuickBooks online connection](/assets/QBO_connect1.D_Fk-JGJ.png)_QuickBooks online connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Sandbox** drop-down menu to specify whether the QuickBooks Online account is a sandbox account.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
5. Click **Connect to QuickBooks** to open the QuickBooks sign in window.
   
   ![Connect to QuickBooks Online](/assets/QBO_connect2.DOeG2fRE.png)_Connect to QuickBooks Online_
   
6. Enter your QuickBooks Online account email address and password.
   
7. Click **Sign in** to complete the connection.
   

## How to use QuickBooks Online AP and Expenses MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_expenses tool

The **list\_expenses** tool retrieves a list of expense transactions with optional filters, such as date range and account. Your LLM uses this tool to view, list, or review expenses, including requests for recent expenses or expenses within a specific date range.

**Try asking**:

- `Show me all expenses from the past 30 days.`
- `List expenses charged to the Travel account this quarter.`
- `What have we spent in the last week?`
- `Show me all expenses from last month.`

### get\_expense tool

The **get\_expense** tool retrieves detailed information for an expense transaction you specify. Your LLM uses this tool to retrieve details for a expense.

**Try asking**:

- `Get the details for this expense transaction.`
- `Show me the full breakdown for this expense.`
- `What vendor and account is this expense recorded under?`
- `Pull up the details for the expense I logged yesterday.`

### record\_expense tool

The **record\_expense** tool creates a new expense transaction using vendor and account references. Your LLM resolves these references and prompts for any missing details before it records the expense.

**Try asking**:

- `Record a $250 expense from Office Depot for office supplies.`
- `Log a travel expense from last week.`
- `Record a software subscription charge under the Software account.`
- `Add this receipt as an expense transaction.`

### search\_vendors tool

The **search\_vendors** tool searches for vendors using a name or partial identifier. Your LLM uses this tool to find a vendor reference for an expense workflow when you provide a name or partial identifier.

**Try asking**:

- `Find the vendor record for Staples.`
- `Search for a vendor named Office Depot.`
- `Look up this vendor before I record the expense.`
- `Find all vendors matching this partial name.`

### get\_vendor tool

The **get\_vendor** tool retrieves full details for a vendor you specify. Your LLM uses this tool to search by vendor ID to obtain complete vendor details for an expense workflow.

**Try asking**:

- `Get the full details for this vendor.`
- `Show me all information for this vendor record.`
- `Retrieve the payment details for this vendor.`
- `Pull up the full profile for this vendor.`

### search\_accounts tool

The **search\_accounts** tool searches for accounts or categories using a name or partial identifier. Your LLM uses this tool to provide an account or category reference for expense classification.

**Try asking**:

- `Look up the Office Supplies account before I log this expense.`
- `Search for the Travel and Entertainment account.`
- `Find the right expense category for this transaction.`
- `What accounts are available for classifying this expense?`

### get\_account tool

The **get\_account** tool retrieves full details for an account you specify. Your LLM uses this tool to search by account ID to obtain complete account details for expense classification.

**Try asking**:

- `Retrieve the details for this account category.`
- `Show me the full details for the Travel account.`
- `Get the account information before I classify this expense.`
- `Pull up the details for this expense account.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/quickbooks-online-billing-and-ar-mcp-server.md
description: >-
  Use the QuickBooks Online Billing and AR MCP server to connect your LLM to
  QuickBooks Online with tools to list, review, create, and send invoices, and
  look up customers and items through natural language.
---

# QuickBooks Online Billing and AR MCP server

The QuickBooks Online Billing and AR MCP server enables LLMs to manage QuickBooks Online billing workflows through natural conversation. This MCP server supports accounts receivable workflows so you can track billed amounts, review outstanding invoices, and generate and send invoices. It provides tools to list invoices, retrieve invoice details, and create and send invoices without requiring direct interaction with the QuickBooks Online interface.

## Uses

Use the QuickBooks Online Billing and AR MCP server to perform the following actions:

- List invoices with optional filters such as date range and customer
- Retrieve detailed information for a specific invoice, including line items, totals, and payment status
- Create a new invoice for an existing customer using specified items and pricing
- Send an existing invoice to the associated customer
- Search for customers by name or partial identifier
- Search for items (products or services) by name or partial identifier
- Retrieve full details for a specific customer
- Retrieve full details for a specific item

### Example prompts

Use the following example prompts to invoke QuickBooks Online Billing and AR MCP server tools:

- `Show me all invoices from the past 30 days.`
- `List overdue invoices for this customer.`
- `Get the details for invoice #1042.`
- `Create an invoice for Acme Corp for 10 hours of consulting.`
- `Send invoice #1042 to the customer.`
- `Find the customer record for Riverside Catering.`
- `Search for the item called Monthly Retainer.`
- `Get the full details for this customer before I create the invoice.`
- `Look up this item's pricing before I add it to the invoice.`

## QuickBooks Online Billing and AR MCP server tools

The QuickBooks Online Billing and AR MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_invoices](#list-invoices-tool) | Retrieves a list of invoices with optional filters, such as date range and customer. |
| [get\_invoice](#get-invoice-tool) | Retrieves detailed information for an invoice you specify, including line items, totals, and payment status. |
| [create\_invoice](#create-invoice-tool) | Creates a new invoice for an existing customer using specified items and pricing. |
| [send\_invoice](#send-invoice-tool) | Sends an existing invoice to the associated customer. |
| [search\_customers](#search-customers-tool) | Searches for customers using a name or partial identifier. |
| [search\_items](#search-items-tool) | Searches for items, such as products or services, using a name or partial identifier. |
| [get\_customer](#get-customer-tool) | Retrieves full details for a customer you specify. |
| [get\_item](#get-item-tool) | Retrieves full details for an item you specify. |

## Install the QuickBooks Online Billing and AR MCP server

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
    

## QuickBooks Online connection setup

View QuickBooks Online connection setup steps

### Supported editions and versions

View Supported editions and versions

The QuickBooks connector works with the following QuickBooks Online versions:

- QuickBooks Self-Employed
- QuickBooks Simple Start
- QuickBooks Essentials
- QuickBooks Plus

Workato doesn't support QuickBooks Desktop/Enterprise versions.

### How to connect to QuickBooks on Workato

View How to connect to QuickBooks on Workato steps

Complete the following steps to establish a connection to QuickBooks Online in Workato:

1. Provide a **Connection name** that identifies which QuickBooks instance Workato is connected to.
   
   ![QuickBooks online connection](/assets/QBO_connect1.D_Fk-JGJ.png)_QuickBooks online connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
3. Use the **Sandbox** drop-down menu to specify whether the QuickBooks Online account is a sandbox account.
   
4. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
5. Click **Connect to QuickBooks** to open the QuickBooks sign in window.
   
   ![Connect to QuickBooks Online](/assets/QBO_connect2.DOeG2fRE.png)_Connect to QuickBooks Online_
   
6. Enter your QuickBooks Online account email address and password.
   
7. Click **Sign in** to complete the connection.
   

## How to use QuickBooks Online Billing and AR MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_invoices tool

The **list\_invoices** tool retrieves a list of invoices with optional filters, such as date range and customer. Your LLM uses this tool to view, list, or review invoices, including requests for recent invoices, overdue invoices, or invoices within a specific date range.

**Try asking**:

- `Show me all invoices from the past 30 days.`
- `List overdue invoices for this customer.`
- `Show me all open invoices from last quarter.`
- `Which invoices are still outstanding?`

### get\_invoice tool

The **get\_invoice** tool retrieves detailed information for an invoice you specify, including line items, totals, and payment status. Your LLM uses this tool to retrieve the details for an invoice.

**Try asking**:

- `Get the details for invoice #1042.`
- `Show me the line items and total for this invoice.`
- `What is the payment status of this invoice?`
- `Pull up the full details for the invoice I sent last week.`

### create\_invoice tool

The **create\_invoice** tool creates a new invoice for an existing customer using items and pricing you specify. Your LLM resolves customer and item references before creating the invoice, and asks for missing required details, such as customer, items, quantities, or pricing.

**Try asking**:

- `Create an invoice for Acme Corp for 10 hours of consulting.`
- `Generate an invoice for the Monthly Retainer service.`
- `Bill Riverside Catering for the items from last week's order.`
- `Create a new invoice for this customer with these line items.`

### send\_invoice tool

The **send\_invoice** tool sends an existing invoice to the associated customer. Your LLM uses this tool to send or resend an invoice.

**Try asking**:

- `Send invoice #1042 to the customer.`
- `Resend the invoice I created for Acme Corp.`
- `Email this invoice to the customer now.`
- `Send the outstanding invoice for this account.`

### search\_customers tool

The **search\_customers** tool searches for customers using a name or partial identifier. Your LLM uses this tool to retrieve a customer reference for invoice workflows by name or partial identifier.

**Try asking**:

- `Find the customer record for Riverside Catering.`
- `Search for a customer named Acme.`
- `Look up this customer before I create their invoice.`
- `Find all customers matching this partial name.`

### search\_items tool

The **search\_items** tool searches for items, such as products or services, using a name or partial identifier. Your LLM uses this tool to find invoices for a product or service name you provide.

**Try asking**:

- `Search for the item called Monthly Retainer.`
- `Find the consulting hours product in QuickBooks.`
- `Look up this service item before I add it to the invoice.`
- `Search for items matching this product name.`

### get\_customer tool

The **get\_customer** tool retrieves full details for a customer you specify. Your LLM uses this tool to return a customer ID or complete customer details for invoice workflows.

**Try asking**:

- `Get the full details for this customer before I create the invoice.`
- `Show me all information for this customer record.`
- `Retrieve the billing details for this customer.`
- `Pull up this customer's full profile.`

### get\_item tool

The **get\_item** tool retrieves full details for an item you specify, including pricing and description. Your LLM uses this tool to retrieve item details to construct invoice line items.

**Try asking**:

- `Look up this item's pricing before I add it to the invoice.`
- `Get the full details for this product.`
- `Show me the description and rate for this service item.`
- `Retrieve this item's details before I include it on the invoice.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/salesforce-sales-explorer-mcp-server.md
description: >-
  Use the Salesforce Sales Explorer MCP server to connect your LLM to Salesforce
  with a curated set of tools to search for records, retrieve details, create
  new entries, and update existing information.
---

# Salesforce Sales Explorer MCP server

The Salesforce Sales Explorer MCP server enables LLMs to work with leads, accounts, contacts, opportunities, tasks, events, and products in Salesforce. It provides tools to search for records, retrieve details, create new entries, and update existing information through natural conversation.

## Uses

Use the Salesforce Sales Explorer MCP server when you plan to perform the following actions:

- Search for leads, accounts, contacts, opportunities, tasks, and products
- Retrieve detailed information about specific sales records
- Create new leads, accounts, contacts, opportunities, tasks, and events
- Update existing sales records with new information or status changes
- Add product line items to opportunities
- Execute SOQL queries for custom data retrieval
- Retrieve schema information for Salesforce objects

### Example prompts

Use the following example prompts to invoke Salesforce Sales Explorer MCP server tools:

- `Find all qualified leads from last month.`
- `Show me opportunities closing this quarter over $100k.`
- `Get details on the Acme Corp account.`
- `Create a lead for Jane Smith at TechCo.`
- `Update the Acme renewal opportunity to Negotiation stage.`
- `Schedule a call with the customer for tomorrow at 2pm.`
- `Add the Enterprise subscription product to this opportunity.`
- `What are my high-priority tasks due this week?`

## Salesforce Sales Explorer MCP server tools

The Salesforce Sales Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_leads](#search-leads-tool) | Searches for leads matching specified criteria. |
| [search\_accounts](#search-accounts-tool) | Searches for accounts matching specified criteria. |
| [search\_contacts](#search-contacts-tool) | Searches for contacts matching specified criteria. |
| [search\_opportunities](#search-opportunities-tool) | Searches for opportunities matching specified criteria. |
| [search\_tasks](#search-tasks-tool) | Searches for tasks matching specified criteria. |
| [search\_products](#search-products-tool) | Searches for products in the Salesforce product catalog. |
| [upsert\_lead](#upsert-lead-tool) | Creates a new lead or updates an existing lead. |
| [upsert\_account](#upsert-account-tool) | Creates a new account or updates an existing account. |
| [upsert\_contact](#upsert-contact-tool) | Creates a new contact or updates an existing contact. |
| [upsert\_opportunity](#upsert-opportunity-tool) | Creates a new opportunity or updates an existing opportunity. |
| [upsert\_task](#upsert-task-tool) | Creates a new task or updates an existing task. |
| [upsert\_event](#upsert-event-tool) | Creates a new calendar event or updates an existing event. |
| [add\_opportunity\_line\_item](#add-opportunity-line-item-tool) | Adds a product line item to an existing opportunity. |
| [retrieve\_semantic\_model](#retrieve-semantic-model-tool) | Retrieves schema information for a specified Salesforce object. |
| [execute\_soql\_query](#execute-soql-query-tool) | Executes SOQL queries in Salesforce. |

## Install the Salesforce Sales Explorer MCP server

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
    

## Salesforce connection setup

View Salesforce connection setup steps

Workato supports OAuth 2.0 authentication and JWT bearer authentication connections for Salesforce Sales Explorer.

### OAuth 2.0 authentication

View OAuth 2.0 authentication steps

#### Connect to Salesforce using OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 (Authorization Code Grant) connection to Salesforce in Workato:

> **OAUTH RESTRICTIONS**
> 
> As of early September 2025, Salesforce restricts the use of uninstalled Salesforce Connected Apps. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for required actions if you encounter errors when you create a new connection. These steps are required for all new Salesforce connections starting **September 17, 2025**.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_OAuth2.0 Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Optional. Expand **Advanced settings** to configure the following options:
   
   Advanced settings
   
   - **Organization/community custom domain URL**: Enter the URL to your Salesforce community's custom domain. Required for community connections with unique domains.
   - **Requested permissions**: Select [permissions](https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5) to request for this connection. Refer to [Requested scopes](/en/connectors/salesforce#oauth2-scopes) for the scopes Workato requests.
   - **Verified user access configuration**: Configure custom auth for personal connections. Refer to [Runtime user connections](/en/features/runtime-user-connections) for more information.
   
   > **REFRESH TOKEN SCOPE IS REQUIRED**
   > 
   > The **Perform requests at any time (`refresh_token`, `offline_access`)** scope is one of the scopes Workato requests for OAuth 2.0 connections, but whether Salesforce actually grants this scope depends on the Connected App's own OAuth policies, not on the Workato connection's settings. Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) if your connection later disconnects when the access token expires. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
   
9. Click **Connect**.
   
10. Optional. If your Salesforce organization or community uses a custom domain, complete the following in the sign-in modal:
    
    - Click **Use Custom Domain**.
    - Enter your **Custom domain**, then click **Continue**.
    
    ![Salesforce custom domains](/assets/connection-custom-domain.D3hJN8X8.png)_Enter your Custom domain._
    
11. Enter your Salesforce **Username** and **Password**.
    
    ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
    
12. Click **Log In** to complete the setup.
    
    > **OAUTH\_APPROVAL\_ERROR\_GENERIC**
    > 
    > If you see this error, Salesforce is restricting the Workato app because it isn't installed. A Salesforce admin must install the app in **Connected Apps OAuth Usage** or assign the Salesforce permissions. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for details.
    

### JWT bearer authentication

View JWT bearer authentication steps

> **ACTIONS ON BEHALF OF USER**
> 
> JWT connections can perform actions on behalf of a user you specify using the **On-behalf-of-user email** field. Contact your Workato Customer Success Manager to enable this feature.

#### How it works

JWT bearer authentication connects using a digital certificate that signs a JWT request. Workato sends a JWT to the Salesforce OAuth token endpoint, where Salesforce processes the JWT and issues an access token based on prior approval of Workato in Salesforce.

Although JWT bearer skips interactive sign-in, Salesforce still evaluates every request against the permissions of the user specified in the connection and attributes any changes to that user. Use a dedicated integration user rather than a personal account.

Refer to [Required roles and permissions](/en/connectors/salesforce#roles-and-permissions-required-to-connect) for the Salesforce permissions the connected user needs.

#### Generate a private key and certificate

JWT bearer authentication requires a private key and a certificate. The following command generates both using OpenSSL. Replace the `-subj` values with your own:

```bash
openssl req -x509 -sha256 -nodes -newkey rsa:2048 \
  -keyout server.key \
  -out server.crt \
  -days 365 \
  -subj "/CN=Your App Name/O=Your Organization/C=US"
```

This generates two files:

| File | Description |
| --- | --- |
| `server.key` | Your private key for Workato. Keep this secret. |
| `server.crt` | Your public certificate for Salesforce. |

Refer to Salesforce's documentation for more information:

- [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5): Details on how Salesforce uses this certificate to sign and validate JWTs.
- [Create a Private Key and Self-Signed Digital Certificate](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm): Other ways to generate a private key and certificate.

#### Create an external client app for JWT bearer

JWT bearer authentication also requires a registered external client app in Salesforce. Complete the following steps before creating your connection in Workato. Refer to Salesforce's [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US&type=5) documentation for more information.

1. Sign in to Salesforce.
   
2. Go to **Setup > Apps > External Client Apps > External Client App Manager**.
   
3. Click **New External Client App**.
   
4. Enter a name in the **External Client App Name** field, such as `Workato`.
   
5. Enter a name in the **API Name** field that meets the following requirements:
   
   - Contains only underscores and alphanumeric characters.
   - Is unique.
   - Starts with a letter.
   - Doesn't include spaces.
   - Doesn't end with an underscore.
   - Doesn't contain consecutive underscores.
6. Enter the contact email address for your app in the **Contact Email** field.
   
7. Use the **Distribution State** drop-down menu to select either **Local** or **Packaged**.
   
8. Expand **API (Enable OAuth Settings)** and select the **Enable OAuth** checkbox. Refer to Salesforce's [Configure the External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure_external_client_app_oauth_settings.htm&language=en_US&type=5) documentation for more information.
   
9. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
10. Select your OAuth scopes in the **OAuth Scopes** field based on the actions and triggers you plan to use, then click the **Move selection to Selected OAuth Scopes** arrow to apply them.
    
    ![Configure scopes for your external client app](/assets/oauth-scopes.B-mGtuor.png)_Configure scopes for your external client app_
    
    > **REFRESH\_TOKEN SCOPE IS REQUIRED**
    > 
    > If you see the error `refresh_token scope is required and the connected app should be installed and preauthorized`, add **Perform requests at any time (refresh\_token, offline\_access)** to your OAuth scopes. If you then see an invalid session error, also add **Manage user data via APIs (api)**.
    
11. Select **Enable JWT Bearer Flow** in the **Flow Enablement** section. Refer to Salesforce's [Configure a JWT Bearer Flow](https://help.salesforce.com/s/articleView?id=xcloud.configure_oauth_jwt_flow_external_client_apps.htm&language=en_US&type=5) documentation for more information.
    
12. Upload `server.crt` as the digital certificate.
    
13. Click **Create**.
    
14. Click the **Policies** tab, then click **Edit**.
    
15. Expand the **OAuth Policies** section and set **Permitted Users** to **Admin approved users are pre-authorized**.
    
    > **USER HASN'T APPROVED THIS CONSUMER**
    > 
    > If you see this error when connecting, this step was likely missed.
    
16. Locate the **App Policies** section. Add either the [profile](https://help.salesforce.com/s/articleView?id=admin_userprofiles.htm&language=en_US&type=5) or [permission set](https://help.salesforce.com/s/articleView?id=000386289&language=en_US&type=1) assigned to the Salesforce user Workato connects as to the **Select Profiles** or **Select Permission Sets** list. Refer to Salesforce's [Preauthorize User App Access Through External Client App Policies](https://help.salesforce.com/s/articleView?id=xcloud.preauth_user_app_access_through_eca.htm&language=en_US&type=5) documentation for more information.
    
    > **USER IS NOT ADMIN APPROVED TO ACCESS THIS APP**
    > 
    > If you see this error when connecting, this step was likely missed.
    
17. Click **Save**.
    
18. Click the **Settings** tab for your external client app.
    
19. Expand the **OAuth Settings** section.
    
20. Click **Consumer Key and Secret**.
    
21. Verify your identity when prompted.
    
22. Copy the **Consumer Key**. You'll enter this as the **Issuer** when connecting in Workato.
    

#### Connect to Salesforce using JWT bearer

Complete the following steps to connect to Salesforce using JWT bearer authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce JWT Connection](/assets/salesforce-new-jwt-connection.BCDJGTAT.png)_Configure Salesforce JWT Bearer connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **JWT token**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Paste the full contents of `server.key` in the **Private key** field, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
   
8. Enter the **Consumer Key** from your external client app in the **Issuer** field.
   
9. Enter the **Subject** for the JWT connection. This is the username of the Salesforce user you want Workato to authenticate as, or a valid Experience Cloud username if you're connecting to an Experience Cloud site. You can use principal (`prn`) in place of subject (`sub`) for backward compatibility. If you specify both, Workato uses `prn`.
   
10. Enter your **Salesforce Subdomain**. For example, if your Salesforce URL is `yourInstance.salesforce.com`, the subdomain is `yourInstance`.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
    
12. Click **Connect**.
    

## How to use Salesforce Sales Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_leads tool

The **search\_leads** tool searches for leads matching the criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve leads by ID, status, source, owner, company, or date ranges.

**Try asking**:

- `Find leads from last week.`
- `Show me all open leads.`
- `Find leads from Acme Corp.`
- `Show me qualified leads assigned to me.`
- `Find leads from the trade show.`
- `Show me leads created this month.`

### search\_accounts tool

The **search\_accounts** tool searches for accounts matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve accounts by ID, name, type, industry, owner, or parent account.

**Try asking**:

- `Find accounts in the technology industry.`
- `Show me all customer accounts.`
- `Find Acme Corp account.`
- `Show me prospect accounts owned by Sarah.`
- `Find child accounts of Acme Corp.`
- `Show me accounts created this quarter.`

### search\_contacts tool

The **search\_contacts** tool searches for contacts matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve contacts by ID, name, account, title, email, or owner.

**Try asking**:

- `Find contacts at Acme Corp.`
- `Find Jane Smith in Salesforce.`
- `Show me all VP-level contacts.`
- `Find contact with email jane@acme.com.`
- `Show me contacts owned by John.`
- `Get Jane Smith's contact information.`

### search\_opportunities tool

The **search\_opportunities** tool searches for opportunities matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve opportunities by ID, name, account, stage, close date, amount, or owner.

**Try asking**:

- `Find deals closing this quarter.`
- `Find the Acme Corp renewal opportunity.`
- `Show me all opportunities in negotiation stage.`
- `Find deals over $100k.`
- `Show me opportunities I'm working on.`
- `Show me deals closing next month.`

### search\_tasks tool

The **search\_tasks** tool searches for tasks matching criteria you specify. Your LLM uses this tool when you need to find, list, filter, or retrieve tasks by ID, subject, status, priority, due date, owner, or related records.

**Try asking**:

- `Find my tasks for this week.`
- `Find tasks about contract review.`
- `Show me open tasks.`
- `Show me high-priority tasks.`
- `What tasks are due today?`
- `Show me tasks for the Acme Corp account.`

### search\_products tool

The **search\_products** tool searches for products in the Salesforce product catalog. Your LLM uses this tool when you need to find, list, or retrieve products by ID, name, product code, or active status.

**Try asking**:

- `Find products in our catalog.`
- `Find the Enterprise subscription product.`
- `Find product SKU-12345.`
- `Show me software products.`
- `Show me discontinued products.`
- `What products can I add to this opportunity?`

### upsert\_lead tool

The **upsert\_lead** tool creates a new lead if it doesn't exist, or updates an existing lead if you provide the lead ID. Your LLM uses this tool when you need to create a new prospect or update lead information.

**Try asking**:

- `Create a lead for Josh Hernandez at Acme Corp.`
- `Log this person as a lead.`
- `Update the lead status to Qualified.`
- `I met Jade Anderson from TechCo at the conference - create a lead.`
- `Assign this lead to Sarah.`
- `Update the lead - they're interested in the enterprise plan.`

### upsert\_account tool

The **upsert\_account** tool creates a new account if it doesn't exist, or updates an existing account if provided with account ID. Your LLM uses this tool when you need to create a new company record or update account information.

**Try asking**:

- `Create an account for Acme Corp.`
- `Update Acme Corp's industry to Technology.`
- `Add this company to Salesforce.`
- `Update the account - their revenue is $50M.`
- `Reassign this account to John.`

### upsert\_contact tool

The **upsert\_contact** tool creates a new contact if it doesn't exist, or updates an existing contact if you provide the contact ID. Your LLM uses this tool when you need to create a new person record or update contact information.

**Try asking**:

- `Create a contact for Jane Smith.`
- `Update Jane's email address.`
- `Add John Doe as a contact at Acme Corp.`
- `Save this person's information as a contact.`

### upsert\_opportunity tool

The **upsert\_opportunity** tool creates a new opportunity if it doesn't exist, or updates an existing opportunity if you provide the opportunity ID. Your LLM uses this tool when you need to create a new sales deal or update opportunity information.

**Try asking**:

- `Create an opportunity for Acme Corp renewal.`
- `Update the Acme deal amount to $100k.`
- `Move this opportunity to Negotiation stage.`
- `Push the close date to end of quarter.`
- `Create an opportunity for what we just discussed.`

### upsert\_task tool

The **upsert\_task** tool creates a new task if it doesn't exist, or updates an existing task if you provide the task ID. Your LLM uses this tool when you need to create a to-do item or update task information, and can link tasks to leads, accounts, contacts, or opportunities.

**Try asking**:

- `Create a task to follow up with Acme Corp.`
- `Remind me to call them next week.`
- `Make a task for what we discussed.`
- `Create a task for this opportunity to send the proposal.`
- `Mark that task as completed.`
- `Push the task due date to Friday.`

### upsert\_event tool

The **upsert\_event** tool creates a new calendar event if it doesn't exist, or updates an existing event if you provide the event ID. Your LLM uses this tool when you need to schedule a meeting, call, or calendar activity with specific date and time.

**Try asking**:

- `Schedule a call with Acme Corp for tomorrow at 2pm.`
- `Put a meeting on my calendar for Friday at 10am.`
- `Move that meeting to next Tuesday.`
- `Schedule a demo for this opportunity on Wednesday.`

### add\_opportunity\_line\_item tool

The **add\_opportunity\_line\_item** tool adds a product line item to an existing opportunity. Your LLM uses this tool when you need to add products or services to a sales deal.

**Try asking**:

- `Add the Enterprise subscription to this opportunity.`
- `Add 5 licenses to the Acme deal.`
- `Add the product at $1000 per unit to this opportunity.`
- `Add the Professional Services package to the renewal deal.`

### retrieve\_semantic\_model tool

The **retrieve\_semantic\_model** tool retrieves schema information for a Salesforce object you specify, including field names, field types, field labels, relationships to other objects, and field-level permissions. Your LLM uses this tool when you need to understand object structure before building queries or creating records.

**Try asking**:

- `What fields are available on the Lead object?`
- `Show me the schema for Opportunity.`
- `What are the field types for Account?`
- `Get the object structure for Contact.`

### execute\_soql\_query tool

The **execute\_soql\_query** tool executes SOQL queries in Salesforce. Your LLM uses this tool after reviewing semantic models to build custom queries that answer specific questions about your Salesforce data.

**Try asking**:

- `Query all opportunities with amount greater than $50k closing this quarter.`
- `Find accounts in the technology industry with annual revenue over $10M.`
- `Get all contacts associated with closed-won opportunities.`
- `Query tasks due this week for my team members.`

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
