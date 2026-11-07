---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/google-sheets-mcp-server.md'
description: >-
  Use the Google Sheets MCP server to connect your LLM to Google Sheets with a
  curated set of tools to access tabular data, append and update rows, manage
  sheets, and perform multi-step updates.
---

# Google Sheets MCP server

The Google Sheets MCP server enables LLMs to read, update, and structurally modify Google Sheets spreadsheets in a reliable, permission-respecting manner. It provides tools to access tabular data, append and update rows, manage sheets, and perform multi-step updates through natural conversation.

## Uses

Use the Google Sheets MCP server when you plan to perform the following actions:

- Create new spreadsheets, trackers, or reports
- Read values, formulas, and structure from existing spreadsheets
- Append new rows to operational trackers or data tables
- Update specific cell values or formulas in targeted ranges
- Add, rename, or delete sheets (tabs) within a spreadsheet
- Perform multi-step updates that must succeed or fail together
- Retrieve spreadsheet metadata for navigation and planning

### Example prompts

Use the following example prompts to invoke Google Sheets MCP server tools:

- `Add these three deals to my Sales Pipeline sheet.`
- `Update the status to 'Closed Won' for the Acme Corp deal.`
- `Show me all the data in the Q1 Revenue sheet.`
- `Add a new tab called 'January 2026' to my monthly tracker.`
- `Rename Sheet1 to 'Pipeline Overview'.`
- `What sheets are in my Q4 Planning spreadsheet?`

## Google Sheets MCP server tools

