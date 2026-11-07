---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/google-contacts-mcp-server.md'
description: >-
  Use the Google Contacts MCP server to connect your LLM to Google Contacts with
  tools to find, create, update, delete, and organize personal contacts through
  natural language.
---

# Google Contacts MCP server

The Google Contacts MCP server enables LLMs to manage personal contacts within Google Contacts through natural conversation. It provides tools to retrieve, create, update, and delete contact records, merge and remove duplicate contacts, and promote auto-captured contacts into saved contacts without requiring direct interaction with the Google Contacts interface.

## Uses

Use the Google Contacts MCP server to perform the following actions:

- Search contacts using name, email, phone, or organization
- Retrieve full details for specific contacts
- List contacts with pagination support
- Create new contacts with provided details
- Update fields on existing contacts
- Delete contacts from the user's contact list
- Merge duplicate contacts into a single contact
- List all contact groups
- Get details and members of contact groups
- Create new contact groups
- Rename existing contact groups
- Delete contact groups
- Add contacts to groups
- Remove contacts from groups
- Browse auto-captured contacts from user interactions
- Search auto-captured contacts by name or email
- Promote auto-captured contacts to saved contacts

### Example prompts

Use the following example prompts to invoke Google Contacts MCP server tools:

- `Find Jade Anderson's email address.`
- `Show me contact details for Marco Reyes.`
- `List all my contacts.`
- `Create a new contact for Alex Miller at acme.com.`
- `Update Mei's phone number to 555-0123.`
- `Delete the outdated contact for Josh.`
- `Merge these duplicate contacts for Sarah.`
- `What contact groups do I have?`
- `Who is in my Vendors group?`
- `Create a new group called Team Leads.`
- `Add these contacts to the Clients group.`
- `Show my auto-captured contacts.`
- `Save this auto-captured contact to my contacts.`

## Google Contacts MCP server tools

