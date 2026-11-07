---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/google-directory-end-user-mcp-server.md
description: >-
  Use the Google Directory End User MCP server to connect your LLM to Google
  Workspace with a curated set of tools to search for colleagues, retrieve
  profile information, and explore organizational relationships.
---

# Google Directory End User MCP server

The Google Directory End User MCP server enables LLMs to help you discover people and understand organizational context using Google Workspace directory information through natural conversation. It provides tools to search for colleagues, retrieve profile information, and explore organizational relationships without navigating directory interfaces or admin tools.

The Google Directory End User MCP server helps you answer basic identity and context questions—such as who someone is, what team they're on, or who to contact—by accessing Google Workspace directory information as your system of record for user identities and organizational relationships.

## Uses

Use the Google Directory End User MCP server when you plan to perform the following actions:

- Search for colleagues by name, email, or phone number
- Look up someone's role, department, and contact information
- Find the right person to contact for a specific team or function
- Understand organizational relationships and reporting structures
- Discover profile information for people in your organization
- Browse directory listings to explore your organization's structure

### Example prompts

Use the following example prompts to invoke Google Directory End User MCP server tools:

- `Find Sarah Chen in the directory.`
- `Who is the engineering manager for the mobile team?`
- `Look up the contact information for someone in HR.`
- `What's Maria's job title and department?`
- `Search for people named Alex in the product organization.`
- `Show me everyone in the sales department.`

## Google Directory End User MCP server tools

The Google Directory End User MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_users](#search-users-tool) | Searches for people in the directory by matching names, email addresses, or phone numbers. |
| [get\_user\_profile](#get-user-profile-tool) | Retrieves profile information for a user you specify, including organizational role, department, and contact details. |
| [list\_users](#list-users-tool) | Returns a paginated list of users from the directory. |

## Install the Google Directory End User MCP server

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
    

## Google Directory connection setup

View Google Directory connection setup steps

The Google Workspace connector supports the following authentication methods:

- [Service account](/en/connectors/google-workspace#service-account)
- [OAuth 2.0](/en/connectors/google-workspace#oauth-2-0)

You can use a service account to authenticate without a personal user account. For consistent use, Workato recommends service account authentication.

You must enable the Google Workspace API to complete the connection setup.

> **REQUIRED SCOPES FOR SERVICE ACCOUNT AUTHENTICATION**
> 
> Ensure that you have the following required permissions to successfully connect to Google Workspace using a service account:
> 
> - `admin.directory.user`
> - `admin.directory.orgunit`
> - `admin.directory.domain`
> - `admin.directory.group`
> - `admin.directory.group.member`
> - `admin.datatransfer`
> - `admin.directory.device.mobile.action`
> - `admin.directory.userschema`
> - `admin.reports.audit.readonly`
> - `admin.reports.usage.readonly`
> - `admin.directory.rolemanagement`
> - `admin.directory.user.security`
> 
> The service account impersonates the user based on the email address you provide during the connection setup after authentication is complete.

### Service account authentication

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

View Service account authentication steps

Complete the following steps to connect to Google Workspace using service account authentication:

Service account authentication requires the following prerequisites:

- [Create a service account and generate a private key](#set-up-a-google-service-account)
- [Enable the Google Workspace API](https://support.google.com/googleapi/answer/6158841)

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace** as your connection.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Service account**.
   
6. Enter the service account's email address in the **GCP project service account email** field.
   
   ![Retrieve your GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Retrieve your GCP Project service account email_
   
7. Enter the **Private key** and **User email**. Retrieve the private key from the downloadable JSON. Include both the `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n`.
   
8. Click **Sign in with Google**.
   

#### Set up a Google service account

View Google service account setup steps

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
   

### OAuth 2.0 authentication

View OAuth 2.0 authentication steps

Complete the following steps to connect to Google Workspace using OAuth 2.0 authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **Google Workspace** as your connection.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **OAuth 2.0**.
   
6. Optional. Expand the **Advanced settings** section and select OAuth 2.0 scopes to request for your connection.
   
   Workato requests the following scopes by default in addition to the scopes you select:
   
   | Description | Scope requested |
   | --- | --- |
   | View and manage the provisioning of users on your domain | `admin.directory.user` |
   | View and manage organization units on your domain | `admin.directory.orgunit` |
   | View and manage the provisioning of domains for your customers | `admin.directory.domain` |
   | View and manage the provisioning of user schemas on your domain | `admin.directory.userschema` |
   | View and manage the provisioning of groups on your domain | `admin.directory.group` |
   | View and manage group subscriptions on your domain | `admin.directory.group.member` |
   | View and manage data transfers between users in your organization | `admin.datatransfer` |
   | Manage your mobile devices by performing administrative tasks | `admin.directory.device.mobile.action` |
   | View audit reports for your Google Workspace domain | `admin.reports.audit.readonly` |
   | View usage reports for your Google Workspace domain | `admin.reports.usage.readonly` |
   | Manage delegated admin roles for your domain | `admin.directory.rolemanagement` |
   | Manage data access permissions for users on your domain | `admin.directory.user.security` |
   
   Refer to the [Google Directory API scopes](https://developers.google.com/admin-sdk/directory/v1/guides/authorizing) or [OAuth 2.0 Scopes for Google APIs](https://developers.google.com/identity/protocols/oauth2/scopes) guide for more information about scopes.
   
7. Click **Sign in with Google**.
   
   ![Connect to Google Workspace](/assets/setup-1.CAQwtw4I.png)_Connect to Google Workspace_
   
8. Sign in with your Google account. Your Google account must have admin privileges to make organization-wide changes in Google Workspace.
   
9. Click **Allow** to enable Workato to access your Google account.
   
   ![Enable Workato to access your Google account](/assets/oauth-scopes.qLH22Y9E.png)_Enable Workato to access your Google account_
   

## How to use Google Directory End User MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_users tool

The **search\_users** tool searches the Google Workspace directory for users matching the criteria you provide and returns basic identity and organizational information for each matching user. Your LLM uses this tool to find people when you provide partial, ambiguous, or informal references to colleagues.

> **CLARIFY AMBIGUOUS SEARCHES**
> 
> If your search query is likely to return many results, your LLM may ask a clarifying question to narrow down the results (such as department or location).

**Try asking**:

- `Find Sarah Chen in the directory.`
- `Search for people named Alex in engineering.`
- `Look up someone with the email address starting with j.anderson.`
- `Who works in the San Francisco office with 'Manager' in their title?`

### get\_user\_profile tool

The **get\_user\_profile** tool retrieves profile and organizational information for a user by their unique directory identifier. Your LLM uses this tool to provide authoritative identity context after discovering or selecting a person, including profile attributes and organizational relationship information visible in the directory.

**Try asking**:

- `What's Maria Rodriguez's job title and department?`
- `Show me the full profile for sarah.chen@company.com.`
- `Get the contact details and organizational info for Alex Johnson.`
- `Who does Jordan Kim report to and what team are they on?`

### list\_users tool

The **list\_users** tool returns a paginated list of users from the directory. Your LLM uses this tool to browse the directory, explore organizational structure, or get an overview of people in specific departments or locations.

**Try asking**:

- `List all users in the engineering department.`
- `Show me everyone in the New York office.`
- `Give me a list of people in the product organization.`
- `Browse the directory to see who's on the sales team.`

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
