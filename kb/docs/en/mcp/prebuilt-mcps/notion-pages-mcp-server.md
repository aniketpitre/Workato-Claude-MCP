---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/notion-pages-mcp-server.md'
description: >-
  Use the Notion Pages MCP server to let LLMs create, read, update, organize,
  and archive pages and contribute to page discussions.
---

# Notion Pages MCP server

The Notion Pages MCP server enables your LLM to work with Notion pages as collaborative content containers through natural conversation. It provides tools to create, find, read, update, organize, and archive pages, and contribute to page-level discussions without requiring direct interaction with the Notion interface.

## Uses

Use the Notion Pages MCP server to perform the following actions:

- Search for Notion pages by name, topic, or keywords
- Retrieve page metadata and properties
- Read page content including all blocks
- Create new pages as standalone or child pages
- Update page metadata and properties
- Archive or restore pages
- List child pages to navigate page hierarchy
- Append new content blocks to existing pages
- Update text content in specific blocks
- Delete blocks from pages
- View open comment threads on pages
- Add comments or reply to discussions on pages

### Example prompts

- `Find my project planning page in Notion.`
- `Show me the metadata for the API documentation page.`
- `Read the content of the team onboarding page.`
- `Create a new page for meeting notes under the Team folder.`
- `Update the status property on this project page.`
- `Archive the old roadmap page.`
- `What pages are under the Product Documentation page?`
- `Add a new section to the troubleshooting guide.`
- `Update the heading text in the introduction block.`
- `Delete the outdated section from this page.`
- `Show me the open comments on the requirements page.`
- `Add a comment asking about the timeline.`

## Notion Pages MCP server tools

