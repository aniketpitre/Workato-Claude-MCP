---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/docusign-esignature-mcp-server.md
description: >-
  Use the Docusign MCP server to connect your LLM to Docusign with tools to send
  agreements for signature, track progress, retrieve signed documents, and
  manage in-progress agreements through natural language.
---

# Docusign MCP server

The Docusign MCP server enables LLMs to manage the lifecycle of agreements sent for electronic signature within Docusign through natural conversation. It provides tools to create agreements from templates, send agreements for signature, track the progress of agreement documentation, and retrieve completed documents without requiring direct interaction with the Docusign interface.

## Uses

Use the Docusign MCP server to perform the following actions:

- List and search envelopes filtered by status, date range, sender, or recipient
- Retrieve summary details and status for a specific envelope
- Check recipient-level signing status to identify who has signed or is pending
- List documents attached to an envelope
- List available templates and retrieve template structure and required fields
- Create a draft envelope from a template
- Send a draft envelope to recipients for signature
- Cancel an in-progress envelope
- Resend signing notifications to remind recipients

### Example prompts

Use the following example prompts to invoke Docusign MCP server tools:

- `Show me all agreements awaiting signature.`
- `List envelopes sent to this recipient in the last 30 days.`
- `Get the status of this agreement.`
- `Who still needs to sign this envelope?`
- `List the documents attached to this envelope.`
- `What templates are available for sending agreements?`
- `Show me the required fields for this template.`
- `Create a draft agreement from the NDA template.`
- `Send this draft envelope to the recipients.`
- `Cancel this in-progress agreement.`
- `Remind the recipients who haven't signed yet.`

## Docusign MCP server tools

