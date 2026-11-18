---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-powerpoint-mcp-server.md
description: >-
  Use the Microsoft PowerPoint MCP server to connect your LLM to Microsoft
  PowerPoint with content retrieval, slide structure manipulation, targeted text
  updates, and speaker notes management.
---

# Microsoft PowerPoint MCP server

The Microsoft PowerPoint MCP server enables LLMs to interact with Microsoft PowerPoint for presentation content and structure management through natural conversation. It provides tools to read and summarize slide content, manipulate presentation structure, update text, and manage speaker notes without requiring direct interaction with the Microsoft PowerPoint interface.

## Uses

Use the Microsoft PowerPoint MCP server to perform the following actions:

- Retrieve presentation metadata and structural overview.
- Read and summarize slide content, including text elements and speaker notes.
- Inspect individual slide elements for targeted operations.
- List available slide layouts for adding new slides.
- Add, delete, and copy slides to build presentations.
- Update text content on specific slides.
- Perform find-and-replace across entire presentations.
- Generate and add speaker notes.

### Example prompts

Use the following example prompts to invoke Microsoft PowerPoint MCP server tools:

- `Summarize my Q4 board presentation.`
- `Update the date on slide 1 to January 2026.`
- `What are the key points in the investor deck?`
- `Change the revenue figure from $2.3M to $2.5M on slide 7.`
- `Give me talking points for slides 5-10.`
- `Replace all instances of 'Q3' with 'Q4'.`
- `Add a new slide after the roadmap section for Q2 priorities.`
- `Delete the case study slides and add two more comparison slides.`
- `Generate speaker notes for my board presentation.`

## Microsoft PowerPoint MCP server tools

