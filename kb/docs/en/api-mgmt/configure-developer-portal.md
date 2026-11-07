---
url: 'https://docs.workato.com/en/api-mgmt/configure-developer-portal.md'
description: >-
  Set up the Workato developer portal to brand your client portal, manage client
  access, and publish API collections.
---

# Configure the developer portal

Use this guide to set up your developer portal, manage client access, and publish API collections.

## Set up your portal

Complete the following steps to configure your client portal's branding, URL, and appearance:

1. Go to **Platform > API platform > Settings > Developer Portal > Branding**.
   
2. Select **Get started** to open the portal setup wizard.
   
   ![Set up your developer portal](/assets/set-developer-portal.BZvGOli7.png)_Set up your developer portal_
   
3. Enter a name in the **Portal name** field.
   
   ![Set up portal details](/assets/set-portal-details-new.CnjSTKYx.png)_Set up portal details_
   
4. Enter a portal subdomain in the **Portal URL** field. This is the URL your clients use to access the portal. For example, enter `acme` to create the portal URL `https://acme.portal.app.workato.com`.
   
   > **SUBDOMAIN REQUIREMENTS**
   > 
   > Ensure your portal subdomain meets the following criteria:
   > 
   > - Contains only lowercase letters (`a-z`), numbers (`0-9`), and hyphens (`-`).
   > - Starts with a letter.
   > - Doesn't end with a hyphen (`-`).
   > - Is a maximum of 63 characters.
   
   > **CUSTOM DOMAIN**
   > 
   > Refer to [Custom domain](/en/api-mgmt/custom-domain-portal) to use a branded domain instead of `portal.app.workato.com`.
   
5. Upload an image in the **Portal logo** field by dragging and dropping or selecting a file from your device. Accepted formats are PNG/JPG, with a maximum size of 10 MB.
   
6. Set a color in the **Brand color** field. This color applies to headers, buttons, and other elements for consistent branding.
   
7. Review the **Preview** to see how your changes will appear to clients.
   
8. Click **Next**.
   
9. Use the **Select API collections to publish to portal** drop-down menu to choose which collections to publish. These appear in the **Discover new APIs** section, where clients can search for and request access.
   
   ![Select which API collections to publish](/assets/publish-collections.BXH0dO1D.png)_Select which API collections to publish_
   
10. Click **Next** to publish your portal.
    

After publishing, the portal remains live and cannot be taken offline. You can update branding, collections, and client access at any time. Use the portal preview to see how it appears to your clients.

![Developer portal settings](/assets/portal-settings.Y5p-0nfT.png)_Developer portal settings_

## Configure authentication settings

Each developer portal uses one of two authentication methods to control how clients log in:

- **Magic link**: Clients receive a magic link by email to log in.
- **Identity provider**: Clients authenticate using an identity provider (SSO).

New portals use **Identity provider** by default.

