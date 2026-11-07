---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/google-tasks-mcp-server.md'
description: >-
  Use the Google Tasks MCP server to connect your LLM to Google Tasks with tools
  to create, view, edit, complete, reopen, delete, move, and reorder tasks, and
  to create and browse task lists.
---

# Google Tasks MCP server

The Google Tasks MCP server enables LLMs to interact with Google Tasks for checklist management through natural conversation. It provides tools to create, view, edit, complete, reopen, delete, move, and reorder tasks, and to create or browse task lists, without requiring direct interaction with the Google Tasks interface.

## Uses

Use the Google Tasks MCP server to perform the following actions:

- Capture a new task with a title, notes, and a due date.
- Review what's on an existing list.
- Mark a task complete, or reopen a task marked complete by mistake.
- Update a task's title, notes, or due date, or explicitly clear a field.
- Break a task into subtasks by nesting it under a parent task.
- Move a task to a different list or reorder it among its siblings.
- Create a new task list to organize tasks.
- Browse the task lists in your account.

### Example prompts

Use the following example prompts to invoke Google Tasks MCP server tools:

- `Add a task to follow up with the vendor on the signed SOW.`
- `What's due on my list today?`
- `Mark "Submit expense report" as done.`
- `Reopen the task I marked complete by mistake.`
- `Change the due date on my renewal call task to next Friday.`
- `Move my onboarding task to the Customer Success list.`
- `Break "Plan the offsite" into a few subtasks.`
- `Create a new list called Q4 Renewals.`

## Google Tasks MCP server tools

