---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-to-do-mcp-server.md'
description: >-
  Use the Microsoft To Do MCP server to connect your LLM to Microsoft To Do with
  semantic task management for personal productivity.
---

# Microsoft To Do MCP server

The Microsoft To Do MCP server enables LLMs to manage personal tasks in Microsoft To Do using natural conversation. It provides tools to capture, find, update, and organize tasks with semantic filters, manage checklist steps, and complete work without requiring direct interaction with the Microsoft To Do interface.

## Uses

Use the Microsoft To Do MCP server to perform the following actions:

- Capture tasks from conversations and set due dates, reminders, recurrence, importance, and categories
- Retrieve and triage tasks due today, due this week, or marked as important
- Search for tasks by keyword across all your task lists
- Break tasks into checklist steps and complete individual steps
- Reschedule tasks, change recurrence, update importance, and add notes
- Complete recurring tasks and automatically create the next occurrence
- Create and manage multiple task lists
- Access tasks from flagged emails in your Flagged Emails list
- Organize tasks by categories and importance levels
- Delete tasks you no longer need

### Example prompts

Use the following example prompts to invoke Microsoft To Do MCP server tools:

- `Add a task to follow up with the vendor by Friday.`
- `What's due today?`
- `Show me all high-importance tasks due this week.`
- `Break the contract review into steps: legal review, stakeholder feedback, finalization.`
- `Mark the first two steps of the launch task as done.`
- `Push the Q4 planning meeting task to next Tuesday at 2pm.`
- `What tasks did I flag in email?`
- `Search for the vendor follow-up task.`
- `Make the standup recurring weekly on Mondays.`
- `Actually that's done, remove the old duplicate task.`

## Microsoft To Do MCP server tools