The Notion Pages MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_pages](#search-pages-tool) | Searches for Notion pages by keyword. |
| [get\_page](#get-page-tool) | Retrieves metadata and properties for a Notion page. |
| [get\_page\_content](#get-page-content-tool) | Retrieves the block content of a Notion page, with pagination for long pages. |
| [create\_page](#create-page-tool) | Creates a new Notion page under a specified parent. |
| [update\_page](#update-page-tool) | Updates metadata and properties for an existing Notion page. |
| [set\_page\_archived\_status](#set-page-archived-status-tool) | Archives or restores a Notion page by updating its archived status. |
| [list\_page\_children](#list-page-children-tool) | Lists the direct child pages under a specified Notion page. |
| [append\_page\_blocks](#append-page-blocks-tool) | Appends new content blocks to a Notion page. |
| [update\_text\_block](#update-text-block-tool) | Updates the text content of a supported block on a Notion page. |
| [delete\_block](#delete-block-tool) | Deletes a single block subtree from a Notion page. |
| [list\_open\_comments](#list-open-comments-tool) | Retrieves open (unresolved) comment threads for a Notion page. |
| [add\_comment](#add-comment-tool) | Adds a new page-level comment or replies to an existing discussion on a Notion page. |

## Install the Notion Pages MCP server

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

#### Download the Notion connector from the Community library

View download steps

Complete the following steps to install the Notion connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

#### OAuth 2.0 authentication

Use OAuth 2.0 to create a public integration that accesses multiple Notion workspaces.

View OAuth 2.0 authentication steps

Complete the following steps to set up your Notion connection using OAuth 2.0:

1. Enter a **Connection name** that identifies which Notion instance Workato is connected to.
   
2. Select **OAuth (Public integration)** in the **Authentication** field.
   
3. Enter the **Client ID** and **Client secret** for your Notion integration. Refer to Notion's [Public integration auth flow setup](https://developers.notion.com/docs/authorization#public-integration-auth-flow-set-up) guide to generate these credentials.
   
4. Click **Connect** to complete the setup.
   

#### API key authentication

Use an API key for authentication to create an internal integration accessible only in a specific Notion workspace.

View API key authentication steps

Complete the following steps to set up your Notion connection using an API key:

1. Enter a **Connection name** that identifies which Notion instance Workato is connected to.
   
2. Select **API Key (Internal integration)** in the **Authentication** field.
   
3. Enter your Notion integration's **Integration Token**. Refer to Notion's [Internal integration auth flow setup](https://developers.notion.com/docs/authorization#internal-integration-auth-flow-set-up) guide to generate this token.
   
4. Click **Connect** to complete the setup.
   

## How to use Notion Pages MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_pages tool

The **search\_pages** tool searches for Notion pages by keyword and returns a list of pages that match the query text across your accessible Notion workspace. Your LLM uses this tool to find a Notion page by name, topic, or keywords.

**Try asking**:

- `Find my project planning page in Notion.`
- `Search for pages about API documentation.`
- `Look for the team onboarding guide.`
- `Find pages related to the product roadmap.`

### get\_page tool

The **get\_page** tool retrieves metadata and properties for a Notion page including page identifier, title, parent reference, archived status, and created/updated timestamps. Your LLM uses this tool to find details about a specific page, such as its title, location, metadata, or current status, or to confirm page identity before performing follow-on actions.

**Try asking**:

- `Show me the metadata for the API documentation page.`
- `Get the details for this project planning page.`
- `What's the parent page of the onboarding guide?`
- `Is this page archived or active?`

### get\_page\_content tool

The **get\_page\_content** tool retrieves the block content of a Notion page, with pagination for long pages. Your LLM uses this tool to read or review the contents of a specific Notion page. Your LLM retrieves content incrementally for long pages.

**Try asking**:

- `Read the content of the team onboarding page.`
- `Show me what's in the API documentation.`
- `Get the full contents of the project requirements page.`
- `What does the troubleshooting guide say?`

### create\_page tool

The **create\_page** tool creates a new Notion page under a specified parent. Your LLM uses this tool to create a new page in Notion, either as a standalone page or as a child of an existing page or database entry.

**Try asking**:

- `Create a new page for meeting notes under the Team folder.`
- `Make a new project planning page in the workspace.`
- `Create a child page under the API documentation for authentication.`
- `Add a new page to the Product section for the feature spec.`

### update\_page tool

The **update\_page** tool updates metadata and properties for an existing Notion page. Your LLM uses this tool to modify page properties, update metadata, or change page attributes.

**Try asking**:

- `Update the status property on this project page to 'In Progress'.`
- `Change the owner of the requirements page to Sarah.`
- `Update the due date property to next Friday.`
- `Modify the priority tag on this page to 'High'.`

### set\_page\_archived\_status tool

The **set\_page\_archived\_status** tool archives or restores a Notion page by updating its archived status. Your LLM uses this tool to archive, unarchive, retire, restore, or reactivate a page.

**Try asking**:

- `Archive the old roadmap page.`
- `Restore the archived meeting notes from last quarter.`
- `Retire the deprecated product specification page.`
- `Unarchive the Q3 planning document.`

### list\_page\_children tool

The **list\_page\_children** tool retrieves the direct child pages under a Notion page that you specify. Your LLM uses this tool to see what pages are nested under another page, explore related documentation, or navigate through the page hierarchy.

**Try asking**:

- `What pages are under the Product Documentation page?`
- `Show me the child pages of the Team Wiki.`
- `List the subpages under the API documentation.`
- `What's nested under the Project Planning page?`

### append\_page\_blocks tool

The **append\_page\_blocks** tool appends new content blocks to a Notion page. Your LLM uses this tool to add new content to an existing page, such as notes, sections, bullets, or code snippets.

**Try asking**:

- `Add a new section to the troubleshooting guide about timeout errors.`
- `Append these meeting notes to the project page.`
- `Add a bullet list of action items to the planning page.`
- `Insert a code snippet at the end of the API documentation.`

### update\_text\_block tool

The **update\_text\_block** tool updates the text content of a supported block on a Notion page. Your LLM uses this tool to edit or correct the text of a specific block within a page.

**Try asking**:

- `Update the heading text in the introduction block.`
- `Fix the typo in the second paragraph.`
- `Change the text in the first bullet point.`
- `Edit the description in the overview section.`

### delete\_block tool

The **delete\_block** tool deletes a single block subtree from a Notion page. Your LLM uses this tool only when you explicitly ask to remove specific page content. **Try asking**:

- `Delete the outdated section from this page.`
- `Remove the old timeline block from the roadmap.`
- `Delete the third bullet point in the list.`
- `Remove the deprecated warning section.`

### list\_open\_comments tool

The **list\_open\_comments** tool retrieves open (unresolved) comment threads for a Notion page. Your LLM uses this tool to review feedback, see comments, or understand discussion context on a page.

**Try asking**:

- `Show me the open comments on the requirements page.`
- `What feedback is pending on this document?`
- `List the unresolved comments on the API spec.`
- `What discussions are active on this page?`

### add\_comment tool

The **add\_comment** tool adds a new page-level comment or replies to an existing discussion on a Notion page. Your LLM uses this tool to leave feedback, ask questions, or participate in discussions on a page.

**Try asking**:

- `Add a comment asking about the timeline on this page.`
- `Leave feedback on the requirements document about the scope.`
- `Reply to the open discussion about the API design.`
- `Comment on this page to flag the outdated information.`

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
