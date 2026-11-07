---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/marketing-event-program-orchestration-mcp-server.md
description: >-
  Use the Marketing Event Program Orchestration MCP server to connect your LLM
  to Marketo, Google Calendar, Slack, and ZoomInfo with governed event program
  creation, calendar scheduling, and registrant list imports that commit only
  after you approve a real preview.
---

# Marketing Event Program Orchestration MCP server

The Marketing Event Program Orchestration MCP server enables LLMs to interact with Marketo, Google Calendar, Slack, and ZoomInfo for managing event programs and registrant lists through natural conversation. It provides tools to resolve an event's type and region to the correct template, folder, and channel, create or clone a program, book a calendar hold, look up existing programs, and validate and import a lead list.

## Uses

Use the Marketing Event Program Orchestration MCP server to perform the following actions:

- Create a new Marketo event program from a pre-configured template, folder, and channel
- Book a calendar hold on Google Calendar or Outlook for a newly created event program
- Look up an existing Marketo event program by name or ID before importing members into it
- Import a registrant or lead list into an existing Marketo event program
- Review row counts and a create-versus-update breakdown before an import commits
- Approve a preview before creating a program or importing members
- Fill blank lead fields with ZoomInfo firmographic data during import
- Check the status of an in-progress program creation or lead import
- Recover an interrupted import or program creation session without repeating earlier steps
- Receive a Slack notification for newly created programs and completed imports

Additionally, use the server's built-in [Event360 MCP app](#event360-mcp-app) to fill in an event's details or review a lead file's column mapping before either one commits.

### Example prompts

Use the following example prompts to invoke Marketing Event Program Orchestration MCP server tools:

- `Set up a new webinar program for APJ next month.`
- `Get this registrant CSV into the Q2 webinar program.`
- `Did my lead import finish?`
- `What's the URL for the trade show program I created last week?`
- `I navigated away. What was I uploading?`
- `Create a field event in NORAM and book the calendar for it.`
- `Open Event Ops.`
- `Set up a new live event for Japan on March 3rd.`
- `Show me my recent event and import operations.`
- `Import these leads into the program I just created.`

## Marketing Event Program Orchestration MCP server tools

