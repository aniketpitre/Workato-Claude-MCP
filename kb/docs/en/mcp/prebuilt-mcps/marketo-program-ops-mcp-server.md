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
