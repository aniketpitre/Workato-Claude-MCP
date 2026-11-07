---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/gitlab-explorer-mcp-server.md'
description: >-
  Use the GitLab Explorer MCP server to connect your LLM to GitLab with tools to
  retrieve and manage projects, issues, merge requests, commits, and pipelines
  through natural language.
---

# GitLab Explorer MCP server

The GitLab Explorer MCP server enables LLMs to interact with GitLab projects through natural conversation. It provides tools to retrieve and manage issues, merge requests (MRs), access repository context, and check pipeline status without requiring direct interaction with the GitLab interface.

## Uses

Use the GitLab Explorer MCP server to perform the following actions:

- Retrieve metadata and overview information for a GitLab project
- List and retrieve issues with filtering and sorting
- Create new issues and update existing issue metadata
- List and retrieve merge requests
- Create new merge requests and update existing merge request metadata
- Add comments to issues or merge requests
- Retrieve commit history for a project
- Search across GitLab projects for issues, merge requests, code, or projects
- Retrieve user context and associated projects
- Retrieve group or subgroup context, including metadata and structure
- Check pipeline status at the job level for a merge request or commit

### Example prompts

Use the following example prompts to invoke GitLab Explorer MCP server tools:

- `Give me an overview of this project.`
- `List all open issues assigned to me.`
- `Get the details for issue #142.`
- `Create a new issue for this bug.`
- `Update this issue's assignee and label.`
- `Show me open merge requests waiting for review.`
- `Get the details for this MR.`
- `Open a new merge request from this branch.`
- `Add a comment to this issue.`
- `What commits have been made in the last week?`
- `Search for issues mentioning this error across my projects.`
- `Show me my projects and team repos.`
- `Why did the pipeline fail on this MR?`

## GitLab Explorer MCP server tools

