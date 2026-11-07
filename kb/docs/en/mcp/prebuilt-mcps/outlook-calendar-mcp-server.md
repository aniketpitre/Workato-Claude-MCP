---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/outlook-calendar-mcp-server.md'
description: >-
  Use the Outlook Calendar MCP server to connect your LLM to Outlook Calendar
  with a curated set of tools to retrieve events, check availability, and
  create, update, or delete calendar entries.
---

# Outlook Calendar MCP server

The Outlook Calendar MCP server enables LLMs to read, interpret, and modify calendar data stored in Microsoft Outlook Calendar through natural conversation. It provides tools to retrieve events, check availability, and create, update, or delete calendar entries without requiring direct interaction with the Outlook interface.

## Uses

Use the Outlook Calendar MCP server when you plan to perform the following actions:

- View upcoming or past calendar events for planning or reporting
- Check availability for yourself or other attendees to support scheduling
- Retrieve full details for specific events
- Schedule new meetings, focus time, or out-of-office events
- Reschedule, update, or cancel existing calendar events
- Access multiple calendars including shared and delegate calendars
- Find open time slots for meetings or personal time
- Manage recurring meetings and series

### Example prompts

Use the following example prompts to invoke Outlook Calendar MCP server tools:

- `What's on my calendar for this week?`
- `Schedule a 30-minute meeting with Alex and Priya next Tuesday.`
- `When am I free tomorrow afternoon?`
- `Get the details for my 2pm meeting today.`
- `Move my standup meeting to 10am instead of 9am.`
- `Cancel the budget review meeting on Friday.`
- `What calendars do I have access to?`
- `Find a time when Sarah and I are both free this week.`

## Outlook Calendar MCP server tools

