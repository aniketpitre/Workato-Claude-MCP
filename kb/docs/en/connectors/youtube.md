---
url: 'https://docs.workato.com/en/connectors/youtube.md'
description: >-
  The YouTube connector lets you search videos, retrieve video and channel data,
  manage comments and playlists, and update video metadata in Workato.
---

# YouTube

[YouTube](https://www.youtube.com/) is a video-sharing platform that lets creators upload and manage video content, engage with viewers through comments, and organize content into playlists. The YouTube connector lets you automate workflows to search videos, retrieve video and channel data, manage comments, organize playlists, and update video metadata in Workato.

## API version

The YouTube connector uses the [YouTube Data API v3](https://developers.google.com/youtube/v3).

## Install YouTube from the community library

Complete the following steps to install the YouTube connector from the [community library](https://www.workato.com/browse/connectors):

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

The YouTube connector supports the following authentication types:

- [API key](#api-key)
- [OAuth 2.0](#oauth-2-0)

### API key authentication

Use API key authentication to access public YouTube data, such as videos, channels, and playlists, without connecting a specific YouTube account. You must enable the YouTube Data API v3 and generate an API key.

#### YouTube setup for API key authentication

Complete the following steps to set up YouTube for API key authentication:

> **PREREQUISITES**
> 
> You must have a project in the Google Cloud Console. Refer to the Google [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project) guide for more information.

1. Sign in to your [Google Cloud Console](https://console.cloud.google.com/).
   
2. Open the navigation menu and select **APIs & Services > Library**.
   
3. Search for `YouTube Data API v3` and select the API.
   
4. Click **Enable**.
   
5. Use the project drop-down menu next to the Google Cloud logo to select the project for which you plan to create credentials.
   
6. Go to **APIs & Services > Credentials**.
   
7. Select **\+ Create credentials > API key**.
   
8. Enter a name for the API key.
   
9. Use the **Select API restrictions** drop-down menu to select `YouTube Data API v3`. This restriction allows the key to call only the YouTube Data API v3.
   
10. Click **OK**.
    
11. Optional. Select the **Authenticate API calls through a service account** checkbox to bind the key to a service account.
    
12. Optional. Select an application type to restrict where you can use the key.
    
13. Click **Create**.
    
14. Copy and save the API key for use in Workato.
    

#### Connect to YouTube with API key authentication

Complete the following steps to set up an API key connection to YouTube in Workato:

1. Click **Create > Connection**.
   
2. Search for `YouTube` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![YouTube API key connection setup](/assets/youtube-api-key-connection.BKtrv_au.png)_YouTube API key connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authorization type** drop-down menu to select **API key**.
   
6. Enter the **API key**. Refer to [YouTube setup for API key authentication](#api-key-setup) for more information.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   

### OAuth 2.0 authentication

Use OAuth 2.0 authentication to manage data in your own YouTube channel, such as replying to comments, updating video metadata, and managing playlists.

#### Default scopes

You can customize the OAuth scope that Workato requests in the **Scopes** field. Workato requests `read-only` access by default. The following scopes are available:

- `Read-only access (search, comments)`
- `Force SSL (secure access)`
- `YouTube Analytics reports`
- `YouTube Analytics monetary reports`
- `Manage YouTube account`
- `YouTube Partner access`

#### YouTube setup for OAuth 2.0 authentication

Complete the following steps to set up YouTube for OAuth 2.0 authentication:

> **PREREQUISITES**
> 
> You must have a project in the Google Cloud Console. Refer to the Google [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project) guide for more information.

1. Sign in to your [Google Cloud Console](https://console.cloud.google.com/).
   
2. Use the project drop-down menu next to the Google Cloud logo to select the project for which you plan to create credentials.
   
3. Go to **Google Auth platform > Clients**.
   
4. Click **Create Client**.
   
5. Use the **Application type** drop-down menu to select **Web application**.
   
6. Enter a name for the OAuth 2.0 client. Google Cloud Console only displays this name internally.
   
7. Click **\+ Add URI** under **Authorized redirect URIs**.
   
8. Enter `https://www.workato.com/oauth/callback` as the authorized redirect URI.\`
   
9. Click **Create**.
   
10. Copy and save the **Client ID** and **Client secret** for use in Workato.
    
    > **SAVE YOUR SECRET**
    > 
    > Google only displays the client secret once. You must create a new one if you lose the client secret.
    

#### Create a custom OAuth profile

You must create a custom OAuth profile with your client ID and secret before you can connect. Complete the following steps to create a custom OAuth profile for your YouTube connection:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Search for `YouTube` and select it as your app.
   
4. Provide a **Name** for this account.
   
5. Click **Create new app**.
   
6. Create a new OAuth app in your Google Cloud Console account.
   
7. Enter the **Client ID** and **Client secret** in Workato. Refer to [YouTube setup for OAuth 2.0 authentication](#oauth2-setup) for more information.
   
8. Click **Save**.
   
9. Click **Done**.
   

#### Connect to YouTube with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to YouTube in Workato:

1. Click **Create > Connection**.
   
2. Search for `YouTube` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![YouTube OAuth 2.0 connection setup](/assets/youtube-connection.Bp_Re1i_.png)_YouTube OAuth 2.0 connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authorization type** drop-down menu to select **OAuth 2.0**.
   
6. Optional. Expand the **Advanced settings** section to configure **Scopes** for your connection. Defaults to `read-only` if left empty.
   
7. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile](#create-a-custom-oauth-profile) for more information.
   
8. Click **Connect**.
   
9. Select a Google account if prompted.
   
10. Click **Allow** to grant Workato access to your Google account.

---
