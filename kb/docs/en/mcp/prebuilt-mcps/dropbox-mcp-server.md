---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/dropbox-mcp-server.md'
description: >-
  Use the Dropbox MCP server to connect your LLM to Dropbox with tools to find,
  browse, retrieve, organize, and share files through natural language.
---

# Dropbox MCP server

The Dropbox MCP server enables LLMs to interact with files and folders stored in Dropbox through natural conversation. It provides tools to search files, browse folder contents, retrieve file metadata, access file content, organize files, and share files through links without requiring direct interaction with the Dropbox interface.

## Uses

Use the Dropbox MCP server to perform the following actions:

- List files and subfolders within a specified Dropbox folder
- Search for files using keywords and filters
- Retrieve metadata for a specific file or folder
- Access a file's content
- Move or rename a file or folder
- Create a duplicate of a file
- Create a new folder
- Delete a file or folder
- Create or retrieve a shared link for a file or folder
- List existing shared links for a file or across the account
- Revoke a shared link to remove access

### Example prompts

Use the following example prompts to invoke Dropbox MCP server tools:

- `What's inside my Projects folder?`
- `Find files related to the Q2 budget.`
- `Get the metadata for this file before I move it.`
- `Open this document so I can review it.`
- `Move this file to the Archive folder.`
- `Rename this folder to match the new project name.`
- `Make a copy of this file before I start editing.`
- `Create a new folder called Client Deliverables.`
- `Delete this old draft.`
- `Share a link to this file with the client.`
- `Is this file already shared?`
- `Revoke the shared link for this document.`

## Dropbox MCP server tools

