---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/excel-mcp-server.md'
description: >-
  Use the Excel MCP server to connect your LLM to Microsoft Excel with a curated
  set of tools to read, update, and manage workbooks and tabular data stored in
  Microsoft 365.
---

# Excel MCP server

The Excel MCP server enables LLMs to read, update, and structurally modify Microsoft Excel workbooks stored in Microsoft 365 through natural conversation. It provides tools to access tabular data, append and update rows, manage worksheets, and perform atomic multi-step updates without requiring direct interaction with the Excel interface.

## Uses

Use the Excel MCP server to perform the following actions:

- Retrieve workbook metadata including worksheet names and Excel Tables
- Read cell data, formulas, and table contents from worksheets
- Append new rows to trackers or data tables
- Update specific cell values or formulas in ranges
- Perform atomic multi-step updates that must succeed or fail together
- Add new worksheets to workbooks
- Rename existing worksheets
- Delete worksheets when explicitly requested
- Access named ranges and Excel Table definitions

### Example prompts

- `What worksheets are in my Sales Tracker workbook?`
- `Read the data from the Q1 Revenue sheet.`
- `Add these three deals to my Pipeline tracker.`
- `Update the status column to 'Closed Won' for the Acme Corp row.`
- `Create a new January 2026 tab and add headers.`
- `Rename Sheet1 to 'Sales Pipeline'.`
- `Get the current session ID for this workbook.`
- `Show me the data in the Revenue table.`

## Excel MCP server tools

