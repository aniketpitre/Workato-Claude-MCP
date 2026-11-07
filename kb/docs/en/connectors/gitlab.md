---
url: 'https://docs.workato.com/en/connectors/gitlab.md'
description: >-
  The GitLab connector lets you automate tools and features to manage Git
  repositories.
---

# GitLab

[GitLab](https://about.gitlab.com/) is an open-source platform built around Git. It provides a comprehensive set of tools and features to manage Git repositories, project planning, continuous integration/continuous deployment (CI/CD), code review, issue tracking, and more.

## API version

The GitLab connector uses the [GitLab REST API](https://docs.gitlab.com/api/rest/).

## Install GitLab from the community library

Complete the following steps to install the GitLab connector from the [community library](https://www.workato.com/browse/connectors):

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

The GitLab connector supports the following authentication types:

- [Personal access token](#pat)
- [OAuth 2.0](#oauth2)
- [Password grant](#password-grant)

### Minimum scopes

You must add the following minimum scopes to connect to GitLab:

- `api`
- `read_api`
- `create_runner`
- `manage_runner`
- `read_repository`
- `read_user`
- `write_repository`
- `read_registry`
- `write_registry`

### Personal access token authentication

You must create a personal access token in GitLab to use this authentication method.

#### GitLab setup for personal access token authentication

Complete the following steps to set up GitLab for personal access token authentication:

1. Select your avatar.
   
2. Click **Edit profile**.
   
3. Click **Access > Personal access tokens** in the sidebar.
   
4. Use the **Generate token** drop-down menu to select **Legacy token**.
   
5. Enter a **Token name**.
   
6. Optional. Enter a **Token description**.
   
7. Enter an **Expiration date** for the token, or leave this field blank to use the default of 365 days from today (the maximum).
   
8. Select the personal access token scopes. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
9. Click **Generate token**.
   
10. Copy and save the **personal access token** for use in Workato.
    
    > **SAVE YOUR TOKEN**
    > 
    > You can't view it again after you leave or refresh the page. If you lose the token, you must generate a new one.
    

#### Connect to GitLab with personal access token authentication

Complete the following steps to set up a personal access token connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab personal access token connection](/assets/gitlab-pat-connection.kVTQpRZC.png)_GitLab personal access token connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **Personal access token**.
   
7. Enter the **Personal access token**. Refer to [GitLab setup for personal access token authentication](#pat-setup) for more information.
   
8. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
9. Click **Connect**.
   

### OAuth 2.0 authentication

You must generate credentials in GitLab to use this authentication method.

#### GitLab setup for OAuth 2.0 authentication

Complete the following steps to set up GitLab for OAuth 2.0 authentication:

1. Select your avatar.
   
2. Click **Edit profile**.
   
3. Click **Access > Applications** in the sidebar.
   
4. Click **Add new application**.
   
5. Enter a **Name** for the new application.
   
6. Enter `https://www.workato.com/oauth/callback` for the **Redirect URI**.
   
7. Select the **Scopes** required for your application. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
8. Click **Save application**.
   
9. Copy and save the **Application ID** and **Secret** for use in Workato.
   
   > **SAVE YOUR SECRET**
   > 
   > You can't view it again after you leave or refresh the page. If you lose the secret, you must generate a new one.
   

#### Connect to GitLab with OAuth 2.0 authentication

Complete the following steps to set up an OAuth 2.0 connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab OAuth 2.0 connection](/assets/gitlab-oauth2-connection.B4EVGr8U.png)_GitLab OAuth 2.0 connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **OAuth 2.0 (Client ID & Secret)**.
   
7. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
8. Enter the **Application ID** and **Client secret**. Refer to [GitLab setup for OAuth 2.0 authentication](#oauth2-setup) for more information.
   
9. Select the **Scopes**. Refer to [Minimum scopes](#minimum-scopes) for more information.
   
10. Click **Connect**.
    
11. Click **Authorize `<your app name>`** to authorize the connection.
    

### Password grant authentication

Use your GitLab account username and password for this authentication method.

#### Connect to GitLab with password grant authentication

Complete the following steps to set up a password grant connection to GitLab in Workato:

1. Click **Create > Connection**.
   
2. Search for `GitLab` and select it as your app.
   
3. Enter a name for the connection in the **Connection name** field.
   
   ![GitLab password grant connection](/assets/gitlab-password-grant-connection.B_EovV0-.png)_GitLab password grant connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down menu to select the connection type.
   
6. Use the **Authentication type** drop-down menu to select **Password grant**.
   
7. Enter the **Username** and **Password**.
   
8. Enter the **Domain**. This is your GitLab instance URL. For example, `gitlab.example.com`.
   
9. Click **Connect**.

---
