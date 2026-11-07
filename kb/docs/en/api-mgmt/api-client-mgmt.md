---
url: 'https://docs.workato.com/en/api-mgmt/api-client-mgmt.md'
description: >-
  Manage API clients and applications in Workato to group users, authenticate
  requests, control collection access, and set security parameters.
---

# API clients and applications

Clients are logical groups of users, such as members from the same organization, who receive access to one or more API collections. A client can create applications to authenticate requests, manage access to API collections, and define security parameters.

## API clients

Go to **Platform > API platform > Clients** to manage existing clients and add new ones.

![API platform client tab](/assets/api-client-homepage.1SeYCab0.png)_API platform client tab_

### Create a new API client

Complete the following steps to add and configure a new client:

1. Add an API client
   
   1. Go to **Platform > API Platform**.
      
   2. Select the **Clients** tab.
      
   3. Click **\+ Add new client**.
      
      ![Add new client](/assets/add-a-client.CzD77CsN.png)_Add new client_
      
   
2. Set up client details
   
   1. Enter a **Name** for your client. Use a descriptive identifier, such as the client's company or department name.
      
      ![Set up client details](/assets/add-client-details.DQ-ipDux.png)_Set up client details_
      
   2. Enter a **Description** for the client.
      
   3. Upload a **Client logo**. Drag and drop a JPG/PNG image or click **Upload from device** to select a file. This logo visually identifies your client in the portal.
      
   4. Enable the **Grant client access to portal** toggle to enable portal access. This grants your client permission to browse published API collections and manage their API keys. If your client only requires API tokens for testing or internal purposes, you can leave the toggle disabled.
      
   5. Provide the client identity based on your portal's [authentication method](/en/api-mgmt/configure-developer-portal#configure-authentication-settings):
      
      **Workato Identity**
      
      Use the **Client** drop-down menu to select the client. The list only includes end users already added to Workato Identity.
      
      **Magic link**
      
      Enter the client's email address in the **Email** field. Workato sends the client an email with a portal invitation.
      
   6. Click **Next** to proceed to the **Define access configuration** screen, where you can configure your client's API access.
      
   
3. Define access configuration
   
   1. Choose an **Authentication method** for the client. Refer to the [available authentication methods](/en/api-mgmt/access-tokens.html) for more information.
      
   2. Optional. Toggle **Enforce mutual TLS (mTLS)** to require clients to present a valid certificate during the SSL handshake. This enforces two-way authentication. Refer to the [mTLS authentication](/en/api-mgmt/mtls) guide for more information.
      
      > **Note**: This setting appears only if you configure your workspace with a custom domain.
      
   3. Use the **API collections to include** drop-down menu to select one or more API collections. This defines the APIs your client can access and invoke in the portal. You can also create a client without collections to allow discovery before you grant API access.
      
   4. Optional. Assign a **Policy** to control your client’s API usage. Policies define rules such as rate limits or usage quotas.
      
   5. Click **Next**.
      
   

If portal access is enabled, Workato sends an email invitation to the client's email address. Permissions, such as access to API collections and authentication methods, are configured at the client level.

![Create client](/assets/create-successful-client.fOtqdtwy.png)_Create client_

