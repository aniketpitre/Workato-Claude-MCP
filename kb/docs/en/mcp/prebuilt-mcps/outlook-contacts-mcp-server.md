---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/outlook-contacts-mcp-server.md'
description: >-
  Use the Outlook Contacts MCP server to connect your LLM to Microsoft Outlook
  with tools to find, create, update, delete, and organize personal contacts
  through natural language.
---

# Outlook Contacts MCP server

The Outlook Contacts MCP server enables LLMs to manage a user's personal contacts within Microsoft Outlook through natural conversation. It provides tools to search, retrieve, create, update, delete, and organize contact records, manage contact folders, deduplicate contacts, and apply Outlook categories as cross-cutting organizational labels without requiring direct interaction with the Outlook interface.

## Uses

Use the Outlook Contacts MCP server to perform the following actions:

- Search personal contacts by name or email address
- List contacts from a folder with optional filters for company or category
- Retrieve full details for a specific contact by ID
- Create a new contact in Outlook
- Update specific fields on an existing contact
- Permanently delete a contact
- Move a contact from one folder to another
- List contact folders and check folder contents
- Retrieve full details for a specific contact folder
- Create, rename, and delete contact folders
- List all Outlook category labels in use across contacts

### Example prompts

Use the following example prompts to invoke Outlook Contacts MCP server tools:

- `Find Sarah's contact details.`
- `Show all contacts in my Vendors folder.`
- `Show contacts tagged VIP.`
- `Get the full profile for this contact.`
- `Save Marcus as a new contact.`
- `Update the phone number for this contact.`
- `Delete this contact from my Outlook.`
- `Move this contact to the Partners folder.`
- `What contact folders do I have?`
- `Create a new folder called Prospects.`
- `Rename this contact folder.`
- `What categories have I applied to my contacts?`

## Outlook Contacts MCP server tools