The Google Contacts MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_contacts](#search-contacts-tool) | Searches contacts using name, email, phone, or organization. |
| [get\_contact](#get-contact-tool) | Retrieves full details for a specific contact. |
| [list\_contacts](#list-contacts-tool) | Lists contacts with optional pagination. |
| [create\_contact](#create-contact-tool) | Creates a new contact with details you provide. |
| [update\_contact](#update-contact-tool) | Updates fields on an existing contact. |
| [delete\_contact](#delete-contact-tool) | Deletes a contact from the user's contacts. |
| [merge\_contacts](#merge-contacts-tool) | Merges multiple contacts into a single contact. |
| [list\_contact\_groups](#list-contact-groups-tool) | Lists all contact groups. |
| [get\_contact\_group](#get-contact-group-tool) | Retrieves details and members of a contact group. |
| [create\_contact\_group](#create-contact-group-tool) | Creates a new contact group. |
| [update\_contact\_group](#update-contact-group-tool) | Renames an existing contact group. |
| [delete\_contact\_group](#delete-contact-group-tool) | Deletes a contact group. |
| [add\_contacts\_to\_group](#add-contacts-to-group-tool) | Adds contacts to a contact group. |
| [remove\_contacts\_from\_group](#remove-contacts-from-group-tool) | Removes contacts from a contact group. |
| [list\_other\_contacts](#list-other-contacts-tool) | Lists auto-captured contacts from user interactions. |
| [search\_other\_contacts](#search-other-contacts-tool) | Searches auto-captured contacts by name or email. |
| [copy\_other\_contact](#copy-other-contact-tool) | Creates a saved contact from an auto-captured contact. |

## Install the Google Contacts MCP server

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
    

## Google Contacts connection setup

View Google Contacts connection setup steps

### Permissions

Google Contacts uses the Google [People API](https://developers.google.com/people). Google People API defaults to the following permissions if left blank:

- `https://www.googleapis.com/auth/userinfo.email`
- `https://www.googleapis.com/auth/contacts`
- `https://www.googleapis.com/auth/contacts.other.readonly`

Workato requests `https://www.googleapis.com/auth/contacts.readonly` with the default or selected permissions.

### How to connect to Google Contacts

View Google Contacts connection setup steps

Complete the following steps to create a connection to the Google Contacts MCP server in Workato:

1. Click **Create > Connection**.
   
2. Search for `Google People` and select it as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Set up your connection](/assets/google-people-connection.C4xXx4gs.png)_Set up your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Optional. Expand **Advanced settings** and use the **Requested permissions (Oauth scopes)** to select permissions for your connection. Selecting permissions overwrites the [default permissions](#permissions).
   
6. Click **Sign in with Google**.
   

## How to use Google Contacts MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_contacts tool

The **search\_contacts** tool searches contacts using name, email, phone, or organization. Your LLM uses this tool to find a contact or resolve a person in a workflow when no contact ID exists, such as before it sends an email or schedules a meeting.

**Try asking**:

- `Find Jade Anderson's email address.`
- `Search for contacts at Acme.`
- `Look up the contact with phone number 555-0123.`
- `Find Marco's contact information.`

### get\_contact tool

The **get\_contact** tool retrieves full details for a specific contact. Your LLM uses this tool after it identifies a contact and needs complete details, typically after `search_contacts`.

**Try asking**:

- `Show me contact details for Marco Reyes.`
- `Get the complete information for this contact.`
- `What are all the details for Jade Anderson?`
- `Retrieve full contact record for Alex Miller.`

### list\_contacts tool

The **list\_contacts** tool lists contacts with optional pagination. Your LLM uses this tool to view contacts without a specific search query.

**Try asking**:

- `List all my contacts.`
- `Show me my contacts.`
- `Display my contact list.`
- `What contacts do I have saved?`

### create\_contact tool

The **create\_contact** tool creates a new contact using details you provide. Your LLM uses this tool to save a new contact or add a person to your contacts.

**Try asking**:

- `Create a new contact for Mei Chen at acme.com.`
- `Save Marco Reyes with phone 555-0123.`
- `Add Jade Anderson as a contact.`
- `Create a contact for the new vendor representative.`

### update\_contact tool

The **update\_contact** tool updates fields on an existing contact. Your LLM uses this tool to modify details of an existing contact after identifying the correct contact.

**Try asking**:

- `Update Mei's phone number to 555-0123.`
- `Change Alex's email to a.miller@acme.com.`
- `Update this contact's job title to VP of Sales.`
- `Modify Marco's company name to Acme Corp.`

### delete\_contact tool

The **delete\_contact** tool deletes a contact from your contacts. Your LLM uses this tool when you explicitly request to remove a contact.

**Try asking**:

- `Delete the outdated contact for Josh.`
- `Remove this contact from my list.`
- `Delete Marco's duplicate entry.`
- `Remove the contact for sarah@acme.com.`

### merge\_contacts tool

The **merge\_contacts** tool merges multiple contacts into a single contact. Your LLM uses this tool to combine duplicate contacts and ensure it selects the correct records before merging.

**Try asking**:

- `Merge these duplicate contacts for Sarah.`
- `Combine the two entries for Alex Miller.`
- `Merge Marco's personal and work contacts.`
- `Consolidate these duplicate contact records.`

### list\_contact\_groups tool

The **list\_contact\_groups** tool lists all contact groups. Your LLM uses this tool to view or list your contact groups.

**Try asking**:

- `What contact groups do I have?`
- `Show me all my groups.`
- `List my contact groups.`
- `What groups have I created?`

### get\_contact\_group tool

The **get\_contact\_group** tool retrieves details and members of a contact group. Your LLM uses this tool to get details of a specific group or its members.

**Try asking**:

- `Who is in my Vendors group?`
- `Show me members of the Team Leads group.`
- `Get details for the Clients group.`
- `What contacts are in Family?`

### create\_contact\_group tool

The **create\_contact\_group** tool creates a new contact group. Your LLM uses this tool to create a new group after checking existing groups to avoid duplicate names.

**Try asking**:

- `Create a new group called Team Leads.`
- `Make a contact group for my Clients.`
- `Set up a group named Vendors.`
- `Create a Family group.`

### update\_contact\_group tool

The **update\_contact\_group** tool renames an existing contact group. Your LLM uses this tool after it identifies the correct group.

**Try asking**:

- `Rename the Vendors group to Suppliers.`
- `Change the Team Leads group name to Leadership.`
- `Update the group name from Clients to Customers.`
- `Rename this group to Active Projects.`

### delete\_contact\_group tool

The **delete\_contact\_group** tool deletes a contact group. Your LLM uses this tool when you explicitly request to delete a group after retrieving and confirming the correct group.

**Try asking**:

- `Delete the Old Vendors group.`
- `Remove the Archived Clients group.`
- `Delete this contact group.`
- `Remove the inactive group.`

### add\_contacts\_to\_group tool

The **add\_contacts\_to\_group** tool adds contacts to a contact group. Your LLM uses this tool to add contacts to a group.

**Try asking**:

- `Add these contacts to the Clients group.`
- `Put Jade and Marco in the Team Leads group.`
- `Add Alex Miller to the Vendors group.`
- `Include these people in the Family group.`

### remove\_contacts\_from\_group tool

The **remove\_contacts\_from\_group** tool removes contacts from a contact group. Your LLM uses this tool to remove contacts from a group.

**Try asking**:

- `Remove Marco from the Vendors group.`
- `Take Jade out of the Team Leads group.`
- `Remove these contacts from the Clients group.`
- `Delete Alex from the Family group.`

### list\_other\_contacts tool

The **list\_other\_contacts** tool lists auto-captured contacts from user interactions. Your LLM uses this tool to browse auto-captured contacts that aren't saved.

**Try asking**:

- `Show my auto-captured contacts.`
- `List contacts I haven't saved.`
- `What auto-captured contacts do I have?`
- `Show people from my interactions.`

### search\_other\_contacts tool

The **search\_other\_contacts** tool searches auto-captured contacts by name or email. Your LLM uses this tool to find a specific auto-captured contact.

**Try asking**:

- `Search auto-captured contacts for Jade.`
- `Find the auto-captured contact with email marco@acme.com.`
- `Look for Alex in my unsaved contacts.`
- `Search for this person in auto-captured contacts.`

### copy\_other\_contact tool

The **copy\_other\_contact** tool creates a new saved contact by copying data from an existing Other Contact. Your LLM uses this tool to copy and save an auto-captured contact into your contacts.

**Try asking**:

- `Save this auto-captured contact to my contacts.`
- `Promote this person to a saved contact.`
- `Add this auto-captured contact to my contact list.`
- `Save this person permanently.`

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

---