The Outlook Calendar MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_events](#list-events-tool) | Retrieves calendar events from one or more Outlook calendars within a time window you specify or by direction and count. |
| [get\_event](#get-event-tool) | Retrieves full details for a single Outlook Calendar event by unique ID. |
| [get\_availability](#get-availability-tool) | Retrieves free or busy availability for the user and attendees over a time window you specify. |
| [create\_event](#create-event-tool) | Creates a new Outlook Calendar event on a calendar the user is allowed to modify. |
| [update\_event](#update-event-tool) | Updates an existing Outlook Calendar event with new details, including time, attendees, description, or recurrence. |
| [delete\_event](#delete-event-tool) | Deletes or cancels an existing Outlook Calendar event identified by its unique ID. |
| [list\_calendars](#list-calendars-tool) | Retrieves the list of Outlook calendars accessible to the user. |

## Install the Outlook Calendar MCP server

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
    

## Outlook Calendar connection setup

View Outlook Calendar connection setup steps

The Outlook connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials): _Only available for tenant-specific connections_

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

The connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Mail.Send`
- `Mail.ReadWrite`
- `Mail.ReadWrite.Shared`
- `Calendars.ReadWrite`
- `Calendars.ReadWrite.Shared`
- `User.Read`
- `offline_access`

The following minimum scopes are required to establish a connection to using authorization code grant authentication:

- `User.Read`
- `offline_access`

#### Outlook setup for authorization code grant authentication

Complete the following steps to set up Outlook for authorization code grant authentication:

- [Register the Workato App in Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

#### Register the Workato app in the Azure portal

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

This step is required if you plan to use a tenant-specific account. You can skip this step if you plan to use a common, consumer, or organization account type for your connection.

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Outlook with authorization code grant authentication

View connect to Outlook with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Outlook in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Outlook` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection account type** drop-down menu to select the type of account you plan to use. The available choices are **Common**, **Tenant-specific**, **Consumer**, and **Organization**.
   
   **Common**
   
   - **Common**: This option allows you to sign in using enterprise and multi-tenant accounts that are not restricted to a specific organization (tenant).
   
   ![Common connection](/assets/connect-common.n5OKFNtM.png)_Common connections_
   
   **Tenant specific**
   
   - **Tenant specific**: This option is specifically designed for users who belong to a particular organization (tenant).
   
   ![Provide the tenant ID/domain](/assets/connect-tenant.Te-J1c-V.png)_Tenant specific connections_
   
   Provide the `tenant ID` of the Microsoft Entra ID tenant (a GUID) or its `tenant domain` in the **Tenant ID/Domain** field. This ensures that you access resources specifically configured for that tenant. Refer to [Register the Workato app in the Azure portal](#auth-register) for more information.
   
   **Consumer**
   
   - **Consumer**: This option supports personal Microsoft accounts.
   
   ![Consumer connection](/assets/connect-consumer.DM8X7YiA.png)_Consumer connections_
   
   **Organization**
   
   - **Organization**: This option supports work or school accounts.
   
   ![Organization connection](/assets/connect-organization.BB6uVVjE.png)_Organization connections_
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Optional. The connector requests a set of scopes necessary for all triggers and actions to function properly by default. Go to the **Advanced settings** section to manually select the permissions instead. The minimum permissions required to establish a connection are `User.Read` and `offline_access`. Workato requests these permissions regardless of the permissions you select. Refer to [Minimum and default scopes](#authorization-code-grant-scopes) for more information.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Outlook custom OAuth](/en/connectors/outlook/custom-oauth) for more information.
   
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

We recommend the following scopes for client credentials connections. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Application** permissions in the Azure portal.

- `Calendars.Read`
- `Calendars.ReadWrite`
- `Contacts.Read`
- `Contacts.ReadWrite`
- `Mail.Read`
- `Mail.ReadWrite`
- `Mail.Send`

The following minimum scopes are required to establish a connection to with client credentials-based authentication:

- `Mail.Read`

#### Outlook setup for client credentials-based authentication

Complete the following steps to set up Outlook for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#obtain-ids)
- [Obtain the User ID from the Azure portal](#obtain-user-id)

##### Register the Workato app in the Azure portal

View Register the Workato app in the Azure portal steps

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

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
   

#### Connect to Outlook with client credentials-based authentication

View connect to Outlook with client credential-based authentication steps

Complete the following steps to set up a client credentials-based connection to Outlook in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Outlook` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Client credentials connection](/assets/client-credentials-connection.BNf4ndnr.png)_Client credentials connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Select **Tenant specific** as the **Connection account type**. This option is specifically designed for users who belong to a particular organization (tenant).
   
6. Provide your **Tenant ID/Domain**. This is the **Directory (tenant) ID** for your app. Refer to [Register an app in Azure](/en/connectors/outlook/outlook#client-credentials-register) for more information.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Supply the **User ID**, **Client ID**, and **Client secret** for your app. Refer to [Register an app in Azure](/en/connectors/outlook/outlook#client-credentials-register) for more information.
   
9. Click **Sign in with Microsoft**.
   

## How to use Outlook Calendar MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_events tool

The **list\_events** tool retrieves calendar events from one or more Outlook calendars within a time window you specify or by direction and count. Your LLM uses this tool to see what's on your calendar, plan your day or week, or review past events.

**Try asking**:

- `What's on my calendar for this week?`
- `Show me my meetings for tomorrow.`
- `List all events on my calendar between January 1st and January 15th.`
- `What do I have scheduled for next Monday?`

### get\_event tool

The **get\_event** tool retrieves full details for a single Outlook Calendar event by its unique event ID. Your LLM uses this tool to read, inspect, or open a specific event, retrieve complete details before modifying or deleting the event, summarize a particular meeting, or confirm metadata prior to scheduling decisions.

**Try asking**:

- `Get the details for my 2pm meeting today.`
- `Show me the full information for the quarterly review meeting.`
- `What are the details of my next appointment?`
- `Read the agenda for the product planning meeting.`

### get\_availability tool

The **get\_availability** tool retrieves free and busy availability for you and attendees over a time window you specify. Your LLM uses this tool to find times to schedule a meeting, check whether you or others are free, evaluate potential windows for rescheduling, or identify open periods for PTO or focus time.

**Try asking**:

- `When am I free tomorrow afternoon?`
- `Find a time when Sarah and I are both free this week.`
- `Check my availability for Thursday between 2pm and 5pm.`
- `When are Alex, Mei, and I all available next week?`

### create\_event tool

The **create\_event** tool creates a new Outlook Calendar event. Your LLM uses this tool to schedule a new meeting or call, add a calendar hold or focus time block, create a recurring event, block off PTO or OOO time, or create follow-up meetings.

**Try asking**:

- `Schedule a 30-minute meeting with Marco and Jade next Tuesday at 2pm.`
- `Create a recurring weekly standup every Monday at 9am.`
- `Block off next Friday as PTO.`
- `Set up a focus time block for tomorrow morning from 9am to 11am.`

### update\_event tool

The **update\_event** tool updates an existing Outlook Calendar event with new details including time, attendees, description, or recurrence. Your LLM uses this tool to move or reschedule a meeting, shorten or extend an event's duration, add, remove, or update attendees, update meeting descriptions or agendas, or modify a recurring series.

**Try asking**:

- `Move my standup meeting to 10am instead of 9am.`
- `Reschedule the budget review to next Wednesday.`
- `Add Josh to the product planning meeting.`
- `Extend my 1pm meeting by 30 minutes.`

### delete\_event tool

The **delete\_event** tool deletes or cancels an existing Outlook Calendar event identified by its unique ID. Your LLM uses this tool to cancel meetings, remove calendar blocks, or delete events that are no longer needed.

**Try asking**:

- `Cancel the budget review meeting on Friday.`
- `Delete my 3pm appointment tomorrow.`
- `Remove the team lunch from my calendar.`
- `Cancel the recurring standup for next week only.`

### list\_calendars tool

The **list\_calendars** tool retrieves the list of Outlook calendars accessible to you, including default, secondary, shared, and delegate calendars. Your LLM uses this tool to discover available calendars, select a specific calendar for operations, or understand your calendar access.

**Try asking**:

- `What calendars do I have access to?`
- `Show me all my Outlook calendars.`
- `List the shared calendars I can view.`
- `What calendars are available for scheduling?`

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
