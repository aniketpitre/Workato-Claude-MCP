---
url: 'https://docs.workato.com/en/connectors/docusign.md'
description: >-
  Connect to Docusign to send, sign, and manage digital documents and eSignature
  workflows.
---

# Docusign

[Docusign](https://www.docusign.com/) is a secure eSignature solution that provides electronic signature technology and digital transaction management services that enable businesses to create fully digital workflows.

## API version

The Docusign connector uses the [Docusign eSignature REST API](https://developers.docusign.com/docs/esign-rest-api/reference/), and calls a mix of v2.0 and v2.1 endpoints depending on the trigger or action. Refer to [API version by trigger and action](#api-version-by-trigger-and-action) for the version each one calls.

## Supported editions and versions

The Docusign connector works with the following Docusign plans:

- Personal
- Standard
- Business Pro

## Connection setup

The Docusign connector supports the following authentication types:

- [JWT Grant](#jwt-token)
- [OAuth 2.0 (Authorization Code Grant)](#oauth-2-0)

> **AUTHENTICATION AND SENDING**
> 
> **JWT Grant** authentication uses the Docusign `impersonation` scope to send documents from the email address of the user you connect with, without requiring that user to sign in. The impersonated user, or their account admin, must grant consent before you can connect.
> 
> **OAuth 2.0** (Authorization Code Grant) sends all documents from the email address of the user who signs in to authorize the connection.

> **ROLES AND PERMISSIONS**
> 
> Users who can sign in to Docusign can connect it to Workato. Users have the same permissions and capabilities to view, manage, and send envelopes on Workato as in Docusign. Refer to the Docusign [Permission Profiles](https://support.docusign.com/en/guides/ndse-admin-guide-permission-sets) documentation for more information.

### JWT Grant

Use JWT Grant authentication to connect to Docusign with a private key for server-to-server authentication. This method sends documents from the email address of the User ID you connect with, using the Docusign user impersonation. That user, or their account admin, must grant consent before you can connect. Refer to [Retrieve your User ID](#retrieve-your-user-id) for more information.

#### Docusign setup for JWT Grant authentication

Complete the following to set up JWT Grant authentication:

- [Retrieve your User ID](#retrieve-your-user-id)
- [Create an integration key](#create-an-integration-key)
- [Generate an RSA keypair](#generate-an-rsa-keypair)
- [Add the redirect URI](#add-the-redirect-uri)
- Optional: [Obtain consent for user impersonation](#obtain-consent-for-send-on-behalf-of)

##### Retrieve your User ID

Complete the following steps to retrieve your User ID in Docusign:

1. Sign in to Docusign.
   
2. Go to **Admin > Apps and Keys**.
   
3. Copy and save the **User ID** for use in Workato.
   

##### Generate an integration key

You must create an app to generate an integration key.

Complete the following steps to generate an integration key in Docusign:

1. Go to the **Apps and Keys** page and click **Add App and Integration Key**.
   
2. Enter a name for your application, such as `Workato Integration`.
   
3. Click **Create App**.
   
4. Copy and save the **Integration Key** (also known as the Client ID) for use in Workato.
   

##### Generate an RSA keypair

Complete the following steps to generate an RSA keypair in Docusign:

1. Go to the **Service Integration** section in your newly created app settings.
   
2. Click **Generate RSA** to create a new RSA keypair.
   
3. Copy the **Private Key** and save it in a secure location. This value is required to establish the connection in Workato.
   
   > **SAVE YOUR PRIVATE KEY**
   > 
   > The private key is only displayed once. After you close this dialog, you won't be able to retrieve it again. If you lose it, you must generate a new keypair.
   
4. Click **Close** to save the keypair to your integration.
   

##### Add the redirect URI

Complete the following steps to add the redirect URI in Docusign:

1. Go to the **Additional settings > Redirect URIs** section in your newly created app settings.
   
2. Click **\+ Add URI**.
   
3. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field.
   
4. Click **Save**.
   

##### Obtain consent for user impersonation

JWT Grant authentication sends envelopes from the email address of the user you connect with, using Docusign's user impersonation. Connecting as that user requires consent, which comes in two forms:

- [Admin consent](#obtain-admin-consent) for the JWT app (one-time setup for the organization)
- [Individual user consent](#obtain-individual-user-consent) for the user you connect as

###### Obtain admin consent

Use the Docusign Admin panel to grant consent to your JWT app on behalf of all users within your organization's claimed domains. This authorization grants app access to all domain users, with access limited by the permissions you specify. This is a one-time configuration.

> **PREREQUISITES FOR ADMIN CONSENT**
> 
> - Your organization must have the Docusign Admin feature enabled.
> - Your organization must have at least one claimed domain. Refer to the Docusign [Claim a domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256_1.html) documentation.
> - You must have created an [integration key](#create-an-integration-key) for your app.

Complete the following steps to obtain admin consent:

1. Sign in to Docusign as an organization administrator.
   
2. Open your [Organization](https://apps-d.docusign.com/admin/organization/) home page in Docusign Admin.
   
3. Select **Connected Apps** from the navigation pane.
   
4. Select **Authorize Application** and choose your application from the drop-down menu. This menu lists every integration key by name (for example, `Workato Integration`).
   
5. Enter `signature impersonation` in the **Permissions** field of the **Add New Application** dialog.
   
   These permissions apply to every user who's a member of the organization's claimed domains.
   
6. Click **Add** to confirm and authorize the application.
   

Refer to the Docusign [How to obtain admin consent for internal applications](https://developers.docusign.com/platform/auth/consent/obtaining-admin-consent-internal/) documentation for more information.

###### Obtain individual user consent

Each user you plan to connect as must grant individual consent to your JWT app. This allows the app to act on their behalf when sending envelopes.

> **INTEGRATION KEY AND REDIRECT URI**
> 
> Ensure you complete the [integration key](#create-an-integration-key) and [redirect URI](#add-the-redirect-uri) steps from the JWT Grant setup section before you set up individual consent.

Complete the following steps to obtain individual user consent:

**For administrators**

1. Construct the individual consent URL using the following format:
   
   **For production accounts:**
   
   ```
   https://account.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=YOUR_INTEGRATION_KEY&redirect_uri=https://www.workato.com/oauth/callback
   ```
   
   **For demo/sandbox accounts:**
   
   ```
   https://account-d.docusign.com/oauth/auth?response_type=code&scope=signature%20impersonation&client_id=YOUR_INTEGRATION_KEY&redirect_uri=https://www.workato.com/oauth/callback
   ```
   
   Replace `YOUR_INTEGRATION_KEY` with your integration key (Client ID).
   
2. Provide the consent URL to each user who needs to grant consent. Users can open this URL in their web browser.
   

**For users**

1. Open the consent URL provided by your administrator in a web browser.
   
2. Sign in to Docusign.
   
3. Review the consent screen and click **Accept** to grant consent. You won't be prompted again unless consent is revoked.
   

  

> **CONSENT DURING CONNECTION**
> 
> Docusign prompts you to grant consent when you [connect with JWT Grant authentication](#jwt-token). This grants individual consent for the user who authenticates the connection. You only need to follow the steps above to pre-authorize consent for users who won't personally set up the connection, for example, so an admin can grant consent ahead of time for another user's connection.

Refer to the Docusign [How to obtain individual consent](https://developers.docusign.com/platform/auth/consent/obtaining-individual-consent/) documentation for more information.

#### Connect to Docusign with JWT Grant authentication

Complete the following steps to set up a JWT Grant connection to Docusign in Workato:

1. Click **Create > Connection**.
   
2. Search for `Docusign` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Docusign JWT Grant connection](/assets/jwt-grant-connection.D5bvWRRz.png)_Docusign JWT Grant connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Auth type** drop-down menu to select **JWT Grant**.
   
6. Use the **Demo** drop-down menu to indicate if this is a demo Docusign account. Select **Yes** for demo/sandbox accounts or **No** for production accounts.
   
7. Enter the [integration key](#create-an-integration-key) from your Docusign application in the **Client ID** field.
   
8. Enter the [User ID](#retrieve-your-user-id) from the [JWT Grant setup](#jwt-token-setup) steps in the **User ID** field.
   
9. Enter the [RSA private key](#generate-an-rsa-keypair) from the [JWT Grant setup](#jwt-token-setup) steps in the **Private key** field. Enter the complete private key including the `-----BEGIN RSA PRIVATE KEY-----` and `-----END RSA PRIVATE KEY-----` headers.
   
10. Optional. Enter the **Account ID** to specify a Docusign account when you have multiple accounts. You can find the account ID by navigating to **Admin > Apps and Keys > API Account ID**. The connection selects your first Docusign account by default.
    
11. Optional. Enter the Connect key in the **Connect key** field to validate your webhook requests. Refer to the Docusign [Add HMAC keys for your app](https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/) documentation for more information.
    
12. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
    
13. Click **Connect**. Workato redirects you to Docusign to authorize the connection.
    
14. Click **Allow Access** to grant the Workato integration permission to access your account.
    
    ![JWT consent screen](/assets/jwt-consent.C2zP7euJ.png)_JWT consent screen_
    

### OAuth 2.0 (Authorization Code Grant)

Use OAuth 2.0 (Authorization Code Grant) to connect to Docusign by signing in and granting access through Docusign's authorization flow. All documents are sent from the email address of the user who authorized the connection.

#### Connect to Docusign with OAuth 2.0 (Authorization Code Grant)

Complete the following steps to set up an OAuth 2.0 authentication connection to Docusign in Workato:

1. Click **Create > Connection**.
   
2. Search for `Docusign` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Docusign OAuth 2.0 (Authorization Code Grant) connection](/assets/oauth-2.NAxc7mKJ.png)_Docusign OAuth 2.0 (Authorization Code Grant) connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Demo** drop-down menu to indicate if this is a demo Docusign account. Select **Yes** for demo/sandbox accounts or **No** for production accounts.
   
7. Optional. Enter the **Account ID** to specify a Docusign account when you have multiple accounts. You can find the account ID by navigating to **Admin > Apps and Keys > API Account ID**. The connection selects your first Docusign account by default.
   
8. Optional. Enter the Connect key in the **Connect key** field to validate your webhook requests. Refer to the Docusign [Add HMAC keys for your app](https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/) documentation for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

## API version by trigger and action

The Docusign connector's actions and triggers call a mix of Docusign eSignature REST API v2.0 and v2.1 endpoints. If you see response differences from what the Docusign [API reference](https://developers.docusign.com/docs/esign-rest-api/reference/) documentation describes, check whether the action or trigger you're using is on v2.0.

| Type | Name | API version |
| --- | --- | --- |
| Trigger | [New document event](/en/connectors/docusign/trigger-new-document-event) | v2.0 |
| Trigger | [New document received](/en/connectors/docusign/trigger-new-document-received) | Mixed (v2.1 and v2.0) |
| Trigger | [New recipient event](/en/connectors/docusign/trigger-new-recipient-event) | v2.1 |
| Action | [Create draft envelope from template](/en/connectors/docusign/action-create-draft-envelope-from-template) | v2.1 |
| Action | [Create recipient view](/en/connectors/docusign/action-create-recipient-view) | v2.1 |
| Action | [Create template](/en/connectors/docusign/action-create-template) | v2.1 |
| Action | [Create/send document](/en/connectors/docusign/action-create-send-document) | v2.0 |
| Action | [Download document](/en/connectors/docusign/action-download-document) | v2.0 |
| Action | [Get envelope](/en/connectors/docusign/action-get-envelope) | v2.1 |
| Action | [Get envelope form data](/en/connectors/docusign/action-get-envelope-form-data) | v2.1 |
| Action | [Get envelope recipients](/en/connectors/docusign/action-get-envelope-recipients) | v2.1 |
| Action | [Get template](/en/connectors/docusign/action-get-template) | v2.1 |
| Action | [Get template document tabs](/en/connectors/docusign/action-get-template-document-tabs) | v2.1 |
| Action | [List documents in envelope (batch)](/en/connectors/docusign/action-list-documents-in-envelope) | v2.0 |
| Action | [List envelopes (batch)](/en/connectors/docusign/action-list-envelopes-batch) | v2.1 |
| Action | [List templates (batch)](/en/connectors/docusign/action-list-templates-batch) | v2.1 |
| Action | [Resend envelope](/en/connectors/docusign/action-resend-envelope) | v2.1 |
| Action | [Resend envelope by ID](/en/connectors/docusign/action-resend-envelope-by-id) | v2.1 |
| Action | [Send document using a template](/en/connectors/docusign/action-send-document-using-template) | v2.0 |
| Action | [Send document using composite templates](/en/connectors/docusign/action-send-document-using-composite-templates) | v2.1 |
| Action | [Send envelope by ID](/en/connectors/docusign/action-send-envelope-by-id) | v2.1 |
| Action | [Void envelope](/en/connectors/docusign/action-void-envelope) | v2.1 |

---
