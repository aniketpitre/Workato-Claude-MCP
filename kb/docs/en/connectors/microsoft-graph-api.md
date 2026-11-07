---
url: 'https://docs.workato.com/en/connectors/microsoft-graph-api.md'
description: >-
  Connect to the Microsoft Graph API connector using authorization code grant or
  client credentials authentication.
---

# Microsoft Graph API

[Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) is a powerful unified endpoint that allows organizations to access and interact with Microsoft 365 services and other Microsoft cloud-based resources. It enables developers to integrate and automate various application actions, such as managing users, groups, mail, calendars, tasks, and security insights.

With Microsoft Graph API, organizations can enhance security, streamline user management, and enable seamless single sign-on experiences across different applications. It provides access to:

- External resources, such as Microsoft 365, the Azure portal, and thousands of other SaaS applications.
- Internal resources, such as apps on your corporate network, intranet, and any cloud apps developed by your organization.

## Install Microsoft Graph API from the community library

Complete the following steps to install the Microsoft Graph API connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

## Connection setup

The Microsoft Graph API connector supports the following authentication types:

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

Authorization code grant authentication signs in as a specific user and uses **Delegated** permissions.

This authentication type requires the following values:

- **Client ID**
- **Client secret**
- **Tenant ID** (required for single tenant)

#### Minimum and default scopes

When no scopes are provided in the **Scopes** input field, the Microsoft Graph API connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. You must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `offline_access`
- `openid`
- `profile`
- `User.Read`
- `User.Read.All`
- `User.ReadBasic.All`
- `User.ReadWrite`
- `User.ReadWrite.All`
- `Directory.Read.All`
- `Directory.ReadWrite.All`
- `Files.ReadWrite.All`
- `Mail.ReadBasic`
- `Mail.Read`
- `Mail.ReadWrite`
- `Mail.Send`
- `MailboxFolder.Read`
- `MailboxFolder.ReadWrite`
- `Calendars.Read`
- `Calendars.ReadBasic`
- `Calendars.ReadWrite`
- `OnlineMeetings.Read`
- `OnlineMeetings.ReadWrite`
- `OnlineMeetingArtifact.Read.All`
- `OnlineMeetingTranscript.Read.All`
- `OnlineMeetingRecording.Read.All`

The following scopes are not requested by default. Add them through the **Scopes** input field when you create a connection if your use case requires them:

- `DeviceManagementManagedDevices.Read.All`
- `DeviceManagementManagedDevices.ReadWrite.All`

The following minimum scopes are required to establish a connection to Microsoft Graph API using authorization code grant authentication:

- `User.Read`
- `offline_access`

#### Microsoft Graph API setup for authorization code grant authentication