The Microsoft PowerPoint MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_presentation](#get-presentation-tool) | Retrieves metadata and structural overview of a PowerPoint presentation. |
| [get\_slide\_content](#get-slide-content-tool) | Extracts text content from specified slides including text elements and speaker notes. |
| [get\_slide\_elements](#get-slide-elements-tool) | Lists all elements on a specific slide with type, position, size, and content preview. |
| [list\_layouts](#list-layouts-tool) | Returns available slide layouts from the presentation's masters with placeholder information. |
| [add\_slide](#add-slide-tool) | Inserts a new slide with the specified layout at a given position. |
| [delete\_slide](#delete-slide-tool) | Removes one or more slides from a presentation. |
| [copy\_slide](#copy-slide-tool) | Duplicates a slide within the same presentation. |
| [update\_text\_content](#update-text-content-tool) | Updates text within a specific element on a slide. |
| [find\_and\_replace\_text](#find-and-replace-text-tool) | Performs find-and-replace across all slides in a presentation. |
| [update\_speaker\_notes](#update-speaker-notes-tool) | Sets or replaces speaker notes for a specific slide. |

## Install the Microsoft PowerPoint MCP server

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
    

## Microsoft PowerPoint connection setup

View Microsoft PowerPoint connection setup steps

The Microsoft PowerPoint MCP server supports [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code).

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

### Authorization code grant authentication (OAuth 2.0)

This authentication method requires the following value for tenant-specific account types:

- Tenant ID

#### Minimum and default scopes

View minimum and default scopes

The Microsoft PowerPoint connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

| Permission | Description | Relevant action |
| --- | --- | --- |
| `Files.Read.All` | Allows the app to read all files the signed-in user can access. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Files.ReadWrite.All` | Allows the app to read and write all files the signed-in user can access. | All actions in `Files.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Sites.ReadWrite.All` | Allows the app to read and write documents in all SharePoint site collections on behalf of the signed-in user. | All actions in `Sites.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `User.Read` | Allows the app to sign in and read the profile of the signed-in user. | The connector always requests this permission. |
| `offline_access` | Allows the app to access Microsoft Graph data after the user signs out or the session expires. | The connector always requests this permission. |

Use **Requested permissions (OAuth scopes)** in **Advanced settings** to limit the requested permissions. Select `Files.ReadWrite.All`, `Sites.ReadWrite.All`, or both to use actions that create or modify slides. Those actions fail on connections that request only read permissions.

You must add the following minimum scopes to establish a connection to Microsoft PowerPoint with authorization code grant authentication:

- `offline_access`
- `User.Read`

#### Microsoft PowerPoint setup for authorization code grant authentication

View Microsoft PowerPoint setup for authorization code grant authentication steps

Complete the following steps to set up Microsoft PowerPoint for authorization code grant authentication:

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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Assign **Delegated** permissions for authorization code grant connections and **Application** permissions for client credentials-based connections.
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Microsoft PowerPoint connector](/en/connectors/microsoft-powerpoint#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft PowerPoint with authorization code grant authentication

View connect to Microsoft PowerPoint with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft PowerPoint in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft PowerPoint` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select the type of Microsoft account to connect to. The available choices are **Common** and **Tenant specific**.
   
   **Common**
   
   - **Common**: This option supports personal and enterprise Microsoft accounts.
   
   ![Microsoft PowerPoint Common connection setup](/assets/connect-common.D2AA5xSb.png)_Microsoft PowerPoint Common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option requires a Tenant ID.
   
   ![Microsoft PowerPoint Tenant specific connection setup with authorization code grant](/assets/connect-tenant-specific-auth-code.CxxIfBQr.png)_Microsoft PowerPoint Tenant specific connection setup with authorization code grant_
   
   Provide the Microsoft Entra ID tenant ID (a GUID) or its domain name in the **Tenant ID** field.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Expand the **Advanced settings** section to configure **Requested permissions (OAuth scopes)** for your connection. Ensure your connection provides write permissions if you plan to use actions or MCP server tools that create or modify slides. `User.Read` and `offline_access` are requested in addition to any selected permissions.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Project property configuration

The Microsoft PowerPoint MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| Maximum slides per read request | Limits the number of slides returned by **get\_slide\_content** in a single call. Retrieve slides in batches using the `slide_numbers` parameter for presentations that exceed this quota. Defaults to `50`. |
| Maximum presentation file size | Limits the accepted file size of presentations. Defaults to `100` MB. Presentations exceeding this size return an error on any read or write operation. |
| Maximum speaker notes length per slide | Limits the size of the `notes_content` parameter in **update\_speaker\_notes**. Notes exceeding this quota are rejected. Defaults to `5,000` characters. |
| Maximum find-and-replace operations | Limits the number of replacements per **find\_and\_replace\_text** call. The operation is rejected if more instances match than this quota. Defaults to `1,000`. |
| Write conflict policy | Controls conflict detection and retry. Before a server uploads a modified file, it checks whether the file's last-modified timestamp changed since the last download. The server returns a conflict error rather than overwriting concurrent changes. |
| Response truncation policy | Controls response truncation. Text content from individual elements returns up to `10,000` characters per element. Tables return up to `50` rows. Speaker notes return up to `5,000` characters per slide. Content beyond these quotas is truncated with an indicator. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato workspace and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
6. Go to the **Value** field and make your changes.
   

## How to use Microsoft PowerPoint MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_presentation tool

The **get\_presentation** tool retrieves metadata and structural overview of a PowerPoint presentation. Your LLM uses this tool as the first step before any content retrieval or modification to understand a presentation's scope. This tool returns a presentation's title, slide count, dimensions, author, and modification history.

**Try asking**:

- `How many slides are in my Q4 board deck?`
- `When was this presentation last modified and by whom?`
- `What are the slide dimensions for this deck?`

### get\_slide\_content tool

The **get\_slide\_content** tool extracts text content from specified slides including text elements and speaker notes. Your LLM uses this tool when a user wants to understand slide content, needs a summary, or is preparing for a presentation. This tool retrieves either all slides or slides you specify.

**Try asking**:

- `Summarize the content of slides 5 through 10.`
- `What does the executive summary slide say?`
- `Read the speaker notes for my entire presentation.`
- `Pull the text from every slide so I can review it.`

### get\_slide\_elements tool

The **get\_slide\_elements** tool lists all elements on a specific slide with type, position, size, and content preview. Your LLM uses this tool before **update\_text\_content** to identify the correct element for modification and to disambiguate when content appears in multiple elements.

**Try asking**:

- `List all the elements on slide 3.`
- `Which text boxes are on the title slide?`
- `Show me the placeholders on slide 7 so I can update one.`
- `What elements appear on the comparison slide?`

### list\_layouts tool

The **list\_layouts** tool returns available slide layouts from the presentation's masters with placeholder information. Your LLM uses this tool before **add\_slide** to discover what layouts exist and help the user choose appropriate structure. This tool retrieves layout names, types, and placeholders as a flat list.

**Try asking**:

- `What slide layouts are available in this presentation?`
- `Show me the layouts I can use to add a new slide.`
- `Which layout should I use for a section header?`
- `List the placeholders for each available layout.`

### add\_slide tool

The **add\_slide** tool inserts a new slide with the specified layout at a given position. Your LLM uses this tool to build and extend presentation structure.

**Try asking**:

- `Add a new slide after the roadmap section for Q2 priorities.`
- `Insert a Title and Content slide at position 4.`
- `Append a section header slide to the end of the deck.`
- `Add two more comparison slides to this presentation.`

### delete\_slide tool

The **delete\_slide** tool removes one or more slides from a presentation. Your LLM uses this tool to clean up templates, remove placeholder slides, and restructure. This tool confirms the target slide numbers with the user before deletion.

**Try asking**:

- `Delete the case study slides from this deck.`
- `Remove slide 8.`
- `Delete slides 3, 4, and 5.`
- `Clean up the placeholder example slides in this template.`

### copy\_slide tool

The **copy\_slide** tool duplicates a slide within the same presentation. Your LLM uses this tool to create variations, repeat structures, or iterate on content. You can specify a location to insert the copy.

**Try asking**:

- `Duplicate slide 6.`
- `Make a copy of the pricing slide and place it after slide 10.`
- `Copy the template slide so I can build a variation.`
- `Repeat the customer overview slide later in the deck.`

### update\_text\_content tool

The **update\_text\_content** tool updates text within a specific element on a slide. Your LLM uses this tool to make targeted edits such as changing dates, updating numbers, or fixing text. This tool identifies the element by element ID or by matching existing text.

**Try asking**:

- `Update the date on slide 1 to January 2026.`
- `Change the revenue figure from $2.3M to $2.5M on slide 7.`
- `Fix the typo on slide 12 — change 'teh' to 'the'.`
- `Replace the title on the opening slide with "Acme Corp QBR".`

### find\_and\_replace\_text tool

The **find\_and\_replace\_text** tool performs find-and-replace across all slides in a presentation. Your LLM uses this tool for bulk updates such as changing dates throughout, fixing repeated terms, or updating terminology. The tool returns the count and location of replacements.

**Try asking**:

- `Replace all instances of 'Q3' with 'Q4'.`
- `Change every mention of "2025" to "2026" across the deck.`
- `Update the company name everywhere it appears.`
- `Find and replace "Beta" with "GA" throughout the presentation.`

### update\_speaker\_notes tool

The **update\_speaker\_notes** tool sets or replaces the speaker notes content for a specific slide. Your LLM uses this tool after generating notes from slide content or when the user provides talking points. This tool confirms with the user before overwriting existing content.

**Try asking**:

- `Generate speaker notes for my board presentation.`
- `Add talking points to slides 5 through 10.`
- `Write presenter notes for the financial summary slide.`
- `Replace the speaker notes on slide 2 with these talking points.`

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