The Dropbox MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_folder](#list-folder-tool) | Lists files and subfolders within a Dropbox folder you specify. |
| [search\_files](#search-files-tool) | Searches for files using keywords and filters. |
| [get\_file\_metadata](#get-file-metadata-tool) | Retrieves metadata for a file or folder you specify. |
| [download\_file](#download-file-tool) | Retrieves access to a file's content. |
| [move\_file](#move-file-tool) | Moves or renames a file or folder. |
| [copy\_file](#copy-file-tool) | Creates a duplicate of a file. |
| [create\_folder](#create-folder-tool) | Creates a new folder. |
| [delete\_file](#delete-file-tool) | Deletes a file or folder. |
| [create\_shared\_link](#create-shared-link-tool) | Creates or retrieves a shared link for a file or folder. |
| [list\_shared\_links](#list-shared-links-tool) | Lists shared links for a file or across the account. |
| [revoke\_shared\_link](#revoke-shared-link-tool) | Revokes a shared link. |

## Install the Dropbox MCP server

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
    

## Dropbox connection setup

View Dropbox connection setup steps

The Dropbox connector uses OAuth 2.0 authentication.

### Minimum and default scopes

The Dropbox connector supports two scope types: **individual scopes** and **team scopes**.

#### Individual scopes

View individual scopes

The following individual scopes are requested by default:

- `account_info.read`
- `files.metadata.write`
- `files.content.write`
- `files.content.read`
- `sharing.write`
- `file_requests.write`
- `contacts.write`

The minimum required scope is `account_info.read`, which is requested in addition to any selected permissions. You can select scopes from the drop-down menu to overwrite the default scopes.

#### Team scopes

View team scopes

The following team scopes are requested by default:

- `account_info.read`
- `files.metadata.write`
- `files.content.write`
- `files.content.read`
- `sharing.write`
- `file_requests.write`
- `contacts.write`

The minimum required scopes are `team_info.read` and `team_data.member`, which are requested in addition to any selected permissions. Note that `team_data.member` is required for folder access in team accounts. You can select scopes from the drop-down menu to overwrite the default scopes.

> **INDIVIDUAL SCOPES AND TEAM SCOPES**
> 
> `account_info.read` is also requested when team scopes are selected but individual scopes are left blank.

### Connect to Dropbox with OAuth 2.0

View connect to Dropbox with OAuth 2.0 steps

Complete the following steps to connect to Dropbox in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Dropbox` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Dropbox connection](/assets/dropbox-connection-setup.CSoyzHTt.png)_Dropbox connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand **Advanced settings** to select any additional individual or team scopes required by the actions and triggers you plan to use. Refer to [Minimum and default scopes](#scopes) for more information.
   
6. Click **Connect**.
   
7. Sign in to your Dropbox account and click **Allow** to grant Workato access when prompted.
   

### Project property configuration

The Dropbox MCP server supports the following project-level properties to control behavior and defaults:

| Parameter | Description |
| --- | --- |
| `inline_content_max_size_bytes` | Defines the maximum file size eligible for inline content return in download\_file. Files larger than this threshold return only a temporary access link. Recommended default: `1,048,576` bytes (1 MB). |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes.
   

## How to use Dropbox MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_folder tool

The **list\_folder** tool lists files and subfolders within a specified Dropbox folder. Your LLM uses this tool to view folder contents or to browse your Dropbox file structure.

**Try asking**:

- `What's inside my Projects folder?`
- `Show me the contents of this folder.`
- `Browse my Dropbox root folder.`
- `What files and subfolders are in the Client Work directory?`

### search\_files tool

The **search\_files** tool searches for files using keywords and filters. Your LLM uses this tool to find files by name, keyword, or other attributes without navigating folder by folder.

**Try asking**:

- `Find files related to the Q2 budget.`
- `Search for any presentations about the product launch.`
- `Look for all PDFs with "contract" in the name.`
- `Find the latest version of the project proposal.`

### get\_file\_metadata tool

The **get\_file\_metadata** tool retrieves metadata, such as size, type, and modification dates, for a file or folder you specify. Your LLM uses this tool to confirm the file is correct before performing an action on it.

**Try asking**:

- `Get the metadata for this file before I move it.`
- `When was this file last modified?`
- `Confirm the details of this folder before I delete it.`
- `What is the size and type of this file?`

### download\_file tool

The **download\_file** tool retrieves access to a file's content. Your LLM uses this tool to open or view a file stored in Dropbox.

> **CONTENT LIMITATIONS**
> 
> The **download\_file** tool doesn't support binary file content.

**Try asking**:

- `Open this document so I can review it.`
- `Show me the contents of this file.`
- `Retrieve this spreadsheet so I can read the data.`
- `Access this file so I can summarize it.`

### move\_file tool

The **move\_file** tool moves or renames a file or folder. Your LLM uses this tool to reorganize files into a different location or give a file or folder a new name.

**Try asking**:

- `Move this file to the Archive folder.`
- `Rename this folder to match the new project name.`
- `Move all draft files into the Drafts directory.`
- `Rename this document to the final version name.`

### copy\_file tool

The **copy\_file** tool creates a duplicate of a file. Your LLM uses this tool when you explicitly ask to duplicate a file or need a working copy before making edits.

**Try asking**:

- `Make a copy of this file before I start editing.`
- `Duplicate this template so I can use it for a new project.`
- `Create a backup copy of this document.`
- `Copy this file into the new client folder.`

### create\_folder tool

The **create\_folder** tool creates a new folder in Dropbox. Your LLM uses this tool to set up a new location for organizing files.

**Try asking**:

- `Create a new folder called Client Deliverables.`
- `Set up a folder for the new project.`
- `Add a subfolder inside the Q2 directory.`
- `Create an Archive folder to store old files.`

### delete\_file tool

The **delete\_file** tool deletes a file or folder. Your LLM uses this tool only when you explicitly request deletion.

**Try asking**:

- `Delete this old draft.`
- `Remove this folder and its contents.`
- `Delete the duplicate files from this directory.`
- `Permanently remove this outdated document.`

### create\_shared\_link tool

The **create\_shared\_link** tool creates or retrieves a shared link for a file or folder. Your LLM uses this tool to share a file with someone outside your Dropbox account.

**Try asking**:

- `Share a link to this file with the client.`
- `Generate a shareable link for this folder.`
- `Create a link I can send to the team.`
- `Get the shared link for this document.`

### list\_shared\_links tool

The **list\_shared\_links** tool lists shared links for a file or across the account. Your LLM uses this tool to check whether a file is already shared or view all existing shared links.

**Try asking**:

- `Is this file already shared?`
- `Show me all shared links for this document.`
- `List all active shared links across my Dropbox.`
- `Check what files I currently have shared.`

### revoke\_shared\_link tool

The **revoke\_shared\_link** tool revokes a shared link, removing access for anyone who has it. Your LLM uses this tool to stop sharing a file or folder.

**Try asking**:

- `Revoke the shared link for this document.`
- `Remove access to this shared file.`
- `Stop sharing this folder.`
- `Disable the link I sent for this file.`

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