The Docusign MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_envelopes](#list-envelopes-tool) | Lists envelopes filtered by status, date range, sender, or recipient. |
| [get\_envelope](#get-envelope-tool) | Retrieves summary details and status for an envelope you specify. |
| [get\_envelope\_recipients](#get-envelope-recipients-tool) | Retrieves recipient-level signing status for an envelope. |
| [get\_envelope\_documents](#get-envelope-documents-tool) | Lists documents attached to an envelope. |
| [list\_templates](#list-templates-tool) | Lists available templates for agreement creation. |
| [get\_template](#get-template-tool) | Retrieves structure and required fields for a template. |
| [create\_envelope\_from\_template](#create-envelope-from-template-tool) | Creates a draft envelope using a selected template. |
| [send\_envelope](#send-envelope-tool) | Sends a draft envelope to recipients for signature. |
| [void\_envelope](#void-envelope-tool) | Cancels an in-progress envelope. |
| [resend\_envelope](#resend-envelope-tool) | Resends signing notifications for an envelope. |

## Install the Docusign MCP server

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
    

## Docusign connection setup

View Docusign connection setup steps

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

The Docusign connector works with the following Docusign plans:

- Personal
- Standard
- Business Pro

View JWT Grant authentication setup steps

Use JWT Grant authentication to connect to Docusign with a private key for server-to-server authentication. This method sends documents from the email address of the User ID you connect with, using the Docusign user impersonation. That user, or their account admin, must grant consent before you can connect. Refer to [Retrieve your User ID](#retrieve-your-user-id) for more information.

#### JWT Grant setup

Complete the following to set up JWT Grant authentication:

- [Retrieve your User ID](#retrieve-your-user-id)
- [Create an integration key](#create-an-integration-key)
- [Generate an RSA keypair](#generate-an-rsa-keypair)
- [Add the redirect URI](#add-the-redirect-uri)
- Optional: [Obtain consent for user impersonation](#obtain-consent-for-send-on-behalf-of)

##### Retrieve your User ID

View retrieve your User ID steps

Complete the following steps to retrieve your User ID in Docusign:

1. Sign in to Docusign.
   
2. Go to **Admin > Apps and Keys**.
   
3. Copy and save the **User ID** for use in Workato.
   

##### Generate an integration key

View generate an integration key steps

You must create an app to generate an integration key.

Complete the following steps to generate an integration key in Docusign:

1. Go to the **Apps and Keys** page and click **Add App and Integration Key**.
   
2. Enter a name for your application, such as `Workato Integration`.
   
3. Click **Create App**.
   
4. Copy and save the **Integration Key** (also known as the Client ID) for use in Workato.
   

##### Generate an RSA keypair

View generate an RSA keypair steps

Complete the following steps to generate an RSA keypair in Docusign:

1. Go to the **Service Integration** section in your newly created app settings.
   
2. Click **Generate RSA** to create a new RSA keypair.
   
3. Copy the **Private Key** and save it in a secure location. This value is required to establish the connection in Workato.
   
   > **SAVE YOUR PRIVATE KEY**
   > 
   > The private key is only displayed once. After you close this dialog, you won't be able to retrieve it again. If you lose it, you must generate a new keypair.
   
4. Click **Close** to save the keypair to your integration.
   

##### Add the redirect URI

View add the redirect URI steps

Complete the following steps to add the redirect URI in Docusign:

1. Go to the **Additional settings > Redirect URIs** section in your newly created app settings.
   
2. Click **\+ Add URI**.
   
3. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field.
   
4. Click **Save**.
   

##### Obtain consent for user impersonation

View obtain consent for user impersonation steps

JWT Grant authentication sends envelopes from the email address of the user you connect with, using Docusign's user impersonation. Connecting as that user requires consent, which comes in two forms:

- [Admin consent](#obtain-admin-consent) for the JWT app (one-time setup for the organization)
- [Individual user consent](#obtain-individual-user-consent) for the user you connect as

###### Obtain admin consent

View obtain admin consent steps

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

View obtain individual user consent steps

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

View connect to Docusign with JWT Grant authentication steps

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
    

View OAuth 2.0 (Authorization Code Grant) setup steps

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
    

## How to use Docusign MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_envelopes tool

The **list\_envelopes** tool lists envelopes filtered by status, date range, sender, or recipient. Your LLM uses this tool to search and surface agreements matching the criteria you provide.

**Try asking**:

- `Show me all agreements awaiting signature.`
- `List envelopes sent to this recipient in the last 30 days.`
- `Show me completed agreements from this month.`
- `Find envelopes sent by this team member.`

### get\_envelope tool

The **get\_envelope** tool retrieves summary details and status for an envelope you specify. Your LLM uses this tool to return its current state, sent date, and recipient summary.

**Try asking**:

- `Get the status of this agreement.`
- `Show me the details for this envelope.`
- `What's the current state of this agreement?`
- `Pull up the summary for this envelope.`

### get\_envelope\_recipients tool

The **get\_envelope\_recipients** tool retrieves recipient-level signing status for an envelope. Your LLM uses this tool to return each recipient's current status, identifying who has signed and who is still pending.

**Try asking**:

- `Who still needs to sign this envelope?`
- `Show me the signing status for each recipient on this agreement.`
- `Which recipients have completed signing?`
- `Who is holding up this agreement?`

### get\_envelope\_documents tool

The **get\_envelope\_documents** tool lists documents attached to an envelope. Your LLM uses this tool to return available documents.

**Try asking**:

- `List the documents attached to this envelope.`
- `What documents are included in this agreement?`
- `Show me the files associated with this envelope.`
- `What documents are available for this completed agreement?`

### list\_templates tool

The **list\_templates** tool lists available templates for agreement creation. Your LLM uses this tool to match template references and help select the right starting point before creating an envelope.

**Try asking**:

- `What templates are available for sending agreements?`
- `Show me all Docusign templates I can use.`
- `Find a template for an NDA.`
- `List available templates before I create a new agreement.`

### get\_template tool

The **get\_template** tool retrieves the structure and required fields for a template. Your LLM uses this to provide required roles and fields before creating an envelope from the template.

**Try asking**:

- `Show me the required fields for this template.`
- `What roles and fields does the NDA template require?`
- `Get the structure of this template before I create an agreement.`
- `What information do I need to fill in for this template?`

### create\_envelope\_from\_template tool

The **create\_envelope\_from\_template** tool creates a draft envelope using a template you select. Your LLM uses this tool to apply the template structure and the recipient and field information you provide to build the draft before sending.

**Try asking**:

- `Create a draft agreement from the NDA template.`
- `Set up a new envelope using the MSA template for this recipient.`
- `Draft an agreement from this template with these signer details.`
- `Create an envelope from the SOW template before I send it.`

### send\_envelope tool

The **send\_envelope** tool sends a draft envelope to recipients for signature. Your LLM uses this tool to send an envelope to the recipients you specify.

**Try asking**:

- `Send this draft envelope to the recipients.`
- `Deliver this agreement for signature.`
- `Send the NDA I just created to this contact.`
- `Dispatch this envelope now that it's ready.`

### void\_envelope tool

The **void\_envelope** tool cancels an in-progress envelope. The tool uses the envelope ID to stop the agreement and notify recipients that it has been voided. This tool is only used when you explicitly ask to cancel or stop an agreement.

**Try asking**:

- `Cancel this in-progress agreement.`
- `Void this envelope — we're using a different version.`
- `Stop this agreement from being signed.`
- `Cancel and void this envelope.`

### resend\_envelope tool

The **resend\_envelope** tool resends signing notifications for an envelope. Your LLM uses this tool to re-notify recipients who haven't completed signing.

**Try asking**:

- `Remind the recipients who haven't signed yet.`
- `Resend the signing notification for this envelope.`
- `Send a reminder to the pending signers on this agreement.`
- `Nudge the recipients who are holding up this agreement.`

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
