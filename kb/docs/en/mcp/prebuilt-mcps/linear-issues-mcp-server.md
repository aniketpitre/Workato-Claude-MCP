---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/linear-issues-mcp-server.md'
description: >-
  Use the Linear Issues MCP server to let your LLM search, create, update,
  transition, assign, label, and comment on Linear issues.
---

# Linear Issues MCP server

The Linear Issues MCP server enables LLMs to run the Linear issue lifecycle through natural conversation. It provides tools to search and retrieve issues, create and edit them, move them through workflow states, assign owners, manage labels and relations, and comment without requiring direct interaction with the Linear interface.

> **SERVER SCOPE**
> 
> The Linear Issues MCP server manages the issue object and its directly attached entities. It can associate an issue with an existing project or cycle, but it doesn't manage projects, initiatives, cycles, or documents. Use the [Linear Project Planning](/en/mcp/prebuilt-mcps/linear-project-planning-mcp-server) MCP server for the roadmap and planning layer.

## Uses

Use the Linear Issues MCP server to perform the following actions:

- Search for issues by keyword, or by team, assignee, state, label, priority, or project.
- Retrieve full details for a specific issue, including its labels, assignee, and relations.
- Create a new issue, or a sub-issue, with a team and title.
- Update issue fields such as title, description, priority, estimate, or due date.
- Move an issue through workflow states, including closing or canceling it.
- Assign or unassign an issue's owner.
- Add labels to an issue without removing its existing labels.
- Comment on an issue and review its comment thread.
- Relate issues to each other, such as `blocks`, `duplicate`, or `related`.
- Archive or delete (trash) an issue.

### Example prompts

Use the following example prompts to invoke Linear Issues MCP server tools:

- `Find all urgent bugs assigned to me on the Platform team.`
- `Show me the details for WOR-123.`
- `Create a bug titled "Checkout button unresponsive on mobile" for the Growth team.`
- `Update the priority on WOR-123 to urgent.`
- `Move WOR-123 to Done.`
- `Assign WOR-123 to Jane Smith.`
- `Add the needs-design label to WOR-123.`
- `Add a comment to WOR-123 saying the fix is deployed.`
- `Mark WOR-200 as a duplicate of WOR-123.`
- `Archive WOR-456.`

## Linear Issues MCP server tools