The Google Tasks MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [create\_task](#create-task-tool) | Creates a new task in a task list. |
| [get\_task](#get-task-tool) | Retrieves a single task by its identifier. |
| [list\_tasks](#list-tasks-tool) | Lists tasks in a task list and optionally filters by completion status, due date range, and whether a task is dated, undated, or overdue. |
| [update\_task](#update-task-tool) | Updates the title, notes, or due date of an existing task. |
| [complete\_task](#complete-task-tool) | Marks a task as completed. |
| [reopen\_task](#reopen-task-tool) | Marks a completed task as not completed. |
| [move\_task](#move-task-tool) | Repositions a task among its siblings, changes its parent task, or moves it to a different task list. |
| [delete\_task](#delete-task-tool) | Permanently deletes a task. |
| [create\_task\_list](#create-task-list-tool) | Creates a new task list. |
| [list\_task\_lists](#list-task-lists-tool) | Lists one page of the user's task lists. |

## Install the Google Tasks MCP server

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
    

## Google Tasks connection setup

View Google Tasks connection setup steps

You must [Enable the Google Tasks API](https://support.google.com/googleapi/answer/6158841) in the Google Cloud API console before you can connect to Google Tasks.

Refer to the following sections to connect to Google Tasks in Workato:

### Configure the OAuth consent screen

View Configure the OAuth consent screen steps

Complete the following steps to configure the OAuth consent screen:

1. Open the [Google Cloud Console](https://console.cloud.google.com) and go to **APIs & Services > OAuth consent screen**.
   
2. Click **Get started**.
   
3. Enter `Workato` in the **App name** field.
   
4. Enter an email in the **User support email** field.
   
5. Click **Next**.
   
6. Select **External** as the **Audience**. Refer to [Manage App Audience](https://support.google.com/cloud/answer/15549945) to learn more about user types.
   
7. Click **Next**.
   
8. Enter an email address in the **Contact information** section.
   
9. Select the checkbox to agree to Google API Services User Data Policy and click **Continue**. Refer to [Google API Services User Data Policy](https://developers.google.com/terms/api-services-user-data-policy) for more information.
   
10. Click **Create**.
    
11. Click the **Data access** tab and select **Add or Remove Scopes**.
    
12. Select the `https://www.googleapis.com/auth/tasks` scope.
    
13. Click **Save**.
    

### Create a custom OAuth profile

View Create a custom OAuth profile steps

You must create a custom OAuth profile with your client ID and secret before you can connect. Complete the following steps to create a custom OAuth profile:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `Google Tasks` and select it as your app.
   
4. Enter a name for your custom OAuth profile in the **Name** field.
   
5. Enter the **Client ID** and **Client secret**. Refer to the Google [Manage OAuth Clients](https://support.google.com/cloud/answer/15549257) guide to generate these values using `https://www.workato.com/oauth/callback` as the redirect URI.
   
6. Click **Save**.
   

### Connect to Google Tasks with OAuth 2.0 authentication

View Connect to Google Tasks with OAuth 2.0 authentication steps

Complete the following steps to set up your connection with OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Google Tasks` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Use the **Custom OAuth profile** drop-down menu to select the [custom OAuth profile](#create-a-custom-oauth-profile) you created for Google Tasks.
   
6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the tasks and lists you plan to use in Workato.
   

## How to use Google Tasks MCP server tools

Refer to the following sections for detailed information on available tools:

### create\_task tool

The **create\_task** tool creates a new task in a task list. Your LLM uses this tool to create a standalone to-do or a subtask nested one level under an existing task. If you specify a time, the LLM asks whether to create a Google Calendar event because Google Tasks due dates don't support times.

**Try asking**:

- `Add a task to call the vendor about the contract renewal.`
- `Create a task due next Monday to review the budget draft.`
- `Add "Book flights" as a subtask under "Plan the offsite."`

### get\_task tool

The **get\_task** tool retrieves a single task by its identifier. Your LLM uses this tool to retrieve the task's current details, typically before it updates the task.

**Try asking**:

- `Show me the full details of this task.`
- `What are the current notes on my renewal call task?`
- `Check the due date on this task before I change it.`

### list\_tasks tool

The **list\_tasks** tool lists tasks in a task list and optionally filters by completion status, due date range, and whether a task is dated, undated, or overdue. Your LLM uses this tool to show what's on a known or default list, applying the filters you specify.

**Try asking**:

- `What's on my default task list?`
- `Show me everything due this week in my Work list.`
- `What's overdue on my Customer Success list?`

### update\_task tool

The **update\_task** tool updates the title, notes, or due date of an existing task. Your LLM uses this tool to edit task details, or to explicitly clear a due date or notes field instead of replacing it.

**Try asking**:

- `Change the due date on my renewal call task to next Friday.`
- `Update the notes on my expense report task.`
- `Clear the due date on this task.`

### complete\_task tool

The **complete\_task** tool marks a task as completed. Your LLM uses this tool to check off a task. For tasks that appear to be recurring, the LLM asks you for confirmation because completing one occurrence can affect other occurrences, and the action can't be safely retried.

**Try asking**:

- `Mark "Submit expense report" as done.`
- `Check off my renewal call task.`
- `I finished the budget review, mark it complete.`

### reopen\_task tool

The **reopen\_task** tool marks a completed task as not completed. Your LLM uses this tool to un-check or undo the completion of a task, and asks you to confirm before reopening a task that appears recurring, because reopening one occurrence can affect others and can't be safely retried.

**Try asking**:

- `Reopen the task I marked complete by mistake.`
- `Un-check my expense report task.`
- `Undo completion on my renewal call task.`

### move\_task tool

The **move\_task** tool repositions a task among its siblings, changes its parent task, or moves it to a different task list. Your LLM uses this tool to reorder a task, nest or un-nest it under another task, or move it to a different list.

**Try asking**:

- `Move my onboarding task to the Customer Success list.`
- `Nest "Book flights" under "Plan the offsite."`
- `Move this task to the top of my list.`

### delete\_task tool

The **delete\_task** tool permanently deletes a task. Your LLM uses this tool only when you explicitly ask to delete or remove a task, confirming the specific task first if it was resolved from a vague reference.

**Try asking**:

- `Delete my task about the old vendor contract.`
- `Remove the "draft proposal" task from my list.`
- `Delete this task, I don't need it anymore.`

### create\_task\_list tool

The **create\_task\_list** tool creates a new task list. Your LLM uses this tool to create a new named grouping for tasks.

**Try asking**:

- `Create a new list called Q4 Renewals.`
- `Make a task list for the Q3 launch.`
- `Set up a new list to track the onboarding checklist.`

### list\_task\_lists tool

The **list\_task\_lists** tool lists one page of the user's task lists. Your LLM uses this tool when you ask what lists you have, or when it needs to resolve a list name to an identifier before another tool call.

**Try asking**:

- `What task lists do I have?`
- `Show me all my lists.`
- `Which list should I add this task to?`

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