The Marketing Event Program Orchestration MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [open\_event\_intake](#open-event-intake-tool) | Opens the companion app to create an event program or import a lead list. |
| [provision\_event\_program](#provision-event-program-tool) | Looks up the details for a Marketo event, presents a preview for your approval, then creates the program and books a calendar hold. |
| [get\_lead\_field\_map](#get-lead-field-map-tool) | Returns the deployment's Marketo lead field catalog for mapping a lead import file. |
| [search\_event\_programs](#search-event-programs-tool) | Finds existing Marketo event programs by name prefix on the recent-program list, or by numeric ID. |
| [import\_program\_members](#import-program-members-tool) | Receives a lead CSV from the [Event360 app](#event360-mcp-app), checks the file's row counts and validity, presents the results for your approval, then imports into Marketo. |
| [get\_operation\_status](#get-operation-status-tool) | Lists recent operations, or polls a specific operation's status when you provide an ID. |

## Install the Marketing Event Program Orchestration MCP server

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
    

## Marketing Event Program Orchestration connection setup

View Marketing Event Program Orchestration connection setup steps

Configure the following connections to set up the Marketing Event Program Orchestration MCP server:

- [Marketo](#marketo-connection): Required.
- [Google Calendar](#google-calendar-connection): Required.
- [Slack](#slack-connection): Optional. Connect to Slack to receive a notification when a new program is created or a lead import finishes.
- [ZoomInfo](#zoominfo-connection): Optional. Connect to ZoomInfo to automatically fill blank lead fields during import.

### Role requirements

Each tool's availability depends on the permissions granted to connected accounts. Missing scopes for these connections block the corresponding tool with a `permission_denied` outcome rather than a partial result. Required connections must have the following access:

- Marketo: Requires read and write access to `Lead`, `Asset`, and `Activity`
- Google Calendar: Requires access to create events on the target calendar

Missing scopes on the optional Slack and ZoomInfo connections result in non-blocking outcomes: Slack notifications report as `partial_success`, and the server silently skips lead enrichment for the affected rows.

### Marketo connection

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

#### Marketo setup for custom authentication

Complete the following steps to set up a custom authentication connection to Marketo in Workato:

- [Retrieve the REST API endpoint](#retrieve-rest-api-endpoint)
- [Create an API role](#create-an-api-role)
- [Create an API user](#create-an-api-user)
- [Create a custom service for Workato](#create-a-custom-service-for-workato)
- [Retrieve client credentials](#retrieve-client-credentials)

##### Retrieve the REST API endpoint

View retrieve the REST API endpoint steps

Complete the following steps to retrieve the REST API Endpoint in Marketo:

1. Sign in to your Marketo instance as a user with administrator privileges.
   
2. Go to **Admin > Web Services**.
   
3. In the **REST API** section, copy and save the **Endpoint** for use in Workato.
   

##### Create an API role

View create an API role steps

Complete the following steps to create an API role in Marketo:

1. Go to **Admin > Users & Roles** and select the **Roles** tab.
   
2. Click **New Role**.
   
3. Provide a name for your new role in the **Role Name** field. Optionally, add a description in the **Description** field.
   
4. Select the **Access API** checkbox in the **Permissions** field.
   
5. Click **Create** to create the API role.
   

##### Create an API user

View create an API user steps

Complete the following steps to create an API user in Marketo:

1. Go to **Admin > Users & Roles** and select the **Users** tab.
   
2. Click **Create API Only User**.
   
3. Fill out the **Email**, **First Name**, and **Last Name** fields.
   
4. Select the checkbox for the API role you created in the previous step from the **Roles** menu.
   
5. Click **CREATE API ONLY USER**.
   

##### Create a custom service

View create a custom service steps

Creating a custom service enables you to retrieve the client ID and client secret used to establish a connection in Workato. Refer to the [Marketo Engage Developer Documentation](https://developers.marketo.com/rest-api/custom-services/) for more information about custom services.

Complete the following steps to create a custom service in Marketo:

1. Go to **Admin > LaunchPoint**.
   
2. Click **New > New Service**.
   
3. Enter a descriptive **Display name** and select **Custom** from the **Service** drop-down menu.
   
4. Enter a description in the **Description** field.
   
5. Select the user you created in the previous step from the **API Only User** drop-down menu.
   
6. Click **Create**.
   

##### Retrieve client credentials

View retrieve client credentials steps

Complete the following steps to retrieve client credentials in Marketo:

1. Select **View details** for the new custom service you created in the previous step.
   
   ![View custom service](/assets/view-details-marketo.DY2NcPr5.png)_View custom service_
   
2. Copy and save the **Client Id** and **Client Secret** for use in Workato.
   

#### Connect to Marketo with custom authentication

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
   

### Google Calendar connection

View Google Calendar connection setup steps

Refer to the following sections to set up your Google Calendar connection:

#### OAuth 2.0 authentication

Complete the following steps to set up your Google Calendar connection using OAuth 2.0:

View OAuth 2.0 authentication steps

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Select the project where you plan to store the connection from the **Location** drop-down menu.
   
5. Select **OAuth 2.0** as the **Authentication type**.
   
6. Click **Sign in with Google**, then sign in to your Google account. Ensure your Google account has sufficient permissions to manage the events and calendars you plan to use in Workato. ![Click Sign in with Google](/assets/google-calendar-sign-in-with-google.DQ57V-DM.png)_Click **Sign in with Google**._
   

#### Service account authentication

View Service account authentication steps

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

Service account authentication consists of the following actions:

- [Set up a Google service account](#set-up-a-google-service-account)
- [Enable the Google Calendar API](#api-setup)
- [Complete setup in Workato](#setup)

##### Minimum scopes for service account connections

The following scopes are required to connect to Google Calendar using a service account:

- `https://www.googleapis.com/auth/calendar`
- `https://www.googleapis.com/auth/calendar.events`
- `https://www.googleapis.com/auth/admin.directory.resource.calendar`
- `https://www.googleapis.com/auth/tasks`
- `https://www.googleapis.com/auth/userinfo.email`

A `401 Unauthorized error` may occur when the service account uses the `Owner` role or lacks required scopes. Assign the `Editor` role to the service account in the Google Cloud Console and confirm it includes all required scopes listed above. This ensures the service account can authenticate and access Google Calendar successfully.

Refer to the [Google Calendar API scopes](https://developers.google.com/calendar/api/auth) documentation for a complete list of supported scopes.

##### Set up a Google service account

View Set up a Google service account steps

Complete the following steps to set up a Google service account:

1. [Create a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating) in your GCP project.
   
2. Go to **IAM & Admin > Service accounts**. Ensure your dashboard is scoped to the project that contains your service account. ![Check the scope of your dashboard.](/assets/service-project-scope.8Rf50DK2.png)_Check the scope of your dashboard._
   
3. Click the **Email** of the service account you intend to use. ![Click the email of the service account you intend to use.](/assets/service-email-button.C9qaZFkJ.png)_Click the **Email** of the service account you intend to use._
   
4. Copy the service account's **Email** and save it to configure your connection later. ![Copy the account's email](/assets/service-account-email.DM6BBBhN.png)_Copy the account's **Email**._
   
5. Go to the **KEYS** tab.
   
6. [Generate a private key](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and download it in JSON format. You can only download the key once.
   
7. Open the JSON file, then copy the entire private key from `-----BEGIN PRIVATE KEY-----` to `-----END PRIVATE KEY-----\n` (inclusive) and save it to configure your connection later.
   

##### Enable the Google Calendar API

View Enable the Google Calendar API steps

You must enable the Google Calendar API before you return to Workato to finish setting up your connection.

1. Sign in to Google's [API library](https://console.developers.google.com/apis/library).
   
2. Search for and select the `Google Calendar API`.
   
3. Click **Enable** to enable the API. ![Enable the Google Calendar API](/assets/google-calendar-api.DMWBkrRb.png)_**Enable** the `Google Calendar API`_
   

##### Complete setup in Workato

View Workato setup steps

Complete the following steps in Workato to set up your Google Calendar connection using a service account:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select `Google Calendar` as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Service account** as the **Authentication type**.
   
6. Enter your service account's **Private key**.
   
7. Provide the **User email** of the account you plan to impersonate.
   
   User impersonation lets the service account act on behalf of a designated user, accessing and managing events in their Google Calendar. Impersonating a user ensures data accuracy and enforces the permissions and access controls set for that user in Google Calendar. Refer to Google's [Service account impersonation](https://cloud.google.com/iam/docs/service-account-impersonation) guide for more information.
   
8. Click **Sign in with Google** to complete the setup. ![Configure Google Calendar service account connection](/assets/service-account-connection.CG2N5lxI.png)_Configure Google Calendar service account connection_
   

### Slack connection (optional)

View Slack connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `notifications_enabled` to `true` in the [`event360_config` data table](#data-table-configuration) to use Slack for notifications.

Complete the following steps to connect to Slack in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Slack` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Slack connection](/assets/slack-connection.BT6h8ZMj.png)_Slack connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand **Advanced** and use the **Is this a Classic Slack app?** drop-down menu to select `Yes` or `No`. Select `Yes` only if you haven't migrated your Slack app to granular permission scopes. Refer to [Moving to granular permission scopes](/en/connectors/slack#moving-to-granular-permission-scopes) for more information.
   
6. Optional. Use the **OAuth user scopes** drop-down menu to select the OAuth user scopes to request for your connection. Leave this field empty to request the [default scopes](/en/connectors/slack#scopes).
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Custom OAuth profiles for Slack](/en/connectors/slack/custom-oauth) for more information.
   
8. Click **Connect**.
   
9. Click **Allow** to grant Workato permission to access your account.
   

#### Slack permissions

The connected account must have the OAuth scope required to post messages and access to the notification channel you select. Refer to Slack's [OAuth scopes documentation](https://docs.slack.dev/reference/scopes) for the complete list of scope capabilities.

### ZoomInfo connection (optional)

View ZoomInfo connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `enrich_enabled` to `true` in the [`event360_config` data table](#data-table-configuration) to use ZoomInfo for lead enrichment.

Complete the following steps to set up your ZoomInfo connection:

> **REQUIRED ZOOMINFO PERMISSIONS**
> 
> Your ZoomInfo account must have [ZoomInfo API](https://docs.zoominfo.com/reference/overview) access permissions to connect to Workato.

1. Enter a name for your connection in the **Connection name** field.
   
   ![Set up your ZoomInfo connection](/assets/zoominfo.BGW04mkl.png)_Set up your ZoomInfo connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
3. Enter your ZoomInfo username in the **Username** field.
   
4. Enter your ZoomInfo password in the **Password** field.
   
5. Click **Connect**.
   

### Data table configuration

Edit the following data tables to control event routing, lead field mapping, optional integrations, and import limits:

- `event_type_region_map`: Map each event type and region to a Marketo folder ID, template program ID, naming prefix, channel, and timezone.
  
- `marketo_lead_field_map`: Catalog your Marketo lead fields (API name, label, aliases, required, and sort order) for the `get_lead_field_map` tool. Lead-to-CSV column mapping for an import is set for each upload in the [Event360 app](#event360-mcp-app), not here.
  
- `event360_config` contains the following keys:
  

| Key | Description |
| --- | --- |
| `calendar_id` | Enter the ID of the target calendar. |
| `calendar_timezone_source` | Choose `per_region`, to resolve event times using `event_type_region_map`, or `fixed`, for one timezone across the whole deployment. |
| `notifications_enabled` | Configure whether to send Slack notifications for program creation and import completion. |
| `notifications_channel` | Enter the Slack channel to notify. Required when `notifications_enabled` is `true`. |
| `enrich_enabled` | Configure whether ZoomInfo enrichment automatically fills blank lead fields during import. |
| `preview_expiry_seconds` | Enter how long a server-issued preview remains valid before the server rejects a commit attempt as expired. Defaults to `300`. |
| `max_file_bytes` | Enter the maximum lead-import file size, in bytes. Defaults to `9,500,000`. |
| `max_rows` | Enter the maximum row count allowed for a lead import. Defaults to `50,000`. |
| `max_poll_seconds` | Enter the maximum polling duration allowed for a lead import. Defaults to `600`. |
| `ledger_retention_days` | Enter the number of days to retain lead-import ledger records. Defaults to `365`. |
| `artifact_retention_days` | Enter the number of days to retain uploaded-file artifacts. Defaults to `30`. |
| `search_enabled` | Configure whether the nightly job that populates the search index `search_event_programs` uses for name-based lookups runs. |
| `search_lookback_days` | Enter how many days of programs the search-index job covers. Defaults to `30`. |
| `marketo_url_template` | Enter a URL template to use for links, with a placeholder for your Marketo org. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data tables:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Data Tables** folder.
   
4. Select the data table to update, such as `event360_config` or `event_type_region_map`.
   
5. [Add](/en/data-tables/user-interface/edit#add-a-new-row) or [edit](/en/data-tables/user-interface/edit#edit-a-row) rows to make your changes. For example, set the `event360_config` row with key `notifications_enabled` to `false`, or `ledger_retention_days` to `5`.
   

## How to use Marketing Event Program Orchestration MCP server tools

Refer to the following sections for detailed information on available tools:

### open\_event\_intake tool

The **open\_event\_intake** tool opens the [Event360 companion app](#event360-mcp-app) to create an event program or import a lead list. Your LLM uses this tool to set up a new event program or import a registrant list into Marketo.

**Try asking**:

- `Set up a new webinar program.`
- `I have an event to add.`
- `Open Event Ops.`
- `Get this list into Marketo.`

### provision\_event\_program tool

The **provision\_event\_program** tool looks up the details for a Marketo event, presents a preview for your approval, then creates the program and books a calendar hold. Your LLM calls this tool once to retrieve information and display a preview, then calls it again after receiving approval to create the program and book the hold.

**Try asking**:

- `Set up a new webinar program for APJ next month.`
- `Create a field event in NORAM and book the calendar for it.`
- `Set up a new live event for Japan on March 3rd.`
- `Approve this event program preview.`

### get\_lead\_field\_map tool

The **get\_lead\_field\_map** tool returns the configured Marketo lead field catalog from the `marketo_lead_field_map` data table, such as the API name, label, aliases, whether the field is required, and sort order. The [Event360 companion app](#event360-mcp-app) uses this tool to create the CSV column mapping for a lead import.

**Try asking**:

- `What lead fields does this deployment support for import?`
- `Show me the required fields for a lead import.`
- `Which column maps to the Company field in Marketo?`

### search\_event\_programs tool

The **search\_event\_programs** tool finds existing Marketo event programs by name prefix on the recent-program list, or by numeric ID through a live Marketo lookup. Your LLM uses this tool to resolve a program by name or ID before importing members into it, or to answer questions about a program you've recently created.

**Try asking**:

- `What's the URL for the trade show program I created last week?`
- `Find the Q2 webinar program.`
- `Search for the NORAM field event program.`
- `Look up program 123074.`

### import\_program\_members tool

The **import\_program\_members** tool receives a lead CSV from the [Event360 app](#event360-mcp-app), checks the file's row counts and validity, presents the results for your approval, then imports into Marketo.

**Try asking**:

- `Get this registrant CSV into the Q2 webinar program.`
- `Import these leads into the program I just created.`
- `Here's the mapping for my registrant file.`
- `Commit this lead import.`

### get\_operation\_status tool

The **get\_operation\_status** tool lists recent operations, or polls a specific operation's status when you provide an ID. You can explicitly ask for the live result or allow the tool to poll Marketo and update cached statuses automatically. Your LLM uses this tool to check progress on a program creation or lead import, or to recover an in-progress operation after you reconnect.

**Try asking**:

- `Did my lead import finish?`
- `What's the URL for the trade show program I created last week?`
- `I navigated away. What was I uploading?`
- `Check the real current status of my import, not the cached one.`

## Event360 MCP app

The [open\_event\_intake](#open-event-intake-tool) tool opens the Event360 [MCP app](/en/mcp/mcp-apps), which manages event program creation and lead list uploads. Both workflows present a preview for your approval before writing. The app also monitors the status of in-progress operations to help you resume work after you reconnect.

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