After you add the client, you or the client can [create an application](#create-a-new-application) to authenticate API requests and manage access to assigned collections.

## Applications

The **Applications** tab enables you to create and manage the credentials your consumers use to call your APIs. You can generate a Workato-issued API key, or configure [custom validation](/en/api-mgmt/custom-validation) to accept JWTs issued by the consumer's own identity provider.

> **RENAMED FROM API KEYS**
> 
> The **API keys** tab is now called **Applications**. A client's applications can use more than one credential type, such as an API key or custom validation, not API keys alone.

![Manage applications](/assets/manage-applications.C_6eZlDj.png)_Manage applications_

Applications provide secure authentication. They allow your clients to access their assigned API collections while maintaining strict access controls.

> **APPLICATION LIMIT**
> 
> Each client can have up to 20 applications.

### Create a new application

Complete the following steps to create a new application:

1. Go to **API Platform > Clients**, select the client, and go to the **Applications** tab.
   
2. Click **\+ Create application**.
   
   ![Create application](/assets/create-application.DsD4ZywD.png)_Create application_
   
3. Enter an **Application name** to identify the application.
   
   ![Configure new application](/assets/configure-application.Kw7db-IM.png)_Configure new application_
   
4. Select **API key** under **Credential type**.
   
   > **CUSTOM VALIDATION**
   > 
   > To validate JWT tokens using claim and scope rules instead of a Workato-issued key, select **Custom validation** instead. Custom validation is only available for clients using the JWT or OpenID Connect authentication method. Refer to [Custom validation for API applications](/en/api-mgmt/custom-validation) for the complete configuration procedure.
   
5. Click **Next**.
   
6. Optional. Add **Allowed IPs** to restrict requests to specific IP addresses. To allow multiple IPs, separate them with commas or define a range.
   
   ![Configure IP access rules](/assets/configure-ip-rules.DpX9N8hd.png)_Configure IP access rules_
   
7. Optional. Add **Blocked IPs** to prevent requests from specific IP addresses. Blocked IPs take precedence over allowed IPs. For example, if you add the IP address `123.456.123.456` to your allow list, but also block it, users who attempt to access the portal from this IP address are denied access.
   
8. Click **Create application**. Workato displays the authentication token. Save this token securely, as it doesn't display again. You must refresh or create a new application if you lose it.
   

## Access profiles

Every client has one or more access profiles that are associated with [API collections](/en/api-mgmt/api-collections). An access profile gives a client access to one or more [API recipe collections](/en/api-mgmt/api-collections#create-api-recipe-collection) and/or [API proxy collections](/en/api-mgmt/api-collections#create-api-proxy-collection).

We recommend that API owners create a unique access profile for each API consumer. This allows you as the API owner to delegate access to specific API collections and impose [access policies](/en/api-mgmt/api-access-policies). Furthermore, it allows you to generate usage information about how API consumers are using your API endpoints.

> **API CONSUMERS**
> 
> An API consumer can be a person, script, or automated program.

To view a client's access profiles and create new profiles, navigate to **API platform > Clients** and select a client. The following screenshot contains an example of a client (ACME Company) with one access profile (also called ACME Company).

![API client with access profile](/assets/api-client-creation.KK91lQW0.png)_API client with access profile_

> **LEGACY ACCESS PROFILES**
> 
> Access profiles are the legacy method for API access management. [Applications](#api-keys) have replaced access profiles, which offer streamlined control over API authentication and permissions.
> 
> After **December 1, 2025**, you can't modify existing access profiles or create new ones. This includes configurations such as authentication methods, collection access, policies, and allowed IP addresses.
> 
> As of **July 1, 2026**, Workato has fully deprecated legacy API clients and access profiles. Access tokens associated with legacy access profiles are no longer valid.
> 
> We recommend that you use [Applications](#api-keys) for new clients and integrations.

### Access profile fields

A unique API key is generated for each client in the **Auth Token** field. This token is a long string of characters. It must be supplied to the client so that the client can connect to the API. Treat this API key as confidential information; it should be known only to the API owner and the client.

An API key can be revoked, and a new one issued, by clicking the **Refresh** button next to the token.

A client can be **Active** or **Inactive**. An inactive client cannot call any APIs. Click the toggle to set the client's status to **Active** and enable the client to call APIs.

### Create new access profile

**Prerequisites:**

1. [Configure an API collection](/en/api-mgmt/api-collections)
2. **(Optional)** [Create an access policy](/en/api-mgmt/api-access-policies)
3. [Create a client](#create-new-client)

1. Go to **Platform > API platform > Clients** and select the new client.
   
2. Select **Create new access profile**.
   
   ![Create new access profile](/assets/api-client-new-access-profile.nEpKvsEZ.png) _Create new access profile_
   
3. Fill in the following fields:
   
   - Profile name
     
   - Enter a descriptive name for the access profile.
     
   - API collections to include
     
   - Select one or more collections. You can send requests to endpoints in these collections using your access profile.
     
   - Authentication method
     
   - This can be an [Auth token](/en/api-mgmt/auth-token), an [OAuth 2.0](/en/api-mgmt/oauth2) access token, a [JSON web token (JWT)](/en/api-mgmt/jwt-token), or [OpenID Connect](/en/api-mgmt/oidc).
     
   - Policy _(optional)_
     
   - Select a policy that will govern access to API collections included in this profile.
     
   - Allowed IPs
     
   - Specify which IP addresses can access this profile. To add multiple IP addresses, separate them using commas or define a range (`106.226.100.3/20`). When this field is set, only requests initiated from these addresses are allowed.
     
   - Blocked IPs
     
   - Specify which IP addresses cannot access this profile. Blocked IPs take precedence over allowed IPs. For example, if an IP appears in both the **Allowed IPs** and **Blocked IPs** lists, requests from that IP are blocked.
     
   
   ![Configure new access profile settings](/assets/api-new-access-profile.CD6XdSzS.png) _Configure new access profile settings_
   
4. Select **Next**.
   
5. Select **Create access profile**.
   
   ![Confirm creating an access profile](/assets/api-access-profile-setup.CBDSWfJD.png) _Confirm creating an access profile_
   
6. Copy the auth token and save it in a secure place. This is the only time you can view the token. If you lose the token, you must create a new one.
   
   ![Example auth token](/assets/api-profile-sample-auth-token.D6SI5xXH.png) _Example auth token_
   
7. Select **Done**. The new access profile is visible on the client's page.

---
