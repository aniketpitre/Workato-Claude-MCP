---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-word-mcp-server.md'
description: >-
  Use the Microsoft Word MCP server to connect your LLM to Word with tools to
  create, read, update, and collaborate on documents through natural language.
---

# Microsoft Word MCP server

The Microsoft Word MCP server enables LLMs to create, read, update, and collaborate on Word documents through natural conversation. It provides tools to author content, apply edits, manage comments, surface tracked changes, and create documents from templates without requiring direct interaction with the Word interface.

## Uses

Use the Microsoft Word MCP server to perform the following actions:

- Create new Word documents with optional titles and initial content
- Create documents from existing Word templates
- Retrieve document metadata and revision identifiers
- Get structured content and metadata from documents
- Find document blocks by text or structural criteria
- Apply block-level updates to documents with revision safety
- Add comments to documents and associate them with specific content blocks
- List comment threads with filtering and pagination
- Reply to existing comment threads
- Resolve or close comment threads
- List pending tracked changes with authorship information

### Example prompts

Use the following example prompts to invoke Microsoft Word MCP server tools:

- `Create a new Word document for the project proposal.`
- `Make a document from the quarterly report template.`
- `What's in the marketing plan document?`
- `Find the Executive Summary section in this document.`
- `Update the budget section to reflect the new numbers.`
- `Add a comment to the intro paragraph about tone.`
- `What comments are on the proposal document?`
- `Reply to Jade's comment about the timeline.`
- `Resolve all comments from Marco.`
- `Show me the tracked changes in this document.`

## Microsoft Word MCP server tools