> **USING WORKATO IDENTITY?**
> 
> End users must exist in Workato Identity before you can add them as API clients:
> 
> - **Password authentication**: [Add end users manually](/en/workato-identity/add-end-user-manually).
> - **SAML SSO**: [Configure SAML-based authentication](/en/workato-identity/saml-sso#configure-saml-based-authentication) and [set up IdP user access](/en/workato-identity/saml-sso#configure-idp-user-access), then provision users [manually](/en/workato-identity/add-end-user-manually) or through [JIT provisioning](/en/workato-identity/jit-provisioning). If using JIT, also [configure JIT user settings](/en/api-mgmt/developer-portal-jit) before directing users to the portal.

### Change the authentication method

You can change a portal's authentication method only while it has no existing clients. After you add the first client, the method is locked. Remove all clients first to change the method on a portal that already has clients.

Complete the following steps to change the authentication method:

1. Go to **Platform > API platform > Settings > Developer Portal > Auth settings**.
   
2. Use the **Authentication method** drop-down menu to select **Magic link** or **Identity provider (Default)**.
   
   ![Authentication settings](/assets/auth-settings.DqNDztZ5.png)_Authentication settings_
   
3. Click **Save**.
   

> **AUTHENTICATION METHOD AFFECTS CLIENT CREATION**
> 
> The authentication method determines which field identifies a client during creation:
> 
> - Magic link portals use the client's email address.
> - Identity provider portals use the client's Workato Identity user ID (`idp_user_id`).
> 
> If you create API clients programmatically, refer to [Create an API client](/en/workato-api/api-platform#create-api-client-v2) for the required payload.

## Add and configure clients in the portal

You can add API clients to the portal and define the API collections they can access and their authentication method.

Complete the following steps to add and configure clients in the portal:

1. Go to **Platform > API platform > Clients > All clients**.
   
2. Click **\+ Add new client**.
   
   ![Add new client](/assets/add-a-client.CzD77CsN.png)_Add new client_
   
3. Enter a name in the **Name** field. Use a descriptive identifier, such as the client's company or department name.
   
   ![Set up client details](/assets/add-client-details.DQ-ipDux.png)_Set up client details_
   
4. Enter a description in the **Description** field.
   
5. Upload an image in the **Client logo** field. Drag and drop a JPG/PNG image or click **Upload from device** to select a file. This logo visually identifies your client in the portal.
   
6. Enable the **Grant client access to portal** toggle to allow the client to log in and browse published API collections.
   
7. Provide the client identity based on your portal's [authentication method](#configure-authentication-settings):
   
   **Workato Identity**
   
   Select the client from the **Client** drop-down menu. The list only includes end users already added to Workato Identity.
   
   **Magic link**
   
   Enter the client's email address in the **Email** field. Workato sends them a portal invitation.
   
8. Click **Next**.
   
9. Choose an authentication method from the **Authentication method** drop-down menu. Refer to the [available authentication methods](/en/api-mgmt/access-tokens) for more information.
   
   > **WARNING**
   > 
   > You can't change the authentication method after the client is created.
   
   ![Define access configuration](/assets/define-access-configuration.DmXhsOJh.png)_Define access configuration_
   
10. Enable the **Enforce mutual TLS (mTLS)** toggle to require clients to present a valid certificate during the SSL handshake. This enforces two-way authentication. Refer to the [mTLS authentication](/en/api-mgmt/mtls) guide for more information.
    
    > **CUSTOM DOMAIN REQUIRED**
    > 
    > This setting appears only if you configure your workspace with a custom domain.
    
11. Use the **API collections to include** drop-down menu to select one or more API collections. You can also create a client without collections to let them [explore APIs](/en/api-mgmt/access-developer-portal#discover-new-apis) and [request access](/en/api-mgmt/access-developer-portal#request-access-to-new-apis) as needed.
    
12. Optional. Select a policy from the **Policy** drop-down menu to control your client's API usage. Policies define rules such as rate limits or usage quotas. Refer to [API access policies](/en/api-mgmt/api-access-policies) to create and manage API access policies.
    
13. Click **Next**. Workato sends the client a portal invitation email for magic link portals.
    
    ![Create client](/assets/create-successful-client.fOtqdtwy.png)_Create client_
    

Clients can log in to the portal and create up to 20 API keys to authenticate requests to their assigned collections.

## Manage client access

The **Clients** tab provides access to the **All clients** page, where you can review and update client details, access configurations, and policy assignments.

![All clients page](/assets/all-clients-page.BJ8ZzTRR.png)_All clients page_

To manage a specific client's access, click their name to open their details page. From here, you can configure the following settings:

- [Edit client details](#edit-client-details)
- [Access configuration](#access-configuration)
- [Applications](#api-keys)
- [Review collection access requests](#review-collection-access-requests)

### Edit client details

Click **Edit client** to update basic client information, such as the client's name or email address, from the client details page.

![Edit client details](/assets/edit-client-details.7JfPuC2s.png)_Edit client details_

### Access configuration

Use the **Access configuration** tab to manage your client's access to API collections and set usage policies.

View and adjust the **Accessible collections** assigned to the client. Add or remove collections to tailor access based on the client's specific requirements.

![Edit accessible API collections](/assets/edit-accessible-collections.AE1djwU_.png)_Edit accessible API collections_

> **CLIENT ACCESS LIMITATION**
> 
> Every client must have access to at least one API collection. You can't remove a client's last remaining accessible collection.
> 
> If you try to remove the last collection and click **Save**, the action fails, and Workato displays an error message explaining the limitation. Ensure the client retains access to at least one collection before saving your changes.

To enforce usage restrictions, add or edit a **Policy** that defines rules such as rate limits or usage quotas.

### Applications

The **Applications** tab lets you create and manage the credentials clients use to authenticate requests. You can apply optional IP restrictions when you create an application, and refresh or deactivate existing applications as needed.

> **RENAMED FROM API KEYS**
> 
> The **API keys** tab is now called **Applications**. A client's applications can use more than one credential type, such as an API key or custom validation, not API keys alone.

![Manage applications](/assets/manage-applications.C_6eZlDj.png)_Manage applications_

### Review collection access requests

When a portal client requests access to an API collection, the request appears in the **Pending collection access requests** section within the **Clients** tab.

Review the requested API collections and the client's justification for needing access.

![Review requested API collections](/assets/review-requested-apis.DaMURky_.png)_Review requested API collections_

Choose to **Approve** or **Reject** requests directly from this page. Approving grants the client access to the requested collections, while rejecting keeps the client's current permissions unchanged.

## Publish API collections

Only active collections appear in the portal catalog. A collection is active if it contains at least one active endpoint. Inactive collections with zero active endpoints don't appear in the **Discover new APIs** section, even if published.

Complete the following steps to publish an API collection in the developer portal:

1. Go to **Platform > API platform > API collections** page and select the collection you plan to publish.
   
2. Locate the **Visibility on portal** section on the collection's **Endpoints** page. Collections default to **Private** if they are not initially published to the portal.
   
3. Click **Publish to portal** to make the collection discoverable to your clients.
   
   ![Publish your API collection](/assets/publish-collection.DH3V8Dae.png)_Publish your API collection_
   

You can also publish collections from the **API collections** tab. Click **•••** (ellipsis) next to the collection and select **Publish collection**.

![Publish your API collection](/assets/publish-collection-tab.C_Xcdq61.png)_Publish your API collection from the API collections tab_

---