The Microsoft To Do MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_task\_lists](#list-task-lists-tool) | Retrieves all of your task lists with names and semantic types. |
| [create\_task\_list](#create-task-list-tool) | Creates a new task list in your Microsoft To Do account. |
| [list\_tasks](#list-tasks-tool) | Retrieves tasks from one list or across all lists with semantic status, due-date, and importance filters. |
| [search\_tasks](#search-tasks-tool) | Searches tasks by keyword across all of your task lists. |
| [get\_task](#get-task-tool) | Retrieves the full details of a task, including checklist steps and linked resources. |
| [create\_task](#create-task-tool) | Creates a new task with full property support in a specified list or the default list. |
| [update\_task](#update-task-tool) | Updates any properties of an existing task. Only provided fields change. |
| [complete\_task](#complete-task-tool) | Marks a task complete, generating the next occurrence for recurring tasks. |
| [delete\_task](#delete-task-tool) | Permanently deletes a task and its checklist items. |
| [add\_checklist\_items](#add-checklist-items-tool) | Adds one or more checklist steps to a task, with per-item results. |
| [update\_checklist\_item](#update-checklist-item-tool) | Checks off, rewords, or deletes a single checklist step. |

## Install the Microsoft To Do MCP server

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
    

## Microsoft To Do connection setup

View Microsoft To Do connection setup steps

The Microsoft To Do MCP server only supports authorization code grant authentication.

Complete the following steps to connect to Microsoft To Do in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Microsoft To Do** as your connection on the **New connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select your account type:
   
   - **Common**: Supports work or school accounts across multiple organizations, not restricted to a single tenant.
   - **Tenant specific**: Restricts sign-in to a single Microsoft Entra ID tenant.
6. Enter a tenant ID (a GUID) or verified domain name in the **Tenant ID** field if you selected **Tenant specific** as your account type.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Sign in with Microsoft** and complete the Microsoft sign-in flow.
   

### Microsoft To Do access requirements

All tools require a Microsoft 365 work or school account with an Exchange Online-backed mailbox. Microsoft To Do requires no premium tier. The server connects using delegated OAuth 2.0 authorization and acts only as the signed-in user. It supports no cross-user or administrative operations.

## How to use Microsoft To Do MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_task\_lists tool

The **list\_task\_lists** tool lists every task list in your account, including the default Tasks list and the Flagged Emails list. Your LLM uses this tool to discover your available lists and resolve a list name to its ID before creating or filtering tasks. On accounts with a very large number of lists, a single call may not return every list, so ask for a specific list by name if it's missing from the full listing.

**Try asking**:

- `What task lists do I have?`
- `Show me my lists.`
- `Do I have a vendor contracts list?`

### create\_task\_list tool

The **create\_task\_list** tool creates a new task list under your account. The tool returns an existing list if one with the name you provide already exists. Creating a duplicate list requires your explicit confirmation. Your LLM uses this tool to set up a new list on request.

**Try asking**:

- `Create a list called Client Renewals.`
- `Make a new list for the offsite planning.`
- `Add a list for new hire onboarding.`

### list\_tasks tool

The **list\_tasks** tool retrieves tasks from one list or across your entire account, filtered by status, due date, and importance. Your LLM uses this tool to triage what's due and plan your day without building a raw query.

**Try asking**:

- `What's due today?`
- `Show me what's overdue.`
- `What's on my plate this week?`
- `Any important tasks I'm missing?`
- `What's due by Friday?`

### search\_tasks tool

The **search\_tasks** tool searches for tasks by keyword across your task lists, matching against task titles and notes. Your LLM uses this tool to locate a task from a description.

**Try asking**:

- `Find the vendor follow-up task.`
- `Where did I put the contract review?`
- `Do I have anything about the Q4 planning?`

### get\_task tool

The **get\_task** tool retrieves everything recorded for one task, including its checklist steps and any linked resources, such as the email a flagged task came from. Your LLM uses this tool to read current state before editing or to answer detailed questions about a task.

**Try asking**:

- `What are the steps on the launch task?`
- `Show me the details of the contract review task.`
- `What's the due date and steps for this task?`

### create\_task tool

The **create\_task** tool creates a task with the properties your LLM provides, including title, notes, due date, reminder, start date, importance, categories, and recurrence. It records exactly what's stated, without inferring or adding anything you didn't ask for. Your LLM uses this tool to capture tasks from conversation and to deposit follow-ups from other systems.

**Try asking**:

- `Remind me to send the vendor follow-up Friday.`
- `Add a task to renew the software license.`
- `I need to review the contract before the 25th, high priority.`
- `Schedule a weekly standup reminder for Mondays at 9am.`

### update\_task tool

The **update\_task** tool updates any property of an existing task, including its due date, reminder, recurrence, importance, categories, or status. Only the fields you provide change, and every other property stays exactly as it was. Your LLM uses this tool to reschedule a task, edit its details, change its importance, or reopen one you completed by mistake.

**Try asking**:

- `Push the report task to next Tuesday.`
- `Make the standup recurring weekly.`
- `Change that to high priority.`
- `Add a note about the stakeholder feedback.`

### complete\_task tool

The **complete\_task** tool marks a task complete. For recurring tasks, it also creates the next occurrence. The tool preserves the completed task and its history instead of deleting it. You can reopen it later with `update_task` if needed. Your LLM uses this tool to mark a task done whenever you say it's finished.

**Try asking**:

- `Mark it done.`
- `Check off the weekly standup.`
- `That's finished.`

### delete\_task tool

The **delete\_task** tool permanently deletes a task and its checklist items. It takes no action until you explicitly confirm the deletion. Your LLM uses this tool to remove a task you've asked to delete.

**Try asking**:

- `Delete that duplicate task.`
- `Remove the outdated vendor task.`
- `Get rid of that one.`

### add\_checklist\_items tool

The **add\_checklist\_items** tool adds one or more checklist steps to a task in a single call. It reports success or failure for each step independently, so a failed step doesn't affect the remaining steps. Your LLM uses this tool to break a task down into steps or add steps you specify.

**Try asking**:

- `Break the contract review into steps.`
- `Add these steps to the launch task: marketing review, QA sign-off, release notes.`
- `Make a checklist for the presentation prep.`

### update\_checklist\_item tool

The **update\_checklist\_item** tool makes exactly one change to a single step per call. Your LLM uses this tool to complete, reword, or remove an individual step without touching the parent task.

**Try asking**:

- `Mark the first step done.`
- `Check off the legal review.`
- `Reword that step to be clearer.`

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