The Outlook Contacts MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_contacts](#search-contacts-tool) | Searches personal contacts by name or email address. |
| [list\_contacts](#list-contacts-tool) | Lists contacts from a contact folder, with optional filtering. |
| [get\_contact](#get-contact-tool) | Retrieves full details for a contact by ID. |
| [create\_contact](#create-contact-tool) | Creates a new contact in the user's Outlook contacts. |
| [update\_contact](#update-contact-tool) | Updates fields you specify on an existing contact. |
| [delete\_contact](#delete-contact-tool) | Permanently deletes a contact from the user's Outlook contacts. |
| [move\_contact](#move-contact-tool) | Moves a contact from one contact folder to another. |
| [list\_contact\_folders](#list-contact-folders-tool) | Lists the user's contact folders. |
| [get\_contact\_folder](#get-contact-folder-tool) | Retrieves details for a contact folder you specify, including child folders. |
| [create\_contact\_folder](#create-contact-folder-tool) | Creates a new contact folder. |
| [update\_contact\_folder](#update-contact-folder-tool) | Renames an existing contact folder. |
| [delete\_contact\_folder](#delete-contact-folder-tool) | Deletes a contact folder and all contacts within it. |
| [list\_categories](#list-categories-tool) | Lists all Outlook category labels currently in use across the user's contacts. |

## Install the Outlook Contacts MCP server

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
    

### Outlook connection setup

View Outlook connection setup steps

Workato supports the following connection types for Outlook:

- [Authorization code grant authentication (OAuth 2.0)](#authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#authentication-client-credentials)

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

This authentication method requires the following value for tenant-specific account types:

- Tenant ID/Domain

#### Register the Workato App in Azure Portal

Complete the following steps to register the Workato app and assign it permissions for authorization code grant connections:

View Register the Workato app in the Azure Portal steps

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
   
   Complete the following steps to assign permissions to your app:
   
   1. Go to your newly registered app and select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Microsoft Graph**.
      
   3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
      
      ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
      
   4. Click **Add permissions**.
      
      Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
      
   
3. Obtain the Directory (tenant ID) from the Azure Portal
   
   This step is required if you plan to use a tenant-specific account. You can skip this step if you plan to use a common, consumer, or organization account type for your connection.
   
   Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy and save the `Directory (tenant) ID` for use in Workato.
      
   

#### Complete setup in Workato

View Complete setup in Workato steps

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

This method requires the following fields:

- Tenant ID/Domain
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Register the Workato App in the Azure Portal

Complete the following steps to register the Workato app and assign it permissions for client credentials-based connections:

View Register the Workato App in the Azure Portal steps

1. Register the Workato App in the Azure Portal
   
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
   
   Complete the following steps to assign permissions to your app:
   
   1. Go to your newly registered app and select **Manage > API permissions**.
      
   2. Click **\+ Add a permission** and select **Microsoft Graph**.
      
   3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
      
      ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
      
   4. Click **Add permissions**.
      
      Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
      
   
3. Generate a client secret
   
   Complete the following steps to generate a client secret:
   
   1. Go to **Manage > Certificates & Secrets > Client secrets**.
      
   2. Click **\+ New client secret**.
      
   3. Provide a **Description** for the client secret and specify an **Expires** date.
      
   4. Click **Add**.
      
   5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
      
      ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
      
   
4. Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure Portal
   
   Complete the following steps to obtain the Application ID, Object ID, and Directory (tenant) ID from the Azure portal:
   
   1. Go to the **Overview > Essentials** section.
      
      ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
      
   2. Copy and save the **Application (client) ID**, **Object ID**, and **Directory (tenant) ID** for use in Workato.
      
   
5. Obtain the User ID from the Azure Portal
   
   Complete the following steps to obtain the User ID from the Azure portal:
   
   1. Go to **Home > Users** to obtain the `User ID`.
      
      ![Users](/assets/users.CuDgSGeL.png)_Select users_
      
   2. Search for and select the default user you plan to use to perform operations. This user doesn't establish the connection but is required for performing certain operations that an app can't perform. It's also required in picklists to pull user data. For example, the folder picklist populates folders belonging to the default user.
      
   3. Copy and save the **User principal name**. Use this value as the **User ID** in Workato.
      
   

Return to Workato to finish setting up your connection.

#### Complete setup in Workato

View Complete setup in Workato steps

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
   

## How to use Outlook Contacts MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_contacts tool

The **search\_contacts** tool searches personal contacts by name or email address. Your LLM uses this tool to find contacts or retrieve details for downstream actions, such as sending an email or scheduling a meeting. **Try asking**:

- `Find Sarah's contact details.`
- `Search for marco@acme.com.`
- `Look up the contact for this person before I email them.`
- `Find the contact I need to schedule a meeting with.`

### list\_contacts tool

The **list\_contacts** tool lists contacts from a contact folder with optional filtering. Your LLM uses this tool to browse contacts, list everyone in a specific folder, or filter by company, folder, or category without a specific name search.

**Try asking**:

- `Show all my contacts.`
- `List everyone in my Vendors folder.`
- `Show contacts tagged VIP.`
- `List all contacts at Acme.`

### get\_contact tool

The **get\_contact** tool retrieves full details for a contact by ID. Your LLM uses this tool after **search\_contacts** or **list\_contacts** to retrieve information for a selected result, and before performing write operations such as **update\_contact** or **delete\_contact** to confirm current state and read array field values.

**Try asking**:

- `Get the full profile for this contact.`
- `Show me all details for this person before I update their record.`
- `Retrieve the complete contact information for this result.`
- `Get this contact's details before I delete them.`

### create\_contact tool

The **create\_contact** tool creates a new contact in the user's Outlook contacts. Your LLM asks for at least one identifying field, such as display name, first name, last name, or email address, before creating the record.

**Try asking**:

- `Save Marcus as a new contact.`
- `Add this person to my Outlook contacts.`
- `Create a contact for the new account manager I met today.`
- `Save this lead's details as a contact.`

### update\_contact tool

The **update\_contact** tool updates fields you specify on an existing contact. Your LLM uses this tool to change contact details, such as phone numbers, email addresses, job titles, or category tags.

**Try asking**:

- `Update the phone number for this contact.`
- `Change Sarah's job title to VP of Marketing.`
- `Add the VIP category tag to this contact.`
- `Update Marco's email address.`

### delete\_contact tool

The **delete\_contact** tool permanently deletes a contact from the user's Outlook contacts. Your LLM uses this tool only when you explicitly request deletion. Your LLM retrieves and presents the contact to you before deleting. Deletion is permanent.

**Try asking**:

- `Delete this contact from my Outlook.`
- `Remove this person from my contacts.`
- `Permanently delete this contact record.`
- `Clean up this duplicate contact.`

### move\_contact tool

The **move\_contact** tool moves a contact from one contact folder to another. Your LLM identifies both the contact and the destination folder before moving.

**Try asking**:

- `Move this contact to the Partners folder.`
- `Reorganize Sarah into the Vendors folder.`
- `Transfer this contact from Prospects to Customers.`
- `Move Mei into my VIP folder.`

### list\_contact\_folders tool

The **list\_contact\_folders** tool lists the user's contact folders. Your LLM uses this tool when you ask what folders you have, or when a folder ID is needed before creating, moving, or managing contacts. Your LLM also uses this tool before creating a new folder to check for duplicate names, and before deleting a folder to retrieve the contact count.

**Try asking**:

- `What contact folders do I have?`
- `Show me all my Outlook contact folders.`
- `List my folders before I create a new one.`
- `What folders can I move this contact into?`

### get\_contact\_folder tool

The **get\_contact\_folder** tool retrieves details for a contact folder you specify, including child folders. Your LLM uses this tool when a folder ID is available and folder details or structure are needed, and before deleting a folder to retrieve the contact count.

**Try asking**:

- `Get details for the Vendors folder.`
- `Show me the subfolders inside this folder.`
- `How many contacts are in this folder before I delete it?`
- `Get the full details of this contact folder.`

### create\_contact\_folder tool

The **create\_contact\_folder** tool creates a new contact folder, with the option to create it as a subfolder. Your LLM checks existing folders through **list\_contact\_folders** before creating. Your LLM informs you if a folder with the same name already exists and asks for confirmation before proceeding.

**Try asking**:

- `Create a new folder called Prospects.`
- `Add a subfolder called Enterprise inside my Customers folder.`
- `Set up a new contact folder for this project.`
- `Create a VIP folder for my top accounts.`

### update\_contact\_folder tool

The **update\_contact\_folder** tool renames an existing contact folder. Your LLM confirms the correct folder through **list\_contact\_folders** or **get\_contact\_folder** before renaming.

**Try asking**:

- `Rename the Prospects folder to Pipeline.`
- `Change this folder's name to Active Customers.`
- `Rename my VIP folder to Priority Accounts.`
- `Update the name of this contact folder.`

### delete\_contact\_folder tool

The **delete\_contact\_folder** tool deletes a contact folder and all contacts within it. Your LLM uses this tool only when you explicitly request deletion.

**Try asking**:

- `Delete the old Prospects folder.`
- `Remove this contact folder and its contents.`
- `Clean up this unused folder.`
- `Delete the archived contacts folder.`

### list\_categories tool

The **list\_categories** tool lists all Outlook category labels currently in use across the user's contacts. Your LLM uses this tool before applying a category to a contact to surface existing labels and validate spelling before using **update\_contact** or **create\_contact**.

**Try asking**:

- `What categories have I applied to my contacts?`
- `Show me all my contact tags.`
- `What labels are available before I tag this contact?`
- `List my existing Outlook categories.`

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