The Microsoft Word MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_document](#create-document-tool) | Creates a new Word document with an optional title and initial content. |
| [create\_document\_from\_template](#create-document-from-template-tool) | Creates a new Word document pre-populated from an existing Word template file. |
| [get\_document\_info](#get-document-info-tool) | Retrieves Word document metadata and the current revision identifier without returning content. |
| [get\_document\_content](#get-document-content-tool) | Retrieves structured content and metadata for a Word document. |
| [find\_blocks](#find-blocks-tool) | Finds document blocks by text or structural criteria and returns block identifiers for targeted edits. |
| [update\_document\_content](#update-document-content-tool) | Applies structured, block-level updates to a Word document with revision safety enforcement. |
| [add\_comment](#add-comment-tool) | Adds a new comment to a Word document, optionally associated with a specific content block. |
| [list\_comments](#list-comments-tool) | Lists comment threads in a Word document with filtering and pagination support. |
| [reply\_to\_comment](#reply-to-comment-tool) | Adds a reply to an existing comment thread in a Word document. |
| [resolve\_comment](#resolve-comment-tool) | Marks an existing comment thread as resolved in a Word document. |
| [list\_tracked\_changes](#list-tracked-changes-tool) | Lists pending tracked changes in a Word document with authorship and location information. |

## Install the Microsoft Word MCP server

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
    

## Microsoft Word connection setup

View Microsoft Word connection setup steps

Workato supports the following types of connections to Microsoft Word:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials)

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

This authentication method requires the following value for tenant-specific account types:

- Tenant ID

#### Minimum and default scopes

The Microsoft Word connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Files.Read`
- `Files.ReadWrite`
- `Files.Read.All`
- `Files.ReadWrite.All`
- `User.Read`
- `offline_access`

The following minimum scopes are required to establish a connection to Microsoft Word using authorization code grant authentication:

- `User.Read`
- `offline_access`

#### Microsoft Word setup for authorization code grant authentication

Complete the following steps to set up Microsoft Word for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

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
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions based on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Microsoft Word connector](/en/connectors/microsoft-word#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft Word with authorization code grant authentication

View connect to Microsoft Word with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Word in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Word` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that are not restricted to a specific organization (tenant).
   
   ![Microsoft Word common connection setup](/assets/word-common-auth-code-grant-connection.B7q0iZ4k.png)_Microsoft Word common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Word Tenant specific connection setup](/assets/word-tenant-specific-auth-code-grant-connection.BRrvVsyi.png)_Microsoft Word tenant specific connection setup_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID) or its `tenant domain` in the **Tenant ID** field. This ensures that you access resources specifically configured for that tenant. Refer to [Register the Workato app in the Azure portal](#auth-register) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication method requires the following values:

- Tenant ID
- User ID
- Client ID
- Client secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Microsoft Word setup for client credentials-based authentication

Complete the following steps to set up Microsoft Word for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
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
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions. You must assign **Application** or **Delegated** permissions based on your connection type.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**. If specific permissions require admin consent, refer to [Connect Microsoft Entra ID to the Microsoft Word connector](/en/connectors/microsoft-word#admin-consent) to learn more.
   

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
   

#### Connect to Microsoft Word with client credentials-based authentication

View connect to Microsoft Word with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Word in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Word` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Account type**. This option supports accounts tied to a specific organization (tenant).
   
   ![Microsoft Word client credentials-based connection setup](/assets/word-client-credentials-connection.CeEI1P8j.png)_Microsoft Word client credentials-based connection setup_
   
6. Provide your **Tenant ID**. This is the **Directory (tenant) ID** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Provide the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids) and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## How to use Microsoft Word MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_document tool

The **create\_document** tool creates a Word document with an optional title and initial content for the authenticated user. Your LLM uses this tool to create a new Word document or to turn a discussion, notes, or outline into a document.

**Try asking**:

- `Create a new Word document for the project proposal.`
- `Turn these meeting notes into a Word document.`
- `Make a new document titled 'Q1 Marketing Plan'.`
- `Create a Word doc from this outline.`

### create\_document\_from\_template tool

The **create\_document\_from\_template** tool creates a new Word document pre-populated from an existing Word template file. Your LLM uses this tool to create a document from a template.

**Try asking**:

- `Make a document from the quarterly report template.`
- `Create a new proposal using the standard template.`
- `Use the meeting notes template to create a document.`
- `Start a document from the project plan template.`

### get\_document\_info tool

The **get\_document\_info** tool retrieves Word document metadata and the current revision identifier without returning content. Your LLM uses this tool to get the current revision\_id before attempting a write operation, or to confirm document access before retrieving content.

**Try asking**:

- `Get the metadata for this document.`
- `What's the current revision ID for the proposal?`
- `Check if I have access to this document.`
- `Show me the document info for the marketing plan.`

### get\_document\_content tool

The **get\_document\_content** tool retrieves structured content and metadata for a Word document using the Document Content Representation. Your LLM uses this tool to see what a document contains, reference a specific section, or get document content to perform edits or analysis.

**Try asking**:

- `What's in the marketing plan document?`
- `Show me the contents of the proposal.`
- `Read the project charter document.`
- `Get the full content of this Word doc.`

### find\_blocks tool

The **find\_blocks** tool finds document blocks by text or structural criteria and returns block identifiers for targeted edits. Your LLM uses this tool to locate specific blocks before calling update\_document\_content, especially when you refer to a named section, specific text, or a structural element that needs to be edited.

**Try asking**:

- `Find the Executive Summary section in this document.`
- `Locate the budget table in the proposal.`
- `Search for the paragraph about timeline.`
- `Find the heading that says 'Q1 Goals'.`

### update\_document\_content tool

The **update\_document\_content** tool applies structured, block-level updates to a Word document with revision safety enforcement. Your LLM uses this tool to edit, revise, update, or rewrite a section of a document.

**Try asking**:

- `Update the budget section to reflect the new numbers.`
- `Revise the Executive Summary to be more concise.`
- `Edit the timeline to push dates back two weeks.`
- `Rewrite the conclusion paragraph.`

### add\_comment tool

The **add\_comment** tool adds a new comment to a Word document and can associate it with a specific content block. Your LLM uses this tool to leave a comment, add a note, or flag a document. If you refer to a specific section or passage, your LLM will use find\_blocks first to obtain the relevant block\_id.

**Try asking**:

- `Add a comment to the intro paragraph about tone.`
- `Leave a note on the budget section asking for clarification.`
- `Flag this paragraph for review.`
- `Comment on the timeline that it seems aggressive.`

### list\_comments tool

The **list\_comments** tool lists comment threads in a Word document with filtering and pagination support. Your LLM uses this tool to see what comments exist, what feedback is outstanding, or who has commented on a document.

**Try asking**:

- `What comments are on the proposal document?`
- `Show me all unresolved comments.`
- `List feedback from Alex on this document.`
- `What comments has Mei left on the marketing plan?`

### reply\_to\_comment tool

The **reply\_to\_comment** tool adds a reply to an existing comment thread in a Word document. Your LLM uses this tool to reply to a comment, respond to feedback, or follow up on an existing thread. Your LLM uses list\_comments first to identify the correct comment\_id.

**Try asking**:

- `Reply to Jade's comment about the timeline.`
- `Respond to the feedback on the budget section.`
- `Answer Marco's question in the comments.`
- `Reply to the comment about the Executive Summary.`

### resolve\_comment tool

The **resolve\_comment** tool marks an existing comment thread as resolved in a Word document. Your LLM uses this tool to resolve, close, or mark a comment as addressed.

**Try asking**:

- `Resolve all comments from Marco.`
- `Mark Jade's comment as resolved.`
- `Close the comment thread about the budget.`
- `Resolve the feedback on the introduction.`

### list\_tracked\_changes tool

The **list\_tracked\_changes** tool lists pending tracked changes in a Word document with authorship and location information. Your LLM uses this tool to see what changes have been tracked, who made edits, or what revisions are pending in a document.

**Try asking**:

- `Show me the tracked changes in this document.`
- `What edits has Alex made to the proposal?`
- `List all pending revisions.`
- `What changes are tracked in the marketing plan?`

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
