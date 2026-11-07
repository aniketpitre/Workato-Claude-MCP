---
url: 'https://docs.workato.com/en/connectors/salesforce.md'
description: >-
  The Salesforce connector lets you automate CRM workflows: create, update,
  search, and delete records, manage files and approvals, and trigger on
  changes.
---

# Salesforce

[Salesforce](https://www.salesforce.com/) is a cloud-based CRM platform for managing leads, contacts, and opportunities across sales, marketing, and customer service teams. It's built on the Force.com platform and extends with a wide range of third-party marketplace apps and other Salesforce products.

Watch a quick video guide

[Video](https://www.youtube.com/embed/yVG3qGbKXwM?rel=0&rel=0)

## Use cases

The Salesforce connector supports multi-app workflows that connect Salesforce to other business apps. For example:

- [Display Salesforce account details](/en/getting-started/use-cases/salesforce-workbot-slack) directly in Slack with Workbot for Slack.
- Set up a [workflow to track leads](/en/getting-started/use-cases/marketo-salesforce-snowflake) by creating a Salesforce task and adding a Snowflake row when new lead activity is detected in Marketo.
- Try a [batch-sync solution](/en/getting-started/use-cases/mysql-salesforce) that transfers data from MySQL to Salesforce.
- Ensure [phone numbers are validated](/en/getting-started/use-cases/salesforce-js-snippets-snowflake-email) before syncing contacts from Salesforce to Snowflake.

Refer to [Recipe use cases](/en/getting-started/use-cases/recipes/recipe-use-cases) for more examples.

## API version

The Salesforce connector uses [Salesforce REST API version 65.0](https://developer.salesforce.com/docs/atlas.en-us.258.0.api_rest.meta/api_rest/intro_what_is_rest_api.htm).

## Supported editions and versions

The Salesforce connector works with all Salesforce editions, for example, **Professional**, **Enterprise**, **Unlimited**, and **Developer**, as well as the following Salesforce products:

- Salesforce Sales Cloud
- Salesforce Service Cloud
- Salesforce Partner Community
  - Provide the community custom domain in **Advanced settings** to sign in.
- Salesforce Consumer Goods Cloud
- Salesforce Marketing Cloud
  - SFMC has a separate connector
- Salesforce Data Cloud
  - Available as a [community connector](https://app.workato.com/custom_adapters/605867/details?community=true) built and supported by Workato

It also works with Force.com applications. Contact your Workato representative for other editions.

## Connection setup

The Salesforce connector supports the following authentication types:

- [OAuth 2.0 (Authorization Code Grant)](#oauth2-0-connection)
  
- [JWT bearer](#jwt-bearer-authentication)
  

Refer to [Required roles and permissions](#roles-and-permissions-required-to-connect) for information about prerequisite permissions.

### OAuth 2.0 (Authorization Code Grant)

Use **OAuth 2.0 (Authorization Code Grant)** to connect to Salesforce by signing in and granting access through Salesforce's authorization flow. This method supports both production and sandbox environments.

#### Requested scopes

Workato requests the following scopes for OAuth 2.0 connections if you select any option in the **Requested permissions** field in **Advanced settings** (including **Minimum permissions**):

- **Manage user data via APIs (`api`)**: Required for the connection to read and write Salesforce data.
- **Access your basic information (`id`, `profile`, `email`, `address`, `phone`)**: Identifies the connected user.
- **Perform requests at any time (`refresh_token`, `offline_access`)**: Allows Workato to renew the access token so you don't need to sign in again.

Workato also requests the scope for each additional permission you select.

Workato doesn't send a scope with the authorization request if you leave **Requested permissions** blank. Salesforce then grants the scopes that your Salesforce app's OAuth policies allow. Ensure the app allows **Manage user data via APIs** and **Perform requests at any time**.

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
    

#### OAuth restrictions

Salesforce enforces restrictions on OAuth **Salesforce Connected Apps** in early September 2025. These restrictions affect only new Salesforce connections created in Workato. Existing connections and recipes continue to run. Refer to [Salesforce's official announcement](https://help.salesforce.com/s/articleView?id=005132365&type=1) for more information.

- **If you already created a Salesforce connection in Workato**: Your organization already displays the `Workato connector` in **Connected Apps OAuth Usage**. Existing connections keep working. If the app displays **Install**, a Salesforce admin must install it and configure OAuth policies to avoid errors when you create new connections. If the app displays **Uninstall**, the app is already installed and no further action is required.
  
- **If this is your first Salesforce connection in Workato**: Your organization doesn't display the `Workato connector` until a Salesforce admin creates a connection in Workato. After that, the app appears in **Connected Apps OAuth Usage**, where the admin can install it.
  

As an alternative, the admin can assign Salesforce permissions that allow OAuth without installation. This option is only recommended for trusted integration users, such as admins or developers. These include the following:

- **Approve Uninstalled Connected Apps**: Allows trusted users to self-authorize uninstalled apps. Available when **API Access Control** isn't enabled.
- **Use Any API Client**: Broader bypass permission that works when **API Access Control** is enabled.

Refer to [Salesforce's documentation](https://help.salesforce.com/s/articleView?id=005132365&type=1) for details.

#### Token expiration

OAuth tokens may expire after a set amount of time, depending on their configuration in Salesforce. A connection that repeatedly shows **Connection lost** and requires reconnecting usually means Salesforce isn't returning a refresh token. A Refresh Token Policy or IP Relaxation setting can cause the same symptom.

Salesforce only issues a refresh token when your Salesforce app's OAuth policies explicitly grant the **Perform requests at any time** scope. **Full access** doesn't include this scope by default. Workato can't renew the expired access token without a refresh token, so the connection disconnects and requires manual reconnection.

Refer to [Salesforce connection disconnects repeatedly](/en/connectors/salesforce/troubleshoot-connection-setup#salesforce-connection-disconnects-repeatedly) to diagnose and resolve this.

### JWT bearer

Use JWT bearer for server-to-server authentication without requiring a user to sign in. Choose this method for automated connections that can't complete an interactive sign-in, such as backend integrations running on a schedule.

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
    

## Required roles and permissions

We recommend provisioning and assigning a dedicated Salesforce integration user. Salesforce connections in Workato inherit the [permissions](https://help.salesforce.com/articleView?id=admin_userperms.htm&language=en_US&type=0) of the account used for authentication, including access to [fields](#field-level-security) and [objects](#standard-and-custom-object-permissions).

User [permissions and access settings](https://help.salesforce.com/s/articleView?id=platform.permissions_about_users_access.htm&type=5) control what users can do in your Salesforce organization:

- **Permissions**: Define the actions a user can take, such as editing object records, accessing the Setup menu, permanently deleting items from the Recycle Bin, or resetting another user’s password.
  
- **Access settings**: Control broader features, such as the visibility of apps, access to Apex classes, and more.
  

You can define user permissions and access settings using [profiles](https://help.salesforce.com/s/articleView?id=platform.admin_userprofiles.htm&type=5) and [permission sets](https://help.salesforce.com/s/articleView?id=platform.perm_sets_overview.htm&type=5). Each user is assigned one profile, but can have multiple permission sets. Use profiles to assign the minimum required permissions for a specific group of users. Then use permission sets to add additional permissions as needed.

### API Enabled permission

You must have the **API Enabled** permission in Salesforce to create a connection. Open Salesforce and go to **Setup > Profiles** to configure this permission. ![API enabled permission - profile setup](/assets/api-enabled-permission.a9B0al-H.png)_API enabled permission - profile setup_

### Standard and custom object permissions

We recommend that the connected user's account has `read`, `create`, `edit`, `delete`, `view all`, and `modify all` permissions for standard and custom objects in your Salesforce organization.

Refer to Salesforce's [Object Permissions](https://help.salesforce.com/articleView?id=sf.users_profiles_object_perms.htm&type=5) for details about the difference between standard object privileges and the `View all` and `Modify all` permissions.

![Salesforce standard object permissions - profile setup](/assets/standard-object-profile-permissions.rcC_D2bx.png)_Salesforce standard object profile permissions setup_

![Salesforce custom object permissions - profile setup](/assets/custom-object-profile-permissions.OC72MsLl.png)_Salesforce custom object profile permissions setup_

Object-level security is the broadest way to control data access. It controls whether a user can view, create, edit, or delete records of a specific object type, such as leads or opportunities, and can hide objects and their tabs from users entirely.

> **MISSING OBJECTS**
> 
> Object-level security settings prevent objects from appearing in Workato. Check with your Salesforce admin to confirm that the integration user can access all required objects.

### Platform event permissions

Platform event triggers and actions require that platform events be enabled in your Salesforce organization. Additionally, the connected Salesforce account must have `read` and `create` permissions for platform events.

![Salesforce platform events permissions - profile setup](/assets/platform-events-permissions.3bNr6-hi.png)_Salesforce platform events permissions - profile setup_

### Real-time trigger permissions

Your Salesforce organization must have Workflow rules set up to use real-time triggers. The connected user doesn't need to be the user who creates these rules.

You need the `Customize Application` permission to create workflow rules. Open Salesforce and go to **Setup > Permission sets** to configure this permission.

![Customize application permission - profile setup](/assets/customize-application-permission.Zx_ANjxr.png)_Customize application permission - profile setup_

> **DEPRECATION NOTICE PERTAINING TO REAL-TIME TRIGGERS**
> 
> Real-time triggers in Workato rely on Salesforce Workflow rules. Existing Workflow rules continue to work, but Salesforce has [deprecated](https://admin.salesforce.com/blog/2021/go-with-the-flow-whats-happening-with-workflow-rules-and-process-builder) Workflow rules and Process Builder in favor of Flows, so Workato recommends using Salesforce Flows for all new recipes. Salesforce provides a [migration tool](https://help.salesforce.com/s/articleView?id=release-notes.rn_automate_flow_mgmt_migrate_to_flow_tool.htm&type=5&release=236) to move Workflow rules into Flows.
> 
> The process shouldn't affect Workato recipes, because outbound messages configured in Salesforce remain the same. Test the migration in a Salesforce sandbox first to catch any unexpected issues.

### Bulk/batch action permissions

Bulk actions require the `Manage Data Integrations`, `View Setup and Configuration`, and `API Enabled` permissions on the connected Salesforce account. Refer to Salesforce's [Manage Bulk Data Load Jobs](https://help.salesforce.com/articleView?id=monitoring_async_api_jobs_overview.htm&type=5) for more information.

### Field-level security

[Field-level security](https://help.salesforce.com/s/articleView?id=platform.users_profiles_field_perms.htm&language=en_US&type=5) controls the visibility of fields in Salesforce, including related lists, list views, reports, and search results, and controls whether users can view or edit individual field values. This lets you protect sensitive data without hiding entire objects.

You can configure field-level security using [permission sets](https://help.salesforce.com/s/articleView?id=platform.perm_sets_overview.htm&language=en_US&type=5) and [profiles](https://help.salesforce.com/s/articleView?id=platform.admin_userprofiles.htm&language=en_US&type=5).

> **MISSING FIELDS**
> 
> Field-level security settings can prevent fields from appearing in Workato. Check with your Salesforce admin to confirm that the integration user can access all required fields.

## Additional considerations

### Multiple Salesforce accounts in a single recipe

You can connect to two Salesforce accounts in a single recipe using the Salesforce Secondary connector. Refer to [Secondary connectors](/en/features/secondary-connectors) for more information.

### Salesforce sandboxes

Use a sandbox account or test with non-essential data when you start using Workato with Salesforce. This prevents data loss, because actions performed through Workato can't be undone.

Salesforce sandboxes are isolated from your production organization, so actions in one don’t affect the other. Sandboxes are nearly identical to your production organization. Refer to Salesforce's [Sandbox Setup Tips and Considerations](https://help.salesforce.com/HTViewHelpDoc?id=data_sandbox_implementation_tips.htm&language=en_US) for a list of differences.

---