Complete the following steps to set up the Microsoft Graph API connector for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Generate a client secret](#generate-client-secret)
- [Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal](#obtain-ids)

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Select **Delegated permissions** as the permission type, since your application requires a user to sign in.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Add the required permissions. Refer to [Minimum and default scopes](/en/connectors/microsoft-graph-api#authorization-code-grant-scopes) for the scopes to assign.
   
5. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Microsoft Graph API connector](/en/connectors/microsoft-graph-api#admin-consent) to learn more.
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application (client) ID and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID** and **Directory (tenant) ID** for use in Workato.
   

#### Connect to Microsoft Graph API with authorization code grant authentication

Complete the following steps to establish an authorization code grant connection to Microsoft Graph API in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Graph API` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Graph API with authorization code grant authentication](/assets/connection-setup-acg.CWFbfw7A.png)_Connect to Microsoft Graph API with authorization code grant authentication_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Application (client) ID** from the Azure portal in the **Client ID** field.
   
6. Enter your client secret in the **Client secret** field.
   
7. Select **Authorization code grant** from the **Authentication type** drop-down menu.
   
8. Select an option from the **Account type** drop-down menu. Options include **Single tenant**, **Multitenant**, and **Active directory multitenant**.
   
9. Enter the **Directory (tenant) ID** in the **Tenant ID** field. This field is required if you select **Single tenant** as the **Account type**.
   
10. Optional. Select the scopes you need from the **Scope** drop-down menu. By default, the connector requests the scopes listed in [Minimum and default scopes](#authorization-code-grant-scopes), which cover all of its triggers and actions.
    
11. Click **Connect**.
    

### Client credentials-based authentication (OAuth 2.0)

Client credentials-based authentication connects as the application and uses **Application** permissions.

This authentication type requires the following values:

- **Client ID**
- **Client secret**
- **Tenant ID**

#### Minimum and recommended scopes

For client credentials connections, the connector uses the **Application** permissions consented for the app in the Azure portal. We recommend assigning the following permissions to support common operations across the connector's triggers and actions. Some operations may require additional Application permissions.

- `User.Read.All`
- `Files.ReadWrite.All`
- `Mail.Read`
- `Mail.ReadWrite`
- `Mail.Send`

The following minimum scope is required to establish a connection to Microsoft Graph API using client credentials authentication:

- `User.Read.All`

#### Microsoft Graph API setup for client credentials-based authentication

Complete the following steps to set up the Microsoft Graph API connector for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
- [Assign permissions to your app](#assign-permissions-client-credentials)
- [Generate a client secret](#generate-client-secret-client-credentials)
- [Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal](#obtain-ids-client-credentials)

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

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Select **Application permissions** as the permission type, since your application doesn't require a user to sign in.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Add the required permissions. Refer to [Minimum and recommended scopes](/en/connectors/microsoft-graph-api#client-credentials-scopes) for the scopes to assign.
   
5. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Microsoft Graph API connector](/en/connectors/microsoft-graph-api#admin-consent) to learn more.
   

##### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

##### Obtain the Application (client) ID and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application (client) ID and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID** and **Directory (tenant) ID** for use in Workato.
   

#### Connect to Microsoft Graph API with client credentials-based authentication

Complete the following steps to establish a client credentials-based connection to Microsoft Graph API in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft Graph API` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Connect to Microsoft Graph API with client credentials-based authentication](/assets/connection-setup-cc.CWA0Ti2t.png)_Connect to Microsoft Graph API with client credentials-based authentication_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Application (client) ID** from the Azure portal in the **Client ID** field.
   
6. Enter your client secret in the **Client secret** field.
   
7. Select **Client credentials** from the **Authentication type** drop-down menu.
   
8. Enter the **Directory (tenant) ID** in the **Tenant ID** field.
   
9. Click **Connect**.
   

## Connect Microsoft Entra ID to the Microsoft Graph API connector

View connect Microsoft Entra ID to the Microsoft Graph API connector steps

To connect to the Microsoft Graph API connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-email-trigger.md
description: The New email trigger activates when a new email is received.
---

# Microsoft Graph API - New email trigger

The **New email** trigger activates when a new email is received.

## Input

This trigger doesn’t have any input fields.

## Output

| Output field | Description |
| --- | --- |
| OData ETag | Entity tag for concurrency control. |
| Message ID | Unique identifier for the message. |
| Created DateTime | Date and time when the message was created. |
| Last Modified DateTime | Date and time when the message was last modified. |
| Change Key | Identifies a specific version of the message. |
| Categories | List of categories associated with the message. |
| Received DateTime | Date and time when the message was received. |
| Sent DateTime | Date and time when the message was sent. |
| Has Attachments | Indicates whether the message has attachments (`Yes`/`No`). |
| Internet Message ID | Unique identifier for the message in internet format. |
| Subject | Subject of the message. |
| Body Preview | Preview text of the message body. |
| Importance | Importance level of the message. For example, `Low`, `Normal`, `High`. |
| Parent Folder ID | ID of the parent folder containing the message. |
| Conversation ID | ID of the conversation thread. |
| Conversation Index | Position of the message in the conversation thread. |
| Delivery Receipt Requested | Indicates if a delivery receipt was requested (`Yes`/`No`). |
| Read Receipt Requested | Indicates if a read receipt was requested (`Yes`/`No`). |
| Is Read | Indicates if the message has been read (`Yes`/`No`). |
| Is Draft | Indicates if the message is a draft (`Yes`/`No`). |
| Web Link | URL to access the message in a web browser. |
| Inference Classification | Classification of the message. For example, `Focused`, `Other`. |
| Body Content Type | Type of content in the message body. For example, `Text`, `HTML`. |
| Body Content | Actual content of the message body. |
| Sender Name | Name of the sender. |
| Sender Email Address | Email address of the sender. |
| From Name | Name of the person who sent the message. |
| From Email Address | Email address of the sender. |
| To Recipient Name | Name of the recipient. |
| To Recipient Email Address | Email address of the recipient. |
| CC Recipients | List of CC recipients. |
| BCC Recipients | List of BCC recipients. |
| Reply To | List of reply-to email addresses. |
| Flag Status | Status of the message flag. For example, `Not Flagged`, `Complete`, `Flagged`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-mail-message-trigger.md
description: >-
  The New mail message trigger checks for new events on a polling interval you
  specify.
---

# Microsoft Graph API - New mail message trigger

The **New mail message** trigger checks for new events on a polling interval you specify.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. |
| When first started, this recipe should pick up events from | When you start the recipe for the first time, it picks up trigger events from this specified date and time. Leave empty to get events created one hour ago. |
| User ID or principal name | Provide the user ID or name. If left blank, the messages will be retrieved from the connected user. |
| Mail folder ID | Mail folder ID for the account whose messages are to be retrieved. |

## Output

| Output field | Description |
| --- | --- |
| OData ETag | Entity tag for concurrency control. |
| Message ID | Unique identifier for the message. |
| Created DateTime | Date and time when the message was created. |
| Last Modified DateTime | Date and time when the message was last modified. |
| Change Key | Identifies a specific version of the message. |
| Categories | List of categories associated with the message. |
| Received DateTime | Date and time when the message was received. |
| Sent DateTime | Date and time when the message was sent. |
| Has Attachments | Indicates whether the message has attachments (`Yes`/`No`). |
| Internet Message ID | Unique identifier for the message in internet format. |
| Subject | Subject of the message. |
| Body Preview | Preview text of the message body. |
| Importance | Importance level of the message. For example, `Low`, `Normal`, `High`. |
| Parent Folder ID | ID of the parent folder containing the message. |
| Conversation ID | ID of the conversation thread. |
| Conversation Index | Position of the message in the conversation thread. |
| Delivery Receipt Requested | Indicates if a delivery receipt was requested (`Yes`/`No`). |
| Read Receipt Requested | Indicates if a read receipt was requested (`Yes`/`No`). |
| Is Read | Indicates if the message has been read (`Yes`/`No`). |
| Is Draft | Indicates if the message is a draft (`Yes`/`No`). |
| Web Link | URL to access the message in a web browser. |
| Inference Classification | Classification of the message. For example, `Focused`, `Other`. |
| Body Content Type | Type of content in the message body. For example, `Text`, `HTML`. |
| Body Content | Actual content of the message body. |
| Sender Name | Name of the sender. |
| Sender Email Address | Email address of the sender. |
| From Name | Name of the person who sent the message. |
| From Email Address | Email address of the sender. |
| To Recipient Name | Name of the recipient. |
| To Recipient Email Address | Email address of the recipient. |
| CC Recipients | List of CC recipients. |
| BCC Recipients | List of BCC recipients. |
| Reply To | List of reply-to email addresses. |
| Flag Status | Status of the message flag. For example, `Not Flagged`, `Complete`, `Flagged`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-presence-trigger.md
description: The New presence trigger activates when there is a new presence change.
---

# Microsoft Graph API - New presence trigger

The **New presence** trigger activates when a new presence change occurs.

## Input

| Input field | Description |
| --- | --- |
| User IDs | Select the user IDs to subscribe to multiple users' presence events. Leave blank to select all the users from the list. |

## Output

| Output field | Description |
| --- | --- |
| OData type | Specifies the type of the resource in OData format. It indicates that the returned object is of type `microsoft.graph.presence`. |
| Odata id | Unique identifier for the OData resource. |
| ID | Unique identifier of the presence record associated with a specific user. |
| Availability | Represents the user's availability status. |
| Activity | Represents the specific presence activity of the user. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/new-row-in-sheet-trigger.md
description: >-
  The New row in sheet trigger activates when a new Excel sheet row is created
  in Microsoft Graph API.
---

# Microsoft Graph API - New row in sheet trigger

The **New row in sheet** trigger activates when a new Excel sheet row is created in Microsoft Graph API.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select how frequently to check for new events. |
| File | Select the file from drop-down menu. |
| Worksheet | Sheet will dynamically load based on file selection. |

## Output

The columns of the selected sheet will be returned as output fields of this trigger.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/create-record-action.md
description: >-
  The Create record action enables you to create a new record in Microsoft Graph
  API, such as a user.
---

# Microsoft Graph API - Create record action

The **Create record** action enables you to create a new record in Microsoft Graph API, such as a user.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to create. Fields load dynamically based on your selected object. |

## Output

The output fields depend on the object you select in the input. Each object returns a unique set of fields based on its type.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/create-shareable-link-action.md
description: >-
  The Create shareable link action creates a shareable link in Microsoft Graph
  API. The existing link is returned if a shareable link already exists.
---

# Microsoft Graph API - Create shareable link action

The **Create shareable link** action creates a shareable link in Microsoft Graph API. The existing link is returned if a shareable link already exists.

## Input

| Input field | Description |
| --- | --- |
| Entity type | Select the entity to provide permissions to create a shareable link. |
| Site ID | Select the ID of the site to create a shareable link for. Default is to pick up sites from the communication site directory. |
| Link type | Select the type of link to create. For example, `view`, `edit`, or `embed`. |
| Folder ID | The ID of the folder to create a shareable link for. |
| Retain inherited permissions | Select if existing inherited permissions are retained when you share this item. All existing permissions are removed when sharing the item if set to false. |

## Output

| Output field | Description |
| --- | --- |
| ID | The ID of the shareable link. |
| Roles | Any roles that associated with the shareable link, such as `read`. |
| Link | The shareable link URL. |
| Has password | A boolean response indicating if the shareable link requires a password to access. |
| Share ID | The ID of the resource the shareable link corresponds with. |
| Expiration date time | The date and time that the shareable link expires. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/delete-record-action.md
description: The Delete record action enables you to delete a record using its object ID.
---

# Microsoft Graph API - Delete record action

The **Delete record** action enables you to delete a record using its object ID.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to delete. Fields load dynamically based on your selected object. |
| Item ID | Provide the unique ID of the object to delete. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status of the delete action. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/download-file-action.md
description: The Download file action downloads the contents of a file using its object ID.
---

# Microsoft Graph API - Download file action

The **Download file** action downloads the contents of a file using its object ID.

## Input

| Input field | Description |
| --- | --- |
| Drive | Select the file you plan to download. |
| Item ID | Provide the unique ID of the file to download. |

## Output

| Output field | Description |
| --- | --- |
| File content | The content of the downloaded file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/get-record-action.md
description: >-
  The Get record action retrieves the details of any record, such as a Drive
  item, using its object ID.
---

# Microsoft Graph API - Get record action

The **Get record** action retrieves the details of any record, such as a Drive item, using its object ID.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to retrieve. Fields load dynamically based on your selected object. |

## Output

The output fields generate dynamically based on the object you select. Refer to the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) documentation for a complete list of outputs.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/list-records-action.md
description: >-
  The List records action lists records based on the object you select in
  Microsoft Graph API.
---

# Microsoft Graph API - List records action

The **List records** action lists records based on the object you select in Microsoft Graph API. This action requires a Microsoft Intune license.

## Input

Input fields are generated dynamically based on the object you select. The following input fields are common to all objects.

| Input field | Description |
| --- | --- |
| Object | Select the object to list records for. Options include **Detected app** and **Managed devices**. |

## Output

Output fields are generated dynamically based on the object you select. Refer to the [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/use-the-api) documentation for a complete list of output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/move-mail-message-action.md
description: >-
  The Move mail message action moves a message to another folder within the
  specified user's mailbox. This creates a new copy of the message in the
  destination folder and removes the original message.
---

# Microsoft Graph API - Move mail message action

The **Move mail message** action moves a message to another folder within the specified user's mailbox. This creates a new copy of the message in the destination folder and removes the original message.

## Input

| Input field | Description |
| --- | --- |
| Destination folder ID or name | The target folder's unique ID or well-known name where the email will be moved. |
| Message ID | The unique identifier of the email message to be moved. |
| User ID or principal name | The unique ID or email address of the mailbox owner. |
| Mail folder ID | The unique ID of the source folder containing the email. |

## Output

| Output field | Description |
| --- | --- |
| OData ETag | Entity tag for concurrency control. |
| Message ID | Unique identifier for the message. |
| Created DateTime | Date and time when the message was created. |
| Last Modified DateTime | Date and time when the message was last modified. |
| Change Key | Identifies a specific version of the message. |
| Categories | List of categories associated with the message. |
| Received DateTime | Date and time when the message was received. |
| Sent DateTime | Date and time when the message was sent. |
| Has Attachments | Indicates whether the message has attachments (`Yes`/`No`). |
| Internet Message ID | Unique identifier for the message in internet format. |
| Subject | Subject of the message. |
| Body Preview | Preview text of the message body. |
| Importance | Importance level of the message. For example, `Low`, `Normal`, `High`. |
| Parent Folder ID | ID of the parent folder containing the message. |
| Conversation ID | ID of the conversation thread. |
| Conversation Index | Position of the message in the conversation thread. |
| Delivery Receipt Requested | Indicates if a delivery receipt was requested (`Yes`/`No`). |
| Read Receipt Requested | Indicates if a read receipt was requested (`Yes`/`No`). |
| Is Read | Indicates if the message has been read (`Yes`/`No`). |
| Is Draft | Indicates if the message is a draft (`Yes`/`No`). |
| Web Link | URL to access the message in a web browser. |
| Inference Classification | Classification of the message. For example, `Focused`, `Other`. |
| Body Content Type | Type of content in the message body. For example, `Text`, `HTML`. |
| Body Content | Actual content of the message body. |
| Sender Name | Name of the sender. |
| Sender Email Address | Email address of the sender. |
| From Name | Name of the person who sent the message. |
| From Email Address | Email address of the sender. |
| To Recipient Name | Name of the recipient. |
| To Recipient Email Address | Email address of the recipient. |
| CC Recipients | List of CC recipients. |
| BCC Recipients | List of BCC recipients. |
| Reply To | List of reply-to email addresses. |
| Flag Status | Status of the message flag. For example, `Not Flagged`, `Complete`, `Flagged`. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/search-records-action.md
description: The Search records action returns all records matching your search criteria.
---

# Microsoft Graph API - Search records action

The **Search records** action returns all records matching your search criteria.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to search from the drop-down menu. Fields load dynamically based on the selected object. |

## Output

The output fields depend on the object you select in the input. Each object returns a unique set of fields based on its type.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/send-mail-message-action.md
description: >-
  The Send mail message action sends an existing draft message. Use the Create
  mail message action to send a new mail message.
---

# Microsoft Graph API - Send mail message action

The **Send mail message** action sends an existing draft message. To send a new message, use the **Create mail message** action instead.

## Input

| Input field | Description |
| --- | --- |
| Subject | Subject of the message. |
| Content type | Select the format of the email body from the drop-down menu. |
| Content | The body text of the email message. |
| Address | The recipient's email address. |
| Cc recipients source list | A list of email addresses to be added as CC recipients. |
| Save the sent item | Indicates whether to save the email in the "Sent Items" folder. Select the value from the drop-down menu. |

## Output

This action doesn’t have any output fields.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/update-record-action.md
description: >-
  The Update record action enables you to update a record, such as a list, using
  its object ID.
---

# Microsoft Graph API - Update record action

The **Update record** action enables you to update a record, such as a list, using its object ID.

## Input

| Input field | Description |
| --- | --- |
| Object | Select the object you plan to update from the drop-down menu. Fields load dynamically based on the selected object. |

## Output

The output fields depend on the object you select in the input. Each object returns a unique set of fields based on its type.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-graph-api/upload-file-action.md
description: >-
  The Upload file action enables you to upload a file by providing the file
  contents. If a file with the same name already exists in the folder, this
  action overwrites the file contents.
---

# Microsoft Graph API - Upload file action

The **Upload file** action enables you to upload a file by providing the file contents. If a file with the same name already exists in the folder, this action overwrites the file contents.

## Input

| Input field | Description |
| --- | --- |
| Drive ID | The unique identifier of the OneDrive or SharePoint drive. |
| Folder ID | The unique identifier of the destination folder in the drive. |
| File name | The name of the file to be uploaded. |
| File content | The actual data or content of the file. |
| Mime type | The format of the file. |

## Output

| Output field | Description |
| --- | --- |
| ID | The unique identifier of the item within the Drive. |
| Created by | Identity of the user, device, and application that created the item. |
| Created date time | Timestamp when the file was created. |
| Description | User-provided description of the file. |
| E tag | eTag for the entire item (metadata + content). |
| Last modified by | Identity of the user, device, and application that last modified the item. |
| Last modified date time | Date and time the item was last modified. |
| Name | The name of the item (filename and extension). |
| Parent reference | Parent information, if the item has a parent. |
| Web URL | URL that displays the resource in the browser. |
| Created by user | Identity of the user who created the item. |
| Last modified by user | Identity of the user who last modified the item. |
| Audio | Audio metadata, if the item is an audio file. |
| Bundle | Bundle metadata, if the item is a bundle. |
| Content | The content stream, if the item represents a file. |
| C tag | An eTag for the content of the item. This eTag isn't changed if only the metadata is changed. Note This property isn't returned if the item is a folder. |
| Deleted | Information about the deleted state of the item. |
| File | File metadata, if the item is a file. |
| File system info | File system information on client. |
| Folder | Folder metadata, if the item is a folder. |
| Image | Image metadata, if the item is an image. |
| Location | Location metadata, if the item has location data. |
| Malware | Malware metadata, if the item was detected to contain malware. |
| Package | If present, indicates that this item is a package instead of a folder or file. Packages are treated like files in some contexts and folders in others. |
| Pending operations | If present, indicates that one or more operations that might affect the state of the driveItem are pending completion. |
| Photo | Photo metadata, if the item is a photo. |
| Publication | Provides information about the published or checked-out state of an item, in locations that support such actions. This property isn't returned by default. |
| Remote item | Remote item data, if the item is shared from a drive other than the one being accessed. |
| Root | If this property is non-null, it indicates that the driveItem is the top-most driveItem in the drive. |
| Search result | Search metadata, if the item is from a search result. |
| Shared | Indicates that the item was shared with others and provides information about the shared state of the item. |
| Sharepoint IDs | Returns identifiers useful for SharePoint REST compatibility. |
| Special folder | If the current item is also available as a special folder, this facet is returned. |
| Size | Size of the item in bytes. |
| Video | Video metadata, if the item is a video. |
| Web dav URL | WebDAV compatible URL for the item. |
| Workbook | For files that are Excel spreadsheets, access to the workbook API to work with the spreadsheet's contents. |
| Analytics | Analytics about the view activities that took place on this item. |
| Children | Collection containing Item objects for the immediate children of Item. Only items representing folders have children. |
| List item | For drives in SharePoint, the associated document library list item. |
| Permissions | The set of permissions for the item. |
| Retention label | Information about retention label and settings enforced on the driveItem. |
| Subscriptions | The set of subscriptions on the item. Only supported on the root of a drive. |
| Thumbnails | Collection of [thumbnailSet](https://learn.microsoft.com/en-us/graph/api/resources/thumbnailset?view=graph-rest-1.0) objects associated with the item. For more information, see [getting thumbnails](https://learn.microsoft.com/en-us/graph/api/driveitem-list-thumbnails?view=graph-rest-1.0). |
| Versions | The list of previous versions of the item. For more info, see [getting previous versions](https://learn.microsoft.com/en-us/graph/api/driveitem-list-versions?view=graph-rest-1.0). |

Please refer to the [Properties](https://learn.microsoft.com/en-us/graph/api/resources/driveitem?view=graph-rest-1.0#properties) for detailed schema.

---
