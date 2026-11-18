---
url: 'https://docs.workato.com/en/connectors/microsoft-powerpoint.md'
description: >-
  Use the Microsoft PowerPoint connector in Workato to manage your slide-based
  presentations.
---

# Microsoft PowerPoint

[Microsoft PowerPoint](https://www.microsoft.com/en-us/microsoft-365/powerpoint) is a presentation software program that lets you create, edit, and share slide-based presentations.

The connector can process presentation files up to 100 MB, including their uncompressed size. Actions fail on larger files.

## Connection setup

The Microsoft PowerPoint connector supports the following authentication types:

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

This authentication method requires the following value for tenant-specific account types:

- Tenant ID

#### Minimum and default scopes

The Microsoft PowerPoint connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

| Permission | Description | Relevant action |
| --- | --- | --- |
| `Files.Read.All` | Allows the app to read all files the signed-in user can access. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Files.ReadWrite.All` | Allows the app to read and write all files the signed-in user can access. | All actions in `Files.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections on behalf of the signed-in user. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Sites.ReadWrite.All` | Allows the app to read and write documents in all SharePoint site collections on behalf of the signed-in user. | All actions in `Sites.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `User.Read` | Allows the app to sign in and read the profile of the signed-in user. | The connector always requests this permission. |
| `offline_access` | Allows the app to access Microsoft Graph data after the user signs out or the session expires. | The connector always requests this permission. |

Use **Requested permissions (OAuth scopes)** in **Advanced settings** to limit the requested permissions. Select `Files.ReadWrite.All`, `Sites.ReadWrite.All`, or both to use actions that create or modify slides. Those actions fail on connections that request only read permissions.

You must add the following minimum scopes to establish a connection to Microsoft PowerPoint with authorization code grant authentication:

- `offline_access`
- `User.Read`

#### Microsoft PowerPoint setup for authorization code grant authentication

Complete the following steps to set up Microsoft PowerPoint for authorization code grant authentication:

- [Register the Workato app in the Azure portal](#auth-register)
- [Assign permissions to your app](#assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#obtain-directory-id)

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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Assign **Delegated** permissions for authorization code grant connections and **Application** permissions for client credentials-based connections.
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Microsoft PowerPoint connector](/en/connectors/microsoft-powerpoint#admin-consent) to learn more.
   

##### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

#### Connect to Microsoft PowerPoint with authorization code grant authentication

View connect to Microsoft PowerPoint with authorization code grant authentication steps

Complete the following steps to set up an authorization code grant connection to Microsoft PowerPoint in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft PowerPoint` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select the type of Microsoft account to connect to. The available choices are **Common** and **Tenant specific**.
   
   **Common**
   
   - **Common**: This option supports personal and enterprise Microsoft accounts.
   
   ![Microsoft PowerPoint Common connection setup](/assets/connect-common.D2AA5xSb.png)_Microsoft PowerPoint Common connection setup_
   
   **Tenant specific**
   
   - **Tenant specific**: This option requires a Tenant ID.
   
   ![Microsoft PowerPoint Tenant specific connection setup with authorization code grant](/assets/connect-tenant-specific-auth-code.CxxIfBQr.png)_Microsoft PowerPoint Tenant specific connection setup with authorization code grant_
   
   Provide the Microsoft Entra ID tenant ID (a GUID) or its domain name in the **Tenant ID** field.
   
6. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
7. Expand the **Advanced settings** section to configure **Requested permissions (OAuth scopes)** for your connection. Ensure your connection provides write permissions if you plan to use actions or MCP server tools that create or modify slides. `User.Read` and `offline_access` are requested in addition to any selected permissions.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
9. Click **Sign in with Microsoft**.
   

### Client credentials-based authentication (OAuth 2.0)

This method requires the following fields:

- Tenant ID
- User ID
- Client ID
- Client Secret

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

#### Scopes and permissions

The Microsoft PowerPoint connector doesn't request individual scopes for client credentials connections. Instead, the connector uses the permissions you assign to the Workato app. You must assign these permissions as **Application** permissions in the Azure portal.

| Permission | Description | Relevant action |
| --- | --- | --- |
| `Files.Read.All` | Allows the app to read all files without a signed-in user. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Files.ReadWrite.All` | Allows the app to read and write all files without a signed-in user. | All actions in `Files.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `Sites.Read.All` | Allows the app to read documents in all SharePoint site collections without a signed-in user. | Get presentation info, Get slide content, Get slide elements, and List slide layouts (batch) |
| `Sites.ReadWrite.All` | Allows the app to read and write documents in all SharePoint site collections without a signed-in user. | All actions in `Sites.Read.All` and Add slide, Copy slide, Delete slide, Find and replace text, Update speaker notes, and Update text content |
| `User.Read.All` | Allows the app to read the profile of all users without a signed-in user. | Required to establish the connection. |

The connector uses the **User ID** you enter in **Advanced settings** to access the files of that user.

#### Microsoft PowerPoint setup for client credentials-based authentication (OAuth 2.0)

Complete the following steps to set up Microsoft PowerPoint for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#client-credentials-register)
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

1. In the navigation sidebar, select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph APIs**.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
3. Add the required permissions. Assign **Delegated** permissions for authorization code grant connections and **Application** permissions for client credentials-based connections.
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to the [Connect Microsoft Entra ID to the Microsoft PowerPoint connector](/en/connectors/microsoft-powerpoint#admin-consent) to learn more.
   

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

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure Portal steps

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
   

#### Connect to Microsoft PowerPoint with client credentials-based authentication

View connect to Microsoft PowerPoint with client credentials-based authentication steps

Complete the following steps to set up a client credentials grant connection to Microsoft PowerPoint in Workato:

> **PREREQUISITES**
> 
> Client credentials connections require a tenant ID, user ID, client ID, and client secret.
> 
> Refer to the Microsoft [Application configuration](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration) documentation to generate these values.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Microsoft PowerPoint` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Account type** drop-down menu to select **Tenant specific**.
   
   ![Microsoft PowerPoint Tenant specific connection setup](/assets/connect-tenant-specific.CfAZXYj3.png)_Microsoft PowerPoint Tenant specific connection setup_
   
6. Enter the Azure **Tenant ID**.
   
   Refer to the Microsoft [Authority](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#authority) documentation for more information about tenant IDs.
   
7. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
8. Expand the **Advanced settings** section and provide the following **User ID**, **Client ID**, and **Client secret** for your account.
   
   Refer to the Microsoft [Authority](https://learn.microsoft.com/en-us/entra/identity-platform/msal-client-application-configuration#authority) documentation to generate these values.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Sign in with Microsoft**.
    

## Connect Microsoft Entra ID to the Microsoft PowerPoint connector

View connect Microsoft Entra ID to the Microsoft PowerPoint connector steps

To connect to the Microsoft PowerPoint connector using a Microsoft Entra ID account, ensure that all the consent requests are granted by admins.

Complete the following steps to grant admin consent using an admin account:

1. Sign in to your Azure portal and navigate to **Enterprise Applications > Activity > Admin consent requests**.
   
2. Approve the necessary consent requests.

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/add-slide-action.md
description: >-
  The Add slide action inserts a new slide into a PowerPoint presentation using
  a layout you specify.
---

# Microsoft PowerPoint - Add slide action

The **Add slide** action inserts a new slide into a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Layout ID | Optional. Enter the layout ID from the [List slide layouts (batch)](/en/connectors/microsoft-powerpoint/list-slide-layouts-action-batch) action. Uses a blank-compatible layout if left blank. |
| Position | Optional. Enter the position to insert the slide at. Appends the slide to the end of the presentation if left blank. |

## Output

| Output field | Description |
| --- | --- |
| New slide number | The position of the new slide. |
| Layout used | The ID of the layout the action applied to the new slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/copy-slide-action.md
description: The Copy slide action duplicates a slide within a PowerPoint presentation.
---

# Microsoft PowerPoint - Copy slide action

The **Copy slide** action duplicates a slide within a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Source slide number | Enter the position of the slide to copy. |
| Position | Optional. Enter the position to insert the copied slide at. Inserts the copied slide immediately after the source slide if left blank. |

## Output

| Output field | Description |
| --- | --- |
| New slide number | The position of the new slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/delete-slide-action.md
description: >-
  The Delete slide action permanently removes one or more slides from a
  PowerPoint presentation.
---

# Microsoft PowerPoint - Delete slide action

The **Delete slide** action removes one or more slides from a presentation in Microsoft PowerPoint. At least one slide must remain in the presentation.

> **THIS ACTION CAN'T BE UNDONE**
> 
> You can't recover deleted slides. Confirm the slide numbers before you run this action.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide numbers | Enter the position of the slide or slides to delete. Accepts a single number or a list. |

## Output

| Output field | Description |
| --- | --- |
| Slides deleted | The number of slides the action deleted. |
| Remaining slides | The number of slides remaining in the presentation. |
| Skipped slide numbers (out of range) | The slide numbers the action excluded because they fall outside the presentation's range. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/find-and-replace-text-action.md
description: >-
  The Find and replace text action finds and replaces text across every slide in
  a PowerPoint presentation.
---

# Microsoft PowerPoint - Find and replace text action

The **Find and replace text** action finds and replaces text across every slide in a presentation in Microsoft PowerPoint. The action fails if it finds more than 1,000 matches. Narrow your search text or update slides individually with the [Update text content](/en/connectors/microsoft-powerpoint/update-text-content-action) action.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Find text | Enter the text to search for across all slides. |
| Replace with | Optional. Enter the replacement text. Deletes every instance of the found text if left blank. |
| Match case | Optional. Select to match the exact case of the **Find text** value. Options are **Yes** and **No**. Defaults to **Yes** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Total replacements made | The total number of replacements across the presentation. |
| Affected slides | The slides that contain replacements. |
| Slide number | The position of the affected slide. |
| Replacements on this slide | The number of replacements on the slide. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-presentation-info-action.md
description: >-
  The Get presentation info action retrieves metadata about a PowerPoint
  presentation, including its title, slide count, creator, and last modifier.
---

# Microsoft PowerPoint - Get presentation info action

The **Get presentation info** action retrieves metadata about a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Title | The title of the presentation. |
| Author | The author of the presentation, from the presentation's own document properties. |
| Last modified by | The display name and the email address of the user who last modified the presentation, from the presentation's own document properties. Blank if the presentation doesn't have this property set. |
| Created at | The date and time the presentation was created. |
| Last modified at | The date and time of the last change to the presentation. |
| Slide count | The number of slides in the presentation. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| Created by | The display name and email address of the user who created the presentation file, from the file storage account. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-slide-content-action.md
description: >-
  The Get slide content action retrieves the text content and speaker notes for
  slides in a PowerPoint presentation.
---

# Microsoft PowerPoint - Get slide content action

The **Get slide content** action retrieves the text content and speaker notes of slides in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide numbers | Optional. Enter the slide numbers to retrieve. Retrieves up to the first 50 slides if left blank. Accepts up to 50 slides per request. |
| Include speaker notes | Optional. Select to include each slide's speaker notes in the response. Options are **Yes** and **No**. Defaults to **Yes** if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slides | The slides in the presentation. Returns one entry per slide. |
| Slide number (Slides) | The slide's position in the presentation. |
| Slide title (Slides) | The slide's title. |
| Speaker notes (Slides) | The slide's speaker notes. |
| Text elements (Slides) | The text elements on the slide. Returns one entry per element. |
| Element ID (Text elements) | The text element's unique ID. |
| Placeholder type (Text elements) | The type of placeholder the text element occupies. |
| Text (Text elements) | The element's text content. |
| Has more slides | A boolean response (`true` or `false`) that indicates whether the presentation has slides beyond those included in the response. |
| Total slide count | The total number of slides in the presentation. |
| Skipped slide numbers (out of range) | The slide numbers the action excluded from the response because they fall outside the presentation's range. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/get-slide-elements-action.md
description: >-
  The Get slide elements action retrieves the position, size, and content of
  every element on a PowerPoint slide.
---

# Microsoft PowerPoint - Get slide elements action

The **Get slide elements** action retrieves every element on a single slide in a presentation in Microsoft PowerPoint, including its position, size, and content.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide to retrieve elements from. |

## Output

The following are a representative set of output fields. Refer to the output datapills in the recipe editor to view the remaining fields.

| Output field | Description |
| --- | --- |
| Elements | The elements on the slide. Returns one entry per element. |
| Element ID (Elements) | The element's unique ID. |
| Element type (Elements) | The element's type. |
| Placeholder type (Elements) | The type of placeholder the element occupies, if any. |
| Position (Elements) | The element's position on the slide, in English Metric Units (EMU). |
| X (Position) | The element's horizontal position, in EMU. |
| Y (Position) | The element's vertical position, in EMU. |
| Size (Elements) | The element's size, in English Metric Units (EMU). |
| Width (Size) | The element's width, in EMU. |
| Height (Size) | The element's height, in EMU. |
| Text preview (Elements) | A preview of the element's text content. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/list-slide-layouts-action-batch.md
description: >-
  The List slide layouts (batch) action retrieves the slide layouts and
  placeholders defined in a PowerPoint presentation.
---

# Microsoft PowerPoint - List slide layouts action (batch)

The **List slide layouts (batch)** action retrieves the slide layouts defined in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |

## Output

| Output field | Description |
| --- | --- |
| Layouts | The slide layouts defined in the presentation. Returns one entry per layout. |
| Layout ID (Layouts) | The layout's unique ID. |
| Layout name (Layouts) | The layout's name. |
| Slide master (Layouts) | The name of the slide master the layout belongs to. |
| Placeholders (Layouts) | The placeholders defined in the layout. Returns one entry per placeholder. |
| Placeholder type (Placeholders) | The placeholder's type. |
| Placeholder index (Placeholders) | The placeholder's index. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/update-speaker-notes-action.md
description: >-
  The Update speaker notes action replaces the speaker notes for a slide in a
  PowerPoint presentation.
---

# Microsoft PowerPoint - Update speaker notes action

The **Update speaker notes** action replaces the speaker notes for a slide in a presentation in Microsoft PowerPoint.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide to update. |
| Notes content | Optional. Enter the speaker notes text. Replaces the existing notes entirely. Accepts up to 5,000 characters. Clears the notes if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slide number | The position of the updated slide. |
| Notes preview | A preview of the slide's updated speaker notes. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---

---
url: >-
  https://docs.workato.com/en/connectors/microsoft-powerpoint/update-text-content-action.md
description: >-
  The Update text content action replaces the text of a specific element on a
  PowerPoint slide.
---

# Microsoft PowerPoint - Update text content action

The **Update text content** action replaces the text of a specific element on a slide in a presentation in Microsoft PowerPoint. Identify the element by its element ID or existing text.

## Input

| Input field | Description |
| --- | --- |
| File source | Select the service that stores the presentation. Options are **OneDrive** and **SharePoint**. |
| Presentation | Select the presentation, or enter the file ID. |
| Slide number | Enter the position of the slide that contains the element. |
| Element ID | Optional. Enter the element ID from the [Get slide elements](/en/connectors/microsoft-powerpoint/get-slide-elements-action) action. Use either this field or **Find text**, not both. |
| Find text | Optional. Enter the text to locate within an element on the slide. Use either this field or **Element ID**, not both. Case-sensitive. |
| New text | Optional. Enter the replacement text. Removes the found text if left blank. |

## Output

| Output field | Description |
| --- | --- |
| Slide number | The position of the updated slide. |
| Element ID | The unique ID of the updated element. |
| Updated text preview | A preview of the element's updated text. |
| File ID | The unique ID of the presentation file. |
| File name | The name of the presentation file. |
| Web URL | The URL to view the presentation in a browser. |
| File ETag | The ETag of the presentation file. Use it to detect changes. |
| File last modified | The date and time of the last change to the presentation file. |

---
