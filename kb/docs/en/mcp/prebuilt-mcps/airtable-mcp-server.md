---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/airtable-mcp-server.md'
description: >-
  Use the Airtable MCP server to connect your LLM to Airtable with a curated set
  of tools to retrieve, create, update, and delete records.
---

# Airtable MCP server

The Airtable MCP server enables LLMs to access Airtable bases used as operational systems of record through natural conversation. It provides tools to retrieve, create, update, and delete records within existing Airtable structures without requiring direct interaction with the Airtable interface.

## Uses

Use the Airtable MCP server to perform the following actions:

- Discover which Airtable bases and tables you have access to
- Retrieve records from tables with optional filtering and view constraints
- Find specific records by identifier for review or updates
- Create new records to track projects, customers, or operational entries
- Update existing records to reflect status changes or new information
- Perform batch updates across multiple records efficiently
- Delete records when explicitly requested for cleanup or archiving

### Example prompts

Use the following example prompts to invoke Airtable MCP server tools:

- `What Airtable bases do I have access to?`
- `Show me all tables in the Project Tracker base.`
- `List all high-priority customers from the CRM base.`
- `Get the record for the Q4 Planning milestone.`
- `Add a new blocker to the Issues table.`
- `Update the status to 'Complete' for the authentication task.`
- `Mark all overdue items as 'At Risk' in the Active Projects view.`
- `Delete the archived records from last quarter.`

## Airtable MCP server tools

