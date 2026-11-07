---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/post-meeting-actions-mcp-server.md
description: >-
  Use the Post Meeting Actions MCP server to connect your LLM to Salesforce,
  Gong, Zoom, Gmail, and Outlook to process a completed sales call end-to-end,
  from transcript retrieval to a confirmed Salesforce update and follow-up
  email.
---

# Post Meeting Actions MCP server

The Post Meeting Actions MCP server enables LLMs to interact with Salesforce, Gong, Zoom, Gmail, and Outlook for processing a completed sales call end-to-end through natural conversation. It provides tools to retrieve the Salesforce record and call transcript, generate a summary in your configured sales methodology, and write it to Salesforce, with resource lookup and a follow-up email available on request. Each deployment implements only the tools for its configured transcript source and configured email platform.

## Uses

Use the Post Meeting Actions MCP server to perform the following actions:

- Process a completed sales call end-to-end: Find the Salesforce record, retrieve the call transcript, generate a summary, and write it to Salesforce
- Find the Salesforce Opportunity related to a call or meeting
- Retrieve a call transcript from Gong or Zoom
- Search within a call's transcript for a specific mention or topic without regenerating the whole summary
- Generate a call summary structured to your org's configured sales methodology
- Check which sales methodology and Salesforce fields this deployment is configured to write to
- Write a summary to Salesforce as Opportunity fields and a Task
- Retrieve relevant customer stories or product resources to support a follow-up
- Draft and send a follow-up email to a prospect through Gmail or Outlook
- Check which of your calls have outstanding summarization, writing, or follow-up steps

### Example prompts

Use the following example prompts to invoke Post Meeting Actions MCP server tools:

- `Process my call with Acme.`
- `Update Salesforce based on my latest call with Acme.`
- `Find my last call with Acme.`
- `Search my call with Acme for any mention of budget.`
- `Format my call notes using our sales methodology.`
- `What competitors were mentioned in my call with Acme?`
- `Draft a follow-up email for my call with Acme, including relevant case studies.`
- `Send the follow-up email once I approve it.`
- `Pull my calls with pending follow-up actions.`
- `What have I not finished processing yet?`

## Post Meeting Actions MCP server tools