The Google Sheets MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_spreadsheet](#create-spreadsheet-tool) | Creates a new Google Sheets spreadsheet. |
| [get\_spreadsheet\_info](#get-spreadsheet-info-tool) | Retrieves metadata about a spreadsheet needed for navigation, sheet selection, and write preconditions. |
| [get\_sheet\_info](#get-sheet-info-tool) | Retrieves metadata about a specific sheet needed for navigation, row selection, and write preconditions. |
| [get\_spreadsheet\_content](#get-spreadsheet-content-tool) | Retrieves spreadsheet content including sheet structure and cell-level data. |
| [append\_rows](#append-rows-tool) | Appends one or more rows of structured data to an existing sheet or table. |
| [update\_range\_values](#update-range-values-tool) | Updates values and/or formulas in a range you specify. |
| [batch\_update](#batch-update-tool) | Applies multiple spreadsheet updates as a single change. |
| [add\_sheet](#add-sheet-tool) | Adds a new sheet (tab) to an existing spreadsheet. |
| [rename\_sheet](#rename-sheet-tool) | Renames an existing sheet (tab) in a spreadsheet. |
| [delete\_sheet](#delete-sheet-tool) | Deletes an existing sheet (tab) from a spreadsheet. |

## Install the Google Sheets MCP server

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
    

## Google Sheets connection setup

View Google Sheets connection setup steps

The Google Sheets connector supports the following authentication methods:

- [Service account](#service-account)
- [OAuth 2.0](#oauth-2-0)

> **SERVICE ACCOUNT AUTHENTICATION**
> 
> You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

### Service account

The email associated with your service account must have access to the Google Sheets you plan to use in recipes. You can share specific sheets from within Google Sheets.

![Share Google Sheets spreadsheets with your service account email](/assets/share.BjIcNo1z.png)_Share Google Sheets spreadsheets with your service account email_

#### Set up a Google service account

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Sheets API](https://support.google.com/googleapi/answer/6158841)

View Service account setup steps

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account.
   
   ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use.
   
   ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later.
   
   ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

#### Connect your service account to Workato

View Connect your service account to Workato steps

Complete the following steps to set up a service account connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Sheets** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Google Sheet service account connection fields](/assets/SAconnection.CFNAkoVh.png)_Google Sheets service account connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select `Service account`.
   
6. Enter your service account email in the **GCP Project service account email** field.
   
7. Enter the entire **Private key** for your service account, including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
   
8. Optional. Go to **Advanced settings** and use the **Requested permissions (Service auth scopes)** drop-down menu to adjust the scopes for your connection. Workato requests the **See and download all your Google Drive files** and **See, edit, create, and delete all your Google Sheets spreadsheets** permissions by default. The permissions you select from the drop-down menu overwrite the default permissions.
   
9. Optional. Use the **Disable formula** drop-down menu to select whether to disable adding and updating rows with formulas.
   
10. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
    
11. Click **Sign in with Google**.
    
12. Sign in with your Google account.
    
13. Click **Allow** to enable Workato to access your Google account.
    

Complete the following steps to set up a service account connection:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Sheets** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Google Sheet service account connection fields](/assets/SAconnection.CFNAkoVh.png)_Google Sheets service account connection fields_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select `Service account`.
   
6. Enter your service account email in the **GCP Project service account email** field.
   
7. Enter the entire **Private key** for your service account, including `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----\n`.
   
8. Optional. Go to **Advanced settings** and use the **Requested permissions (Service auth scopes)** drop-down menu to adjust the scopes for your connection. Workato requests the **See and download all your Google Drive files** and **See, edit, create, and delete all your Google Sheets spreadsheets** permissions by default. The permissions you select from the drop-down menu overwrite the default permissions.
   
9. Optional. Use the **Disable formula** drop-down menu to select whether to disable adding and updating rows with formulas.
   
10. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
    
11. Click **Sign in with Google**.
    
12. Sign in with your Google account.
    
13. Click **Allow** to enable Workato to access your Google account.
    

### OAuth 2.0

View OAuth 2.0 setup steps

Complete the following steps to set up an OAuth 2.0 connection:

1. Click **Create > Connection** or press C twice.
   
2. Provide a name for your connection in the **Connection name** field.
   
   ![OAuth 2.0 connection fields](/assets/connection.C-Rm0AtF.png)_OAuth 2.0 connection fields_
   
3. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
4. Search for and select **Google Sheets** as your connection on the **New connection** page.
   
5. Use the **Authentication type** drop-down menu to select `OAuth 2.0`.
   
6. Optional. Use the **Disable formula** drop-down menu to select whether to disable adding and updating rows with formulas.
   
7. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
   
8. Click **Sign in with Google**.
   
9. Sign in with your Google account.
   
10. Click **Allow** to enable Workato to access your Google account.
    
    ![Click Allow to enable Workato to access your Google account](/assets/allow.DBxsc8xF.png)_Click **Allow** to enable Workato to access your Google account_
    

## How to use Google Sheets MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_spreadsheet tool

The **create\_spreadsheet** tool creates a new Google Sheets spreadsheet. Your LLM uses this tool to start new operational spreadsheets, create trackers or reports from scratch, or initialize a spreadsheet before populating it with data. The spreadsheet can be created empty or initialized with a basic structure such as one or more sheets and optional header rows.

**Try asking**:

- `Create a new spreadsheet called 'Q1 Sales Pipeline' with columns for Deal Name, Stage, Amount, and Close Date.`
- `Start a new project tracker with tabs for Tasks, Timeline, and Resources.`
- `Make a new expense report spreadsheet with headers for Date, Category, Amount, and Notes.`
- `Create an empty spreadsheet called 'Monthly Metrics Dashboard'.`

### get\_spreadsheet\_info tool

The **get\_spreadsheet\_info** tool retrieves metadata about a Google Sheets spreadsheet needed for safe navigation, sheet selection, and write preconditions, without returning cell-level content. Your LLM uses this tool to understand spreadsheet structure, get sheet names before performing operations, retrieve the current revision ID before writes, or check for protected areas.

**Try asking**:

- `What sheets are in my Q4 Planning spreadsheet?`
- `Show me the structure of the 'Sales Dashboard' spreadsheet.`
- `Check if the Pipeline tracker has any protected sheets.`
- `Get the metadata for my team's quarterly report before I update it.`

### get\_sheet\_info tool

The **get\_sheet\_info** tool retrieves metadata about a specific sheet needed for navigation, row selection, and write preconditions, without returning cell-level content. Your LLM uses this tool to verify sheet properties, check for protection constraints, or understand the current structure before making updates.

**Try asking**:

- `Get information about the 'January 2026' sheet in my tracker.`
- `Check if the Pipeline sheet is protected or locked.`
- `Show me the metadata for the Q1 Revenue tab.`
- `What's the current row count in the Deals sheet?`

### get\_spreadsheet\_content tool

The **get\_spreadsheet\_content** tool retrieves spreadsheet content including sheet structure and cell-level data. Your LLM uses this tool to read values or formulas, understand spreadsheet contents for summarization, retrieve tables for analysis, or get current values before applying updates.

**Try asking**:

- `Show me all the data in the Sales Pipeline sheet.`
- `Read the values from the Q1 Revenue tab.`
- `Get the contents of cells A1 through E10 in the Dashboard sheet.`
- `What's currently in my expense tracker for January?`

### append\_rows tool

The **append\_rows** tool appends one or more rows of structured data to an existing sheet or table. Your LLM uses this tool for operational workflows such as pipeline tracking and ongoing data collection, where new entries are added over time without overwriting existing data.

**Try asking**:

- `Add these three deals to my Sales Pipeline sheet.`
- `Append today's incident reports to the tracking log.`
- `Add a new row to the expense tracker with Date: 1/15/2026, Category: Travel, Amount: $250.`
- `Log these customer support tickets in the Issues sheet.`

### update\_range\_values tool

The **update\_range\_values** tool updates values and/or formulas in a range you specify. Your LLM uses this tool for user-directed edits to existing spreadsheet content, including updating specific values, correcting data, replacing formulas, or populating previously appended empty rows.

**Try asking**:

- `Update the Stage column to 'Closed Won' for the Acme Corp deal.`
- `Change the Q4 revenue forecast in cell B12 to $450,000.`
- `Set the status to 'Complete' for all tasks in rows 5 through 8.`
- `Update the formula in cell D2 to calculate the quarterly average.`

### batch\_update tool

The **batch\_update** tool applies multiple spreadsheet updates as a single atomic change, ensuring all requested updates succeed or none are applied. Your LLM uses this tool when atomicity matters, such as appending rows and populating formulas in one operation, updating multiple ranges that represent a single logical edit, or creating and initializing a new sheet simultaneously.

**Try asking**:

- `Add a new deal row and calculate its projected revenue in one update.`
- `Create a 'February 2026' tab and initialize it with the same headers as January.`
- `Update the pipeline stages and recalculate all forecast formulas together.`
- `Append these entries and update the summary totals at the same time.`

### add\_sheet tool

The **add\_sheet** tool adds a new sheet (tab) to an existing spreadsheet. Your LLM uses this tool for structural organization workflows such as creating new time-period tabs or adding tracking tabs.

**Try asking**:

- `Add a new tab called 'January 2026' to my monthly tracker.`
- `Create a new sheet named 'Archive' in the Q4 Planning spreadsheet.`
- `Add a 'Completed Tasks' tab to the project tracker.`
- `Insert a new sheet for Q2 metrics in the dashboard.`

### rename\_sheet tool

The **rename\_sheet** tool renames an existing sheet (tab) in a spreadsheet. Your LLM uses this tool for structural cleanup and reorganization.

**Try asking**:

- `Rename Sheet1 to 'Sales Pipeline'.`
- `Change the 'January' tab name to 'January 2026'.`
- `Rename the 'Temp' sheet to 'Archive'.`
- `Update the sheet name from 'Data' to 'Q1 Revenue'.`

### delete\_sheet tool

The **delete\_sheet** tool deletes an existing sheet (tab) from a spreadsheet. This is a destructive operation that removes the sheet and its contents. Your LLM uses this tool to delete a sheet when you ask.

**Try asking**:

- `Delete the 'Archive' tab from my tracker.`
- `Remove the 'Old Data' sheet from the Q4 Planning spreadsheet.`
- `Delete Sheet2 since we don't need it anymore.`
- `Remove the 'Scratch' tab from the project dashboard.`

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
