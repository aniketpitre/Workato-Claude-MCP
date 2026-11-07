---
url: 'https://docs.workato.com/en/api-mgmt/access-developer-portal.md'
description: >-
  Log in to the API developer portal with a magic link or Workato Identity to
  discover, test, and consume published APIs.
---

# Access the developer portal

The developer portal provides everything you need to discover, test, and consume APIs.

## Log in to the portal

How you log in depends on whether your workspace uses [Workato Identity](/en/workato-identity):

- [Log in with magic link](#log-in-with-magic-link): Your admin invites you by email and you access the portal using a link.
- [Log in with Workato Identity](#log-in-with-workato-identity): You log in using your Workato Identity credentials or through your organization's identity provider.

### Log in with magic link

When an admin invites you to the developer portal, you receive an email with a link to access the portal.

**First-time login**

Click the link provided in the invitation email and click **Go to portal**. The link is valid for 24 hours.

![Invitation email](/assets/invitation-email.vDsegpdT.png)_Invitation email_

**Request a new link**

Enter your email address on the portal login page. Workato sends a new link to your inbox. The link is valid for 30 minutes.

![Request a new login link](/assets/login-portal.eGbM1RPX.png)_Enter your email to request a new link_

### Log in with Workato Identity

Follow the **Invited user** tab if you received a portal invitation email. Follow the **JIT user** tab if your organization uses SSO with just-in-time (JIT) provisioning and you didn't receive an invitation.

**Invited user**

Workato sends you a portal invitation email with a **Go to portal** link.

Complete the following steps to access the developer portal:

1. Click **Go to portal** in your portal invitation email.
   
2. Click **Open portal**.
   
3. Sign in with your Workato ID credentials, or through your organization's identity provider if SSO is configured.
   

On first login, you land on the **Discover new APIs** page, where you can browse available API collections and request access. On subsequent logins, you land on your **My APIs** page.

**JIT user**

Your portal account is created automatically on first login if your organization uses SSO with JIT provisioning. You won't receive an email invitation — your admin will share the portal URL with you directly.

1. Go to the portal URL provided by your admin.
   
2. Enter your email address and authenticate through your organization's identity provider.
   

Your portal account is created automatically after authenticating. You land on the **Discover new APIs** page on first login, where you can browse available API collections and request access. On subsequent logins, you land on your **My APIs** page.

  

> **PORTAL ACCESS**
> 
> Contact your admin for the portal URL and to confirm which access method applies to you.

## Navigate the developer portal

After you log in, you can browse your assigned API collections, discover new ones, test endpoints, and manage your API keys.

- [Browse API collections](#browse-api-collections): View your assigned collections and explore endpoint documentation.
- [Discover new APIs](#discover-new-apis): Browse additional available collections and request access.
- [Test endpoints](#test-endpoints): Send test requests to validate endpoint behavior.
- [Manage and create API keys](#manage-and-create-api-keys): Generate and manage keys for authenticating requests.

### Browse API collections

You can access your assigned API collections in the **My APIs** tab. Selecting a collection opens its documentation, where you can explore endpoint methods, descriptions, and schemas. The documentation includes example requests and responses. You can also download the OpenAPI specifications.

![Browse API collections](/assets/browse-collections.BqQiyBTT.png)_Browse API collections_

### Discover new APIs

The **Discover new APIs** tab provides access to additional API collections. Browse collections to find APIs that match your needs, and [request access](#request-access-to-new-apis) directly through the portal.

#### Request access to new APIs

Complete the following steps to request access to new APIs:

1. Go to the **Discover new APIs** tab to browse available API collections.
   
   ![Discover new APIs](/assets/discover-apis.TL2AQeQF.png)_Discover new APIs_
   
2. Select the collection you plan to access and click **Request access**.
   
   ![Request access to an API collection](/assets/request-collection.DgtTGh90.png)_Request access to an API collection_
   
3. Provide a reason for your request and click **Send request**. An admin reviews your request and determines whether to approve or reject it.
   
   ![Request access](/assets/request-access.B2ouwT6v.png)_Request access_
   

The requested APIs appear in your **My APIs** tab if your request is approved, granting you access to their endpoints and documentation.

![Collection added to My APIs](/assets/collection-added.Ck3LjajM.png)_Collection added to **My APIs**_

### Test endpoints

You can test API endpoints directly in the portal to validate their functionality. You must [create an API key](#manage-and-create-api-keys) before testing if you don't already have one.

Complete the following steps to test an endpoint:

1. Go to your assigned collection in the **My APIs** tab and choose the endpoint you plan to test.
   
2. Click **Try it out** to open the testing interface.
   
   ![Try out endpoint](/assets/try-out-endpoint.abCFwAp_.png)_Click **Try it out**_
   
3. Click **Execute** to send a test request.
   
   ![Execute endpoint](/assets/execute-endpoint.J6u8ySP6.png)_Click **Execute**_
   
4. Review the response details, including status codes, headers, and payloads, to confirm the endpoint’s behavior.
   

### Manage and create API keys

Use the **Manage API keys** page to create and manage your API keys. You can define security parameters such as allowed and blocked IP addresses.

Complete the following steps to create an API key:

1. Click your profile icon, then select **Manage API keys** in the drop-down menu.
   
   ![Manage API keys](/assets/manage-keys.BL13BjWw.png)_Manage API keys_
   
2. Click **Create API key**.
   
   ![Create new API key](/assets/create-new-api-key.L23Z1kk2.png)_Create new API key_
   
3. Enter a name in the **API key name** field.
   
   ![Create new API key](/assets/api-key-name.DxEFC_QM.png)_Provide an **API key name**_
   
4. Optional. Enter allowed IP addresses in the **Allowed IPs** field to restrict requests for enhanced security. To add multiple IP addresses, separate them using commas or define a range (`106.226.100.3/20`).
   
5. Optional. Enter blocked IP addresses in the **Blocked IPs** field to prevent requests from specific IP addresses. Blocked IPs take precedence over allowed IPs. Requests from an IP address are denied if it appears on both lists.
   
6. Click **Generate** to create the API key. Workato displays the generated token. Save this token securely, as it won’t display again. If you lose the token, you can refresh the key to generate a new one. Refreshing invalidates the existing token.
   

After creating the key, it appears on the **Manage API keys** page. You can use this page to view the token’s details or refresh, deactivate, or delete the key if required.

## Search with AIRO

AIRO is a smart search capability in the developer portal. You can ask natural-language questions and get help with developer tasks, such as endpoint recommendations, code snippets, and links to documentation.

### How AIRO works

AIRO interprets your natural-language questions and assists with developer tasks in the portal, such as recommending endpoints, generating code, and surfacing related documentation. Responses are scoped to API collections that are published in the portal.

### Search for an API

You can search for an API in the following ways:

- **Search field**: Type a keyword in the **Search collections** field, then select one of the suggested **Ask AIRO** prompts. The portal returns a single response inline. Click **Continue in chat** if you have follow-up questions.
- **AIRO chat**: Click **Ask AIRO** to open the chat directly, or click the **Search collections** field and select **Open AIRO** from the drop-down menu. The chat supports multi-turn conversation, so you can ask follow-ups in the same session.

AIRO typically responds with the following information:

- A natural-language explanation of which endpoint to use and how to use it.
- A `cURL` code example with placeholder authentication.
- A **Related documentation** section linking to the recommended endpoint and its parent collection.

![AIRO responds with a code example and related documentation](/assets/airo-response.Dh5E93CO.png)_AIRO responds with a code example and related documentation_

> **VERIFY AI-GENERATED CONTENT**
> 
> AIRO generates responses using an AI model. Note the following when reviewing responses:
> 
> - Responses are scoped to API collections that are published in your portal and that you have access to or can request access to.
> - Code examples use placeholder authentication. Replace this placeholder with one of your own [API keys](/en/api-mgmt/access-developer-portal#manage-and-create-api-keys) before sending the request.
> - Endpoint paths, parameter names, and example values shown in responses can be inaccurate. Verify generated content against the linked endpoint documentation before using it.

---