The Post Meeting Actions MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [find\_target\_record](#find-target-record-tool) | Finds the Salesforce Opportunity related to a meeting. |
| [search\_call\_activities](#search-call-activities-tool) | Finds Salesforce activity history for logged calls or meetings for a specific account and a date range. |
| [retrieve\_call\_transcript\_gong](#retrieve-call-transcript-gong-tool) | Retrieves transcript and metadata for a Gong-sourced call. |
| [retrieve\_call\_transcript\_zoom](#retrieve-call-transcript-zoom-tool) | Retrieves transcript and metadata for a Zoom-sourced call. |
| [generate\_meeting\_summary](#generate-meeting-summary-tool) | Produces a summary mapped to the configured sales methodology. |
| [get\_salesforce\_write\_policy](#get-salesforce-write-policy-tool) | Returns the configured sales methodology and the Salesforce fields allowed for post-meeting writes. |
| [write\_summary\_to\_system\_of\_record](#write-summary-to-system-of-record-tool) | Writes the confirmed summary to Salesforce as Opportunity fields and a Task, with an optional linked Note. |
| [retrieve\_kb\_resources](#retrieve-kb-resources-tool) | Retrieves supporting customer stories or product resources. |
| [search\_transcript\_chunks](#search-transcript-chunks-tool) | Retrieves chunked transcript documents for a call, or runs a semantic search across transcript chunks. |
| [draft\_followup\_email\_gmail](#draft-followup-email-gmail-tool) | Drafts a follow-up email to a prospect through Gmail, optionally with supporting resources. |
| [draft\_followup\_email\_outlook](#draft-followup-email-outlook-tool) | Drafts a follow-up email to a prospect through Outlook, optionally with supporting resources. |
| [send\_followup\_email\_gmail](#send-followup-email-gmail-tool) | Sends an approved follow-up email through Gmail. |
| [send\_followup\_email\_outlook](#send-followup-email-outlook-tool) | Sends an approved follow-up email through Outlook. |
| [list\_pending\_meetings](#list-pending-meetings-tool) | Lists meetings this server has started processing but hasn't finished. |

## Install the Post Meeting Actions MCP server

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
    

## Post Meeting Actions connection setup

Configure the following connections to set up the Post Meeting Actions MCP server:

- [Salesforce](#salesforce-connection): Required.
- [Gong](#gong-connection): Optional. Connect to Gong to retrieve Gong-sourced call transcripts.
- [Zoom](#zoom-connection): Optional. Connect to Zoom to retrieve Zoom-sourced call transcripts.
- [Gmail](#gmail-connection): Optional. Connect to Gmail to draft and send follow-up emails through Gmail.
- [Outlook](#outlook-connection): Optional. Connect to Outlook to draft and send follow-up emails through Outlook.

### Post Meeting Actions role requirements

Each tool's availability depends on the permissions granted to its connected account:

- **[Salesforce](#salesforce-connection)**: Requires write access to the `Task` object and to each field listed in `salesforce_fields_allowed_to_update`, and create access to `ContentVersion` when `write_content_note` is enabled. A missing permission returns a `permission_denied` outcome rather than a partial result.
- **[Gong](#gong-connection)**: Requires access to basic call metadata and the transcript body. A connection missing the transcript scope still returns call metadata and Gong's own summary.
- **[Zoom](#zoom-connection)**: Requires access to transcripts and AI-generated meeting summaries. A connection missing the summary scope still returns the transcript.
- **[Gmail](#gmail-connection) and [Outlook](#outlook-connection)**: Requires access to draft and send email on behalf of the connected mailbox.

#### Salesforce connection setup steps

View Salesforce connection setup steps

Workato supports OAuth 2.0 authentication and JWT bearer authentication connections for Salesforce.

##### Salesforce OAuth 2.0 authentication

View OAuth 2.0 authentication steps

#### Connect to Salesforce using OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 (Authorization Code Grant) connection to Salesforce in Workato:

> **OAUTH RESTRICTIONS**
> 
> As of early September 2025, Salesforce restricts the use of uninstalled Salesforce Connected Apps. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for required actions if you encounter errors when you create a new connection. These steps are required for all new Salesforce connections starting **September 17, 2025**.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce connection setup](/assets/connect.CnntY3nd.png)_OAuth2.0 Salesforce connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Optional. Expand **Advanced settings** to configure the following options:
   
   Advanced settings
   
   - **Organization/community custom domain URL**: Enter the URL to your Salesforce community's custom domain. Required for community connections with unique domains.
   - **Requested permissions**: Select [permissions](https://help.salesforce.com/articleView?id=remoteaccess_oauth_scopes.htm&type=5) to request for this connection. Refer to [Requested scopes](/en/connectors/salesforce#oauth2-scopes) for the scopes Workato requests.
   - **Verified user access configuration**: Configure custom auth for personal connections. Refer to [Runtime user connections](/en/features/runtime-user-connections) for more information.
   
   > **REFRESH TOKEN SCOPE IS REQUIRED**
   > 
   > The **Perform requests at any time (`refresh_token`, `offline_access`)** scope is one of the scopes Workato requests for OAuth 2.0 connections, but whether Salesforce actually grants this scope depends on the Connected App's own OAuth policies, not on the Workato connection's settings. Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) if your connection later disconnects when the access token expires. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.
   
8. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
   
9. Click **Connect**.
   
10. Optional. If your Salesforce organization or community uses a custom domain, complete the following in the sign-in modal:
    
    - Click **Use Custom Domain**.
    - Enter your **Custom domain**, then click **Continue**.
    
    ![Salesforce custom domains](/assets/connection-custom-domain.D3hJN8X8.png)_Enter your Custom domain._
    
11. Enter your Salesforce **Username** and **Password**.
    
    ![Salesforce connection setup](/assets/login.CIu5oc0P.png)_Log in to your Salesforce account_
    
12. Click **Log In** to complete the setup.
    
    > **OAUTH\_APPROVAL\_ERROR\_GENERIC**
    > 
    > If you see this error, Salesforce is restricting the Workato app because it isn't installed. A Salesforce admin must install the app in **Connected Apps OAuth Usage** or assign the Salesforce permissions. Refer to [OAuth restrictions](/en/connectors/salesforce#oauth-restrictions) for details.
    

##### Salesforce JWT bearer authentication

View JWT bearer authentication steps

> **ACTIONS ON BEHALF OF USER**
> 
> JWT connections can perform actions on behalf of a user you specify using the **On-behalf-of-user email** field. Contact your Workato Customer Success Manager to enable this feature.

#### How it works

JWT bearer authentication connects using a digital certificate that signs a JWT request. Workato sends a JWT to the Salesforce OAuth token endpoint, where Salesforce processes the JWT and issues an access token based on prior approval of Workato in Salesforce.

Although JWT bearer skips interactive sign-in, Salesforce still evaluates every request against the permissions of the user specified in the connection and attributes any changes to that user. Use a dedicated integration user rather than a personal account.

Refer to [Required roles and permissions](/en/connectors/salesforce#roles-and-permissions-required-to-connect) for the Salesforce permissions the connected user needs.

#### Generate a private key and certificate

JWT bearer authentication requires a private key and a certificate. The following command generates both using OpenSSL. Replace the `-subj` values with your own:

```bash
openssl req -x509 -sha256 -nodes -newkey rsa:2048 \
  -keyout server.key \
  -out server.crt \
  -days 365 \
  -subj "/CN=Your App Name/O=Your Organization/C=US"
```

This generates two files:

| File | Description |
| --- | --- |
| `server.key` | Your private key for Workato. Keep this secret. |
| `server.crt` | Your public certificate for Salesforce. |

Refer to Salesforce's documentation for more information:

- [OAuth 2.0 JWT Bearer Flow for Server-to-Server Integration](https://help.salesforce.com/s/articleView?id=xcloud.remoteaccess_oauth_jwt_flow.htm&language=en_US&type=5): Details on how Salesforce uses this certificate to sign and validate JWTs.
- [Create a Private Key and Self-Signed Digital Certificate](https://developer.salesforce.com/docs/atlas.en-us.sfdx_dev.meta/sfdx_dev/sfdx_dev_auth_key_and_cert.htm): Other ways to generate a private key and certificate.

#### Create an external client app for JWT bearer

JWT bearer authentication also requires a registered external client app in Salesforce. Complete the following steps before creating your connection in Workato. Refer to Salesforce's [Create an External Client App](https://help.salesforce.com/s/articleView?id=xcloud.create_a_local_external_client_app.htm&language=en_US&type=5) documentation for more information.

1. Sign in to Salesforce.
   
2. Go to **Setup > Apps > External Client Apps > External Client App Manager**.
   
3. Click **New External Client App**.
   
4. Enter a name in the **External Client App Name** field, such as `Workato`.
   
5. Enter a name in the **API Name** field that meets the following requirements:
   
   - Contains only underscores and alphanumeric characters.
   - Is unique.
   - Starts with a letter.
   - Doesn't include spaces.
   - Doesn't end with an underscore.
   - Doesn't contain consecutive underscores.
6. Enter the contact email address for your app in the **Contact Email** field.
   
7. Use the **Distribution State** drop-down menu to select either **Local** or **Packaged**.
   
8. Expand **API (Enable OAuth Settings)** and select the **Enable OAuth** checkbox. Refer to Salesforce's [Configure the External Client App OAuth Settings](https://help.salesforce.com/s/articleView?id=xcloud.configure_external_client_app_oauth_settings.htm&language=en_US&type=5) documentation for more information.
   
9. Enter `https://www.workato.com/oauth/callback` in the **Callback URL** field.
   
10. Select your OAuth scopes in the **OAuth Scopes** field based on the actions and triggers you plan to use, then click the **Move selection to Selected OAuth Scopes** arrow to apply them.
    
    ![Configure scopes for your external client app](/assets/oauth-scopes.B-mGtuor.png)_Configure scopes for your external client app_
    
    > **REFRESH\_TOKEN SCOPE IS REQUIRED**
    > 
    > If you see the error `refresh_token scope is required and the connected app should be installed and preauthorized`, add **Perform requests at any time (refresh\_token, offline\_access)** to your OAuth scopes. If you then see an invalid session error, also add **Manage user data via APIs (api)**.
    
11. Select **Enable JWT Bearer Flow** in the **Flow Enablement** section. Refer to Salesforce's [Configure a JWT Bearer Flow](https://help.salesforce.com/s/articleView?id=xcloud.configure_oauth_jwt_flow_external_client_apps.htm&language=en_US&type=5) documentation for more information.
    
12. Upload `server.crt` as the digital certificate.
    
13. Click **Create**.
    
14. Click the **Policies** tab, then click **Edit**.
    
15. Expand the **OAuth Policies** section and set **Permitted Users** to **Admin approved users are pre-authorized**.
    
    > **USER HASN'T APPROVED THIS CONSUMER**
    > 
    > If you see this error when connecting, this step was likely missed.
    
16. Locate the **App Policies** section. Add either the [profile](https://help.salesforce.com/s/articleView?id=admin_userprofiles.htm&language=en_US&type=5) or [permission set](https://help.salesforce.com/s/articleView?id=000386289&language=en_US&type=1) assigned to the Salesforce user Workato connects as to the **Select Profiles** or **Select Permission Sets** list. Refer to Salesforce's [Preauthorize User App Access Through External Client App Policies](https://help.salesforce.com/s/articleView?id=xcloud.preauth_user_app_access_through_eca.htm&language=en_US&type=5) documentation for more information.
    
    > **USER IS NOT ADMIN APPROVED TO ACCESS THIS APP**
    > 
    > If you see this error when connecting, this step was likely missed.
    
17. Click **Save**.
    
18. Click the **Settings** tab for your external client app.
    
19. Expand the **OAuth Settings** section.
    
20. Click **Consumer Key and Secret**.
    
21. Verify your identity when prompted.
    
22. Copy the **Consumer Key**. You'll enter this as the **Issuer** when connecting in Workato.
    

#### Connect to Salesforce using JWT bearer

Complete the following steps to connect to Salesforce using JWT bearer authentication:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Salesforce` and select it as your app.
   
3. Enter a name in the **Connection name** field.
   
   ![Salesforce JWT Connection](/assets/salesforce-new-jwt-connection.BCDJGTAT.png)_Configure Salesforce JWT Bearer connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **JWT token**.
   
6. Use the **Sandbox** drop-down menu to specify whether the Salesforce account is a sandbox account.
   
7. Paste the full contents of `server.key` in the **Private key** field, including the `-----BEGIN PRIVATE KEY-----` and `-----END PRIVATE KEY-----` lines.
   
8. Enter the **Consumer Key** from your external client app in the **Issuer** field.
   
9. Enter the **Subject** for the JWT connection. This is the username of the Salesforce user you want Workato to authenticate as, or a valid Experience Cloud username if you're connecting to an Experience Cloud site. You can use principal (`prn`) in place of subject (`sub`) for backward compatibility. If you specify both, Workato uses `prn`.
   
10. Enter your **Salesforce Subdomain**. For example, if your Salesforce URL is `yourInstance.salesforce.com`, the subdomain is `yourInstance`.
    
11. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection. Refer to [Create a custom OAuth profile for Salesforce](/en/connectors/salesforce/custom-oauth) for more information.
    
12. Click **Connect**.
    

#### Gong connection setup steps (optional)

View Gong connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `enabled_sources` to `gong` in the [server configuration](#server-configuration) to retrieve Gong-sourced call transcripts.

The Gong connector uses OAuth 2.0 authentication.

##### Gong minimum and default scopes

Workato requires the `api:users:read` scope. Refer to the [Gong API documentation](https://app.gong.io/settings/api/documentation#overview) for more detailed information about the available scopes.

##### Gong setup

Complete the following steps in Gong to generate credentials:

1. Sign in to your Gong developer instance. Refer to [Request a developer instance](https://help.gong.io/docs/create-an-app-for-gong#request-a-developer-instance) for more information.
   
2. Go to **Admin center**.
   
   ![Admin center](/assets/admin-center.ynD0MeHK.png)_Admin center_
   
3. Click **API** in the **Ecosystem** section.
   
4. Click **CREATE INTEGRATIONS** in the **INTEGRATIONS** tab.
   
5. Complete the **CREATE YOUR GONG INTEGRATION** page, including name, description, and required authorization scopes. Refer to [Submit your integration details to Gong](https://help.gong.io/docs/create-an-app-for-gong?highlight=client%20secret) for more information.
   
   > **SELF-SERVICE (WORKATO FREE, WORKATO PRO, OR DEVELOPER SANDBOX) WORKSPACES**
   > 
   > If you created your workspace as a [Self-service](https://www.workato.com/developers/sandbox) user, use `https://app.trial.workato.com/oauth/callback` as the redirect URI or callback URL when you configure the OAuth integration.
   
6. Click **Save**. Your integration information appears as a new row in the list of integrations.
   
7. Copy and save the **CLIENT ID** and **CLIENT SECRET** for use in Workato.
   

##### Connect to Gong with OAuth 2.0

Complete the following steps to connect to Gong in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Gong.io` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Gong](/assets/connect.B5wWXAjX.png)_Connect to Gong_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Expand the **Advanced settings** section to configure **Scopes** for your connection. Workato requests all available scopes by default. You can select granular scopes from the multi-select list to limit access.
   
6. Enter the **Client ID** and **Client secret**. Refer to [Gong setup](#gong-setup) for more information.
   
7. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
8. Click **Connect**.
   
9. Sign in to Gong using your credentials when prompted.
   
10. Click **Allow** to provision access to Workato.
    

#### Zoom connection setup steps (optional)

View Zoom connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `enabled_sources` to `zoom` in the [server configuration](#server-configuration) to retrieve Zoom-sourced call transcripts.

The Zoom connector uses OAuth 2.0 authentication.

Complete the following steps to connect to Zoom in Workato with OAuth 2.0 authentication:

- [Add an API user](#add-an-api-user)
- [Create a custom OAuth profile](#create-a-custom-oauth-profile)
- [Connect to Zoom with OAuth 2.0 authentication](#connect-to-zoom-with-oauth-2-0-authentication)

> **RECOMMENDED SETUP**
> 
> We recommend that you set up a dedicated API user account in Zoom or create a custom OAuth profile to authorize Workato. This allows you to assign the API user to a role with only the necessary permissions.
> 
> Alternatively, you can use an existing Zoom owner or admin account if it has the required permissions. Some admin accounts may have restricted access based on their configuration.

##### Add an API user

View add an API user steps

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
    

##### Create a custom OAuth profile

View create a custom OAuth profile steps

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
    

##### Connect to Zoom with OAuth 2.0 authentication

View connect to Zoom with OAuth 2.0 authentication steps

Complete the following steps to connect to Zoom in Workato:

1. Click **Create > Connection**.
   
2. Search for `Zoom` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Zoom Connection Setup](/assets/connection-setup-zoom.i8W0drY7.png)_Name your connection_
   
4. Optional. Expand the **Advanced settings** section and use the **OAuth 2.0 scopes** drop-down menu to specify OAuth scopes to request for your connection.
   
5. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile to use for the connection.
   
6. Click **Connect**.
   
7. Sign in to your Zoom account.
   

#### Gmail connection setup steps (optional)

View Gmail connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `enabled_platforms` to `gmail` in the [server configuration](#server-configuration) to draft and send follow-up emails through Gmail.

Workato supports OAuth 2.0 authentication and Service account authentication for Gmail.

##### Gmail minimum and default scopes

The **See your primary Google Account email address** scope is required to establish a connection at a minimum.

Workato requests the following scopes by default if you don't request specific scopes:

- **See your primary Google Account email address**
- **See and edit your email labels**
- **Send email on your behalf**
- **View your email messages and settings**
- **Read, compose, and send emails from your Gmail account**

Ensure your Google Workspace Admin grants [domain-wide authority delegation](https://developers.google.com/cloud-search/docs/guides/delegation#delegate_domain-wide_authority_to_your_service_account) to your service account if you plan to use a service account to connect to Gmail. This allows it to impersonate the user email entered during connection setup, with the necessary scopes and permissions.

##### Gmail OAuth 2.0 authentication

View OAuth 2.0 authentication steps

Complete the following steps to set up an OAuth 2.0 connection:

1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
   
2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
   
3. Provide a **Connection name** that uniquely identifies the Gmail connection instance.
   
4. Click the **Authentication type** menu and select **OAuth 2.0**.
   
5. Optional. Click **Advanced settings** and select additional **OAuth 2.0 scopes**. If left blank, the following scopes are requested:
   
   - **See your primary Google Account email address**
   - **See and edit your email labels**
   - **Send email on your behalf**
   - **View your email messages and settings**
   - **Read, compose, and send emails from your Gmail account**
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Sign in with Google** and sign in to your Google account to complete the setup.
   

##### Gmail service account authentication

View Service account authentication steps

A Google service account is a specialized Google account associated with a Google Cloud Project (GCP) that can run API requests on your behalf.

Service accounts provide the following benefits:

- **Continuous operation:** Service accounts ensure that operations continue even if individual user permissions change.
- **Dedicated permissions:** Service accounts can only access projects that you share with them.
- **Dedicated API quotas:** You can manage a service account's API quotas through GCP and request quota increases directly from Google.

Refer to the [Google service account documentation](https://cloud.google.com/iam/docs/understanding-service-accounts) to learn more about service accounts.

![Getting GCP Project service account email](/assets/service-auth-email.BdQybqOr.png)_Obtain a GCP Project service account email_

###### Set up a Google service account

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
   

##### Connect to a Gmail service account in Workato

View Connect to a service account in Workato steps

Complete the following steps to set up a service account connection:

1. Sign in to your Workato account and navigate to the project where you plan to add your Gmail connection.
   
2. Click **Create > Connection** (or press C twice), then select **Gmail** as your connection.
   
3. Select the **Authentication type** drop-down menu.
   
4. Click **Sign in with Google** and sign in to your Google account to complete the setup.
   

#### Outlook connection setup steps (optional)

View Outlook connection setup steps

> **REQUIRED CONFIGURATION**
> 
> Set `enabled_platforms` to `outlook` in the [server configuration](#server-configuration) to draft and send follow-up emails through Outlook.

The Outlook connector supports the following authentication types:

- [Authorization code grant authentication (OAuth 2.0)](#outlook-authentication-auth-code)
- [Client credentials-based authentication (OAuth 2.0)](#outlook-authentication-client-credentials): _Only available for tenant-specific connections_

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

##### Authorization code grant authentication (OAuth 2.0)

View authorization code grant authentication steps

This authentication method requires the following value for tenant-specific account types:

- Tenant ID/Domain

###### Outlook minimum and default scopes (authorization code grant)

View minimum and default scopes

The Salesforce, Gong, Zoom, Gmail, and Outlook connector requests the following scopes for authorization code grant connections by default. These scopes are necessary to use all of the connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Delegated** permissions in the Azure portal.

- `Mail.Send`
- `Mail.ReadWrite`
- `Mail.ReadWrite.Shared`
- `Calendars.ReadWrite`
- `Calendars.ReadWrite.Shared`
- `User.Read`
- `offline_access`

The following minimum scopes are required to establish a connection to Salesforce, Gong, Zoom, Gmail, and Outlook using authorization code grant authentication:

- `User.Read`
- `offline_access`

###### Outlook setup for authorization code grant authentication

Complete the following steps to set up Outlook for authorization code grant authentication:

- [Register the Workato App in Azure portal](#outlook-auth-register)
- [Assign permissions to your app](#outlook-assign-permissions)
- [Obtain the Directory (tenant) ID from the Azure portal](#outlook-obtain-directory-id)

###### Register the Workato app in the Azure portal

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
   

###### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

###### Obtain the Directory (tenant) ID from the Azure portal

View obtain the Directory (tenant) ID from the Azure portal steps

This step is required if you plan to use a tenant-specific account. You can skip this step if you plan to use a common, consumer, or organization account type for your connection.

Complete the following steps to obtain the Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the `Directory (tenant) ID` for use in Workato.
   

###### Connect to Outlook with authorization code grant authentication

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
   

##### Client credentials-based authentication (OAuth 2.0)

View client credentials-based authentication steps

###### Outlook minimum and default scopes (client credentials)

View minimum and default scopes

We recommend the following scopes for client credentials connections. These scopes are necessary to use all of this connector's triggers and actions. Additionally, you must assign these permissions to the Workato app as **Application** permissions in the Azure portal.

- `Calendars.Read`
- `Calendars.ReadWrite`
- `Contacts.Read`
- `Contacts.ReadWrite`
- `Mail.Read`
- `Mail.ReadWrite`
- `Mail.Send`

The following minimum scopes are required to establish a connection to Salesforce, Gong, Zoom, Gmail, and Outlook with client credentials-based authentication:

- `Mail.Read`

###### Outlook setup for client credentials-based authentication

Complete the following steps to set up Outlook for client credentials-based authentication:

- [Register the Workato app in the Azure portal](#outlook-client-credentials-register)
- [Assign permissions to your app](#outlook-assign-permissions-client-credentials)
- [Generate a client secret](#outlook-generate-client-secret)
- [Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal](#outlook-obtain-ids)
- [Obtain the User ID from the Azure portal](#outlook-obtain-user-id)

> **COMPATIBLE AUTHENTICATION**
> 
> Client credentials-based authentication is only compatible with tenant-specific connections.

###### Register the Workato app in the Azure portal

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
   

###### Assign permissions to your app

View assign permissions to your app steps

Complete the following steps to assign permissions to your app:

1. Go to your newly registered app and select **Manage > API permissions**.
   
2. Click **\+ Add a permission** and select **Microsoft Graph**.
   
3. Add the required permissions as outlined in [Minimum and default scopes](/en/connectors/outlook/outlook#authorization-code-grant-scopes). Depending on your connection type, you must assign **Application** or **Delegated** permissions.
   
   ![Add permissions](/assets/app-permissions.Cbe76A6a.png)_Add permissions_
   
4. Click **Add permissions**.
   
   Admin consent is required for specific permissions. Refer to [Connect Microsoft Entra ID to the Outlook connector](/en/connectors/outlook/outlook#admin-consent) to learn more.
   

###### Generate a client secret

View generate a client secret steps

Complete the following steps to generate a client secret:

1. Go to **Manage > Certificates & Secrets > Client secrets**.
   
2. Click **\+ New client secret**.
   
3. Provide a **Description** for the client secret and specify an **Expires** date.
   
4. Click **Add**.
   
5. Copy and save the client secret **Value**—not the **Secret ID**—for use in Workato.
   
   ![Copy and save the client secret value](/assets/sharepoint-troubleshoot.DPBGyl4B.png)_Copy and save the client secret value_
   

###### Obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal

View obtain the Application (client) ID, Object ID, and Directory (tenant) ID from the Azure portal steps

Complete the following steps to obtain the Application ID, Object ID, and Directory (tenant) ID from the Azure portal:

1. Go to the **Overview > Essentials** section.
   
   ![App details](/assets/app-details.Qi8HIQ2x.png)_App details_
   
2. Copy and save the **Application (client) ID**, **Object ID**, and **Directory (tenant) ID** for use in Workato.
   

###### Obtain the User ID from the Azure portal

View obtain the User ID from the Azure portal steps

Complete the following steps to obtain the User ID from the Azure portal:

1. Go to **Home > Users** to obtain the `User ID`.
   
   ![Users](/assets/users.CuDgSGeL.png)_Select users_
   
2. Search for and select the default user you plan to use to perform operations. This user doesn't establish the connection but is required for performing certain operations that an app can't perform. It's also required in picklists to pull user data. For example, the folder picklist populates folders belonging to the default user.
   
3. Copy and save the **User principal name**. Use this value as the **User ID** in Workato.
   

###### Connect to Outlook with client credentials-based authentication

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
   

### Server configuration

Edit the **Server Configuration** recipe function in the project folder to control this deployment's enabled integrations, Salesforce write permissions, and operational limits:

| Key | Description |
| --- | --- |
| `enabled_sources` | Choose the transcript source this deployment retrieves calls from: `gong` or `zoom`. A deployment can't enable both. |
| `enabled_platforms` | Choose the follow-up email platform this deployment sends through: `gmail` or `outlook`. A deployment can't enable both. |
| `methodology_label` | Enter a human-readable label for your organization's sales methodology, such as `MEDDIC/MEDDPICC` or `Value Selling`, used for documentation and LLM phrasing. |
| `write_content_note` | Configure whether to create a linked content note when the server writes a Salesforce summary. |
| `salesforce_fields_allowed_to_update` | Enter the allowlist of Salesforce `Object.FieldApiName` pairs `write_summary_to_system_of_record` is permitted to write, for example `Opportunity.NextStep`, `Opportunity.Description`, and `Task.Subject`. The LLM must use these exact field names. |
| `max_schedule_days_out` | Enter the bound on how far ahead you can schedule an action. Defaults to `14`. |
| `max_transcript_chars` | Enter the maximum number of transcript characters processed in each call. Defaults to `200,000`. |
| `max_activity_lookback_days` | Enter the maximum number of days `search_call_activities` looks back. Defaults to `90`. |
| `data_retention_days` | Enter the number of days to retain Workflow State and Audit Log records before a scheduled cleanup job deletes them. Defaults to `60`. |

View server configuration steps

Complete the following steps to configure the Post Meeting Actions MCP server:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Server Configuration** recipe.
   
4. Edit the value in the step for the setting you plan to change. For example, increase `max_transcript_chars` from `200,000` to `300,000`.
   
5. Save and start the recipe for the new value to take effect.
   

## How to use Post Meeting Actions MCP server tools

Refer to the following sections for detailed information on available tools.

> **TOOL CONFIGURATION**
> 
> A deployed MCP server only exposes the tools for its `enabled_sources` and `enabled_platforms` [server configuration](#server-configuration) values. For example, a deployment configured with `gong` and `gmail` exposes `retrieve_call_transcript_gong` and the Gmail follow-up tools, not the Zoom or Outlook variants.

### find\_target\_record tool

The **find\_target\_record** tool finds the Salesforce Opportunity related to a meeting. Your LLM uses this tool to match a company or account name to a specific Opportunity. The tool uses `search_call_activities` or a transcript tool to find the company if you don't name it directly.

**Try asking**:

- `What's the Opportunity for my call with Acme?`
- `Which account does this call belong to?`
- `Find the record for my call with Acme.`

### search\_call\_activities tool

The **search\_call\_activities** tool finds Salesforce activity history for logged calls or meetings tied to an account within a date range. Your LLM uses this tool to find calls you reference.

**Try asking**:

- `Find my last call with Acme.`
- `Show me my calls with Acme last month.`
- `What calls do I have logged with Acme in the past 30 days?`
- `Find the most recent call logged against this Opportunity.`

### retrieve\_call\_transcript\_gong tool

The **retrieve\_call\_transcript\_gong** tool retrieves transcript and metadata for a Gong-sourced call by its ID. Your LLM uses this tool to retrieve a transcript after `search_call_activities` identifies a specific call. The tool resumes any prior progress on the call instead of starting over.

**Try asking**:

- `Pull the transcript from my Gong call with Acme.`
- `Get the Gong recording for this call.`
- `Summarize what was said on my last Gong call with Acme.`

### retrieve\_call\_transcript\_zoom tool

The **retrieve\_call\_transcript\_zoom** tool retrieves transcript and metadata for a Zoom-sourced call. Your LLM uses this tool to retrieve a transcript after `search_call_activities` identifies a specific call.

**Try asking**:

- `Pull the transcript from my Zoom call with Acme.`
- `Get the Zoom recording summary for this meeting.`
- `What was discussed on my Zoom call with Acme?`

### generate\_meeting\_summary tool

The **generate\_meeting\_summary** tool produces a summary mapped to the configured sales methodology. Your LLM uses this tool to generate a summary after retrieving a transcript, and only passes a different methodology if you explicitly ask for one.

**Try asking**:

- `Format my call notes using our sales methodology.`
- `Summarize this call using MEDDIC/MEDDPICC.`
- `What competitors were mentioned in my call with Acme?`
- `Regenerate the summary for this call.`

### get\_salesforce\_write\_policy tool

The **get\_salesforce\_write\_policy** tool returns the configured sales methodology and the Salesforce fields allowed for post-meeting writes. Your LLM uses this tool to confirm the configured methodology and fields before generating or writing a summary.

**Try asking**:

- `What sales methodology is this deployment using?`
- `Which Salesforce fields can this write to?`
- `Show me the write policy for this deployment.`

### write\_summary\_to\_system\_of\_record tool

The **write\_summary\_to\_system\_of\_record** tool writes a summary to Salesforce as Opportunity fields and a Task, with an optional linked Note. Your LLM uses this tool to commit a summary after showing you a preview and receiving your confirmation.

**Try asking**:

- `Update Salesforce based on my call with Acme.`
- `Change the next step to "Schedule an executive sponsor call" before you save it.`
- `Show me what will be written before you save it.`
- `Go ahead and save this summary to Salesforce.`

### retrieve\_kb\_resources tool

The **retrieve\_kb\_resources** tool retrieves supporting customer stories or product resources. Your LLM uses this tool to pull in supporting resources when you ask for a resourced follow-up. This doesn't retrieve a full call transcript.

**Try asking**:

- `Find relevant case studies for this call.`
- `Pull product resources related to this summary.`
- `What customer stories match the objections raised in this call?`

### search\_transcript\_chunks tool

The **search\_transcript\_chunks** tool retrieves chunked transcript documents for a call, or runs a semantic search across transcript chunks. Your LLM uses this tool to find a specific mention or topic within a call without regenerating the whole summary.

**Try asking**:

- `Search my call with Acme for any mention of budget.`
- `Find where the customer talked about renewal timing in this call.`
- `Pull the transcript chunks that mention our top competitor.`

### draft\_followup\_email\_gmail tool

The **draft\_followup\_email\_gmail** tool drafts a follow-up email to a prospect through Gmail, optionally with supporting resources. Your LLM uses this tool to draft an email and show you the draft for approval before calling the matching send tool.

**Try asking**:

- `Draft a follow-up email for my call with Acme.`
- `Draft a follow-up in Gmail including relevant case studies.`
- `Write a follow-up email to dana@example.com about this call.`
- `Redraft the follow-up email in a more formal tone.`

### draft\_followup\_email\_outlook tool

The **draft\_followup\_email\_outlook** tool drafts a follow-up email to a prospect through Outlook, optionally with supporting resources. Your LLM uses this tool to draft an email and show you the draft for approval before calling the matching send tool.

**Try asking**:

- `Draft a follow-up email for my call with Acme in Outlook.`
- `Write an Outlook follow-up including the case studies you found.`
- `Draft a follow-up to dana@example.com about this call.`
- `Redraft the Outlook follow-up in a more formal tone.`

### send\_followup\_email\_gmail tool

The **send\_followup\_email\_gmail** tool sends an approved follow-up email through Gmail. Your LLM uses this tool to send an email you approved. Sends are immediate. This tool doesn't support scheduling.

**Try asking**:

- `Send the follow-up email.`
- `Go ahead and send the Gmail draft.`
- `Send this email now that I've approved it.`

### send\_followup\_email\_outlook tool

The **send\_followup\_email\_outlook** tool sends an approved follow-up email through Outlook. Your LLM uses this tool to send an email you approved. Sends are immediate. This tool doesn't support scheduling.

**Try asking**:

- `Send the follow-up email.`
- `Go ahead and send the Outlook draft.`
- `Send this email now that I've approved it.`

### list\_pending\_meetings tool

The **list\_pending\_meetings** tool lists meetings being processed by this server. Your LLM uses this tool to surface what you still owe follow-up on, without requiring you to name a specific meeting.

**Try asking**:

- `What calls do I still owe follow-up on?`
- `Show me my pending meetings from the last two weeks.`
- `What have I not finished processing yet?`

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