The Excel MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_workbook\_info](#get-workbook-info-tool) | Retrieves worksheet names, named ranges, Excel Table definitions, and session metadata for a workbook. |
| [get\_workbook\_content](#get-workbook-content-tool) | Retrieves bounded cell data, formulas, and table contents from ranges or worksheets you specify. |
| [append\_rows](#append-rows-tool) | Appends one or more rows of data to an existing worksheet or Excel Table. |
| [update\_range\_values](#update-range-values-tool) | Updates values or formulas in a range or Excel Table you specify. |
| [batch\_update](#batch-update-tool) | Applies multiple workbook updates as a single atomic change. |
| [add\_worksheet](#add-worksheet-tool) | Adds a new worksheet (tab) to an existing workbook. |
| [rename\_worksheet](#rename-worksheet-tool) | Renames an existing worksheet (tab) in a workbook. |
| [delete\_worksheet](#delete-worksheet-tool) | Deletes an existing worksheet (tab) from a workbook. |

## Install the Excel MCP server

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
    

## Excel connection setup

View Excel connection setup steps

Workato supports the following types of connections to Excel:

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

### Authorization code grant authentication (OAuth 2.0)

View authorization code grant authentication steps

This authentication method requires the following value for tenant-specific account types:

- Tenant ID/Domain

#### Minimum and default scopes

View minimum and default scopes

The Excel connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

| Permission | Description | Relevant action or trigger |
| --- | --- | --- |
| `Files.Read` | Allows the app to read the signed-in user's files. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Files.ReadWrite` | Allows the app to read and write to the signed-in user's files. | All actions in `Files.Read` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. |
| `Group.Read.All` | Allows the app to read files for all groups the signed-in user can access. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.ReadWrite.All` | Allows the app to read and write to documents in all SharePoint site collections on behalf of the signed-in user. On the consent page, this scope appears as the `Maintain access to data you have given it access to` permission. | All actions in `Sites.Read.All` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. Add this permission for all actions to preserve the connection's validity. |
| `User.Read` | Allows the app to sign in and read the profile of signed-in users. | Add this permission for all actions. |
| `offline_access` | Allows the app to access Microsoft Graph data after the user has signed out or the session has expired. | You must add this permission to establish a connection. |

To limit the connection to specific SharePoint sites instead of all sites, add the following scope:

- `Sites.Selected`

This scope doesn't grant your app access to any sites by itself. A SharePoint or Global admin must grant your app access to each site you plan to use. After access is granted, Excel actions can work with files on that site. Refer to [Grant site access for Sites.Selected](/en/data-orchestration/data-pipeline-recipe/configure-sharepoint#grant-site-access-for-sites-selected) for more information.

When you use `Sites.Selected`, file and table pick lists show only the files that the connected user can access.

You must add the following minimum scopes to establish a connection to Excel with authorization code grant authentication:

- `Files.Read`
- `offline_access`
- `User.Read`

#### Excel setup for authorization code grant authentication

Complete the following steps to set up Excel for authorization code grant authentication:

- [Register the Workato App in the Azure portal](#auth-register)
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
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Excel connector](/en/connectors/excel#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant ID) from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Excel with authorization code grant authentication

View connect to Excel with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Excel in Workato:

1. Click **Create > Connection**.
   
2. Search for `Excel` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant-specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that aren't restricted to a specific organization (tenant).
   
   ![Common connection](/assets/connect-common.B1wFCm02.png)_Common connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant-specific.QonywkYE.png)_Tenant specific connections_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID), or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `Files.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#code-grant-minimum-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
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

The Excel connector requests the following scopes for client credentials-based connections by default. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Application** permissions in the Azure portal.

| Permission | Description | Relevant action or trigger |
| --- | --- | --- |
| `Files.Read.All` | Allows the app to read the signed-in user's files. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Files.ReadWrite.All` | Allows the app to read and write to the signed-in user's files. | All actions in `Files.Read` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get cells, Get rows, List tables, List worksheets, and Search workbooks |
| `Sites.ReadWrite.All` | Allows the app to read and write to documents in all SharePoint site collections on behalf of the signed-in user. On the consent page, this scope appears as the `Maintain access to data you have given it access to` permission. | All actions in `Sites.Read.All` and Add a table, Add a worksheet, Add rows in batch, Delete row, and Update row. This permission is recommended for all actions to preserve the connection's validity. |
| `User.Read.All` | Allows the app to sign in and read the profile of signed-in users. | This permission is recommended for all actions. |

You must add the following minimum scopes to establish a connection to Excel with client credentials-based authentication:

- `Files.Read.All`
- `User.Read.All`

#### Excel setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Excel for client credentials-based authentication:

- [Register the Workato App in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Excel connector](/en/connectors/excel#admin-consent) to learn more.
   

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

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure Portal steps

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
   

#### Connect to Excel with client credentials-based authentication

View connect to Excel with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Excel in Workato:

1. Click **Create > Connection**.
   
2. Search for `Excel` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Tenant specific connection type](/assets/connect-tenant-specific-2.C8paKuNY.png)_Tenant specific account connection type_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

### Project property configuration

The Excel MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `DEFAULT_RANGE_COLUMNS` | Applies per worksheet when no ranges are explicitly provided. Defaults to `A:Z` (26 columns) per worksheet. |
| `DEFAULT_RANGE_ROWS` | Combines with `DEFAULT_RANGE_COLUMNS`. The default retrieval scope is `A1:Z200` on the first visible worksheet by tab order. Defaults to 200 rows. |
| `DEFAULT_MAX_CELLS` | Applies when the `max_cells` parameter is omitted. Defaults to `20,000` cells. |
| `HARD_MAX_CELLS` | Absolute upper bound enforced regardless of requested parameters. Defaults to `100,000` cells. |
| `MAX_RANGES_PER_CALL` | Maximum distinct ranges per call. Named ranges and Excel table names each count as one range toward this quota. Defaults to `20`. |
| `MAX_OPERATIONS_PER_BATCH` | Maximum operations in a single `batch_update` call. Defaults to `10`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes. For example, set `MAX_RANGES_PER_CALL` to `15` or `MAX_OPERATIONS_PER_BATCH` to `5`.
   

## How to use Excel MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_workbook\_info tool

The **get\_workbook\_info** tool retrieves worksheet names, named ranges, Excel Table definitions, and session metadata for a workbook. Your LLM uses this tool to find worksheet names or identifiers, the current `session_id` before any write action, information about named ranges or Excel Tables, or confirmation of structure before planning updates.

**Try asking**:

- `What worksheets are in my Sales Tracker workbook?`
- `Show me the structure of the Q4 Planning workbook.`
- `What Excel Tables exist in this workbook?`
- `Get the session ID for my Pipeline tracker.`

### get\_workbook\_content tool

The **get\_workbook\_content** tool retrieves bounded cell data, formulas, and table contents from ranges or worksheets you specify. Your LLM uses this tool to read values or formulas, understand workbook contents, retrieve tables or ranges for analysis, or get current values before an update.

**Try asking**:

- `Read the data from the Q1 Revenue sheet.`
- `Show me the values in cells A1 through E10.`
- `Get the contents of the Pipeline table.`
- `What's in the Sales worksheet?`

### append\_rows tool

The **append\_rows** tool appends one or more rows of data to an existing worksheet or Excel Table. Your LLM uses this tool to add new entries to a tracker or table, log operational records over time, or reserve empty rows before population.

**Try asking**:

- `Add these three deals to my Pipeline tracker.`
- `Append today's sales data to the Revenue sheet.`
- `Log these customer records in the CRM table.`
- `Add a new row to the expense tracker with Date: 1/15/2026, Amount: $250.`

### update\_range\_values tool

The **update\_range\_values** tool updates values or formulas in a range or Excel Table you specify. Your LLM uses this tool to update specific values, correct or replace values in a range, write or update formulas, or populate previously appended empty rows.

**Try asking**:

- `Update the status column to 'Closed Won' for the Acme Corp row.`
- `Change the Q4 forecast in cell B12 to $450,000.`
- `Set the priority to 'High' for rows 5 through 8.`
- `Update the formula in cell D2 to calculate the total.`

### batch\_update tool

The **batch\_update** tool applies multiple workbook updates as a single atomic change. Your LLM uses this tool only when atomicity matters, such as appending rows and populating formulas where partial application would leave the workbook inconsistent, or creating a worksheet and initializing it with headers and values as one change.

**Try asking**:

- `Create a new January 2026 tab and add headers in one update.`
- `Append these entries and update the summary totals together.`
- `Add rows and calculate their totals in a single atomic change.`
- `Initialize the new sheet with headers and formulas at once.`

### add\_worksheet tool

The **add\_worksheet** tool adds a new worksheet (tab) to an existing workbook. Your LLM uses this tool to create a new tab or add a worksheet for a new reporting period or tracking category.

**Try asking**:

- `Add a new tab called 'January 2026' to my monthly tracker.`
- `Create a new worksheet named 'Archive'.`
- `Add a 'Completed Tasks' tab to the project tracker.`
- `Insert a new sheet for Q2 metrics.`

### rename\_worksheet tool

The **rename\_worksheet** tool renames an existing worksheet (tab) in a workbook. Your LLM uses this tool to rename a tab or standardize worksheet naming.

**Try asking**:

- `Rename Sheet1 to 'Sales Pipeline'.`
- `Change the 'January' tab name to 'January 2026'.`
- `Rename the 'Temp' sheet to 'Archive'.`
- `Update the sheet name from 'Data' to 'Q1 Revenue'.`

### delete\_worksheet tool

The **delete\_worksheet** tool deletes an existing worksheet (tab) from a workbook. Your LLM uses this tool to delete a worksheet.

**Try asking**:

- `Delete the 'Archive' tab from my tracker.`
- `Remove the 'Old Data' sheet from the workbook.`
- `Delete Sheet2 since we don't need it anymore.`
- `Remove the 'Scratch' worksheet.`

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