The GitLab Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [get\_project](#get-project-tool) | Retrieves metadata and overview information for a GitLab project. |
| [list\_issues](#list-issues-tool) | Lists issues in a GitLab project with filtering and sorting. |
| [get\_issue](#get-issue-tool) | Retrieves detailed information about an issue. |
| [create\_issue](#create-issue-tool) | Creates a new issue in a GitLab project. |
| [update\_issue](#update-issue-tool) | Updates metadata for an existing issue. |
| [list\_merge\_requests](#list-merge-requests-tool) | Lists merge requests in a GitLab project. |
| [get\_merge\_request](#get-merge-request-tool) | Retrieves detailed information about a merge request. |
| [create\_merge\_request](#create-merge-request-tool) | Creates a new merge request from an existing branch. |
| [update\_merge\_request](#update-merge-request-tool) | Updates metadata for an existing merge request. |
| [add\_note](#add-note-tool) | Adds a comment to an issue or merge request. |
| [list\_commits](#list-commits-tool) | Retrieves commit history for a project. |
| [search\_gitlab](#search-gitlab-tool) | Searches across GitLab projects for issues, merge requests, code, or projects. |
| [get\_user\_context](#get-user-context-tool) | Retrieves user context and associated projects. |
| [get\_group\_context](#get-group-context-tool) | Retrieves group or subgroup context, including metadata and structure. |
| [get\_pipeline\_status](#get-pipeline-status-tool) | Retrieves detailed pipeline status for a merge request or commit. |

## Install the GitLab Explorer MCP server

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
    

## GitLab connection setup

View GitLab connection setup steps

The GitLab connector supports the following authentication types:

- [Personal access token](#personal-access-token-authentication)
- [OAuth 2.0](#oauth2-authentication)
- [Password grant](#password-grant-authentication)

### Install GitLab from the community library

View install GitLab from the community library steps

Complete the following steps to install the GitLab connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Minimum scopes

View minimum scopes

You must add the following minimum scopes to connect to GitLab:

- `api`
- `read_api`
- `create_runner`
- `manage_runner`
- `read_repository`
- `read_user`
- `write_repository`
- `read_registry`
- `write_registry`

### Personal access token authentication

You must create a personal access token in GitLab to use this authentication method.

View personal access token authentication setup steps

#### GitLab setup for personal access token authentication

View GitLab setup for personal access token authentication steps

Complete the following steps to set up GitLab for personal access token authentication:

1. Select your avatar.
   
2. Click **Edit profile**.
   
3. Click **Access > Personal access tokens** in the sidebar.
   
4. Use the **Generate token** drop-down menu to select **Legacy token**.
   
5. Enter a **Token name**.
   
6. Optional. Enter a **Token description**.
   
7. Enter an **Expiration date** for the token, or leave this field blank to use the default of 365 days from today (the maximum).
   
8. Select the personal access token scopes. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
9. Click **Generate token**.
   
10. Copy and save the **personal access token** for use in Workato.
    
    > **SAVE YOUR TOKEN**
    > 
    > You can't view it again after you leave or refresh the page. If you lose the token, you must generate a new one.
    

#### Connect to GitLab with personal access token authentication

View connect to GitLab with personal access token authentication steps

Complete the following steps to set up a personal access token connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab personal access token connection](/assets/gitlab-pat-connection.kVTQpRZC.png)_GitLab personal access token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
7. Enter the **Personal access token**. Refer to [GitLab setup for personal access token authentication](#pat-setup) for more information.
   
8. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
9. Click **Connect**.
   

### OAuth 2.0 authentication

You must generate credentials in GitLab to use this authentication method.

View OAuth 2.0 authentication setup steps

#### GitLab setup for OAuth 2.0 authentication

View GitLab setup for OAuth 2.0 authentication steps

Complete the following steps to set up GitLab for OAuth 2.0 authentication:

1. Select your avatar.
   
2. Click **Edit profile**.
   
3. Click **Access > Applications** in the sidebar.
   
4. Click **Add new application**.
   
5. Enter a **Name** for the new application.
   
6. Enter `https://www.workato.com/oauth/callback` for the **Redirect URI**.
   
7. Select the **Scopes** required for your application. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
8. Click **Save application**.
   
9. Copy and save the **Application ID** and **Secret** for use in Workato.
   
   > **SAVE YOUR SECRET**
   > 
   > You can't view it again after you leave or refresh the page. If you lose the secret, you must generate a new one.
   

#### Connect to GitLab with OAuth 2.0 authentication

View connect to GitLab with OAuth 2.0 authentication steps

Complete the following steps to set up an OAuth 2.0 connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab OAuth 2.0 connection](/assets/gitlab-oauth2-connection.B4EVGr8U.png)_GitLab OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **OAuth 2.0 (Client ID & Secret)**.
   
7. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
8. Enter the **Application ID** and **Client secret**. Refer to [GitLab setup for OAuth 2.0 authentication](#oauth2-setup) for more information.
   
9. Select the **Scopes**. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
10. Click **Connect**.
    
11. Click **Authorize `<your app name>`** to authorize the connection.
    

### Password grant authentication

Use your GitLab account username and password for this authentication method.

View password grant authentication steps

#### Connect to GitLab with password grant authentication

Complete the following steps to set up a password grant connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab password grant connection](/assets/gitlab-password-grant-connection.B_EovV0-.png)_GitLab password grant connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **Password grant**.
   
7. Enter the **Username** and **Password**.
   
8. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
9. Click **Connect**.
   

## How to use GitLab Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### get\_project tool

The **get\_project** tool retrieves metadata and overview information for a GitLab project. Your LLM uses this tool to provide a project's details, description, visibility, or general status.

**Try asking**:

- `Give me an overview of this project.`
- `What's the description and visibility of this repo?`
- `Show me the project metadata for this repository.`
- `Get the details for this GitLab project.`

### list\_issues tool

The **list\_issues** tool lists issues in a GitLab project with filtering and sorting. Your LLM uses this tool to provide a list of issues, including requests filtered by status, assignee, label, or milestone.

**Try asking**:

- `List all open issues assigned to me.`
- `Show me issues labeled "bug" that are still open.`
- `What issues are in the current milestone?`
- `List recently closed issues in this project.`

### get\_issue tool

The **get\_issue** tool retrieves detailed information about an issue. Your LLM uses this tool to find a specific issue with its full context, description, comments, or metadata.

**Try asking**:

- `Get the details for issue #142.`
- `Show me the full context for this issue before I work on it.`
- `What's the current status and assignee for this issue?`
- `Pull up the description and comments for this issue.`

### create\_issue tool

The **create\_issue** tool creates a new issue in a GitLab project. Your LLM uses this tool to create an issue.

**Try asking**:

- `Create a new issue for this bug.`
- `Open an issue to track this feature request.`
- `Log a new issue with this title and description.`
- `Create an issue and assign it to this team member.`

### update\_issue tool

The **update\_issue** tool updates metadata for an existing issue. Your LLM uses this tool to update, assign, label, reopen, or close an issue.

**Try asking**:

- `Update this issue's assignee and label.`
- `Close this issue.`
- `Reopen this issue and add the "in progress" label.`
- `Change the milestone for this issue.`

### list\_merge\_requests tool

The **list\_merge\_requests** tool lists merge requests in a GitLab project. Your LLM uses this tool to review workload, including filtering by status, author, or assignee.

**Try asking**:

- `Show me open merge requests waiting for review.`
- `List all MRs I've authored this week.`
- `What merge requests are currently open in this project?`
- `Show me merged MRs from the last 7 days.`

### get\_merge\_request tool

The **get\_merge\_request** tool retrieves detailed information about a merge request. Your LLM uses this tool to find a specific merge request with its full context, diff summary, reviewers, or status.

**Try asking**:

- `Get the details for this MR.`
- `Show me the description and reviewers for merge request #88.`
- `What's the current status of this merge request?`
- `Pull up the full context for this MR before I review it.`

### create\_merge\_request tool

The **create\_merge\_request** tool creates a new merge request from an existing branch. Your LLM uses this tool to create or open a merge request.

**Try asking**:

- `Open a new merge request from this branch.`
- `Create an MR to merge my feature branch into main.`
- `Open a merge request with this title and description.`
- `Create a draft MR from this branch.`

### update\_merge\_request tool

The **update\_merge\_request** tool updates metadata for an existing merge request. Your LLM uses this tool to update merge request details such as title, description, assignee, or labels.

**Try asking**:

- `Update the title and description on this MR.`
- `Assign this merge request to a reviewer.`
- `Add labels to this merge request.`
- `Mark this MR as ready for review.`

### add\_note tool

The **add\_note** tool adds a comment to an issue or merge request. Your LLM uses this tool to comment, add an update, or leave context on an issue or MR.

**Try asking**:

- `Add a comment to this issue.`
- `Leave a note on this MR explaining the approach.`
- `Post an update comment on this issue.`
- `Add context to this merge request as a comment.`

### list\_commits tool

The **list\_commits** tool retrieves commit history for a project. Your LLM uses this tool to provide information on recent changes or commits in a repository.

**Try asking**:

- `What commits have been made in the last week?`
- `Show me the recent commit history for this project.`
- `Who committed to this repo yesterday?`
- `List the latest commits on the main branch.`

### search\_gitlab tool

The **search\_gitlab** tool searches across GitLab projects for issues, merge requests, code, or projects. Your LLM uses this tool to find content across multiple projects rather than within a single known project.

**Try asking**:

- `Search for issues mentioning this error across my projects.`
- `Find merge requests referencing this ticket number.`
- `Search for code containing this function name.`
- `Look for any projects related to this service.`

### get\_user\_context tool

The **get\_user\_context** tool retrieves user context and associated projects. Your LLM uses this tool to resolve references such as "my projects" or "team repositories" and to scope searches or workload to a specific user.

**Try asking**:

- `Show me my projects and team repos.`
- `Look up the profile for this GitLab username.`
- `Resolve my GitLab username and associated projects.`
- `Scope this search to my team's repositories.`

### get\_group\_context tool

The **get\_group\_context** tool retrieves group or subgroup context, including metadata and structure. Your LLM uses this tool to resolve details about a GitLab group or subgroup path, such as finding group metadata or understanding subgroup structure.

**Try asking**:

- `Show me the details for this GitLab group.`
- `What's the subgroup structure under my-group?`
- `Get the metadata for this organization.`
- `List the subgroups in this group.`

### get\_pipeline\_status tool

The **get\_pipeline\_status** tool retrieves detailed pipeline status for a merge request or commit, including job-level results and logs. Your LLM uses this tool to investigate pipeline failures and review job-level details.

**Try asking**:

- `Why did the pipeline fail on this MR?`
- `Show me the job-level results for this pipeline.`
- `Which job is failing in this pipeline?`
- `Get the pipeline logs for this commit.`

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
