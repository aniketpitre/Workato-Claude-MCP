---
url: 'https://docs.workato.com/en/connectors/zoom.md'
description: >-
  Zoom is a cloud platform for video and audio conferencing, collaboration,
  chat, and webinars.
---

# Zoom

[Zoom](https://zoom.us/) provides a cloud platform for video and audio conferencing, collaboration, chat, and webinars. Zoom is accessible across mobile devices, desktops, telephones, and room systems.

Watch a quick video

[Video](https://www.youtube.com/embed/z3L-yqG-HuE)

## API version

The Zoom connector uses [Zoom's REST API v2](https://developers.zoom.us/docs/api/).

## Connection setup

The Zoom connector uses OAuth 2.0 authentication.

### Zoom setup for OAuth 2.0 authentication

Complete the following steps to connect to Zoom in Workato with OAuth 2.0 authentication:

- [Add an API user](#add-an-api-user)
- [Create a custom OAuth profile](#create-custom-oauth-profile)
- [Connect to Zoom with OAuth 2.0 authentication](#connect)

> **RECOMMENDED SETUP**
> 
> We recommend that you set up a dedicated API user account in Zoom or create a custom OAuth profile to authorize Workato. This allows you to assign the API user to a role with only the necessary permissions.
> 
> Alternatively, you can use an existing Zoom owner or admin account if it has the required permissions. Some admin accounts may have restricted access based on their configuration.

#### Add an API user

Complete the following steps to set up a provisioned API user for Workato:

1. Sign into your [Zoom account](https://zoom.us/signin).
   
2. Go to **Admin > User Management > Users**.
   
   ![Add users](/assets/users-tab.CCrDasMU.png)_Add users_
   
3. Click **Add Users**.
   
4. Enter an appropriate email for the API user. We recommend an IT admin alias.
   
5. Enter `N/A` or make selections based on your requirements for the following fields: **Department**, **Manager**, **Job Title**, **Location**, and **User Groups**.
   
6. Click **Add**.
   
7. Go to **Admin > Roles**.
   
8. Select **Add Role**.
   
9. Provide a **Role Name** and **Description**.
   
10. Click **Add**.
    
11. Go to **Roles > Roles Settings** and add the following permissions to your Zoom role. Role permissions are required to allow the Workato Zoom connector to perform account-level actions, such as scheduling meetings or webinars on behalf of other Zoom users.
    
    - `Users: View and Edit`
    - `Role management: View and Edit`
    - `Groups: View and Edit`
    - `Recording management: View and Edit`
    - `Zoom rooms: View and Edit`
    - `Meetings: View`
    - `Webinars: View`
    - `Usage reports: View`
    - `Schedule tracking fields: View and Edit`
12. Click **Save Changes**.
    
13. Go to **User Management > Users** and locate the user you created in the preceding steps.
    
14. Click **Edit** and use the **User Role** drop-down menu to select the role you created.
    
15. Click **Save**.
    

#### Create a custom OAuth profile

Complete the following steps to create a custom OAuth profile for Workato:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `Zoom` and select it as your app.
   
4. Enter a name for your custom OAuth profile in the **Name** field.
   
5. Click **Create new app**.
   
6. Go to the [Zoom App Marketplace](https://marketplace.zoom.us/) and sign in to your Zoom account if you're not signed in already.
   
7. Click **Develop > Build App**.
   
   ![Build app](/assets/build-app.EiC2eXFV.png)_Build app_
   
8. Choose the kind of app to create from the following options: **General App**, **Server to Server OAuth App**, or **Webhook Only App**. If you can't select the options, you must enable the **Zoom for developers** role. Refer to the Zoom [Select general app features](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#prerequisites) page to learn how to enable the **Zoom for developers** role.
   
9. Click **Create**.
   
10. Enter a name for your app and select how the app is managed. Refer to the Zoom [Step 2: Maintain basic information](https://developers.zoom.us/docs/build-flow/create-oauth-apps/#step-2-maintain-basic-information) page for more information.
    
11. Copy and save the **Client ID** and **Client Secret** for use in Workato.
    
    ![Copy the Client ID and Client Secret](/assets/client-id-client-secret.rM4DBfar.png)_Copy the Client ID and Client Secret_
    
12. Enter `https://www.workato.com/oauth/callback` in the **OAuth Redirect URL** field.
    
13. Optional. Configure settings in the **Access**, **Surface**, and **Embed** tabs as required.
    
14. Go to **Scopes** and click **\+ Add Scopes** to add the required scopes.
    
15. Search for and select the required scopes for your connection.
    
    **MCP server**
    
    The Zoom Meetings MCP server requires the following scopes for tool functionality:
    
    - `meeting:read:list_past_participants`
    - `user:read:user`
    - `meeting:read:list_past_instances`
    - `cloud_recording:read:meeting_transcript`
    - `cloud_recording:read:list_recording_files`
    - `meeting:read:meeting`
    - `meeting:write:meeting`
    - `meeting:update:meeting`
    - `meeting:read:list_meetings`
    
    **Connector**
    
    The Zoom connector requires the following minimum scope:
    
    `user:read:user`
    
16. Click **Done**.
    
17. Go to the **Local Test** tab and select **Preview your app listing page** to ensure your settings are properly configured.
    
18. Return to the **New custom profile** page in Workato and paste the **Client ID** and **Client secret** into their respective fields.
    
    ![Paste the client ID and client secret](/assets/enter-client-id-client-secret.BjbVOHtd.png)_Paste the client ID and client secret_
    
19. Click **Save**.
    

#### Connect to Zoom with OAuth 2.0 authentication

Complete the following steps to connect to Zoom in Workato:

1. Click **Create > Connection**.
   
2. Search for `Zoom` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Zoom Connection Setup](/assets/connection-setup-zoom.i8W0drY7.png)_Name your connection_
   
4. Optional. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to specify OAuth scopes to request for your connection.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
6. Click **Connect**.
   
7. Sign in to your Zoom account.
   

## How to uninstall Workato from Zoom

Complete the following steps to uninstall Workato from Zoom:

1. Go to the **Connections** page in Workato and disconnect all active Zoom connections.
   
2. Go to the [Zoom App Marketplace](https://marketplace.zoom.us/) and sign in with your account administrator credentials.
   
3. Click **Manage > Added Apps**.
   
4. Find the app you plan to remove, click **...**, and select **Remove**.
   
   ![Zoom remove app](/assets/remove-app.CabxSaR2.png)_Remove app_
   
5. Optional. Use the drop-down menu to select a reason for removing this app.
   
6. Click **Remove** to confirm the app removal.
   

> **UNINSTALLING ZOOM STOPS ACTIVE RECIPES USING THE CONNECTOR**
> 
> Uninstalling Zoom stops all active recipes that use the Zoom connector in your Workato account. You must establish a new app connection on Workato to reinstall Zoom.

---
