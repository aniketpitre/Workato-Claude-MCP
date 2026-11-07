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

The Microsoft PowerPoint MCP server supports the following authentication types:

- [Authorization code grant authentication](#authentication-auth-code)
- [Client credentials-based authentication](#authentication-client-credentials): _Only available for tenant-specific connections_

### Authorization code grant authentication (OAuth 2.0)

View authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to PowerPoint in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `PowerPoint` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select the type of Microsoft account to connect to.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Expand the **Advanced settings** section to configure **Requested permissions (OAuth scopes)** for your connection. Ensure your connection provides write permissions if you plan to use actions or MCP server tools that create or modify slides. `Files.Read.All`, `User.Read`, and `offline_access` are requested in addition to any selected permissions.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials authentication

View client credentials authentication steps

Complete the following steps to set up a client credentials grant connection to PowerPoint in Workato:

> **PREREQUISITES**
> 
> Client credentials connections require a tenant ID, user ID, client ID, and client secret.
> 
> Refer to the Microsoft [Application configuration](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration) documentation to generate these values.

1. Click **Create > Connection** or press C twice.
   
2. Search for `PowerPoint` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select **Tenant specific**.
   
6. Enter the Azure **Tenant ID**.
   
   Refer to the Microsoft [Authority](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#authority) documentation for more information about tenant IDs.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Expand the **Advanced settings** section and provide the following **User ID**, **Client ID**, and **Client secret** for your account.
   
   Refer to the Microsoft [Authority](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#authority) documentation to generate these values.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

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
