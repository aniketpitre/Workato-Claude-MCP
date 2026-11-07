---
url: 'https://docs.workato.com/en/connectors/box.md'
description: >-
  The Box connector lets you automate content workflows: upload, download, and
  search files, manage shared links, and trigger on new or updated files.
---

# Box

[Box](https://www.box.com/home) is a cloud content management and file sharing service for businesses. The Box platform enables secure and easy team collaboration on-the-go.

## Use cases

Integrate the Box connector with your business applications to enhance collaboration and file management. You can automate document sharing, improve approvals workflows, and securely transfer data across platforms. Explore our [use cases](/en/getting-started/workato-use-cases) to discover how you can optimize your Box workflows:

- [Invite DocuSign signees to collaborate in Box](/en/getting-started/use-cases/docusign-box-slack) and notify your team in Slack.
- [Load Box CSV data](/en/getting-started/use-cases/box-google-cloud-storage-bigquery) to Google BigQuery with Google Cloud Storage.

## API version

The Box connector uses [Box Rest API v2](https://developer.box.com/reference/).

## Supported editions and versions

The Box connector works with all Box plans.

## How to connect to Box on Workato

The Box connector supports the following authentication methods:

- [Authorization code grant](#authorization-code-grant)
- [Client credentials](#client-credentials)

### Roles and permissions required to connect

Your Workato permissions match the permissions you have in Box. This means that you have the same capabilities to view, share, upload, and download files and folders in Workato that you have on the Box platform. Refer to [Box privileges and permissions](#box-privileges-and-permissions) for more information.

> **BOX REFRESH TOKEN**
> 
> Box Refresh Tokens enable you to acquire a new Access Token for Box. However, each Box Refresh Token is valid for only one use within a 60-day period. Consequently, if you maintain an active connection to Box but refrain from using any Box actions for 60 days, an error occurs when you try to perform a Box action.
> 
> Refer to the Box documentation to learn how to manage your access using [Box Refresh Tokens](https://developer.box.com/guides/authentication/tokens/refresh/).

### Authorization code grant

Complete the following steps to set up your Box connection using authorization code grant authentication:

1. Provide a name that identifies which Box instance Workato is connected to in the **Connection name** field.
   
   ![Box Connection 1](/assets/box_connection_1.OJ4XKoIg.png)_Create your connection_
   
2. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
3. Optional. Expand **Advanced settings** to select **Requested permissions (Oauth scopes)** options.
   
   You can select from the following scopes:
   
   - Read files and folders
   - Read and write files and folders
   - Manage app users
   - Manage managed users
   - Manage groups
   - Manage webhooks
   - Manage enterprise properties
   - Manage retention policies
   - Global content manager
   - Admin can make calls on behalf of users
   - Manage signature requests
   - Manage Box Relay
4. Click **Connect**. This opens the Box sign in dialog.
   
5. Enter your Box account email address and password.
   
   ![Box Connection 2](/assets/box_connection_2.DakkUsWJ.png)_Log in to Box_
   
6. Click **Authorize**.
   
7. Review the requested permissions and click **Grant access to Box**.
   
   ![Grant access to Box](/assets/grant-access.CygYC_9w.png)_Grant access to Box_
   

### Client credentials

Complete the following steps to set up your Box connection using client credentials authentication:

1. Create a custom app.
   
   1. Sign in to your Box account.
      
   2. Go to **Dev Console > My Apps**.
      
   3. Click **Create New App**.
      
   4. Select **Custom App** as the app type to create.
      
   5. Enter your app name in the **App Name** field.
      
   6. Enter your app description in the **Description** field.
      
   7. Use the **Purpose** drop-down menu to select **Automation**.
      
   8. Click **Next**.
      
   9. Select **Server Authentication (Client Credentials Grant)** as your authentication method.
      
   10. Click **Create App**. This opens the **Configuration** tab.
       
   
2. Get required values.
   
   You must enable **App + Enterprise Access** and **Generate User Access Tokens** in the Box Developer Console if you plan to authenticate as an admin or a managed user.
   
   1. Scroll to the **OAuth 2.0 Credentials** section and copy the **Client ID**. Store this value securely, as it is required to configure your Box connection in Workato.
      
   2. Click **Fetch Client Secret**. This opens a **2-Step Verification** page.
      
   3. Enter the 6-digit code from your authenticator app in the **Authentication Code** field. This reveals the **Client Secret** field.
      
   4. Click **Copy** to retrieve the client secret. Store this value securely, as it is required to configure your Box connection in Workato.
      
   5. Scroll to the **App Access Level** section and select **App + Enterprise Access**.
      
   6. Click **Save Changes**.
      
   7. Click the **General Settings** tab and copy either the **User ID** or the **Enterprise ID**. Use the **User ID** if the authentication subject type is a managed user, or the **Enterprise ID** if it is a service account. Store this value securely, as it is required to configure your Box connection in Workato.
      
   8. Go to **Advanced Features**, select the **Generate user access tokens** checkbox, and click **Save changes** if the authentication subject type is a managed user.
      
      > **ADVANCED FEATURE CHANGES REQUIRE REAUTHORIZATION**
      > 
      > You must re-authorize your app in the Admin Console if you make changes in **Advanced Features** after the app is authorized. Go to **Authorization > Review and Submit > Admin Console > Authorize App**.
      
   
3. Submit the app for authorization.
   
   1. Go to the **Authorization** tab and click **Review and Submit**.
      
   2. Review your app authorization submission and click **Submit**.
      
   3. Click **Back to My Account**.
      
   
4. Authorize the app.
   
   1. Go to **Admin Console > Integrations > Platform Apps Manager**.
      
   2. Hover over the app you submitted for authorization and click **… More**.
      
   3. Select **Authorize App**.
      
   4. Review the information and click **Authorize**.
      
      > **SKIPPED AUTHORIZATION RESULTS IN ERROR**
      > 
      > The connection returns a 403 Forbidden error if you skip this step or the authorization hasn't been approved by your Box admin. Make sure the app status shows `Authorized` and `Enabled` in the **Platform Apps Manager** before you attempt to connect to Workato.
      
   
5. Sign in to Workato and create a new Box connection.
   
6. Provide a name that identifies which Box instance Workato is connected to in the **Connection name** field.
   
   ![Connect to Box](/assets/box-client-credentials.BcuXtI8f.png)_Connect to Box using client credentials authentication_
   
7. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
8. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
9. Enter the client ID from the **Get required values** step in the **Client ID** field.
   
10. Enter the client secret from the **Get required values** step in the **Client secret** field.
    
11. Use the **Subject type** drop-down menu to select your subject type. Available options include **Managed user** and **Service account**.
    
    - **Managed user**: Enter the user ID from the **Get required values** step in the **User ID** field.
    - **Service account**: Enter the enterprise ID from the **Get required values** step in the **Enterprise ID** field.
12. Optional. Specify the custom OAuth profile you plan to use for this connection in the **Custom OAuth profile** field.
    
13. Click **Connect**.
    

## Working with attachments in Box

### Upload file content

You can upload plain text file content using this action.

1. Enter the text for your file in the **File Content** field.
   
2. Select the **folder** you plan to upload in Box.
   
3. Enter a **name** for the file, including the extension.
   
   ![Box Attachment 1](/assets/box_attachment_1.C2NPpZ7w.png)_Upload file content_
   

### Upload file from URL

You can upload a file directly from a URL rather than entering text content. This allows you to upload non-text files such as images.

1. Enter the URL for the file you plan to upload in the **Source URL** field. Attachment URLs typically end with the file extension for the file (such as .jpg).
   
   ![Box Attachment 2](/assets/box-upload-from-url.Bn55ZhdE.png)_Upload file from URL_
   
2. Select the **Destination folder** where you plan to upload your file. Note that entering a file name is optional as Workato obtains the name of the file from the URL by default.
   

## Create and use shared links to Box folder/file

The **Create shared link** action allows you to create a direct link to a file or folder in Box.

1. Enter the **file ID/folder ID** for the file/folder for which you plan to create a shared link.
   
2. Select an **access** level for the shared link (Open, Company, Collaborators, or Default). Refer to [Shared link permissions](#shared-link-permissions) for more information.
   
   - This sets restrictions on who can view your file/folder using the shared link. If you have a Premium Box subscription, you can also enter a password that link-users must enter before they can access your file/folder.
     
     ![Box Attachment 3](/assets/box_attachment_3.CIHPgnuq.png)_Create shared links_
     
3. Optional. Use the ID (Step 1) datapill from the trigger step to identify the new file when creating the shared URL link, and post the URL in the following schema to your Slack Workbot.
   
   ![Box Shared Link 1](/assets/box_shared_link_1.DgZgXYYd.png)![Box Shared Link 2](/assets/box_shared_link_2.DzWuFaa0.png)_Post the URL in Slack Workbot_
   

## Box privileges and permissions

### Box role privileges

The Box connector only allows you to perform actions you been granted privileges for in the Box account used to make the connection to Workato. The following table describes the available Box role privileges:

| Levels | Access |
| --- | --- |
| Uploader | Can only upload content and see names of items in the folder. Can't view or download any content. |
| Previewer | Can only preview items in the folder. Can't upload, edit, delete, or share any content. |
| Viewer | Can preview/download content, make comments, and generate shared links. Can't add tags, invite new collaborators, edit shared links, or upload, edit, or delete items in the folder. |
| Previewer uploader | Can preview content, add comments, add tasks, and upload content to the folder. Can't add tags, generate shared links, invite new collaborators, or edit/delete items in the folder. |
| Viewer uploader | Can preview content, download content, add comments, generate shared links, and upload content to the folder. Can't add tags, invite new collaborators, or delete items in the folder. Can still download, edit, and re-upload files under the same name manually or using Box Edit. |
| Editor | Can view, download, upload, edit, delete, copy, move, and rename content. Can also generate/edit shared links, make comments, assign tasks, create tags, and invite/remove collaborators. Can't delete or move root level folders. |
| Co-owner | Has all permissions of an editor. Can also manage users in the folder: add new collaborators, change access levels of collaborators, remove collaborators. |
| Owner | Full access. |

### Shared link permissions

When creating a shared link for a file or folder in Box, you can choose from four different options for access levels, as shown below.

| Levels | Access |
| --- | --- |
| Open | Anyone with the link can access the file or folder. A Box account is not required. |
| Company | Only Box users with a validated email address matching your company's domain can access the file or folder via the shared link. |
| Collaborators | Only Box users invited to the folder or file (collaborators) can access the file or folder via the shared link. |
| Default | This option follows whatever the default setting for your account is. You can view and change this in your Box account settings under Content and Sharing. |

---