The Airtable MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_bases](#list-bases-tool) | Returns the Airtable bases accessible to the authenticated user. |
| [list\_tables](#list-tables-tool) | Returns the tables within a specified Airtable base. |
| [list\_records](#list-records-tool) | Retrieves records from a table, optionally constrained to a specific view and/or filtered by criteria. |
| [get\_record](#get-record-tool) | Retrieves a single record by record identifier. |
| [create\_record](#create-record-tool) | Creates a new record in an existing table and returns the created record identifier. |
| [update\_record](#update-record-tool) | Updates an existing record by record identifier. |
| [batch\_update\_records](#batch-update-records-tool) | Updates multiple records using explicit record identifiers. |
| [delete\_record](#delete-record-tool) | Deletes one or more records using explicit record identifiers. |

## Install the Airtable MCP server

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
    

## Airtable connection setup

View Airtable connection setup steps

The Airtable connector supports the following authentication types:

- [Personal access token](#personal-access-token)
- [OAuth 2.0](#oauth2)

### Personal access token

Use personal access token authentication to connect to Airtable with a token generated from your Airtable account.

> **API KEY DEPRECATION**
> 
> Airtable deprecated API keys for authentication at the end of January 2024. API keys no longer work on the platform. Migrate to personal access tokens to maintain API access to Airtable. Personal access tokens provide granular, secure API access to your Airtable data.

#### Create a personal access token

Refer to [Creating personal access tokens](https://support.airtable.com/docs/creating-and-using-api-keys-and-access-tokens) in the Airtable documentation.

#### Connect to Airtable using personal access token

Complete the following steps to set up a personal access token connection to Airtable in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Airtable** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Airtable connection setup](/assets/connection-setup-pat.DaJdezj7.png)_Airtable connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
6. Enter your [personal access token](#pat-create-token) in the **Personal access token** field.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   

### OAuth 2.0

Use OAuth 2.0 to connect to Airtable by signing in and granting access through Airtable's authorization flow.

#### Minimum and default scopes

The scopes `data.records:read` and `schema.bases:read` are requested automatically. The connection defaults to `data.records:read`, `schema.bases:read`, `data.records:write`, and `schema.bases:write` if no additional scopes are selected.

Ensure that any additional scopes you select are supported by your Airtable plan. Selecting unsupported scopes may result in a connection error. For example, the scope **View metadata about workspaces, bases, and views including collaborators** corresponds to `workspacesAndBases:read`, which is available only on the Business and Enterprise Scale plans.

Refer to the Airtable documentation for more information on [Airtable OAuth scopes and associated plans](https://airtable.com/developers/web/api/scopes).

#### Connect to Airtable using OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to Airtable in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Airtable** on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Airtable connection setup](/assets/connection-setup-oauth.Ce6bMao1.png)_Airtable connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Expand **Advanced settings** and use the **Requested permissions (OAuth scopes)** drop-down menu to select the scopes for this connection.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to Airtable when prompted and click **Allow** to grant Workato access.
   

## How to use Airtable MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_bases tool

The **list\_bases** tool retrieves a list of Airtable bases you can access. Your LLM uses this tool to discover what bases are available or when the base is unknown.

**Try asking**:

- `What Airtable bases do I have access to?`
- `Show me all my Airtable bases.`
- `List the bases available in my account.`
- `Which Airtable bases can I work with?`

### list\_tables tool

The **list\_tables** tool retrieves tables within an Airtable base you specify. Your LLM uses this tool to retrieve existing tables in a base.

**Try asking**:

- `What tables are in the Project Tracker base?`
- `Show me all tables in the CRM base.`
- `List the tables available in the Inventory Management base.`
- `What data tables exist in this base?`

### list\_records tool

The **list\_records** tool retrieves records from a table using criteria you specify. Your LLM uses this tool to retrieve records from Airtable, whether viewing all entries, filtering by criteria you specify, or accessing records from a particular view.

**Try asking**:

- `Show me all customers in the CRM base.`
- `Find high-priority items in the Issues table.`
- `What's in the Q1 Roadmap view?`
- `Show overdue items from the Active Projects view with priority 'High'.`

### get\_record tool

The **get\_record** tool retrieves a single record by record identifier. Your LLM uses this tool to access a specific record that's been referenced or before updating or deleting a record.

**Try asking**:

- `Get the details for record rec123456 in the Projects table.`
- `Show me the customer record for Acme Corp.`
- `Retrieve the milestone record with ID rec789012.`
- `Get the full information for the authentication task record.`

### create\_record tool

The **create\_record** tool creates a new record in an existing table and returns the created record identifier. Your LLM uses this tool to add new operational entries such as blockers, milestones, customers, or tasks.

**Try asking**:

- `Add a new blocker to the Issues table with title 'API timeout' and priority 'High'.`
- `Create a new customer record for Acme Corp in the CRM base.`
- `Add a milestone to the Q4 Roadmap for product launch.`
- `Create a new task in the Sprint Planning table.`

### update\_record tool

The **update\_record** tool updates an existing record by record identifier. Your LLM uses this tool to update a single record's status, priority, or other fields.

**Try asking**:

- `Update the status to 'Complete' for the authentication task.`
- `Change the priority to 'Critical' for the API timeout blocker.`
- `Mark the Q4 launch milestone as 'In Progress'.`
- `Update the customer record for Acme Corp with the new contact email.`

### batch\_update\_records tool

The **batch\_update\_records** tool updates multiple records using explicit record identifiers. Your LLM uses this tool to update multiple records at once.

**Try asking**:

- `Mark all overdue items in the Active Projects view as 'At Risk'.`
- `Update all high-priority bugs to assign them to the engineering team.`
- `Change the status to 'Archived' for all completed Q3 projects.`
- `Set all customer records from last year to 'Inactive' status.`

### delete\_record tool

The **delete\_record** tool deletes one or more records using explicit record identifiers. Your LLM uses this tool only when you explicitly ask to delete records.

**Try asking**:

- `Delete the archived records from Q3 in the Projects table.`
- `Remove the duplicate customer entries.`
- `Delete the test records from the Issues table.`
- `Remove all records marked as 'Spam' from the Contacts table.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/asana-work-management-mcp-server.md
description: >-
  Use the Asana Work Management MCP server to connect your LLM to Asana with
  task triage, project setup, and status reporting through natural conversation.
---

# Asana Work Management MCP server

The Asana Work Management MCP server enables LLMs to interact with Asana for day-to-day task and project management through natural conversation. It provides tools to create, update, find, and read tasks, see what's assigned to you, make comments, create projects, and post project status updates without requiring direct interaction with the Asana interface.

## Uses

Use the Asana Work Management MCP server to perform the following actions:

- Resolve task, project, user, and team names to their Asana identifiers.
- Retrieve a task's full details, including its direct and inherited project and section memberships.
- See the tasks assigned to you in your My Tasks list.
- Read a task's comment history.
- Search for tasks across the workspace by criteria such as assignee, project, due date, or custom fields.
- Retrieve a project's details, sections, and custom-field schema.
- List the tasks within a project or one of its sections.
- Create tasks and subtasks with a project, section, assignee, and dates.
- Update a task's fields, move it to a different section, or comment on it.
- Create a project, optionally with an associated team, initial sections, and team access, and post status updates to it.

### Example prompts

Use the following example prompts to invoke Asana Work Management MCP server tools:

- `Find the "Website Redesign" project.`
- `Show me the details for the "Draft press release" task.`
- `List the tasks in the "In Progress" section of the Website Redesign project.`
- `Create a task called "Draft press release" in the Website Redesign project, due next Friday.`
- `Move the "Draft press release" task to the Done section.`
- `Add a comment to the "Draft press release" task saying it's ready for review.`
- `Search for incomplete tasks assigned to Jade Chen in the Website Redesign project.`
- `Create a new project called "Q4 Marketing Campaign" with sections for Backlog, In Progress, and Done.`
- `Post a status update on the Website Redesign project marking it on track.`

## Asana Work Management MCP server tools

The Asana Work Management MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [find\_objects](#find-objects-tool) | Resolves a name to matching Asana objects and their IDs. |
| [get\_task](#get-task-tool) | Returns the full details of a single task, including direct and effective memberships. |
| [get\_my\_tasks](#get-my-tasks-tool) | Returns the tasks in the authenticated user's My Tasks list. |
| [get\_project](#get-project-tool) | Returns a project's details, sections, and optionally its custom-field schema and task counts. |
| [list\_project\_sections](#list-project-sections-tool) | Lists the sections (columns or groups) of a project. |
| [get\_project\_custom\_fields](#get-project-custom-fields-tool) | Returns the custom-field schema associated with a project. |
| [list\_project\_tasks](#list-project-tasks-tool) | Returns the tasks within a project, or within one of its sections. |
| [get\_task\_comments](#get-task-comments-tool) | Returns the comments on a task and related system activity. |
| [search\_tasks](#search-tasks-tool) | Searches tasks across the workspace using full-text and typed filters. |
| [create\_task](#create-task-tool) | Creates a new task or subtask. |
| [update\_task](#update-task-tool) | Updates a task's fields and section placement. |
| [add\_comment](#add-comment-tool) | Adds a comment to a task. |
| [create\_project](#create-project-tool) | Creates a project and optionally associates a team, seeds sections, and shares it with a team. |
| [publish\_status\_update](#publish-status-update-tool) | Posts a status update to a project. |

## Install the Asana Work Management MCP server

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
    

## Asana Work Management connection setup

View Asana Work Management connection setup steps

### API version

The Asana connector uses [Asana API v1](https://developers.asana.com/reference/rest-api-reference).

### How to connect to Asana in Workato

View OAuth 2.0 connection setup steps

Complete the following steps to connect to Asana in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Asana` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Asana](/assets/connect.DeJUsD0Y.png)_Connect to Asana_
   
4. Use the **Location** drop-down menu to select the project or folder to store your connection.
   
5. Optional. Use the **Custom OAuth profiles** drop-down menu to select a custom OAuth profile for this connection.
   
6. Click **Connect**.
   
7. Sign in to Asana using your default login method to authorize Workato.
   

#### Asana role requirements

Each tool's availability depends on the permissions granted to the connected account. A request made without the required permission returns a permission-denied outcome rather than a partial result. Refer to the Asana [OAuth scopes](https://developers.asana.com/docs/oauth-scopes) and [project permissions](https://help.asana.com/s/article/individual-project-permissions?language=en_US) documentation for more information. **search\_tasks** additionally requires the authenticated user to have search entitlement from a premium Asana workspace or membership on a premium team.

### Project property configuration

The Asana Work Management MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| Workspace GID | Required. Enter the globally unique identifier (GID) of the Asana workspace or organization in which all tools operate. |
| Default page size | Enter a default page size to apply to every tool that returns paged results, including the paginated components for subtasks, sections, and custom fields. The default value is 50 and the maximum is 100. |
| Search cursor TTL | Enter how long the opaque search continuation cursor used by **search\_tasks** remains valid. Defaults to 300 seconds. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
6. Go to the **Value** field and make your changes. For example, set `default_page_size` to `75` or `search_cursor_TTL` to `250`.
   

## How to use Asana Work Management MCP server tools

Refer to the following sections for detailed information on available tools:

### find\_objects tool

The **find\_objects** tool resolves a name to matching Asana objects and their IDs. Your LLM uses this tool first when you refer to a task, project, person, or team by name and its ID is unknown. Your LLM asks you to disambiguate when several results match or when matching results aren't found.

**Try asking**:

- `Find the "Website Redesign" project.`
- `Look up the user Jade Chen.`
- `Find the "Engineering" team.`

### get\_task tool

The **get\_task** tool returns the full details of a single task, including direct and effective memberships. Your LLM uses this tool when you ask for a specific task's details or subtasks. **get\_task** relies on the connection's effective memberships to understand the project context a subtask inherits.

**Try asking**:

- `Show me the details for the "Draft press release" task.`
- `What are the subtasks on this task?`
- `Which projects and sections is this task part of?`

### get\_my\_tasks tool

The **get\_my\_tasks** tool returns the tasks in the authenticated user's My Tasks list. Your LLM uses this tool to track "to-do" items. **get\_my\_tasks** returns incomplete tasks assigned to you by default.

**Try asking**:

- `Show me my to-do list.`
- `What tasks are assigned to me, including completed ones?`

### get\_project tool

The **get\_project** tool returns a project's details, sections, and optional details for custom-field schema and task counts. Your LLM uses this tool when you ask about a project's details or sections, or optionally custom-field schema or task counts details.

**Try asking**:

- `Show me the details for the "Website Redesign" project.`
- `Who owns the Website Redesign project?`
- `How many tasks are in the Website Redesign project?`

### list\_project\_sections tool

The **list\_project\_sections** tool lists the sections (columns or groups) of a project. Your LLM uses this tool to resolve a section you name to its ID before placing or moving a task, or before scoping a task list to that section.

**Try asking**:

- `What sections does the Website Redesign project have?`
- `Find the "Done" section in the Website Redesign project.`
- `List the columns on this project's board.`

### get\_project\_custom\_fields tool

The **get\_project\_custom\_fields** tool returns the custom-field schema associated with a project. Your LLM uses this tool to resolve a custom field you name to its ID and subtype before setting or filtering by the ID.

**Try asking**:

- `What custom fields does the Website Redesign project have?`
- `What's the subtype of the Priority field on this project?`
- `Find the field ID for "Stage" on this project.`

### list\_project\_tasks tool

The **list\_project\_tasks** tool returns the tasks within a project or section. Your LLM uses this tool when you need to see the tasks inside a specific project or section.

**Try asking**:

- `List the tasks in the Website Redesign project.`
- `Show me what's in the "In Progress" section.`
- `What tasks are in the Done column of this project?`

### get\_task\_comments tool

The **get\_task\_comments** tool returns the comments on a task and related system activity. Your LLM uses this tool when you need to read a task's discussion, decisions, or feedback.

**Try asking**:

- `What are the comments on the "Draft press release" task?`
- `Show me the discussion on this task.`
- `Has anyone left feedback on this task recently?`

### search\_tasks tool

The **search\_tasks** tool searches tasks across the workspace using full-text and typed filters. Your LLM uses this tool to find tasks by criteria, such as text, assignee, project or section, due or created dates, and custom fields, when advanced task search is available to you.

**Try asking**:

- `Search for incomplete tasks assigned to Jade Chen in the Website Redesign project.`
- `Find tasks due before next Friday in the Website Redesign project.`
- `Search the workspace for tasks mentioning "launch plan".`

### create\_task tool

The **create\_task** tool creates a new task or subtask. Your LLM uses this tool to capture a task with a name, description, assignee, project, section, and dates, or to create a subtask by supplying a parent task.

**Try asking**:

- `Create a task called "Draft press release" in the Website Redesign project, due next Friday.`
- `Add a subtask to this task for reviewing the copy.`
- `Create a task assigned to Dana Park in the "Backlog" section of the Website Redesign project.`

### update\_task tool

The **update\_task** tool updates a task's fields and section placement. Your LLM uses this tool to reassign a task, change task dates, mark a task as complete, edit the task name or description, set a custom-field value, or move a task to another section.

**Try asking**:

- `Move the "Draft press release" task to the Done section.`
- `Mark this task complete.`
- `Reassign this task to Jade Chen and push the due date to next week.`

### add\_comment tool

The **add\_comment** tool adds a comment to a task. Your LLM uses this tool when you need to post a comment, note, or decision on a task.

**Try asking**:

- `Add a comment to the "Draft press release" task saying it's ready for review.`
- `Leave a note on this task about the client's feedback.`
- `Comment on this task that the deadline moved.`

### create\_project tool

The **create\_project** tool creates a project and optionally associates a team, seeds sections, and shares the project with a team. Your LLM uses this tool when you need to stand up a new project and confirms with you before creating one visible to the whole workspace.

**Try asking**:

- `Create a new project called "Q4 Marketing Campaign" with sections for Backlog, In Progress, and Done.`
- `Set up a project for the new initiative and share it with the Engineering team.`
- `Create a private project called "Internal Audit".`

### publish\_status\_update tool

The **publish\_status\_update** tool posts a status update to a project. Your LLM uses this tool when you need to notify a project's followers with a status update that includes a status type, title, and body.

**Try asking**:

- `Post a status update on the Website Redesign project marking it on track.`
- `Update the status of this project to "at risk" with a summary of the blockers.`
- `Mark the Q4 Marketing Campaign project complete with a closing note.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/bamboohr-self-service-mcp-server.md
description: >-
  Use the BambooHR Self-Service MCP server to connect your LLM to BambooHR with
  a curated set of tools to look up coworkers, manage your own profile, request
  time off, and act on requests awaiting your approval.
---

# BambooHR Self-Service MCP server

The BambooHR Self-Service MCP server enables LLMs to interact with BambooHR for everyday employee and approver HR tasks through natural conversation. It provides tools to look up coworkers in the company directory, retrieve and update your own profile, check time-off balances, submit and track time-off requests, respond to requests awaiting your approval, and see who is out, without requiring direct interaction with the BambooHR interface.

## Uses

Use the BambooHR Self-Service MCP server to perform the following actions:

- Look up a coworker's job title, department, manager, or work contact details in the published company directory
- Retrieve your own employee profile, including job context and contact fields
- Update your own self-service fields, such as home address, home email, phone numbers, and preferred name
- Check your accrued time-off balances and year-to-date amounts used
- Discover which time-off categories you are eligible to request
- Submit a time-off request, including per-day amounts for partial or mixed-duration leave
- Review the status of your recent time-off requests and cancel pending requests
- Review time-off requests assigned to you for approval
- Approve or deny a time-off request within your authority on that request
- See who is on approved leave and which company holidays fall within a date range

### Example prompts

Use the following example prompts to invoke BambooHR Self-Service MCP server tools:

- `Who is Sarah in Finance?`
- `Who does Priya report to?`
- `What address does BambooHR have for me?`
- `Update my mobile phone to 415-555-0142.`
- `How much vacation do I have left?`
- `What leave categories can I request?`
- `Request PTO for September 15-19.`
- `What's the status of my time-off request?`
- `What time-off requests are waiting on me?`
- `Who is out this week, and are there any company holidays coming up?`

## BambooHR Self-Service MCP server tools

The BambooHR Self-Service MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_employees](#search-employees-tool) | Finds coworkers in the published company directory by name, department, job title, location, or exact employee ID. |
| [get\_my\_profile](#get-my-profile-tool) | Retrieves the authenticated user's own employee record with self-service fields. |
| [update\_my\_profile](#update-my-profile-tool) | Updates self-service fields on the authenticated user's employee record. |
| [get\_time\_off\_balance](#get-time-off-balance-tool) | Retrieves the authenticated user's accrued time-off balances as of a specified date. |
| [list\_time\_off\_types](#list-time-off-types-tool) | Lists the time-off types the authenticated user is eligible to request. |
| [request\_time\_off](#request-time-off-tool) | Submits a time-off request for the authenticated user. |
| [list\_my\_time\_off\_requests](#list-my-time-off-requests-tool) | Lists the authenticated user's own recent time-off requests and their statuses. |
| [list\_pending\_time\_off\_requests](#list-pending-time-off-requests-tool) | Lists the time-off requests the authenticated user is assigned to approve. |
| [list\_whos\_out](#list-whos-out-tool) | Lists approved time off and company holidays within a date range. |

## Install the BambooHR Self-Service MCP server

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
    

## BambooHR Self-Service connection setup

View BambooHR Self-Service connection setup steps

The BambooHR connector supports the following authentication types:

- [API token](#api-token)
- [OAuth 2.0](#oauth2)

### BambooHR permission requirements

The results each tool returns depend on the authenticated user's BambooHR permissions and on your company's configuration:

- Coworker lookup reads from the published employee directory. Your company's **Company Directory** and **Company Org Chart** sharing settings determine which employees and which fields are available. The tool reports that the directory is unavailable instead of using another source when both settings are disabled, or when the user's access level isn't shared with the directory.
- Profile updates apply BambooHR's field-level permissions in addition to this server's self-service field set.
- Approval authority comes from your BambooHR time-off workflow configuration, which doesn't necessarily follow reporting relationships.

View API token steps

### API token

Use API token authentication to connect to BambooHR with a static key generated in the BambooHR portal.

#### Generate an API key in BambooHR

Complete the following steps to generate an API key before you connect in Workato:

1. Sign in to the [BambooHR](https://app.bamboohr.com/login/) portal.
   
2. Go to **My Account > API Keys**.
   
   ![Go to BambooHR API Keys](/assets/find-api-keys.xegBwE4f.png)_Navigate to BambooHR API Keys_
   
3. Create a new API key by selecting **Add New Key**.
   
4. Provide a descriptive name for this new API Key, for example, `workato_user`.
   
5. Save the generated API key in a secure location.
   
   > **API KEY ONLY VISIBLE IN THIS STEP**
   > 
   > You can't retrieve this key after this step.
   
   Refer to the [BambooHR documentation](https://documentation.bamboohr.com/docs#authentication) for more information.
   

#### Connect to BambooHR with API token authentication

Complete the following steps to set up an API token connection to BambooHR in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `BambooHR` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![BambooHR API token connection](/assets/connect-to-bamboo-hr.BuDzV5cT.png)_Set up an API token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API Token**.
   
6. Enter the API token you generated in [Generate an API key in BambooHR](#api-token-setup) in the **API token** field.
   
7. Enter your BambooHR subdomain in the **Sub-domain** field. This is most often your company name.
   
8. Click **Connect**.
   

View OAuth 2.0 steps

### OAuth 2.0

Use OAuth 2.0 to connect to BambooHR without managing a static key. You authorize the connection through BambooHR when you connect.

#### Connect to BambooHR with OAuth 2.0

Complete the following steps to set up an OAuth 2.0 connection to BambooHR in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `BambooHR` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![BambooHR OAuth 2.0 connection](/assets/oauth-2.JOCMWC8O.png)_Set up an OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth2.0**.
   
6. Enter your BambooHR subdomain in the **Sub-domain** field. This is most often your company name.
   
7. Click **Connect**.
   
8. Sign in to BambooHR when prompted and authorize access to complete the connection.
   

## How to use BambooHR Self-Service MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_employees tool

The **search\_employees** tool finds coworkers in the published company directory by name, department, job title, location, or exact employee ID. Your LLM uses this tool when you refer to a coworker by name or ask directory-scoped questions, such as who works in a team or which engineers are in a specific office.

**Try asking**:

- `Who is Sarah in Finance?`
- `Show me the engineers in our London office.`
- `Who does Priya report to?`
- `What's the work email for the head of Marketing?`

### get\_my\_profile tool

The **get\_my\_profile** tool retrieves the authenticated user's own employee record with self-service fields. Your LLM uses this tool to answer questions about your own information, such as the address on file, your manager, or your hire date, and to check current values before an update.

**Try asking**:

- `What address does BambooHR have for me?`
- `Who is my manager?`
- `When was my hire date?`
- `What phone number is on my record?`

### update\_my\_profile tool

The **update\_my\_profile** tool updates self-service fields on the authenticated user's employee record. Your LLM uses this tool when you ask to change your home address, home email, home phone, mobile phone, or preferred name, and it confirms the exact change with you before submitting.

**Try asking**:

- `Update my mobile phone to 415-555-0142.`
- `Change my home address to 500 Market Street, San Francisco.`
- `Set my preferred name to Mike.`
- `Update the personal email on my record.`

### get\_time\_off\_balance tool

The **get\_time\_off\_balance** tool retrieves the authenticated user's accrued time-off balances based on a date you specify. Your LLM uses this tool to answer questions about your own remaining time off, returning one entry per visible category with the balance, units, policy type, and the amount used year to date.

**Try asking**:

- `How much vacation do I have left?`
- `What's my sick leave balance?`
- `How many PTO days will I have as of December 31?`
- `How much time off have I used this year?`

### list\_time\_off\_types tool

The **list\_time\_off\_types** tool lists the time-off types the authenticated user is eligible to request. Your LLM uses this tool when you ask what leave categories are available to you, or when you need to request a category that didn't appear in your balances, such as bereavement, jury duty, or unpaid leave. Results reflect only what you're eligible to request, not a company-wide catalog of policies.

**Try asking**:

- `What leave categories can I request?`
- `Can I request bereavement leave?`
- `Is unpaid leave an option for me?`
- `What types of time off are available to me?`

### request\_time\_off tool

The **request\_time\_off** tool submits a time-off request for the authenticated user. Your LLM uses this tool after confirming the type, dates, amount, and any note with you, and supports per-day amounts for partial or mixed-duration leave, such as a half day on Friday and full days the following week.

**Try asking**:

- `Request PTO for September 15-19.`
- `Submit a sick day for tomorrow.`
- `Request a half day on Friday and full days Monday and Tuesday.`
- `Request bereavement leave for next week with a note for my approver.`

### list\_my\_time\_off\_requests tool

The **list\_my\_time\_off\_requests** tool lists the authenticated user's own recent time-off requests and statuses. Your LLM uses this tool to check the status of a request you submitted, and to resolve the request ID before a cancellation. Each request returns its type, date range, amount, status, notes, and the actions available to you, so your LLM knows which requests you can cancel.

**Try asking**:

- `What's the status of my time-off request?`
- `Has my PTO for next month been approved?`
- `Show me the time-off requests I've submitted this quarter.`
- `Cancel my time-off request for next Friday.`

### list\_pending\_time\_off\_requests tool

The **list\_pending\_time\_off\_requests** tool lists the time-off requests the authenticated user is assigned to approve. Your LLM uses this tool for review-queue questions, such as requests that need your approval or who has asked for time off.

**Try asking**:

- `What time-off requests are waiting on me?`
- `Does anything need my approval this week?`
- `Who has requested time off in December?`
- `Show me pending requests with the notes my team left.`

### list\_whos\_out tool

The **list\_whos\_out** tool lists approved time off and company holidays within a date range. Your LLM uses this tool for coverage and scheduling questions, such as who is out on a given day or which holidays fall in a period, and returns a date-sorted list where each entry is identified as time off or a holiday.

**Try asking**:

- `Who is out this week?`
- `Is anyone on my team out on October 3?`
- `Any company holidays coming up in September?`
- `Who is on leave between November 20 and December 5?`

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