The Linear Issues MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_issues](#search-issues-tool) | Searches or lists issues by keyword and filters such as team, assignee, state, label, priority, or project. |
| [get\_issue](#get-issue-tool) | Retrieves full details for one issue by its human-readable identifier or UUID. |
| [create\_issue](#create-issue-tool) | Creates a new issue, or a sub-issue, with a team and title. |
| [update\_issue](#update-issue-tool) | Updates one or more fields on an issue, replacing all its labels if labels are supplied. |
| [transition\_issue](#transition-issue-tool) | Moves an issue to a named workflow state, including closing or canceling it. |
| [assign\_issue](#assign-issue-tool) | Assigns an issue to a user by name or email, or unassigns it. |
| [add\_labels\_to\_issue](#add-labels-to-issue-tool) | Adds labels to an issue without removing its existing labels. |
| [archive\_issue](#archive-issue-tool) | Archives (hides) an issue. This is reversible in Linear. |
| [delete\_issue](#delete-issue-tool) | Moves an issue to trash. |
| [create\_comment](#create-comment-tool) | Posts a comment or threaded reply on an issue. |
| [list\_comments](#list-comments-tool) | Lists the newest comments on an issue. |
| [create\_issue\_relation](#create-issue-relation-tool) | Creates a relation between two issues, such as `blocks`, `duplicate`, or `related`. |
| [list\_workflow\_states](#list-workflow-states-tool) | Lists the valid workflow states for a team. |

## Install the Linear Issues MCP server

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
    

## Linear Issues connection setup

View Linear Issues connection setup steps

There are two ways to connect to Linear:

- [OAuth 2.0](#oauth-2-0)
- [API key](#api-key)

### Download the Linear connector from the community library

View steps to download the Linear connector from the community library

Complete the following steps to install the Linear connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### OAuth 2.0

View OAuth 2.0 steps

#### Register an OAuth app

View register an OAuth app steps

Complete the following steps to register an OAuth app in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **API** in the sidebar.
   
   ![API administration page](/assets/linear-api-administration-page.Bvz7kApz.png)_API administration page_
   
4. Click **\+ New OAuth application** to add a new OAuth application.
   
5. Enter a name for your application in the **Application name** field. For example, `Workato`.
   
   ![Registering application](/assets/linear-registering-application.DQFPXn_w.png)_Registering application_
   
6. Enter the **Developer name** and a valid **Developer URL**.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Callback URLs** field. Refer to the [Callback URL](/en/developing-connectors/registering-new-client#callback-url) documentation for more information.
   
8. Click **Create** to register the OAuth app.
   
9. Copy the **Client ID** and **Client secret** and store them in a secure location. These values are required to establish the connection in Workato.
   

#### Connect to Linear using OAuth 2.0

View connect to Linear using OAuth 2.0 steps

Complete the following steps to connect to Linear in Workato using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using OAuth 2.0 authentication](/assets/linear-oauth-connection-setup.iMhSgAAT.png)_Connect to Linear using OAuth 2.0 authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **Client ID** and **Client secret** for your Linear account.
   
6. Select the necessary [OAuth scopes](https://developers.linear.app/docs/oauth/authentication) required for your integration.
   
7. Click **Connect**.
   

### API key

View API key steps

#### Create an API key

View create an API key steps

Complete the following steps to create an API key in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **Security & access** in the sidebar.
   
   ![Personal API keys](/assets/linear-personal-api-keys.CVZ33KIY.png)_Personal API keys_
   
4. Click **New API key**.
   
5. Enter a name for the API key in the **Key name** field.
   
6. Specify permissions for the API key in the **Permissions** field.
   
7. Click **Create** to create the API key.
   
8. Copy the API key and store it in a secure location. This value is required to establish the connection in Workato. Refer to the [Linear documentation](https://linear.app/docs/api-and-webhooks) for more information.
   

#### Connect to Linear using an API key

View connect to Linear using an API key steps

Complete the following steps to connect to Linear in Workato using an API key:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using API key authentication](/assets/linear-api-key-connection-setup.Cww6C7p1.png)_Connect to Linear using API key authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **API key** for your Linear account.
   
6. Click **Connect**.
   

## How to use Linear Issues MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_issues tool

The **search\_issues** tool finds issues by keyword or by filters such as team, assignee, state, label, priority, and project. Your LLM uses this tool to locate issues matching your criteria before opening one with [get\_issue](#get-issue-tool).

**Try asking**:

- `Find all urgent bugs assigned to me on the Platform team.`
- `Search for issues mentioning "checkout timeout".`
- `List issues in the Growth team's backlog.`

> **RATE LIMITING**
> 
> Linear rate-limits keyword search, so repeated searches in a short window may be throttled.

### get\_issue tool

The **get\_issue** tool looks up one issue by its human-readable identifier, such as `WOR-123`, or UUID. Your LLM uses this tool to retrieve a specific issue, including its description, labels, and assignee, before reporting on it or editing it. It doesn't return the issue's relations, such as blocks or duplicates.

**Try asking**:

- `Show me the details for WOR-123.`
- `What's the current status and assignee on WOR-456?`
- `Pull up the full description for this issue.`

### create\_issue tool

The **create\_issue** tool logs a new issue, or a sub-issue of an existing one. Your LLM uses this tool to capture new work after you supply at least a team and title, and optionally a description, assignee, priority, labels, state, project, cycle, or parent issue.

**Try asking**:

- `Create a bug titled "Checkout button unresponsive on mobile" for the Growth team.`
- `Add a task to the Platform team backlog assigned to Sam.`
- `Create a sub-issue under WOR-100 for the API changes.`

### update\_issue tool

The **update\_issue** tool changes one or more fields on an existing issue. Your LLM uses this tool for broader multi-field edits, such as edits to a title, description, priority, estimate, due date, or project/cycle association.

**Try asking**:

- `Update the priority on WOR-123 to urgent.`
- `Set the due date on WOR-456 to next Friday.`
- `Move WOR-123 into the Mobile App Relaunch project.`

> **ALTERNATIVE TOOLS**
> 
> This server contains the following alternatives to [update\_issue](#update-issue-tool):
> 
> - [add\_labels\_to\_issue](#add-labels-to-issue-tool): Add labels without removing existing ones. Supplying a label to [update\_issue](#update-issue-tool) replaces every label already on the issue.
> - [transition\_issue](#transition-issue-tool): Change only an issue's status.
> - [assign\_issue](#assign-issue-tool): Change only an issue's assignee.

### transition\_issue tool

The **transition\_issue** tool changes an issue's workflow state, including moving it to closed or canceled. Your LLM uses this tool when you ask to close, resolve, cancel, or mark an issue done.

**Try asking**:

- `Move WOR-123 to Done.`
- `Cancel WOR-456, it's no longer needed.`
- `Mark this issue as in progress.`

### assign\_issue tool

The **assign\_issue** tool sets or clears an issue's assignee, matching a user by name or email. Your LLM uses this tool for a standalone ownership change, including removing the assignee entirely, which is the only way this server clears a field.

**Try asking**:

- `Assign WOR-123 to Jane Smith.`
- `Reassign this issue to jane@example.com.`
- `Unassign WOR-456.`

### add\_labels\_to\_issue tool

The **add\_labels\_to\_issue** tool attaches one or more labels to an issue while leaving its current labels in place. Your LLM uses this tool to tag an issue with additional labels.

**Try asking**:

- `Add the needs-design label to WOR-123.`
- `Tag this issue as a regression.`
- `Add the labels "frontend" and "P1" to WOR-456.`

> **REMOVE LABELS**
> 
> Use [update\_issue](#update-issue-tool) to remove labels by supplying only the ones you plan to keep.

### archive\_issue tool

The **archive\_issue** tool hides an issue from active views. This change is reversible in Linear. Your LLM uses this tool to set aside a completed or stale issue without trashing it. Archiving an already-archived issue succeeds without error, so it's safe to retry.

**Try asking**:

- `Archive WOR-456.`
- `Hide this completed issue from the active list.`
- `Archive the issues we closed last sprint.`

### delete\_issue tool

The **delete\_issue** tool trashes an issue, which Linear permanently removes after a 30-day grace period. Your LLM uses this tool when you explicitly ask to delete, remove, or trash an exact issue. Your LLM confirms the issue's identifier and title first if they aren't already known and doesn't treat closing, resolving, or canceling an issue as a delete request. Deleting an already-trashed issue succeeds without error, so it's safe to retry.

**Try asking**:

- `Delete WOR-789, it was created by mistake.`
- `Trash the duplicate issue WOR-200.`
- `Remove this test issue from my backlog.`

### create\_comment tool

The **create\_comment** tool adds a comment, or a threaded reply, to an issue. Your LLM uses this tool to leave a markdown comment on an issue, optionally as a reply to an existing comment. Linear supports only one level of threading, so replying to a reply isn't supported.

**Try asking**:

- `Add a comment to WOR-123 saying the fix is deployed.`
- `Reply to the last comment on this issue with an update.`
- `Comment on WOR-456 asking for more details.`

### list\_comments tool

The **list\_comments** tool returns an issue's most recent comments. Your LLM uses this tool to read a discussion before adding a new comment. You can specify a maximum thread length to omit older comments. The default length limit is 50 comments.

**Try asking**:

- `What's the latest discussion on WOR-123?`
- `Show me the comments on this issue.`
- `List the last 10 comments on WOR-456.`

### create\_issue\_relation tool

The **create\_issue\_relation** tool links two issues with a relation type, such as `blocks`, `duplicate`, or `related`. Your LLM uses this tool to sequence dependent work or flag duplicates after you specify both issues and the relation type.

**Try asking**:

- `Mark WOR-200 as a duplicate of WOR-123.`
- `WOR-100 blocks WOR-150, link them.`
- `Relate WOR-50 to WOR-60.`

### list\_workflow\_states tool

The **list\_workflow\_states** tool returns a team's valid workflow state names. Your LLM uses this tool to discover the exact state names available before calling [transition\_issue](#transition-issue-tool) or [create\_issue](#create-issue-tool).

**Try asking**:

- `What workflow states does the Platform team use?`
- `List the valid states I can move this issue to.`
- `Show me the states available for the Growth team.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/linear-project-planning-mcp-server.md
description: >-
  Use the Linear Project Planning MCP server to let your LLM browse projects,
  initiatives, and cycles, post status updates, and manage planning docs.
---

# Linear Project Planning MCP server

The Linear Project Planning MCP server enables LLMs to interact with Linear for the planning and roadmap layer through natural conversation. It provides tools to browse and create projects, post health-tagged status updates, review initiatives and their child projects, inspect cycles and the active cycle's progress, and find and create planning documents without requiring direct interaction with the Linear interface.

> **SERVER SCOPE**
> 
> The Linear Project Planning MCP server manages the Linear planning layer, including projects, initiatives, cycles, and documents. It surfaces issues only inside [get\_active\_cycle](#get-active-cycle-tool), where they're read-only. Use the [Linear Issues](/en/mcp/prebuilt-mcps/linear-issues-mcp-server) MCP server to create, update, and manage issues.

## Uses

Use the Linear Project Planning MCP server to perform the following actions:

- Browse projects workspace-wide or scoped to a team, filtered by status or lead.
- Get a project's full details, including its teams, members, and related initiatives.
- Create a new project with one or more teams and optional lead and dates.
- Update a project's name, description, status, lead, or dates.
- Post a health-tagged status update (on track, at risk, or off track) to a project.
- Browse initiatives and the child projects under each one.
- List a team's cycles and review their progress.
- Check a team's active cycle, including issues grouped by workflow state.
- Find and create planning documents attached to a project.

### Example prompts

Use the following example prompts to invoke Linear Project Planning MCP server tools:

- `List all active projects for the Platform team.`
- `Show me the full details for the Checkout Redesign project.`
- `Create a new project called Q3 Onboarding Revamp for the Growth team.`
- `Update the Billing Migration project's status to Started.`
- `Post a status update on the Mobile App Relaunch project marking it at risk.`
- `What initiatives do we have, and which projects fall under each one?`
- `List the last five cycles for the Platform team.`
- `How is the current sprint going for the Growth team?`
- `Find the planning documents attached to the Checkout Redesign project.`
- `Create a planning doc called Launch Checklist attached to the Mobile App Relaunch project.`

## Linear Project Planning MCP server tools

The Linear Project Planning MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_projects](#list-projects-tool) | Lists projects workspace-wide or scoped to a team, with optional status and lead filters. |
| [get\_project](#get-project-tool) | Retrieves a project's full details, including its teams, members, and initiatives. |
| [create\_project](#create-project-tool) | Creates a new project with one or more teams and optional lead and dates. |
| [update\_project](#update-project-tool) | Updates a project's name, description, status, lead, or dates. |
| [create\_project\_update](#create-project-update-tool) | Posts a health-tagged status update to a project. |
| [list\_initiatives](#list-initiatives-tool) | Lists initiatives and their child projects. |
| [list\_cycles](#list-cycles-tool) | Lists a team's cycles. |
| [get\_active\_cycle](#get-active-cycle-tool) | Returns a team's active cycle with progress and its issues grouped by workflow state. |
| [list\_documents](#list-documents-tool) | Lists planning documents, optionally filtered by project or initiative. |
| [create\_document](#create-document-tool) | Creates a planning document attached to a project. |
| [list\_teams](#list-teams-tool) | Lists teams for scoping projects and cycles. |

## Install the Linear Project Planning MCP server

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
    

## Linear Project Planning connection setup

View Linear Project Planning connection setup steps

There are two ways to connect to Linear:

- [OAuth 2.0](#oauth-2-0)
- [API key](#api-key)

### Download the Linear connector from the community library

View steps to download the Linear connector from the community library

Complete the following steps to install the Linear connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### OAuth 2.0

View OAuth 2.0 steps

#### Register an OAuth app

View register an OAuth app steps

Complete the following steps to register an OAuth app in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **API** in the sidebar.
   
   ![API administration page](/assets/linear-api-administration-page.Bvz7kApz.png)_API administration page_
   
4. Click **\+ New OAuth application** to add a new OAuth application.
   
5. Enter a name for your application in the **Application name** field. For example, `Workato`.
   
   ![Registering application](/assets/linear-registering-application.DQFPXn_w.png)_Registering application_
   
6. Enter the **Developer name** and a valid **Developer URL**.
   
7. Enter `https://www.workato.com/oauth/callback` in the **Callback URLs** field. Refer to the [Callback URL](/en/developing-connectors/registering-new-client#callback-url) documentation for more information.
   
8. Click **Create** to register the OAuth app.
   
9. Copy the **Client ID** and **Client secret** and store them in a secure location. These values are required to establish the connection in Workato.
   

#### Connect to Linear using OAuth 2.0

View connect to Linear using OAuth 2.0 steps

Complete the following steps to connect to Linear in Workato using OAuth 2.0:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using OAuth 2.0 authentication](/assets/linear-oauth-connection-setup.iMhSgAAT.png)_Connect to Linear using OAuth 2.0 authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **Client ID** and **Client secret** for your Linear account.
   
6. Select the necessary [OAuth scopes](https://developers.linear.app/docs/oauth/authentication) required for your integration.
   
7. Click **Connect**.
   

### API key

View API key steps

#### Create an API key

View create an API key steps

Complete the following steps to create an API key in Linear:

1. Sign in to your [Linear](https://linear.app/login) account.
   
2. Select your workspace name, then click **Settings**.
   
3. Select **Security & access** in the sidebar.
   
   ![Personal API keys](/assets/linear-personal-api-keys.CVZ33KIY.png)_Personal API keys_
   
4. Click **New API key**.
   
5. Enter a name for the API key in the **Key name** field.
   
6. Specify permissions for the API key in the **Permissions** field.
   
7. Click **Create** to create the API key.
   
8. Copy the API key and store it in a secure location. This value is required to establish the connection in Workato. Refer to the [Linear documentation](https://linear.app/docs/api-and-webhooks) for more information.
   

#### Connect to Linear using an API key

View connect to Linear using an API key steps

Complete the following steps to connect to Linear in Workato using an API key:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Linear` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Linear using API key authentication](/assets/linear-api-key-connection-setup.Cww6C7p1.png)_Connect to Linear using API key authentication_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the **API key** for your Linear account.
   
6. Click **Connect**.
   

## How to use Linear Project Planning MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_projects tool

The **list\_projects** tool returns projects across the workspace or scoped to one team, with optional status and lead filters. Your LLM uses this tool to find projects by team, status, or lead before retrieving one with [get\_project](#get-project-tool).

**Try asking**:

- `List all projects for the Platform team.`
- `Show me projects that are currently paused.`
- `Find projects led by Priya Patel.`

### get\_project tool

The **get\_project** tool looks up one project by name or ID. Your LLM uses this tool to retrieve a project's teams, members, and initiatives, before reporting on it or updating it. This tool only returns the first 50 project members found.

**Try asking**:

- `Show me the full details for the Checkout Redesign project.`
- `Who's on the Mobile App Relaunch project?`
- `What initiatives is the Billing Migration project part of?`

### create\_project tool

The **create\_project** tool starts a new project under one or more teams, with an optional lead and dates. Your LLM uses this tool when you ask to create a project and provide at least one name and team.

**Try asking**:

- `Create a new project called Q3 Onboarding Revamp for the Growth team.`
- `Set up a project for the mobile redesign, led by Jordan, starting next Monday.`
- `Start a new project on the Platform team with a target date of December 1st.`

> **DEFAULT PROJECT STATUS**
> 
> The new project uses the default status configured in Linear. Use [update\_project](#update-project-tool) afterward if you need to change it.

### update\_project tool

The **update\_project** tool changes a project's name, description, status, lead, or dates. Your LLM uses this tool to adjust one or more project fields when you ask to update them. This tool can't clear existing values.

**Try asking**:

- `Update the Billing Migration project's status to Started.`
- `Change the lead on the Checkout Redesign project to Sam.`
- `Push back the target date on the Mobile App Relaunch project to next quarter.`

### create\_project\_update tool

The **create\_project\_update** tool publishes a health-tagged status update on a project. Your LLM uses this tool to write a markdown narrative tagged `On track`, `At risk`, or `Off track` after you supply the project and the update text.

**Try asking**:

- `Post a status update on the Mobile App Relaunch project marking it at risk.`
- `Add an on-track update to the Checkout Redesign project summarizing this week's progress.`
- `Mark the Billing Migration project off track and explain why.`

### list\_initiatives tool

The **list\_initiatives** tool retrieves initiatives and up to 25 of their child projects. Your LLM uses this tool to review a roadmap.

**Try asking**:

- `What initiatives do we have, and which projects fall under each one?`
- `Show me the status and health of all our initiatives.`
- `List the projects under the Platform Modernization initiative.`

### list\_cycles tool

The **list\_cycles** tool returns a team's cycles. The newest cycles return first. Your LLM uses this tool to review a team's recent or upcoming sprints before inspecting one in detail.

**Try asking**:

- `List the last five cycles for the Platform team.`
- `Show me the Growth team's cycles.`
- `What cycles has the Mobile team run this quarter?`

### get\_active\_cycle tool

The **get\_active\_cycle** tool retrieves a team's current cycle, including its progress and its issues grouped by workflow state. Your LLM uses this tool for a sprint check-in, showing cycle progress alongside up to 200 of the most recently updated issues. Issues are read-only in this view.

**Try asking**:

- `How is the current sprint going for the Growth team?`
- `Show me the active cycle's progress for the Platform team.`
- `What issues are still in progress in this sprint?`

### list\_documents tool

The **list\_documents** tool retrieves planning documents, optionally filtered by project or initiative. Initiative names don't resolve automatically, so filtering by initiative requires an ID. Your LLM uses this tool to find existing planning docs before creating a new one or reporting what documentation already exists for a project.

**Try asking**:

- `Find the planning documents attached to the Checkout Redesign project.`
- `What documents exist for the Mobile App Relaunch project?`
- `List all planning documents in the workspace.`

### create\_document tool

The **create\_document** tool adds a new planning document to a project. Your LLM uses this tool to capture a markdown document after you supply a title, content, and the project to attach it to.

**Try asking**:

- `Create a planning doc called Launch Checklist attached to the Mobile App Relaunch project.`
- `Write up a new document with our Q3 goals for the Growth team's project.`
- `Add a kickoff doc to the Checkout Redesign project.`

### list\_teams tool

The **list\_teams** tool returns the teams available for scoping projects and cycles. Your LLM uses this tool to find a team's identifier or key before using it to filter [list\_projects](#list-projects-tool), [list\_cycles](#list-cycles-tool), or [get\_active\_cycle](#get-active-cycle-tool).

**Try asking**:

- `What teams exist in our workspace?`
- `Find the team key for the Platform team.`
- `List all teams with cycles enabled.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/mailchimp-campaign-management-mcp-server.md
description: >-
  Use the Mailchimp Campaign Management MCP server to connect your LLM to
  Mailchimp with audience curation, campaign authoring, and sending through
  natural conversation.
---

# Mailchimp Campaign Management MCP server

The Mailchimp Campaign Management MCP server enables LLMs to interact with MailChimp for the email-marketing lifecycle through natural conversation. It provides tools to curate audiences, add and tag contacts, assemble campaigns from supplied content, and send or schedule them without requiring direct interaction with the MailChimp interface.

> **MARKETING REPORTS MCP SERVER**
> 
> Use the [Mailchimp Marketing Reports](/en/mcp/prebuilt-mcps/mailchimp-marketing-reports-mcp-server) MCP server for read-only discovery and analytics across audiences, campaigns, and contacts.

## Uses

Use the Mailchimp Campaign Management MCP server to perform the following actions:

- Create audiences and organize the contacts a campaign will reach.
- Add contacts to an audience with a supplied subscription status.
- Update an existing contact's profile fields or status.
- Apply tags to contacts for grouping and targeting.
- Search for contacts to resolve identifiers before updating or tagging.
- Assemble a campaign draft from content you provide, with subject and sender.
- Edit a campaign's subject, sender, or recipient audience.
- Send a test email to preview a campaign before the real send.
- Send a campaign immediately, with explicit user confirmation.
- Schedule a campaign for a future time, or unschedule it before it sends.

### Example prompts

Use the following example prompts to invoke Mailchimp Campaign Management MCP server tools:

- `Add these contacts to my launch list.`
- `Create a new audience for our fall product launch.`
- `Tag these contacts as VIP so we can target them.`
- `Find the contact for jordan@example.com in my newsletter audience.`
- `Draft a campaign to my newsletter audience using this HTML content.`
- `Change the subject line on my draft campaign to "Summer Sale is here".`
- `Send a test of this campaign to me and my teammate.`
- `Send my newsletter campaign now.`
- `Schedule this campaign to send Tuesday at 9am.`
- `Unschedule the campaign I set for tomorrow morning.`

## Mailchimp Campaign Management MCP server tools

The Mailchimp Campaign Management MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_audiences](#list-audiences-tool) | Lists the audiences (lists) in the Mailchimp account. |
| [list\_campaigns](#list-campaigns-tool) | Lists campaigns in the account, with optional status filtering. |
| [get\_campaign](#get-campaign-tool) | Retrieves a single campaign's settings and content. |
| [search\_contacts](#search-contacts-tool) | Searches for contacts by email or name, with optional filtering by an audience. |
| [create\_audience](#create-audience-tool) | Creates a new audience (list) in the account. |
| [add\_contact](#add-contact-tool) | Adds a contact to an audience with a subscription status. |
| [update\_contact](#update-contact-tool) | Updates an existing contact's fields within an audience. |
| [tag\_contact](#tag-contact-tool) | Applies or updates tags on a contact within an audience. |
| [draft\_campaign](#draft-campaign-tool) | Creates a campaign draft from supplied content and settings. |
| [update\_campaign](#update-campaign-tool) | Updates a campaign's subject, sender, or recipient audience. |
| [send\_test](#send-test-tool) | Sends a test email of a campaign to specified addresses. |
| [send\_campaign](#send-campaign-tool) | Sends a campaign immediately. |
| [schedule\_campaign](#schedule-campaign-tool) | Schedules a campaign to send at a future time. |
| [unschedule\_campaign](#unschedule-campaign-tool) | Cancels the schedule of a campaign that has not started sending. |

## Install the Mailchimp Campaign Management MCP server

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
    

## API version

Workato's Mailchimp connector uses Mailchimp's API v2. Refer to Mailchimp's [API documentation](https://mailchimp.com/developer/marketing/docs/fundamentals/#api-versions) for more information.

## Mailchimp Campaign Management connection setup

View Mailchimp Campaign Management connection setup steps

Complete the following steps to connect to Mailchimp in Workato:

> **FEATURE AVAILABILITY**
> 
> The MailChimp connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

1. Provide a **Connection name** that identifies which MailChimp instance Workato is connected to.
   
   ![MailChimp connection](/assets/connection-setup.DX-BBZvF.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select a location for your connection.
   
3. Click **Connect**. This opens a MailChimp login window.
   
4. Enter your MailChimp account username and password. A window opens displaying a summary of the access Workato is provided with for the connection.
   
5. Click **Accept** to complete the connection setup.
   

### Mailchimp role requirements

Each tool's availability depends on the authenticating user's Mailchimp role. A user without the required role receives a permission-denied outcome rather than a partial result. Refer to the Mailchimp [Manage User Levels in Your Account](https://mailchimp.com/help/manage-user-levels-in-your-account/) guide for the complete list of role capabilities.

## How to use Mailchimp Campaign Management MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_audiences tool

The **list\_audiences** tool lists the audiences (lists) in the Mailchimp account. Your LLM uses this tool to return audiences with their identifiers, names, and member counts so it can choose the right audience to add contacts to or target with a campaign, typically before adding contacts or drafting a campaign when the target audience is not yet resolved.

**Try asking**:

- `Show me all the audiences in my Mailchimp account.`
- `Which lists do I have and how many contacts are in each?`
- `Find the audience I should add these contacts to.`

### list\_campaigns tool

The **list\_campaigns** tool lists campaigns in the account, with optional status filtering. Your LLM uses this tool to return campaigns with their identifiers, titles, subjects, status, and target audience so it can find a draft to send or schedule, filtering by status when you specify drafts, scheduled, or sent campaigns.

**Try asking**:

- `List my draft campaigns.`
- `Which campaigns are scheduled to send?`
- `Show me all my sent campaigns.`

### get\_campaign tool

The **get\_campaign** tool retrieves a single campaign's settings and content. Your LLM uses this tool to confirm a campaign's subject, sender, recipient audience, status, and current content before updating, sending, or scheduling it.

**Try asking**:

- `Show me the details of my launch campaign.`
- `What's the current subject and sender on this campaign?`
- `Confirm the recipient audience for this draft before I send it.`

### search\_contacts tool

The **search\_contacts** tool searches for contacts by email or name, with optional filtering by an audience. Your LLM uses this tool to resolve a contact's identifier before updating or tagging it, scoping the search to a single audience when you name one or spanning the account otherwise.

**Try asking**:

- `Find the contact for jordan@example.com.`
- `Search for contacts named Smith in my newsletter audience.`
- `Look up whether this person is already in my launch list.`

### create\_audience tool

The **create\_audience** tool creates a new audience (list) in the account. Your LLM uses this tool when you want to stand up a fresh audience for a campaign, using the name and the required audience settings you supply, such as default campaign settings, a permission reminder, the email-type option, and the physical contact details Mailchimp requires. If this tool fails, check whether your Mailchimp plan has reached its audience quota.

**Try asking**:

- `Create a new audience called "Fall Launch".`
- `Set up a fresh list for our newsletter subscribers.`
- `Make a new audience with these default sender details.`

### add\_contact tool

The **add\_contact** tool adds a contact to an audience with a subscription status. Your LLM uses this tool when you want to add a person to an audience. You can specify whether to set a member to `subscribed`, which immediately adds and asserts pre-existing consent, or send them a double opt-in confirmation email.

**Try asking**:

- `Add jordan@example.com to my newsletter audience as subscribed.`
- `Add these contacts to my launch list and send them a confirmation.`
- `Add this person with their first and last name to my audience.`

### update\_contact tool

The **update\_contact** tool updates an existing contact's fields within an audience. Your LLM uses this tool to change a contact's profile fields or subscription status, resolving the contact first when its identifier is unknown and leaving other fields unchanged.

**Try asking**:

- `Update the first name on this contact to "Jordan".`
- `Change the profile fields for jordan@example.com in my newsletter list.`
- `Fix the last name on this contact record.`

### tag\_contact tool

The **tag\_contact** tool applies or updates tags on a contact within an audience. Your LLM uses this tool to label or group a contact for targeting, adding or removing one or more tags and resolving the contact first when its identifier is unknown.

**Try asking**:

- `Tag jordan@example.com as VIP.`
- `Add the "early access" tag to these contacts.`
- `Remove the "prospect" tag from this contact.`

### draft\_campaign tool

The **draft\_campaign** tool creates a campaign draft from supplied content and settings. Your LLM uses this tool to turn ready content into a Mailchimp campaign, assembling a draft against the chosen audience with the subject and sender you provide and attaching the supplied HTML or plain-text content. The server doesn't generate, design, or modify the content. Subject lines longer than approximately 150 characters are truncated by Mailchimp.

**Try asking**:

- `Draft a campaign to my newsletter audience using this HTML.`
- `Turn this content into a Mailchimp campaign with the subject "Summer Sale".`
- `Create a draft campaign from this plain-text email for my launch list.`

### update\_campaign tool

The **update\_campaign** tool updates a campaign's subject, sender, or recipient audience. Your LLM uses this tool to change a campaign's settings before sending or scheduling, leaving other settings unchanged. It doesn't change body content or send and schedule the campaign.

**Try asking**:

- `Change the subject line on this campaign to "Summer Sale is here".`
- `Update the sender name on my draft campaign.`
- `Switch the recipient audience for this campaign to my VIP list.`

### send\_test tool

The **send\_test** tool sends a test email of a campaign to specified addresses. Your LLM uses this tool to let you preview a campaign safely before the real send by emailing a test to yourself or colleagues, without sending to the campaign's audience. The campaign must have HTML content; a plain-text-only draft can't be tested.

**Try asking**:

- `Send a test of this campaign to me.`
- `Email a preview of my launch campaign to my teammate.`
- `Send a test of this campaign to these addresses.`

### send\_campaign tool

The **send\_campaign** tool sends a campaign immediately. Once sent, a campaign cannot be recalled. The server requires explicit user confirmation that you want to send the campaign now before using this tool.

**Try asking**:

- `Send my newsletter campaign now.`
- `Yes, send the launch campaign to my audience.`
- `Confirm and send this campaign immediately.`

### schedule\_campaign tool

The **schedule\_campaign** tool schedules a campaign to send at a future time. Your LLM uses this tool when you want a campaign to go out at a specific time in the future, after confirming the campaign's settings. Scheduling remains reversible until the send begins. The campaign must have HTML content to be scheduled.

**Try asking**:

- `Schedule this campaign to send Tuesday at 9am.`
- `Set my launch campaign to go out next Monday morning.`
- `Schedule this campaign for tomorrow at noon.`

### unschedule\_campaign tool

The **unschedule\_campaign** tool cancels the schedule of a campaign that has not started sending. Your LLM uses this tool to cancel or change a scheduled send before it goes out, returning the campaign to a paused state. It has no effect once a send has started.

**Try asking**:

- `Unschedule the campaign I set for tomorrow morning.`
- `Cancel the scheduled send on my launch campaign.`
- `Stop this campaign from sending on Tuesday.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/marketo-leads-and-activity-ops-mcp-server.md
description: >-
  Use the Marketo Leads and Activity Ops MCP server to connect your LLM to
  Marketo with tools to retrieve, create, update leads, review activity history,
  and manage static list membership through natural language.
---

# Marketo Leads and Activity Ops MCP server

The Marketo Leads and Activity Ops MCP server enables LLMs to interact with Marketo lead data through natural conversation. It provides tools to retrieve, create, and update lead records, inspect activity history, and manage static list membership, supporting day-to-day operational workflows for Marketing Ops teams without requiring direct interaction with the Marketo interface.

## Uses

Use the Marketo Leads and Activity Ops MCP server to perform the following actions:

- Retrieve leads using filters such as email or Marketo ID
- Get specific lead details by Marketo ID
- Create new lead records with field values
- Update fields on existing lead records
- Review activity history for specific leads
- List and discover static lists with filters
- Get metadata for specific static lists
- Retrieve members of static lists
- View static lists associated with specific leads
- Add leads to static lists
- Remove leads from static lists

### Example prompts

Use the following example prompts to invoke Marketo Leads and Activity Ops MCP server tools:

- `Find the lead with email jade@example.com.`
- `Get details for lead ID 1207345.`
- `Create a new lead for Marco Reyes at techcorp.com.`
- `Update this lead's job title to VP of Marketing.`
- `Show me the activity history for this lead.`
- `List all static lists in the Q1 Campaign program.`
- `Get details about the Webinar Attendees list.`
- `Who are the members of the Enterprise Prospects list?`
- `What lists is this lead a member of?`
- `Add these leads to the Trade Show Contacts list.`
- `Remove this lead from the Nurture Campaign list.`

## Marketo Leads and Activity Ops MCP server tools

The Marketo Leads and Activity Ops MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_leads](#list-leads-tool) | Retrieves leads using explicit filters such as email or Marketo ID. |
| [get\_lead](#get-lead-tool) | Retrieves a Marketo lead by ID. |
| [create\_lead](#create-lead-tool) | Creates a new lead record with provided field values. |
| [update\_lead](#update-lead-tool) | Updates fields on an existing lead record. |
| [get\_lead\_activities](#get-lead-activities-tool) | Retrieves activity history for a lead you specify. |
| [list\_static\_lists](#list-static-lists-tool) | Retrieves static lists using supported filters. |
| [get\_static\_list](#get-static-list-tool) | Retrieves metadata for a static list you specify. |
| [get\_static\_list\_members](#get-static-list-members-tool) | Retrieves members of a static list you specify. |
| [get\_lead\_list\_memberships](#get-lead-list-memberships-tool) | Retrieves static lists associated with a specific lead. |
| [add\_leads\_to\_static\_list](#add-leads-to-static-list-tool) | Adds one or more leads to a static list. |
| [remove\_leads\_from\_static\_list](#remove-leads-from-static-list-tool) | Removes one or more leads from a static list. |

## Install the Marketo Leads and Activity Ops MCP server

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
    

## Marketo connection setup

View Marketo connection setup steps

The Marketo connector uses custom authentication.

> **CUSTOM SERVICE CLIENTS**
> 
> Marketo exposes REST endpoints to enable integration platforms like Workato to remotely access and execute core functionalities. We recommend you create a custom service client specifically for Workato to facilitate this integration.
> 
> Key benefits of using a custom service client include:
> 
> - **Isolated logging**: All operations are logged under a dedicated custom service client for integration and workflow processes. This approach enhances tracking and troubleshooting by isolating issues related to specific integration platforms.
> - **Customized permissions**: A custom service client allows for tailored permissions and security profiles, independent of individual employee user accounts.
> 
> Ensure that the custom service client is granted all necessary permissions to perform the required actions for your integration scenario. If a `403` error occurs during recipe execution, it indicates that the service client lacks the appropriate permissions for the action.

### Minimum scopes

View minimum scopes

You must select the following minimum role scopes when you create a new API role. Refer to [Create an API role](#create-an-api-role) for more information.

- `Read-Only Activity`
- `Read-Write Activity`
- `Read-Only Lead`
- `Read-Write Lead`
- `Read-Only Asset`
- `Read-Write Asset`

### Marketo setup for custom authentication

Complete the following steps to set up a custom authentication connection to Marketo in Workato:

- [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint)
- [Create an API role](#create-an-api-role)
- [Create an API user](#create-an-api-user)
- [Create a custom service for Workato](#create-a-custom-service-for-workato)
- [Retrieve client credentials](#retrieve-client-credentials)

#### Retrieve the REST API endpoint

View retrieve the REST API endpoint steps

Complete the following steps to retrieve the REST API Endpoint in Marketo:

1. Sign in to your Marketo instance as a user with administrator privileges.
   
2. Go to **Admin > Web Services**.
   
3. In the **REST API** section, copy and save the **Endpoint** for use in Workato.
   

#### Create an API role

View create an API role steps

Complete the following steps to create an API role in Marketo:

1. Go to **Admin > Users & Roles** and select the **Roles** tab.
   
2. Click **New Role**.
   
3. Provide a name for your new role in the **Role Name** field. Optionally, add a description in the **Description** field.
   
4. Select the **Access API** checkbox in the **Permissions** field.
   
5. Click **Create** to create the API role.
   

#### Create an API user

View create an API user steps

Complete the following steps to create an API user in Marketo:

1. Go to **Admin > Users & Roles** and select the **Users** tab.
   
2. Click **Create API Only User**.
   
3. Fill out the **Email**, **First Name**, and **Last Name** fields.
   
4. Select the checkbox for the API role you created in the previous step from the **Roles** menu.
   
5. Click **CREATE API ONLY USER**.
   

#### Create a custom service

View create a custom service steps

Creating a custom service enables you to retrieve the client ID and client secret used to establish a connection in Workato. Refer to the [Marketo Engage Developer Documentation](https://developers.marketo.com/rest-api/custom-services/) for more information about custom services.

Complete the following steps to create a custom service in Marketo:

1. Go to **Admin > LaunchPoint**.
   
2. Click **New > New Service**.
   
3. Enter a descriptive **Display name** and select **Custom** from the **Service** drop-down menu.
   
4. Enter a description in the **Description** field.
   
5. Select the user you created in the previous step from the **API Only User** drop-down menu.
   
6. Click **Create**.
   

#### Retrieve client credentials

View retrieve client credentials steps

Complete the following steps to retrieve client credentials in Marketo:

1. Select **View details** for the new custom service you created in the previous step.
   
   ![View custom service](/assets/view-details-marketo.DY2NcPr5.png)_View custom service_
   
2. Copy and save the **Client Id** and **Client Secret** for use in Workato.
   

### Connect to Marketo with custom authentication

View connect to Marketo with custom authentication steps

Complete the following steps to connect to Marketo in Workato:

1. Select **Create > Connection** or press C twice.
   
2. Search for `Marketo` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Name your connection](/assets/marketo-connection.BpjczBep.png)_Name your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the base URL of your Marketo instance in the **REST Endpoint** field. For example, if your REST endpoint is `https://123-ABC-456.mktorest.com/rest`, enter `123-ABC-456` in this field. Refer to [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint) for more information.
   
6. Enter the **Client Id** from Marketo in the **Custom Service client ID** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
7. Enter the **Client Secret** from Marketo in the **Custom Service client secret** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
8. Click **Connect**.
   

### Project property configuration

The Marketo Leads and Activity Ops MCP server supports the following project-level properties to control behavior and defaults:

| Project-level property | Description |
| --- | --- |
| `default_activity_time_window` | Defines the default time range applied when **get\_lead\_activities** is invoked without a **time\_window** parameter. This ensures bounded and predictable activity retrieval. |
| `default_activity_type_ids` | Defines the set of activity type IDs used when **get\_lead\_activities** is invoked without an **activity\_type\_ids** parameter. Defaults to a standard engagement activity set, including: `1 — Visit Webpage`, `2 — Fill Out Form`, `6 — Send Email`, `7 — Email Delivered`, `8 — Email Bounced`, `9 — Unsubscribe Email`, `10 — Open Email`, `11 — Click Email`, and `27 — Email Bounced Soft`. |
| `max_records` | Defines the maximum number of records returned in a single response for collection-returning tools, such as **list\_leads**, **get\_lead\_activities**, **get\_static\_list\_members**, and **get\_lead\_list\_memberships**. This quota applies per response page, not the total retrievable dataset. |
| `max_batch_size` | Defines the maximum number of lead IDs allowed in batch operations. Applies to **add\_leads\_to\_static\_list** and **remove\_leads\_from\_static\_list**. This value can't exceed the Marketo API limit of `300`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/zendesk-knowledge-base-project-property.DGAT1hbT.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and make your changes. For example, set `max_batch_size` to `250` or `max_records` to `25`.
   

## How to use Marketo Leads and Activity Ops MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_leads tool

The **list\_leads** tool retrieves leads using explicit filters, such as email or Marketo ID. Your LLM uses this tool to find or look up a lead using email or Marketo ID.

**Try asking**:

- `Find the lead with email jade@example.com.`
- `Look up leads with Marketo IDs 12345 and 67890.`
- `Search for the lead with email marco@acme.com.`
- `Get leads matching these email addresses.`

### get\_lead tool

The **get\_lead** tool retrieves a Marketo lead by ID. Your LLM uses this tool when a lead has been uniquely identified by Marketo ID.

**Try asking**:

- `Get details for lead ID 1207345.`
- `Show me the complete information for Marketo lead 67890.`
- `Retrieve lead 54321 from Marketo.`
- `What are the details for this lead ID?`

### create\_lead tool

The **create\_lead** tool creates a new lead record with provided field values. Your LLM uses this tool when you explicitly ask to create a new lead.

**Try asking**:

- `Create a new lead for Marco Reyes at acme.com.`
- `Add Jade Anderson as a lead with email jade@acme.com.`
- `Create a lead record for Alex Chen, VP of Sales.`
- `Add a new Marketo lead for this contact.`

### update\_lead tool

The **update\_lead** tool updates fields on an existing lead record. Your LLM uses this tool to modify an existing lead after ensuring the lead is uniquely identified.

**Try asking**:

- `Update this lead's job title to VP of Marketing.`
- `Change the company name for lead 1207345 to Acme Inc.`
- `Update Mei's phone number to 555-0123.`
- `Modify this lead's status to Qualified.`

### get\_lead\_activities tool

The **get\_lead\_activities** tool retrieves activity history for a lead you specify. Your LLM uses this tool to view a lead's activity or engagement.

**Try asking**:

- `Show me the activity history for this lead.`
- `What engagement activities has lead 1207345 had?`
- `Get the activity log for Jade Anderson.`
- `Review this lead's interaction history.`

### list\_static\_lists tool

The **list\_static\_lists** tool retrieves static lists using supported filters. Your LLM uses this tool to discover or browse static lists, using the exact list name when provided or program name when you request lists belonging to a specific program.

**Try asking**:

- `List all static lists in the Q1 Campaign program.`
- `Show me static lists named 'Webinar Attendees'.`
- `What static lists exist in Marketo?`
- `Find lists in the Product Launch program.`

### get\_static\_list tool

The **get\_static\_list** tool retrieves metadata for a static list you specify. Your LLM uses this tool to get details about a specific list.

**Try asking**:

- `Get details about the Webinar Attendees list.`
- `Show me metadata for list ID 456.`
- `What are the details of the Enterprise Prospects list?`
- `Get information about this static list.`

### get\_static\_list\_members tool

The **get\_static\_list\_members** tool retrieves members of a static list you specify with pagination support for large lists. Your LLM uses this tool to view the members of a list.

**Try asking**:

- `Who are the members of the Enterprise Prospects list?`
- `Show me all leads in the Webinar Attendees list.`
- `List members of the Trade Show Contacts list.`
- `Get the leads in list ID 789.`

### get\_lead\_list\_memberships tool

The **get\_lead\_list\_memberships** tool retrieves static lists associated with a lead you specify. Your LLM uses this tool to view which lists a lead belongs to.

**Try asking**:

- `What lists is this lead a member of?`
- `Show me all static lists containing lead 12345.`
- `Which lists include Jade Anderson?`
- `What static lists is Marco in?`

### add\_leads\_to\_static\_list tool

The **add\_leads\_to\_static\_list** tool adds one or more leads to a static list. Your LLM uses this tool to add leads to a list, first resolving lead identities using `list_leads` or `get_lead`.

**Try asking**:

- `Add these leads to the Trade Show Contacts list.`
- `Put lead 12345 in the Enterprise Prospects list.`
- `Add Jade and Marco to the Webinar Attendees list.`
- `Include this lead in the Nurture Campaign list.`

### remove\_leads\_from\_static\_list tool

The **remove\_leads\_from\_static\_list** tool removes one or more leads from a static list. Your LLM uses this tool to remove leads from a list.

**Try asking**:

- `Remove this lead from the Nurture Campaign list.`
- `Take lead 12345 out of the Enterprise Prospects list.`
- `Remove Jade from the Webinar Attendees list.`
- `Remove these leads from the Trade Show Contacts list.`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/marketo-program-ops-mcp-server.md
description: >-
  Use the Marketo Program Ops MCP server to connect your LLM to Marketo with
  tools to create, manage, and run marketing programs, activate campaigns, and
  track performance through natural language.
---

# Marketo Program Ops MCP server

The Marketo Program Ops MCP server enables LLMs to manage and execute marketing programs in Marketo Engage through natural conversation. It provides tools to set up programs, activate campaigns, manage membership and statuses, and track operational performance without requiring direct interaction with the Marketo interface.

## Uses

Use the Marketo Program Ops MCP server to perform the following actions:

- List marketing programs with status and time filters
- Get details for specific programs by ID
- Create new marketing programs
- Clone existing programs for reuse
- Update program metadata
- List smart campaigns within programs
- Get details of specific smart campaigns
- Activate and deactivate trigger campaigns
- Schedule batch campaign runs
- Retrieve program members and their statuses
- Add leads to programs
- Remove leads from programs
- Update program member statuses
- List and update program tokens
- Track program performance metrics
- Monitor email performance within programs

### Example prompts

Use the following example prompts to invoke Marketo Program Ops MCP server tools.

- `List all active marketing programs.`
- `Get details for program ID 123074.`
- `Create a new webinar program for Q2.`
- `Clone the Q1 webinar program for Q2.`
- `Update this program's description.`
- `Show me the smart campaigns in this program.`
- `Activate the trigger campaign for form submissions.`
- `Schedule the batch campaign to run tomorrow at 9am.`
- `Who are the members of this program?`
- `Add these leads to the webinar program.`
- `Update member status to 'Attended' for these leads.`
- `What tokens are defined for this program?`
- `How is the Q1 campaign performing?`
- `Show me email performance for this program.`

## Marketo Program Ops MCP server tools

The Marketo Program Ops MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_programs](#list-programs-tool) | Lists marketing programs with optional status and update-time filters. |
| [get\_program](#get-program-tool) | Retrieves details for a program by ID. |
| [create\_program](#create-program-tool) | Creates a new marketing program. |
| [clone\_program](#clone-program-tool) | Creates a new program by cloning an existing program. |
| [update\_program](#update-program-tool) | Updates program metadata. |
| [list\_smart\_campaigns](#list-smart-campaigns-tool) | Lists smart campaigns within a program. |
| [get\_smart\_campaign](#get-smart-campaign-tool) | Retrieves details of a smart campaign. |
| [activate\_trigger\_campaign](#activate-trigger-campaign-tool) | Activates a trigger campaign. |
| [deactivate\_trigger\_campaign](#deactivate-trigger-campaign-tool) | Deactivates a trigger campaign. |
| [schedule\_batch\_campaign](#schedule-batch-campaign-tool) | Schedules a batch campaign run. |
| [get\_program\_members](#get-program-members-tool) | Retrieves members of a program with their statuses. |
| [add\_program\_members](#add-program-members-tool) | Adds leads to a program. |
| [remove\_program\_members](#remove-program-members-tool) | Removes leads from a program. |
| [update\_program\_member\_status](#update-program-member-status-tool) | Updates the status of program members. |
| [list\_program\_tokens](#list-program-tokens-tool) | Lists tokens defined for a program. |
| [update\_program\_token](#update-program-token-tool) | Updates the value of a program token. |
| [get\_program\_performance](#get-program-performance-tool) | Retrieves operational performance metrics for a program. |
| [get\_email\_performance](#get-email-performance-tool) | Retrieves email performance metrics for emails within a program. |

## Install the Marketo Program Ops MCP server

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
    

## Marketo connection setup

View Marketo connection setup steps

The Marketo connector uses custom authentication.

> **CUSTOM SERVICE CLIENTS**
> 
> Marketo exposes REST endpoints to enable integration platforms like Workato to remotely access and execute core functionalities. We recommend you create a custom service client specifically for Workato to facilitate this integration.
> 
> Key benefits of using a custom service client include:
> 
> - **Isolated logging**: All operations are logged under a dedicated custom service client for integration and workflow processes. This approach enhances tracking and troubleshooting by isolating issues related to specific integration platforms.
> - **Customized permissions**: A custom service client allows for tailored permissions and security profiles, independent of individual employee user accounts.
> 
> Ensure that the custom service client is granted all necessary permissions to perform the required actions for your integration scenario. If a `403` error occurs during recipe execution, it indicates that the service client lacks the appropriate permissions for the action.

#### Minimum scopes

View minimum scopes

You must select the following minimum role scopes when you create a new API role. Refer to [Create an API role](#create-an-api-role) for more information.

- `Read-Only Activity`
- `Read-Write Activity`
- `Read-Only Lead`
- `Read-Write Lead`
- `Read-Only Asset`
- `Read-Write Asset`

### Marketo setup for custom authentication

Complete the following steps to set up a custom authentication connection to Marketo in Workato:

- [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint)
- [Create an API role](#create-an-api-role)
- [Create an API user](#create-an-api-user)
- [Create a custom service for Workato](#create-a-custom-service-for-workato)
- [Retrieve client credentials](#retrieve-client-credentials)

#### Retrieve the REST API endpoint

View retrieve the REST API endpoint steps

Complete the following steps to retrieve the REST API Endpoint in Marketo:

1. Sign in to your Marketo instance as a user with administrator privileges.
   
2. Go to **Admin > Web Services**.
   
3. In the **REST API** section, copy and save the **Endpoint** for use in Workato.
   

#### Create an API role

View create an API role steps

Complete the following steps to create an API role in Marketo:

1. Go to **Admin > Users & Roles** and select the **Roles** tab.
   
2. Click **New Role**.
   
3. Provide a name for your new role in the **Role Name** field. Optionally, add a description in the **Description** field.
   
4. Select the **Access API** checkbox in the **Permissions** field.
   
5. Click **Create** to create the API role.
   

#### Create an API user

View create an API user steps

Complete the following steps to create an API user in Marketo:

1. Go to **Admin > Users & Roles** and select the **Users** tab.
   
2. Click **Create API Only User**.
   
3. Fill out the **Email**, **First Name**, and **Last Name** fields.
   
4. Select the checkbox for the API role you created in the previous step from the **Roles** menu.
   
5. Click **CREATE API ONLY USER**.
   

#### Create a custom service

View create a custom service steps

Creating a custom service enables you to retrieve the client ID and client secret used to establish a connection in Workato. Refer to the [Marketo Engage Developer Documentation](https://developers.marketo.com/rest-api/custom-services/) for more information about custom services.

Complete the following steps to create a custom service in Marketo:

1. Go to **Admin > LaunchPoint**.
   
2. Click **New > New Service**.
   
3. Enter a descriptive **Display name** and select **Custom** from the **Service** drop-down menu.
   
4. Enter a description in the **Description** field.
   
5. Select the user you created in the previous step from the **API Only User** drop-down menu.
   
6. Click **Create**.
   

#### Retrieve client credentials

View retrieve client credentials steps

Complete the following steps to retrieve client credentials in Marketo:

1. Select **View details** for the new custom service you created in the previous step.
   
   ![View custom service](/assets/view-details-marketo.DY2NcPr5.png)_View custom service_
   
2. Copy and save the **Client Id** and **Client Secret** for use in Workato.
   

### Connect to Marketo with custom authentication

View connect to Marketo with custom authentication steps

Complete the following steps to connect to Marketo in Workato:

1. Select **Create > Connection** or press C twice.
   
2. Search for `Marketo` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Name your connection](/assets/marketo-connection.BpjczBep.png)_Name your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the base URL of your Marketo instance in the **REST Endpoint** field. For example, if your REST endpoint is `https://123-ABC-456.mktorest.com/rest`, enter `123-ABC-456` in this field. Refer to [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint) for more information.
   
6. Enter the **Client Id** from Marketo in the **Custom Service client ID** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
7. Enter the **Client Secret** from Marketo in the **Custom Service client secret** field. Refer to [Retrieve client credentials](#retrieve-client-credentials) for more information.
   
8. Click **Connect**.
   

## How to use Marketo Program Ops MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_programs tool

The **list\_programs** tool lists marketing programs with optional status and update-time filters. Your LLM uses this tool to browse or list programs, or to find programs when only partial or approximate information is available.

**Try asking**:

- `List all active marketing programs.`
- `Show me programs updated in the last week.`
- `Find programs with 'webinar' in the name.`
- `List all archived programs.`

### get\_program tool

The **get\_program** tool retrieves details for a program by ID. Your LLM uses this tool to get details for a program using the program ID from **list\_programs** or provided by you.

**Try asking**:

- `Get details for program ID 123074.`
- `Show me complete information for this program.`
- `What are the details of program 5678?`
- `Retrieve program information for the Q1 webinar.`

### create\_program tool

The **create\_program** tool creates a new marketing program. Your LLM uses this tool to create a new program from scratch and asks for required fields if missing.

**Try asking**:

- `Create a new webinar program for Q2.`
- `Set up a new email campaign program.`
- `Make a new event program for the trade show.`
- `Create a nurture program for new leads.`

### clone\_program tool

The **clone\_program** tool creates a new program by cloning an existing program. Your LLM uses this tool to reuse an existing program setup for a new campaign using a source program ID. Your LLM prompts you to verify token values before activation.

**Try asking**:

- `Clone the Q1 webinar program for Q2.`
- `Copy the email campaign setup for a new product.`
- `Duplicate this event program for next month.`
- `Create a copy of the nurture program.`

### update\_program tool

The **update\_program** tool updates program metadata. Your LLM uses this tool to modify program metadata. This tool isn't used for structural changes or smart campaign modifications.

**Try asking**:

- `Update this program's description.`
- `Change the program name to 'Q2 Product Launch'.`
- `Update program tags for better organization.`
- `Modify the program metadata.`

### list\_smart\_campaigns tool

The **list\_smart\_campaigns** tool lists smart campaigns within a program. Your LLM uses this tool to view or inspect campaigns within a program using the program ID.

**Try asking**:

- `Show me the smart campaigns in this program.`
- `List all campaigns for program 123074.`
- `What campaigns are in the webinar program?`
- `Display campaigns for this marketing program.`

### get\_smart\_campaign tool

The **get\_smart\_campaign** tool retrieves details of a smart campaign. Your LLM uses this tool to inspect a campaign before activation or scheduling.

**Try asking**:

- `Get details for this smart campaign.`
- `Show me campaign configuration for the welcome email.`
- `What are the details of campaign ID 78900?`
- `Review the trigger campaign setup.`

### activate\_trigger\_campaign tool

The **activate\_trigger\_campaign** tool activates a trigger campaign. Your LLM uses this tool to start a trigger campaign running automatically on qualifying events.

**Try asking**:

- `Activate the trigger campaign for form submissions.`
- `Turn on the welcome email trigger.`
- `Start the lead scoring campaign.`
- `Activate the automated response campaign.`

### deactivate\_trigger\_campaign tool

The **deactivate\_trigger\_campaign** tool deactivates a trigger campaign. Your LLM uses this tool to stop an active trigger campaign.

**Try asking**:

- `Deactivate the form submission trigger.`
- `Turn off the welcome email campaign.`
- `Stop the automated response trigger.`
- `Deactivate this trigger campaign.`

### schedule\_batch\_campaign tool

The **schedule\_batch\_campaign** tool schedules a batch campaign run. Your LLM uses this tool to run a batch campaign at a time you specify.

**Try asking**:

- `Schedule the batch campaign to run tomorrow at 9am.`
- `Run the email blast on Friday at 2pm.`
- `Schedule this campaign for next Monday morning.`
- `Set the nurture campaign to run at 10am.`

### get\_program\_members tool

The **get\_program\_members** tool retrieves members of a program with their statuses. Your LLM uses this tool to view program participants or their statuses using the program ID.

**Try asking**:

- `Who are the members of this program?`
- `Show me participants in the webinar program.`
- `List members and their statuses for program 123074.`
- `Get the member list for this campaign.`

### add\_program\_members tool

The **add\_program\_members** tool adds leads to a program. Your LLM uses this tool to add leads to a program.

**Try asking**:

- `Add these leads to the webinar program.`
- `Include these people in the nurture campaign.`
- `Add Jade and Marco to this program.`
- `Enroll these leads in the event program.`

### remove\_program\_members tool

The **remove\_program\_members** tool removes leads from a program. Your LLM uses this tool to remove participants from a program.

**Try asking**:

- `Remove these leads from the program.`
- `Take Marco out of the webinar program.`
- `Remove unqualified leads from this campaign.`
- `Delete these members from the program.`

### update\_program\_member\_status tool

The **update\_program\_member\_status** tool updates the status of program members. Your LLM uses this tool to advance or correct the status of program members.

**Try asking**:

- `Update member status to 'Attended' for these leads.`
- `Change Jade's status to 'Registered'.`
- `Mark these members as 'No Show'.`
- `Update status to 'Engaged' for the active participants.`

### list\_program\_tokens tool

The **list\_program\_tokens** tool lists tokens defined for a program. Your LLM uses this tool to inspect token values before execution or cloning.

**Try asking**:

- `What tokens are defined for this program?`
- `Show me program tokens and their values.`
- `List all tokens for the webinar program.`
- `What variables are set for this campaign?`

### update\_program\_token tool

The **update\_program\_token** tool updates the value of a program token. Your LLM uses this tool to set or update execution parameters for a program.

**Try asking**:

- `Update the webinar date token to April 15th.`
- `Change the speaker name token to 'Dr. Sarah Michaels'.`
- `Set the event location token.`
- `Update program variables with new values.`

### get\_program\_performance tool

The **get\_program\_performance** tool retrieves operational performance metrics for a program. Your LLM uses this tool to understand program membership and campaign execution performance.

**Try asking**:

- `How is the Q1 campaign performing?`
- `Show me performance metrics for this program.`
- `Get membership statistics for the webinar program.`
- `What are the program performance numbers?`

### get\_email\_performance tool

The **get\_email\_performance** tool retrieves email performance metrics for emails within a program. Your LLM uses this tool to view email engagement metrics for a program.

**Try asking**:

- `Show me email performance for this program.`
- `What are the open and click rates for the campaign emails?`
- `Get email engagement metrics for the webinar program.`
- `How are the emails in this program performing?`

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
  https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-dynamics-365-crm-mcp-server.md
description: >-
  Use the Microsoft Dynamics 365 CRM MCP server to connect your LLM to Microsoft
  Dynamics 365 with tools to manage accounts, contacts, leads, opportunities,
  and cases.
---

# Microsoft Dynamics 365 CRM MCP server

The Microsoft Dynamics 365 CRM MCP server lets LLMs work with Microsoft Dynamics 365 for core sales and service CRM workflows. It provides tools to search, create, update, and transition accounts, contacts, leads, opportunities, and cases without requiring direct interaction with the Microsoft Dynamics 365 interface.

## Uses

Use the Microsoft Dynamics 365 CRM MCP server to perform the following actions:

- Find accounts, contacts, leads, opportunities, and cases by name, email, phone, or other identifying details
- Create new records or update fields on existing accounts, contacts, leads, opportunities, and cases
- Qualify a lead, and optionally create related account, contact, and opportunity records
- Resolve, reassign, or move a case to a different queue
- Record a win or loss outcome on an opportunity
- Log tasks, calls, appointments, and notes against a record
- Retrieve records related to an account, contact, lead, opportunity, or case
- Look up field definitions and choice values before creating or updating a record

### Example prompts

Use the following example prompts to invoke Microsoft Dynamics 365 CRM MCP server tools:

- `Find the lead for Alex Patel at Acme Corp.`
- `Qualify this lead and create the related opportunity.`
- `Update the estimated close date on this opportunity.`
- `Log the call I just had with Acme Corp.`
- `Resolve this case with a note explaining the fix.`
- `Reassign this case to Kai Lee.`
- `Move this case to the escalations queue.`
- `Mark this opportunity as won.`
- `What fields can I set on a case?`
- `Find the queue ID for the billing team.`

## Microsoft Dynamics 365 CRM MCP server tools

The Microsoft Dynamics 365 CRM MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_record](#get-record-tool) | Retrieves a single CRM record by ID or alternate key. |
| [search\_records](#search-records-tool) | Searches for CRM records by field values you supply, or by identity attributes, such as name, email, or phone. |
| [describe\_schema](#describe-schema-tool) | Describes the fields, types, and choice values of a supported CRM object. |
| [create\_record](#create-record-tool) | Creates a new CRM record on a supported object. |
| [update\_record](#update-record-tool) | Updates selected fields on an existing CRM record. |
| [upsert\_record](#upsert-record-tool) | Creates or updates a CRM record using a declared alternate key. |
| [create\_activity](#create-activity-tool) | Logs a task, phone call, or appointment against an existing CRM record. |
| [create\_note](#create-note-tool) | Adds a note to an existing CRM record. |
| [list\_related\_records](#list-related-records-tool) | Retrieves records related to a given parent record through a supported relationship. |
| [qualify\_lead](#qualify-lead-tool) | Runs the standard lead qualification transition. |
| [resolve\_case](#resolve-case-tool) | Resolves an open case. |
| [close\_opportunity](#close-opportunity-tool) | Records a win or loss outcome on an open opportunity. |
| [reassign\_case](#reassign-case-tool) | Reassigns ownership of a case to a different user or team. |
| [move\_case\_to\_queue](#move-case-to-queue-tool) | Moves a case from its current queue into a specified destination queue. |

## Install the Microsoft Dynamics 365 CRM MCP server

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
    

## Microsoft Dynamics 365 CRM connection setup

View Microsoft Dynamics 365 CRM connection setup steps

### API version

The Microsoft Dynamics 365 connector uses the Microsoft Dynamics 365 API v8.0 and v9.0.

### Register the Workato app in the Azure Portal

The Microsoft Dynamics 365 CRM MCP server requires an authorization code grant connection to Microsoft Dynamics 365.

Complete the following steps to register the Workato app and assign it permissions for authorization code grant connections.

1. Register the Workato app in the Azure Portal
   
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
      
   
2. Assign permissions to your app
   
   1. In the navigation sidebar, select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Dynamics CRM**.
      
      ![Select Dynamics CRM](/assets/dynamics-crm.DFHMudAF.png)_Select Dynamics CRM_
      
   3. Select **Delegated permissions**, then select the `user_impersonation` checkbox.
      
      ![Select permissions](/assets/app-permissions-dynamics.TGgAEhVP.png)_Select permissions_
      
   4. Click **Add permissions**.
      
   
   **Note**: Admin consent is required for specific permissions. Refer to the [Granting admin consent](/en/connectors/dynamics-crm#admin-consent) section to learn more.
   
   ![Admin consent screen](/assets/dynamics-admin-consent.D-ilQt9x.png)_Admin consent screen_
   
3. Obtain the Application (client) ID from the Azure Portal
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy the `Application (client) ID` for use in Workato.
      
   
4. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   

Return to Workato to finish setting up your connection.

### Complete setup in Workato

Complete the following steps to establish a Microsoft Dynamics 365 connection using authorization code grant authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Microsoft Dynamics 365` as your connection on the **New connection** page.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Dynamics 365](/assets/auth-code-grant.AitXdIwi.png)_Connect to Microsoft Dynamics 365_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** to specify a cloud connection or select an on-prem group for the connection.
   
   > **ON-PREM CONNECTIONS**
   > 
   > If using an on-prem connection, you must obtain a client ID by registering your Microsoft Dynamics 365 app with the Active Directory Federation Service. [Learn more](https://technet.microsoft.com/itpro/powershell/windows/adfs/add-adfsclient).
   
6. Select **Authorization code grant** as the **Authentication type**.
   
7. Enter your Microsoft Dynamics 365 environment’s full domain, such as `abc.crm.dynamics.com`, in the **Subdomain** field.
   
8. Use the **Account type** drop-down menu to specify whether the account you're connecting to is hosted in the cloud or on-prem.
   
9. Fill in the **AD domain name** field. This field is required if you select **On-premise** as the **Account type**. For example, if your AD server is `https://abc.adfs.dynamics.com/adfs`, the AD domain name is `abc.adfs.dynamics.com`.
   
10. Enter your [client ID](#auth-register) in the **Client ID** field.
    
11. Enter your [client secret](#auth-register) in the **Client secret** field.
    
12. _Optional_. Use the **Version** drop-down menu to specify the API version you plan to use in your connection. Options include:
    
    - Version 8
    - Version 9
13. _Optional_. Expand the **Advanced settings** section to configure the **Resource URI** for which connection should be authorized. If left empty, all resources in the subdomain will be authorized. For example, `https://abc.crm.dynamics.com/api/data/v9.0/`.
    
14. _Optional_. Select a custom OAuth profile to use for the connection from the **Custom OAuth profile** drop-down menu.
    
15. Click **Sign in with Microsoft**.
    

### Microsoft Dynamics 365 role requirements

Every tool call runs under the Dataverse security role and row-level permissions of the connected account, not a separate service account. Read tools only return records and related data that the connected account's security role and row-level access permit. A request that calls for a privilege the connected account doesn't have fails rather than returning a partial result. Refer to [Create or edit a security role to manage access](https://learn.microsoft.com/en-us/power-platform/admin/create-edit-security-role) for the complete list of role capabilities.

## How to use Microsoft Dynamics 365 CRM MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_record tool

The **get\_record** tool retrieves a single CRM record by ID or alternate key. Your LLM uses this tool to inspect a record's current fields before acting on it, or to confirm a write it just made.

**Try asking**:

- `Show me the full details for this lead.`
- `What are the current fields on this opportunity?`
- `Confirm the case status after I just resolved it.`
- `Get the details for this account.`

### search\_records tool

The **search\_records** tool searches for CRM records by field values or by identity attributes, such as name, email, or phone. Your LLM uses this tool to find accounts, contacts, leads, opportunities, or cases before reading, updating, or transitioning them, or to look up a queue ID before moving a case.

**Try asking**:

- `Find the lead for Alex Patel at Acme Corp.`
- `Search for open cases assigned to Jade Chen.`
- `Find the contact with the email kiran@example.com.`
- `Find the queue ID for the billing team.`

### describe\_schema tool

The **describe\_schema** tool describes the fields, types, and choice values of a supported CRM object. Your LLM uses this tool to discover writable fields and valid choice values on an account, contact, lead, opportunity, or case before creating or updating a record.

**Try asking**:

- `What fields can I set on a case?`
- `List the valid status reasons for an opportunity.`
- `What fields are available on the lead object?`
- `Show me the choice values for case priority.`

### create\_record tool

The **create\_record** tool creates a new CRM record on a supported object. Your LLM uses this tool to add a new account, contact, lead, opportunity, or case after a conversation or inbound request.

**Try asking**:

- `Create a new lead for Dana Lopez at Acme Corp.`
- `Add a contact for Kiran Nguyen.`
- `Create a case for this support request.`
- `Add a new opportunity for the Acme Corp renewal.`

### update\_record tool

The **update\_record** tool updates selected fields on an existing CRM record. Your LLM uses this tool to change fields you specify on an account, contact, lead, opportunity, or case.

**Try asking**:

- `Update the phone number on this contact.`
- `Change the estimated close date on this opportunity.`
- `Update the priority on this case to high.`
- `Set the industry field on this account.`

### upsert\_record tool

The **upsert\_record** tool creates or updates a CRM record using a declared alternate key. Your LLM uses this tool to write a record without first checking whether it already exists, such as when syncing records from another system.

**Try asking**:

- `Create or update the contact with the email jade@example.com.`
- `Upsert this account using its external ID.`
- `Sync this lead using its source system key.`
- `Create or update this record without creating a duplicate.`

### create\_activity tool

The **create\_activity** tool logs a task, phone call, or appointment against an existing CRM record. Your LLM uses this tool to record an interaction on an account, contact, lead, or opportunity after a call, meeting, or follow-up.

**Try asking**:

- `Log the call I just had with Acme Corp.`
- `Schedule a follow-up task on this lead for next week.`
- `Log an appointment with Kiran Patel for tomorrow.`
- `Record a phone call on this opportunity.`

### create\_note tool

The **create\_note** tool adds a note to an existing CRM record. Your LLM uses this tool to capture context on a record that doesn't fit a structured field.

**Try asking**:

- `Add a note to this case explaining how it was fixed.`
- `Note that this opportunity is waiting on legal review.`
- `Add a note to this account about the renewal discussion.`
- `Leave a note on this lead with the qualification details.`

### list\_related\_records tool

The **list\_related\_records** tool retrieves records related to a parent record through a supported relationship. Your LLM uses this tool to review an account's contacts, a contact's opportunities, or a case's activities before acting on the parent record.

**Try asking**:

- `What contacts are linked to this account?`
- `Show me the opportunities associated with this account.`
- `List the activities logged on this case.`
- `What cases are related to this account?`

### qualify\_lead tool

The **qualify\_lead** tool runs the standard lead qualification transition. Your LLM uses this tool to mark a lead as qualified. It creates the related account, contact, or opportunity records only when you ask for them.

**Try asking**:

- `Qualify this lead and create the related opportunity.`
- `Convert this lead now that it's qualified.`
- `Qualify this lead for Acme Corp in USD.`
- `Promote this lead to an opportunity.`

### resolve\_case tool

The **resolve\_case** tool resolves an open case. Your LLM uses this tool to resolve a case with a resolution reason and an optional note after the issue is fixed.

**Try asking**:

- `Resolve this case with a note explaining the fix.`
- `Close this case as resolved.`
- `Mark this support case resolved.`
- `Resolve this case with the reason "Information provided."`

### close\_opportunity tool

The **close\_opportunity** tool records a win or loss outcome on an open opportunity. Your LLM uses this tool to mark an opportunity won or lost and capture the outcome details.

**Try asking**:

- `Mark this opportunity as won.`
- `Close this opportunity as lost and note the reason.`
- `Record a win on the Acme Corp opportunity.`
- `Close this deal with a loss reason of "price."`

### reassign\_case tool

The **reassign\_case** tool reassigns ownership of a case to a different user or team. Your LLM uses this tool to hand off a case without changing its queue.

**Try asking**:

- `Reassign this case to Kai Lee.`
- `Hand this case off to the escalations team.`
- `Change the owner of this case to Kiran Patel.`
- `Reassign this ticket to another agent.`

### move\_case\_to\_queue tool

The **move\_case\_to\_queue** tool moves a case from its current queue into a destination queue you specify. Your LLM uses this tool to route a case to a different team without changing who owns it.

**Try asking**:

- `Move this case to the escalations queue.`
- `Route this case to the billing queue.`
- `Move this ticket into the Tier 2 queue.`
- `Send this case to the on-call queue.`

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/microsoft-teams-conversations-mcp-server.md
description: >-
  Use the Microsoft Teams Conversations MCP server to connect your LLM to
  Microsoft Teams with tools to search, retrieve, and participate in
  conversations across channels and chats through natural language.
---

# Microsoft Teams Conversations MCP server

The Microsoft Teams Conversations MCP server enables LLMs to search, retrieve, and participate in Microsoft Teams conversations through natural conversation. It provides tools to find topics, projects, or customers, retrieve message history, get thread context, list teams, channels, and chats, and post messages or replies without requiring direct interaction with the Microsoft Teams interface.

## Uses

Use the Microsoft Teams Conversations MCP server to perform the following actions:

- List Microsoft Teams teams the authenticated user is a member of
- List channels within a specified Microsoft Teams team
- List one-on-one, group, and meeting chats the user participates in
- Retrieve messages and thread replies from a Microsoft Teams channel or chat
- Search for messages matching a keyword across Microsoft Teams channels and chats
- Post a new message to a Microsoft Teams channel or chat
- Reply to an existing message thread in a Microsoft Teams channel

### Example prompts

Use the following example prompts to invoke Microsoft Teams Conversations MCP server tools:

- `Which Microsoft Teams teams am I a member of?`
- `What channels are available in the Sales team?`
- `Show me my recent Microsoft Teams chats.`
- `Get the last 20 messages from the #general channel.`
- `Find discussions about the Acme renewal across my Microsoft Teams conversations.`
- `Search for any messages about the Q2 launch plan.`
- `Post a message to the #announcements channel.`
- `Reply to this thread in the Engineering channel.`

## Microsoft Teams Conversations MCP server tools

The Microsoft Teams Conversations MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_teams](#list-teams-tool) | Lists teams the authenticated user is a member of. |
| [list\_channels](#list-channels-tool) | Lists team channels that you specify. |
| [list\_chats](#list-chats-tool) | Lists one-on-one or group chats the authenticated user participates in. |
| [get\_messages](#get-messages-tool) | Retrieves messages or thread replies from a Microsoft Teams channel or chat. |
| [search\_messages](#search-messages-tool) | Searches for Microsoft Teams messages matching a keyword query across channels and chats the user can access. |
| [send\_message](#send-message-tool) | Posts a new message to a Microsoft Teams channel or chat on behalf of the authenticated user. |
| [reply\_to\_message](#reply-to-message-tool) | Posts a reply to an existing message thread in a Microsoft Teams channel. |

## Install the Microsoft Teams Conversations MCP server

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
    

## Microsoft Teams connection setup

View Microsoft Teams connection setup steps

The Microsoft Teams Conversations connector supports the following authentication types:

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

### Minimum scopes

View minimum scopes

The Microsoft Teams connector requires the following scopes. You must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Channel.ReadBasic.All`
- `ChannelMessage.Read.All`
- `ChannelMessage.Send`
- `Chat.Read`
- `Chat.ReadWrite`
- `ChatMessage.Send`
- `Team.ReadBasic.All`
- `User.Read`
- `offline_access`

### Authorization code grant authentication (OAuth 2.0)

Use the Tenant ID/Domain value with tenant-specific account types.

#### Microsoft Teams setup for authorization code grant authentication

View Microsoft Teams setup for authorization code grant authentication steps

Complete the following steps to set up Microsoft Teams for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

##### Register the Workato app in the Azure portal

Complete the following steps to register the Workato app and assign permissions for authorization code grant connections:

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
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions as outlined in [Minimum scopes](#minimum-scopes).
   
4. Click **Add permissions**. Refer to [Connect Microsoft Entra ID to the Microsoft Teams connector](/en/connectors/microsoft-teams#admin-consent) if specific permissions require admin consent.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft Teams with authorization code grant authentication

View connect to Microsoft Teams with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common** and **Tenant-specific**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that aren't restricted to a specific organization (tenant).
   
   ![Microsoft Teams Common connection setup](/assets/teams-connect-common.CRs_A8zB.png)_Microsoft Teams Common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection setup](/assets/teams-connect-tenant-auth-code.Dunozk1-.png)_Microsoft Teams Tenant specific connection setup_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID), or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id) for more information.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This authentication type requires the following values:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Microsoft Teams setup for client credentials-based authentication (OAuth 2.0)

View Microsoft Teams setup for client-credentials based authentication steps

Complete the following steps to set up Microsoft Teams for client credentials-based authentication:

- [Register the Workato App in the Azure portal](#client-credentials-register)
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
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
3. Add the required permissions as outlined in [Minimum scopes](#minimum-scopes).
   
4. Click **Add permissions**. Refer to [Connect Microsoft Entra ID to the Microsoft Teams connector](/en/connectors/microsoft-teams#admin-consent) if specific permissions require admin consent.
   

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
   

#### Connect to Microsoft Teams with client credentials-based authentication

View connect to Microsoft Teams with client credentials-based authentication steps

Complete the following steps to set up a client credentials-based connection to Microsoft Teams in Workato:

1. Click **Create > Connection**.
   
2. Search for `Microsoft Teams` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Microsoft Teams Tenant specific connection account type setup](/assets/teams-connect-tenant-client-cred.DUtPSHGJ.png)_Microsoft Teams Tenant specific connection account type setup_
   
6. Provide your **Tenant ID/Domain**. This is the `Directory (tenant) ID` for your app. Refer to [Register an app in Azure](#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Obtain the User ID from the Azure portal](#obtain-user-id), [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids), and [Generate a client secret](#generate-client-secret) for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## How to use Microsoft Teams Conversations MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_teams tool

The **list\_teams** tool lists teams the authenticated user is a member of. Your LLM uses this tool to list teams you belong to.

**Try asking**:

- `Which Microsoft Teams teams am I a member of?`
- `Show me all the teams I have access to.`
- `What teams exist in my Microsoft Teams environment?`
- `Find the team ID for the Sales team.`

### list\_channels tool

The **list\_channels** tool lists channels within a team that you specify. Your LLM uses this tool to list channels for a team. Requires a team ID from `list_teams`.

**Try asking**:

- `What channels are available in the Sales team?`
- `List all channels in the Engineering Microsoft Teams team.`
- `Show me the channels I can access in this team.`
- `Find the channel ID for #announcements.`

### list\_chats tool

The **list\_chats** tool lists one-on-one, group, and meeting chats the authenticated user participates in. Your LLM uses this tool to provide recent chats and chat activity.

**Try asking**:

- `Show me my recent Microsoft Teams chats.`
- `List my group chats in Microsoft Teams.`
- `Find my chat with the project team.`
- `What meeting chats do I have from this week?`

### get\_messages tool

The **get\_messages** tool retrieves messages or thread replies from a Microsoft Teams channel or chat. Your LLM uses this tool to provide recent messages from a channel or chat with conversation context for catch-up or meeting preparation, and thread replies for a specific Microsoft Teams channel message.

**Try asking**:

- `Get the last 20 messages from the #general channel.`
- `Show me recent messages in the product team chat.`
- `Pull the thread replies for this message in the Engineering channel.`
- `Catch me up on what was discussed in #sales-updates today.`

### search\_messages tool

The **search\_messages** tool searches for Microsoft Teams messages matching a keyword query across channels and chats the user can access. Your LLM uses this tool to find discussions about a topic, project, customer, or keyword across your Microsoft Teams conversations, to locate a past decision or discussion, or to search broadly rather than reading a specific channel.

**Try asking**:

- `Find discussions about the Acme renewal across my Microsoft Teams conversations.`
- `Search for any messages about the Q2 launch plan.`
- `Did anyone discuss the budget approval in Microsoft Teams?`
- `Find past decisions about the API migration in my channels.`

### send\_message tool

The **send\_message** tool posts a new message to a Microsoft Teams channel or chat on behalf of the authenticated user. Your LLM presents the message content and target to you for approval before posting.

**Try asking**:

- `Post a message to the #announcements channel.`
- `Send a message to the design team chat in Microsoft Teams.`
- `Post an update to the #project-status channel.`
- `Send this summary to the Sales team channel.`

### reply\_to\_message tool

The **reply\_to\_message** tool posts a reply to an existing message thread in a Microsoft Teams channel on behalf of the authenticated user. Your LLM presents the reply content and target thread to you for approval before posting.

**Try asking**:

- `Reply to this thread in the Engineering channel.`
- `Post my response to this message in the #product channel.`
- `Reply to the latest thread in #customer-success.`
- `Add my update to this Microsoft Teams thread.`

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
