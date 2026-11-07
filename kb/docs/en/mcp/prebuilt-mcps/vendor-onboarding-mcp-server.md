---
url: 'https://docs.workato.com/en/mcp/prebuilt-mcps/vendor-onboarding-mcp-server.md'
description: >-
  Use the Vendor Onboarding MCP server to connect your LLM to Coupa, DocuSign,
  and NetSuite with a confirmation-gated workflow that captures vendor intake,
  collects tax and insurance documents, checks banking and approval status, and
  creates and activates the vendor master record.
---

# Vendor Onboarding MCP server

The Vendor Onboarding MCP server enables LLMs to onboard new vendors across Coupa, DocuSign, and NetSuite through natural conversation. It provides tools to capture vendor intake and check for duplicates, send and track tax and insurance documentation through DocuSign, confirm banking submission and approval status in Coupa, and create and activate the vendor master record in Coupa and NetSuite, without requiring direct interaction with the Coupa, DocuSign, and NetSuite interfaces. Onboarding a vendor can span days to weeks while you wait on the vendor and approvers, so the server tracks progress and lets you pick up an in-flight onboarding in any later conversation.

## Uses

Use the Vendor Onboarding MCP server to perform the following actions:

- Check a new vendor's legal name against existing Coupa suppliers before creating a record
- Send tax forms and insurance documentation to a vendor for signature through DocuSign
- Check whether a vendor has completed and returned requested documents
- Import a completed DocuSign envelope's signer-entered data into the vendor's Coupa record
- Check whether a vendor has submitted banking details through Coupa's Supplier Portal
- Submit a vendor for approval through Coupa's configured approval chain
- Create the vendor master record in Coupa and NetSuite
- Activate a vendor for transactions
- List in-flight vendor onboardings and see what each one is waiting on

### Example prompts

Use the following example prompts to invoke Vendor Onboarding MCP server tools:

- `Onboard Acme Corp as a new vendor.`
- `What's the status of the Acme onboarding?`
- `Which vendor onboardings are stuck waiting on the vendor?`
- `Check whether Acme's banking has come in yet.`
- `Send the tax and insurance forms to Acme Corp.`
- `Has Acme signed and returned their documents yet?`
- `Import Acme's signed form data into their Coupa record.`
- `Submit Acme's onboarding for approval.`
- `Create the vendor master record for Acme now that it's approved.`
- `Activate Acme for transactions.`

## Vendor Onboarding MCP server tools

The Vendor Onboarding MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [initiate\_vendor\_request](#initiate-vendor-request-tool) | Captures new-vendor intake and checks for duplicates against existing Coupa suppliers. |
| [send\_vendor\_onboarding\_documents](#send-vendor-onboarding-documents-tool) | Sends a single composite DocuSign envelope with tax forms and supporting-document requests to the vendor. |
| [check\_vendor\_document\_status](#check-vendor-document-status-tool) | Returns DocuSign envelope status and follows up with form data and document metadata. |
| [import\_vendor\_form\_data](#import-vendor-form-data-tool) | Downloads completed documents and writes validated form data into the Coupa Supplier Information Management (SIM) record. |
| [check\_vendor\_bank\_details](#check-vendor-bank-details-tool) | Checks whether the vendor has submitted banking through Coupa's native SIM flow. |
| [submit\_vendor\_for\_approval](#submit-vendor-for-approval-tool) | Submits the vendor's Easy Form Response(s) for approval into Coupa's configured chain. |
| [create\_vendor\_master\_netsuite](#create-vendor-master-netsuite-tool) | Finalizes the existing Coupa supplier and creates the NetSuite vendor record. |
| [activate\_vendor\_for\_transactions](#activate-vendor-for-transactions-tool) | Activates the vendor in both Coupa and the ERP, making it payment-ready. |
| [list\_pending\_vendor\_onboardings](#list-pending-vendor-onboardings-tool) | Returns a paginated list of in-flight onboardings you initiated. |
| [get\_vendor\_onboarding\_status](#get-vendor-onboarding-status-tool) | Returns the status of a vendor onboarding across every system. |
| [get\_vendor\_write\_policy](#get-vendor-write-policy-tool) | Returns the field mapping, sensitivity flags, and forbidden-field list for writing vendor data. |

## Install the Vendor Onboarding MCP server

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
    

## Vendor Onboarding connection setup

The following connections are required to use the Vendor Onboarding MCP server:

- [Coupa](#coupa-connection)
- [DocuSign](#docusign-connection)
- [NetSuite](#netsuite-rest-connection)

### Role requirements

Each tool's availability depends on the scopes and permissions granted to the relevant connection. A request made without the required permission returns a permission-denied outcome rather than a partial result.

- **[Coupa](#coupa-connection)**: Requires the following permissions at minimum: - Supplier Information (read, write) - Suppliers (read, write) - Easy Form Responses (read, write, approval submission) - Approvals (read) - Attachments (read, write)
- **[DocuSign](#docusign-connection)**: Requires the following: - `impersonation` scope (JWT Grant) or equivalent send-on-behalf-of access (OAuth 2.0) to send envelopes
- **[NetSuite](#netsuite-rest-connection)**: Requires the following: - RESTlets and REST Web Services scopes - A NetSuite role with permission to create and edit Vendor records

#### Coupa connection setup steps

View Coupa connection setup steps

Complete the following steps to configure Coupa for a client credentials connection to Workato:

> **CLIENT CREDENTIALS REQUIRED**
> 
> The Vendor Onboarding MCP server requires an OAuth 2.0 client credentials connection to Coupa. Other authentication methods aren't supported.

1. Sign in to your Coupa instance, for example `https://[your-instance-name].coupacloud.com/oauth2/clients`.
   
2. Click **Create** to create a new OAuth client.
   
3. Use the **Grant type** drop-down menu to select **Authorization Code** or **Client Credentials**. You must select the same option in Workato for the **Authentication type**.
   
4. Provide a name in the **Name** field. For example: `Workato Coupa OAuth connection`.
   
5. Enter the redirect URIs you plan to use in the **Redirect URIs** field. Add the link `https://www.workato.com/oauth/callback` if you plan to use **Authorization code**.
   
6. Select the scopes you plan to provide to Workato. Include all objects and features you plan to automate with the Coupa connector. The scopes you select must match the scopes you configure in Workato. You must include the `core.common.read` and `offline_access` scopes at a minimum to establish a connection.
   
   ![Coupa creating a client](/assets/coupa-create-client.BgDfen2E.png)_Create a new client_
   
7. Click **Save**.
   
8. Copy and store the **Identifier** and the **Secret** for use in Workato.
   
9. Return to your Workato account and go to the project where you plan to add your connection.
   
10. Click **Create > Connection** or press C twice.
    
11. Search for and select `Coupa` as your connection on the **New connection** page.
    
12. Provide a unique name for the connection in the **Connection name** field.
    
13. Use the **Location** drop-down menu to select the project where you plan to store the connection.
    
14. Use the **Authentication** drop-down to select the **Grant type** provided in Coupa.
    
15. Enter the **Client ID** and **Client secret**.
    
16. Enter the Coupa URL for your instance in the **Host** field. For example, enter `acme` if your URL is `http://acme.coupacloud.com`.
    
17. Use the **Scopes** drop-down menu to select the same scopes you configured in Coupa. Include the required scopes `core.common.read` and `offline_access` to connect successfully.
    
18. Click **Connect**.
    

#### DocuSign connection setup steps

View DocuSign connection setup steps

The Coupa, DocuSign, and NetSuite connector supports the following authentication types:

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

The Coupa, DocuSign, and NetSuite connector works with the following Docusign plans:

- Personal
- Standard
- Business Pro

##### DocuSign JWT Grant authentication

View JWT Grant authentication steps

Use JWT Grant authentication to connect to Coupa, DocuSign, and NetSuite with a private key for server-to-server authentication. This method sends documents from the email address of the User ID you connect with, using the Docusign user impersonation. That user, or their account admin, must grant consent before you can connect. Refer to [Retrieve your User ID](#retrieve-your-user-id) for more information.

Complete the following to set up JWT Grant authentication:

- [Retrieve your User ID](#retrieve-your-user-id)
- [Create an integration key](#create-an-integration-key)
- [Generate an RSA keypair](#generate-an-rsa-keypair)
- [Add the redirect URI](#add-the-redirect-uri)
- Optional: [Obtain consent for user impersonation](#obtain-consent-for-send-on-behalf-of)

###### Retrieve your User ID

View retrieve your User ID steps

Complete the following steps to retrieve your User ID in Coupa, DocuSign, and NetSuite:

1. Sign in to Coupa, DocuSign, and NetSuite.
   
2. Go to **Admin > Apps and Keys**.
   
3. Copy and save the **User ID** for use in Workato.
   

###### Generate an integration key

View generate an integration key steps

You must create an app to generate an integration key.

Complete the following steps to generate an integration key in Coupa, DocuSign, and NetSuite:

1. Go to the **Apps and Keys** page and click **Add App and Integration Key**.
   
2. Enter a name for your application, such as `Workato Integration`.
   
3. Click **Create App**.
   
4. Copy and save the **Integration Key** (also known as the Client ID) for use in Workato.
   

###### Generate an RSA keypair

View generate an RSA keypair steps

Complete the following steps to generate an RSA keypair in Coupa, DocuSign, and NetSuite:

1. Go to the **Service Integration** section in your newly created app settings.
   
2. Click **Generate RSA** to create a new RSA keypair.
   
3. Copy the **Private Key** and save it in a secure location. This value is required to establish the connection in Workato.
   
   > **SAVE YOUR PRIVATE KEY**
   > 
   > The private key is only displayed once. After you close this dialog, you won't be able to retrieve it again. If you lose it, you must generate a new keypair.
   
4. Click **Close** to save the keypair to your integration.
   

###### Add the redirect URI

View add the redirect URI steps

Complete the following steps to add the redirect URI in Coupa, DocuSign, and NetSuite:

1. Go to the **Additional settings > Redirect URIs** section in your newly created app settings.
   
2. Click **\+ Add URI**.
   
3. Enter `https://www.workato.com/oauth/callback` in the **Redirect URIs** field.
   
4. Click **Save**.
   

###### Obtain consent for user impersonation

JWT Grant authentication sends envelopes from the email address of the user you connect with, using Docusign's user impersonation. Connecting as that user requires consent, which comes in two forms:

- [Admin consent](#obtain-admin-consent) for the JWT app (one-time setup for the organization)
- [Individual user consent](#obtain-individual-user-consent) for the user you connect as

View obtain admin consent steps

Use the Docusign Admin panel to grant consent to your JWT app on behalf of all users within your organization's claimed domains. This authorization grants app access to all domain users, with access limited by the permissions you specify. This is a one-time configuration.

> **PREREQUISITES FOR ADMIN CONSENT**
> 
> - Your organization must have the Docusign Admin feature enabled.
> - Your organization must have at least one claimed domain. Refer to the Docusign [Claim a domain](https://support.docusign.com/s/document-item?bundleId=rrf1583359212854&topicId=gso1583359141256_1.html) documentation.
> - You must have created an [integration key](#create-an-integration-key) for your app.

Complete the following steps to obtain admin consent:

1. Sign in to Coupa, DocuSign, and NetSuite as an organization administrator.
   
2. Open your [Organization](https://apps-d.docusign.com/admin/organization/) home page in Docusign Admin.
   
3. Select **Connected Apps** from the navigation pane.
   
4. Select **Authorize Application** and choose your application from the drop-down menu. This menu lists every integration key by name (for example, `Workato Integration`).
   
5. Enter `signature impersonation` in the **Permissions** field of the **Add New Application** dialog.
   
   These permissions apply to every user who's a member of the organization's claimed domains.
   
6. Click **Add** to confirm and authorize the application.
   

Refer to the Docusign [How to obtain admin consent for internal applications](https://developers.docusign.com/platform/auth/consent/obtaining-admin-consent-internal/) documentation for more information.

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
   
2. Sign in to Coupa, DocuSign, and NetSuite.
   
3. Review the consent screen and click **Accept** to grant consent. You won't be prompted again unless consent is revoked.
   

  

> **CONSENT DURING CONNECTION**
> 
> Docusign prompts you to grant consent when you [connect with JWT Grant authentication](#jwt-token). This grants individual consent for the user who authenticates the connection. You only need to follow the steps above to pre-authorize consent for users who won't personally set up the connection, for example, so an admin can grant consent ahead of time for another user's connection.

Refer to the Docusign [How to obtain individual consent](https://developers.docusign.com/platform/auth/consent/obtaining-individual-consent/) documentation for more information.

###### Connect to DocuSign with JWT Grant authentication

View connect to DocuSign with JWT Grant authentication steps

Complete the following steps to set up a JWT Grant connection to Coupa, DocuSign, and NetSuite in Workato:

1. Click **Create > Connection**.
   
2. Search for `Coupa, DocuSign, and NetSuite` and select it as your app.
   
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
    

##### DocuSign OAuth 2.0 (Authorization Code Grant) authentication

View OAuth 2.0 (Authorization Code Grant) setup steps

Use OAuth 2.0 (Authorization Code Grant) to connect to Coupa, DocuSign, and NetSuite by signing in and granting access through Coupa, DocuSign, and NetSuite's authorization flow. All documents are sent from the email address of the user who authorized the connection.

Complete the following steps to set up an OAuth 2.0 authentication connection to Coupa, DocuSign, and NetSuite in Workato:

1. Click **Create > Connection**.
   
2. Search for `Coupa, DocuSign, and NetSuite` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Docusign OAuth 2.0 (Authorization Code Grant) connection](/assets/oauth-2.NAxc7mKJ.png)_Docusign OAuth 2.0 (Authorization Code Grant) connection_
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store your connection.
   
5. Use the **Auth type** drop-down menu to select **OAuth 2.0 (Authorization Code Grant)**.
   
6. Use the **Demo** drop-down menu to indicate if this is a demo Docusign account. Select **Yes** for demo/sandbox accounts or **No** for production accounts.
   
7. Optional. Enter the **Account ID** to specify a Docusign account when you have multiple accounts. You can find the account ID by navigating to **Admin > Apps and Keys > API Account ID**. The connection selects your first Docusign account by default.
   
8. Optional. Enter the Connect key in the **Connect key** field to validate your webhook requests. Refer to the Docusign [Add HMAC keys for your app](https://developers.docusign.com/platform/webhooks/connect/setting-up-hmac/) documentation for more information.
   
9. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
10. Click **Connect**.
    

#### NetSuite REST connection setup steps

View NetSuite REST connection setup steps

The NetSuite REST connector supports the following OAuth 2.0 authentication types:

- Client credentials (machine-to-machine)
- Authorization code grant (user-based authentication)

Select the authentication type based on your use case. Use client credentials for backend integrations. Use authorization code grant when actions require user-level access.

##### Prerequisites

Ensure you have the following to connect to NetSuite in Workato:

- The privilege to [create connections](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) in Workato.
- Access to a NetSuite Admin account.
- An understanding of the required NetSuite permissions.

##### Create an integration record in NetSuite

Complete the following steps to create a new integration record. The integration record represents an app, platform, or tool you plan to integrate with NetSuite.

1. Go to **Setup > Integration > Manage Integrations > New**.
   
   ![Go to Setup > Integration > Manage Integrations > New](/assets/manage-integrations.CkBsXBhB.png)_Go to **Setup > Integration > Manage Integrations > New**_
   
2. Provide a name for the integration record in the **Name** field.
   
3. Select the authentication flow based on your use case:
   
   - Select **Client credentials (machine to machine) grant** to use client credentials (machine-to-machine).
   - Select **Authorization code grant** to use user-based authentication.
   
   You can enable one or both authentication methods depending on your integration requirements.
   
4. Select the following scopes:
   
   - **RESTlets**
   - **REST Web Services**
   - **SuiteAnalytics Connect**
   
   ![Create an integration record in NetSuite](/assets/new-integration-record.CdQ_KiXw.png)_Create an integration record in NetSuite_
   
5. Click **Save**.
   
6. Copy the **Consumer key / Client ID** and **Consumer secret / Client secret** and store both values securely.
   
   - Client credentials authentication requires an EC private key and certificate.
   - Authorization code grant requires a client ID and client secret configured in a custom OAuth profile.
   
   Use the **Client ID** for client credentials authentication. Use the **Client ID** and **Client secret** for authorization code grant.
   
   ![Copy the client credentials](/assets/copy-client-credentials.CPnWlFSG.png)_Copy the client credentials_
   

##### NetSuite client credentials authentication

View client credentials setup steps

###### Create key and certificate files

View create key and certificate files steps

Complete the following steps to generate key and certificate files:

1. Open a new terminal window and run the following command to list available elliptic curves and algorithms:
   
   ```shell
   openssl ecparam -list_curves
   ```
   
2. Generate a private key using the `prime256v1` elliptic curve:
   
   ```shell
   openssl ecparam -name prime256v1 -genkey -noout -out private-key.pem
   ```
   
3. Generate the corresponding public key from the private key:
   
   ```shell
   openssl ec -in private-key.pem -pubout -out public-key.pem
   ```
   
4. Self-sign the private key and generate a PEM certificate:
   
   ```shell
   openssl req -new -x509 -key private-key.pem -out cert.pem -days 365
   ```
   

###### Create a machine-to-machine certificate in NetSuite

View create a machine-to-machine certificate steps

Complete the following steps to create a machine-to-machine certificate in NetSuite:

1. Go to **Setup > Integration > OAuth 2.0 Client Credentials (M2M) Setup**.
   
2. Click **Create New**. The **Create a New Client Credentials Mapping** dialog appears.
   
3. Configure the following fields:
   
   - Entity
   - Select the entity that uses the client credentials. Refer to the NetSuite SOAP connector documentation to learn how to [set up an integration user](/en/connectors/netsuite/netsuite-connect#step-4).
   - Role
   - Choose the role that defines the permissions for the entity. Ensure the selected role has the necessary permissions for the integration. Refer to the NetSuite SOAP connector documentation to learn how to [create an integration role](/en/connectors/netsuite/netsuite-connect#step-3).
   - Application
   - Select the integration record you created previously.
   - Certificate
   - Upload the certificate you created previously. The file should be saved on your computer as `cert.pem`.
   
   > **CONFIGURATION FOR RECORD SEARCH**
   > 
   > You must configure the following prerequisites in NetSuite to use the [Search records](/en/connectors/netsuite-rest/search-records-action) action:
   > 
   > - Your account must have the **SuiteAnalytics Workbook** feature enabled.
   > - Your role must have the **SuiteAnalytics Workbook (View)** permission.
   > 
   > Refer to the NetSuite [Prerequisites and Setup for REST Web Services](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/article_5085602973.html#subsect_158219919831) guide for more information about the features and permissions required for REST Web Services.
   
   ![Create a new client credentials mapping](/assets/new-client-credentials-mapping.CXgKG4EU.png)_Create a new client credentials mapping_
   
4. Click **Save**.
   
5. Copy the **Certificate ID** and store it in a secure location. Workato requires this value to establish the NetSuite REST connection.
   
   ![Copy the Certificate ID](/assets/certificate-id.RrrJbYFc.png)_Copy the Certificate ID_
   

###### Connect to NetSuite REST with client credentials

View connect with client credentials steps

Complete the following steps to establish a connection using client credentials:

1. Enter a name for your NetSuite connection in the **Connection name** field.
   
   ![Connection fields](/assets/netsuite-rest-connect.ohtfw5sj.png)_Connect to NetSuite REST using client credentials_
   
2. Enter the folder or project where you plan to store your NetSuite connection in the **Location** field.
   
3. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
4. Enter your **Account ID**.
   
   Sign in to NetSuite as an Administrator and go to **Setup > Company > Company Information** to find your **Account ID**.
   
   You can also find it at the beginning of the NetSuite URL. For example, if the URL is `https://1234567.app.netsuite.com/`, your **Account ID** is `1234567`.
   
   > **SANDBOX ACCOUNT ID FORMAT**
   > 
   > You must replace underscores (`_`) with a hyphen (`-`) and capitalize letters if you are using a sandbox account. For example, `1234567_sb1` must be updated to `1234567-SB1`.
   
5. Enter the client ID you saved when you created your NetSuite integration record into the **Client ID** field.
   
6. Enter the private key you generated into the **EC Private Key** field. Ensure the key is in PEM format and has a length of 256, 384, or 521 bits.
   
   To extract the key, open the `private-key.pem` file and copy the text, starting from `-----BEGIN EC PRIVATE KEY-----` and ending with `-----END EC PRIVATE KEY-----`.
   
7. Enter the certificate ID from the machine-to-machine certificate you created in NetSuite into the **Certificate ID** field.
   
8. Optional. Click **Advanced settings > OAuth 2.0 scopes** and select a value.
   
   - Select OAuth 2.0 scopes and add them along with REST Web Services to define the minimum scope required for a NetSuite REST connection. You must enable the selected scopes in the corresponding integration record.
   
   ![Connection fields](/assets/scope-settings.DzESonA8.png)_Optional OAuth 2.0 scope settings_
   
9. Click **Connect**.
   

##### NetSuite authorization code grant authentication

View authorization code grant setup steps

###### Create a custom OAuth profile in Workato

View create a custom OAuth profile steps

Authorization code grant requires a custom OAuth profile with a valid client ID and client secret. Ensure your integration record in NetSuite supports authorization code grant and includes the required OAuth scopes. Use the following redirect URL when configuring the custom OAuth profile in Workato:

- `https://www.workato.com/oauth/callback`

Complete the following steps to create a custom OAuth profile:

1. Go to **Tools > Custom OAuth profiles** in Workato.
   
2. Click **\+ New custom profile**.
   
3. Select **NetSuite REST** in the **Application** field.
   
4. Enter a name for the custom OAuth profile in the **Name** field.
   
5. Copy the **Client ID** and **Client secret** from the integration record you created in NetSuite.
   
   ![Create a custom OAuth profile](/assets/create-oauth-profile-netsuite.BTL_WPnx.png)_Create a custom OAuth profile_
   
6. Paste the **Client ID** and **Client secret** into their respective fields.
   
7. Click **Save**.
   

###### Connect to NetSuite REST with authorization code grant

View connect with authorization code grant steps

Complete the following steps to establish a connection using authorization code grant:

1. Enter a name for your NetSuite connection in the **Connection name** field.
   
   ![Connection fields](/assets/netsuite-rest-connect-auth-code.DQojyKjp.png)_Connect to NetSuite REST using authorization code grant_
   
2. Enter the folder or project where you plan to store your NetSuite connection in the **Location** field.
   
3. Use the **Authentication type** drop-down menu to select **Authorization code grant**.
   
4. Enter your **Account ID**.
   
   Sign in to NetSuite as an Administrator and go to **Setup > Company > Company Information** to find your **Account ID**.
   
   You can also find it at the beginning of the NetSuite URL. For example, if the URL is `https://1234567.app.netsuite.com/`, your **Account ID** is `1234567`.
   
   > **SANDBOX ACCOUNT ID FORMAT**
   > 
   > You must replace underscores (`_`) with a hyphen (`-`) and capitalize letters if you are using a sandbox account. For example, `1234567_sb1` must be updated to `1234567-SB1`.
   
5. Optional. Expand **Advanced settings** and configure **OAuth 2.0 scopes** and the **NetSuite account timezone**.
   
6. Select your custom OAuth profile in the **Custom OAuth profile** field.
   
7. Click **Connect**.
   
8. Sign in to NetSuite and authorize access when prompted.
   

### Server configuration

Edit the **Server Configuration** recipe function in the project's **Functions** folder to control Coupa setup, vendor deduplication, document delivery, NetSuite vendor creation, and operational limits:

| Key | Description |
| --- | --- |
| `coupa_spend_currency` | Enter the currency used for estimated annual spend in Coupa. Defaults to `USD`. |
| `coupa_tax_easy_form_id` | Enter the Easy Form ID for the tax/general SIM form used for approval submission. |
| `coupa_banking_easy_form_id` | Enter the Easy Form ID for the banking form, if this deployment configures banking as a separate form from tax. |
| `coupa_approval_chain_configured` | Configure whether Coupa's approval chain for new suppliers is set up for this deployment. |
| `dedupe_name_normalization_rules` | Choose how vendor names are normalized before duplicate matching: stripping legal suffixes, collapsing whitespace, casefolding, and stripping punctuation. |
| `dedupe_candidate_query_strategy` | Choose which query strategies run when searching Coupa for duplicate candidates: exact match, starts with, contains, or merge-and-dedupe. |
| `dedupe_max_candidates_per_query` | Enter the cap on duplicate candidates each query retrieves. Defaults to `20`. |
| `docusign_composite_template_ids` | Enter the DocuSign template IDs combined into the single composite envelope sent to the vendor. |
| `docusign_recipient_role_name` | Enter the DocuSign recipient role name shared across all composite templates. Defaults to `Vendor`. |
| `docusign_envelope_expiration_days` | Enter the number of days before a sent DocuSign envelope expires. Defaults to `30`. |
| `docusign_form_data_mapping` | Map how DocuSign form fields correspond to Coupa SIM fields, including each field's type, whether it's required, how the server normalizes it, and match criteria. |
| `erp_netsuite_is_oneworld` | Configure whether the target NetSuite account is OneWorld. Defaults to `true`. |
| `erp_netsuite_subsidiary_id` | Enter the internal ID of the target subsidiary for new vendors. Required when `is_oneworld` is `true`. |
| `erp_netsuite_currency_map` | Map Coupa currency codes to NetSuite currency internal IDs. |
| `erp_netsuite_payment_terms_map` | Map Coupa payment term strings to NetSuite payment term internal IDs. |
| `erp_netsuite_default_vendor_category_id` | Enter the NetSuite vendor category internal ID to apply to every new vendor. |
| `erp_netsuite_default_1099_eligible_rule` | Choose the rule for setting `is1099Eligible` on the NetSuite vendor record. Defaults to deriving it from Coupa's tax classification field. |
| `erp_netsuite_initial_inactive` | Configure whether new NetSuite vendor records are created inactive until activation. Defaults to `true`. |
| `server_limits_max_pending_lookback_days` | Enter how many days back **list\_pending\_vendor\_onboardings** looks for in-flight onboardings. Defaults to `90`. |
| `server_limits_plan_token_ttl_seconds` | Enter how long a previewed plan stays valid before it expires and requires re-review. Defaults to `900` (15 minutes). |

View server configuration steps

Complete the following steps to configure the Vendor Onboarding MCP server:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Open the **Functions** folder, then open the **Server Configuration** recipe.
   
4. Edit the value in the step for the setting you plan to change. For example, lower `docusign_envelope_expiration_days` from `30` to `15`.
   
5. Save and start the recipe for the new value to take effect.
   

## How to use Vendor Onboarding MCP server tools

Refer to the following sections for detailed information on available tools:

### initiate\_vendor\_request tool

The **initiate\_vendor\_request** tool captures new-vendor intake details, checks for duplicates against existing Coupa suppliers, presents a preview for your approval, then creates the Supplier Information Management (SIM) record. Your LLM calls this tool once to capture the vendor's details, then calls it again after receiving your approval to create the SIM record.

**Try asking**:

- `Onboard Acme Corp as a new vendor.`
- `Set up Acme Industries LLC as a new supplier, with annual spend around $500,000 in IT services.`
- `Register this vendor even though a similar name already exists. It's a different company.`

### send\_vendor\_onboarding\_documents tool

The **send\_vendor\_onboarding\_documents** tool assembles a single composite DocuSign envelope combining tax forms (W-9/W-8) and supporting-document requests, presents a preview for your approval, then sends it to the vendor's contact. Your LLM calls this tool once to display the preview, then calls it again after receiving your approval to send the envelope.

**Try asking**:

- `Send the tax and insurance forms to Acme Corp.`
- `Send Acme their onboarding documents now.`
- `What documents will Acme receive, and when do they expire?`

### check\_vendor\_document\_status tool

The **check\_vendor\_document\_status** tool returns the DocuSign envelope's current status and, after the vendor completes it, the extracted form data and a document manifest. Your LLM uses this tool to check whether a vendor has signed and returned their documents. This tool is read-only.

**Try asking**:

- `Has Acme signed and returned their documents yet?`
- `Check the status of Acme's DocuSign envelope.`
- `What did Acme submit on their tax form?`

### import\_vendor\_form\_data tool

The **import\_vendor\_form\_data** tool downloads the vendor's completed documents from DocuSign, prepares the signer-entered form data for the Coupa SIM record, presents a preview with sensitive values masked, then writes the data and attaches the downloaded documents. Your LLM uses this tool in the following four call workflow:

1. **check\_vendor\_document\_status** reports an envelope is complete.
2. **get\_vendor\_write\_policy** maps the fields into a Coupa SIM write payload.
3. **import\_vendor\_form\_data** displays a preview of the payload.
4. **import\_vendor\_form\_data** commits the import after receiving your approval.

A signed envelope can return more fields than the deployment's mapping covers. The tool drops a field without a mapping entry instead of blocking the import, so confirm **get\_vendor\_write\_policy** covers every field you need, especially sensitive fields.

**Try asking**:

- `Import Acme's signed form data into their Coupa record.`
- `Write Acme's completed tax form into their vendor record.`
- `Show me what will be written to Acme's record before you import it.`

### check\_vendor\_bank\_details tool

The **check\_vendor\_bank\_details** tool checks whether the vendor has submitted banking details through Coupa's native Supplier Portal flow and returns masked account and routing numbers. Your LLM uses this tool to check on banking before submitting a vendor for approval. The tool is read-only and doesn't send a banking request to the vendor.

This tool reads a legacy SIM Easy Form Response. The server may not recognize a submission made through Coupa's newer Coupa Pay Payment Methods flow.

**Try asking**:

- `Check whether Acme's banking has come in yet.`
- `Has Acme submitted their bank details?`
- `Show me what banking information Acme has submitted so far.`

### submit\_vendor\_for\_approval tool

The **submit\_vendor\_for\_approval** tool identifies the vendor's Easy Form Response(s), presents a preview of the responses and spend amount for your approval, then submits them into Coupa's configured spend-based approval chain. Your LLM calls this tool once to display the preview, then calls it again after receiving your approval to submit. Coupa determines the approver from its own configured chain at submission time, so the preview doesn't name the approver.

**Try asking**:

- `Submit Acme's onboarding for approval.`
- `Send Acme's vendor record through Coupa approval.`
- `What spend amount will be submitted for Acme's approval?`

### create\_vendor\_master\_netsuite tool

The **create\_vendor\_master\_netsuite** tool prepares the fields needed to finalize the existing Coupa supplier and create the corresponding NetSuite vendor record, presents a preview for your approval, then writes to both systems, creating the vendor inactive in NetSuite until activation. Your LLM calls this tool once, after approval is complete, to display the preview, then calls it again after receiving your approval to commit the write. If a probable duplicate turns up at this stage, your LLM presents it and asks you how to proceed.

**Try asking**:

- `Create the vendor master record for Acme now that it's approved.`
- `What fields will be written to Coupa and NetSuite for Acme?`
- `Finalize Acme's supplier record and create their NetSuite vendor.`

### activate\_vendor\_for\_transactions tool

The **activate\_vendor\_for\_transactions** tool previews the status change for each system, including inactive to active in Coupa and NetSuite, and then activates the vendor in both apps. This makes the vendor eligible for transactions and payments. Your LLM calls this tool once, after the vendor master is created, to display the preview, then calls it again after receiving your approval to activate.

**Try asking**:

- `Activate Acme for transactions.`
- `Turn on Acme so we can start transacting with them.`
- `What changes when I activate Acme in Coupa and NetSuite?`

### list\_pending\_vendor\_onboardings tool

The **list\_pending\_vendor\_onboardings** tool returns a paginated list of the in-flight vendor onboardings you initiated, grouped by why each vendor onboarding is stalled. Your LLM uses this tool when you ask what's outstanding or which vendors are stuck. This tool is read-only.

**Try asking**:

- `Which vendor onboardings are stuck waiting on the vendor?`
- `Show me what's outstanding in my vendor onboarding queue.`
- `List onboardings that are waiting on approval.`

### get\_vendor\_onboarding\_status tool

The **get\_vendor\_onboarding\_status** tool returns the full status of a vendor's onboarding across Coupa, DocuSign, and NetSuite, including the current blocker, if any, and who owes the next action. Your LLM uses this tool when you ask about a specific vendor's progress. This tool is read-only.

**Try asking**:

- `What's the status of the Acme onboarding?`
- `What's holding up Acme's onboarding?`
- `Who still needs to act on Acme's vendor approval?`

### get\_vendor\_write\_policy tool

The **get\_vendor\_write\_policy** tool returns the deployment's configured [`docusign_form_data_mapping`](#server-configuration) setting, which contains the field mapping, types, and sensitivity flags. The tool also returns a fixed list of fields **import\_vendor\_form\_data** rejects, regardless of configuration. Your LLM calls this tool before writing using the **import\_vendor\_form\_data** tool. This tool is read-only.

**Try asking**:

- `What fields will be written when I import Acme's documents?`
- `Which of Acme's submitted fields are treated as sensitive?`
- `Show me the write policy this server uses for importing vendor data.`

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/waterfall-lead-enrichment-mcp-server.md
description: >-
  Use the Waterfall Lead Enrichment MCP server to connect your LLM to ZoomInfo,
  Apollo.io, and LeadIQ with confidence-scored, auditable lead enrichment
  through natural conversation.
---

# Waterfall Lead Enrichment MCP server

The Waterfall Lead Enrichment MCP server enables LLMs to enrich lead records with ZoomInfo, Apollo.io, and LeadIQ through natural conversation. It provides tools to run an enrichment waterfall across all three providers, call a single provider directly, merge results into a confidence-scored lead, and review a merged record in an [MCP app](/en/mcp/mcp-apps) before storing it.

## Uses

Use the Waterfall Lead Enrichment MCP server to perform the following actions:

- Enrich a lead by running the full waterfall across ZoomInfo, Apollo.io, and LeadIQ in that order, and merging the results into one confidence-scored record
- Enrich a lead through a single named provider without running the full waterfall
- Look up a lead by email or LinkedIn URL, and optionally add a name or company to improve match accuracy
- Override the default provider priority for the whole merged record or for individual fields
- Re-enrich a lead whose previous enrichment result is no longer available

Additionally, use the server's built-in [Waterfall Lead Enrichment MCP app](#waterfall-lead-enrichment-mcp-app) to review and edit results.

### Example prompts

Use the following example prompts to invoke Waterfall Lead Enrichment MCP server tools:

- `Enrich this lead: ariel@example.com.`
- `Run the full enrichment waterfall for jade@example.com.`
- `Enrich this contact using only ZoomInfo.`
- `Look up this lead in Apollo.io: dana@example.com.`
- `Get this person's mobile number from LeadIQ.`
- `Enrich the lead at this LinkedIn URL: linkedin.com/in/example-name.`
- `Why did this lead come back as low confidence?`
- `Enrich this lead and use company name and domain to improve the match: Acme Corp, acme.com.`
- `Show me the confidence score and providers used for this enriched lead.`
- `Re-enrich this lead. The last enrichment result expired.`

## Waterfall Lead Enrichment MCP server tools

The Waterfall Lead Enrichment MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [enrich\_via\_zoominfo](#enrich-via-zoominfo-tool) | Calls ZoomInfo to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. |
| [enrich\_via\_apollo](#enrich-via-apollo-tool) | Calls Apollo.io to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. |
| [enrich\_via\_leadiq](#enrich-via-leadiq-tool) | Calls LeadIQ to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. |
| [enrich\_lead](#enrich-lead-tool) | Merges the ZoomInfo, Apollo.io, and LeadIQ results for a lead into one confidence-scored record and evaluates it against the enrichment threshold, without calling the provider APIs itself. |

Don't call the `manage_enriched_lead_data` tool directly. The [Waterfall Lead Enrichment MCP app](#waterfall-lead-enrichment-mcp-app) uses it to fetch, normalize, and store records on your behalf.

## Install the Waterfall Lead Enrichment MCP server

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
    

## Waterfall Lead Enrichment connection setup

View Waterfall Lead Enrichment connection setup steps

This MCP server requires three separate connections: ZoomInfo, Apollo.io, and LeadIQ. Each connection uses its own credentials. The waterfall continues if a provider's connection fails or the account isn't found, and that provider contributes a null result to the merged record.

### ZoomInfo connection

View ZoomInfo connection setup steps

Complete the following steps to set up your ZoomInfo connection:

> **REQUIRED ZOOMINFO PERMISSIONS**
> 
> Your ZoomInfo account must have [ZoomInfo API](https://docs.zoominfo.com/reference/overview) access permissions to connect to Workato.

1. Enter a name for your connection in the **Connection name** field.
   
   ![Set up your ZoomInfo connection](/assets/zoominfo.BGW04mkl.png)_Set up your ZoomInfo connection_
   
2. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
3. Enter your ZoomInfo username in the **Username** field.
   
4. Enter your ZoomInfo password in the **Password** field.
   
5. Click **Connect**.
   

### Apollo.io connection

View Apollo.io connection setup steps

Complete the following steps to set up your Apollo.io connection:

1. Enter a name for your connection in the **Connection name** field.
   
2. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
3. Sign in to the Apollo [Developer portal](https://developer.apollo.io/) and select **API Keys**. Copy an existing key or create a new one.
   
4. Paste the value into the **API key** field.
   
5. Click **Connect**.
   

### LeadIQ connection

View LeadIQ connection setup steps

Complete the following steps to set up your LeadIQ connection:

1. Enter a name for your connection in the **Connection name** field.
   
2. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
3. Sign in to LeadIQ and go to **Settings > API Keys**.
   
4. Copy the **Secret base64** value.
   
5. Paste the value into the **Secret base64 API Key (from LeadIQ)** field.
   
6. Click **Connect**.
   

### Configuration options

Use the following resources to configure the Waterfall Lead Enrichment MCP server:

- The [project properties](#project-property-configuration) control how the server processes a record's fields.
- The [Provider waterfall order](#data-table-configuration) data table sets the default order providers run in.

#### Project property configuration

Edit the following project properties to control how the server processes a record's fields:

| Project-level property | Description |
| --- | --- |
| `lead_enrichment_required_fields` | Enter a comma-separated list of fields that must be present for a record to reach `enriched` status. Defaults to `work_email, first_name, last_name, job_title, company_name`. |
| `lead_enrichment_desired_fields` | Enter a comma-separated list of fields that count toward confidence scoring but aren't required for `enriched` status. Defaults to `company_size, direct_phone, mobile_phone, linkedin_url, industry, company_revenue_range, company_domain, seniority_level`. |

View project-level property configuration steps

Complete the following steps to configure your project-level properties:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the project property you plan to update and click the **Edit** (pencil) icon.
   
6. Go to the **Value** field and make your changes. For example, set `lead_enrichment_required_fields` to `work_email, company_name`.
   

#### Data table configuration

Edit the **Provider waterfall order** data table to configure the default provider order:

| Column | Description |
| --- | --- |
| `priority` | Enter this row's position in the waterfall call sequence. For example, enter `1` to call this row first. |
| `provider` | Enter the default provider to use for the row's `priority` level. Options include: `ZoomInfo`, `Apollo`, or `LeadIQ`. |
| `work_email`, `first_name`, `last_name`, `job_title`, `company_name`, `company_size`, `direct_phone`, `mobile_phone`, `linkedin_url`, `industry`, `company_revenue_range`, `company_domain`, `seniority_level` | Enter the name of a provider to use for this field and priority level. Leave a column blank to use the row's `provider`. |

View data table configuration steps

Complete the following steps to configure settings using the MCP's data table:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Select the **Provider waterfall order** data table.
   
4. [Edit](/en/data-tables/user-interface/edit#edit-a-row) a row's `priority` to reorder the providers. For example, set the priority for LeadIQ to `1` to call it first.
   

## How to use Waterfall Lead Enrichment MCP server tools

Refer to the following sections for detailed information on available tools. All three provider tools accept a first name, last name, company name, or company domain to speed up or improve the match, and a provider error or missing match contributes a null result instead of stopping the waterfall.

### enrich\_via\_zoominfo tool

The **enrich\_via\_zoominfo** tool calls ZoomInfo to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. Your LLM calls this tool first in a waterfall enrichment, or calls it alone and returns the result directly when you name ZoomInfo specifically.

**Try asking**:

- `Enrich this lead: ariel@example.com.`
- `Look up this contact in ZoomInfo only.`
- `Run the full enrichment waterfall for this lead.`
- `Enrich this lead in ZoomInfo and add company name and domain to improve the match: Acme Corp, acme.com.`

### enrich\_via\_apollo tool

The **enrich\_via\_apollo** tool calls Apollo.io to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. Your LLM calls this tool second in a waterfall enrichment, after **enrich\_via\_zoominfo**, or calls it alone and returns the result directly when you name Apollo.io specifically.

**Try asking**:

- `Get this lead's details from Apollo.io only.`
- `Enrich dana@example.com using Apollo.io.`
- `Run the enrichment waterfall for this contact.`
- `Enrich this lead in Apollo.io and add a first and last name to improve the match.`

### enrich\_via\_leadiq tool

The **enrich\_via\_leadiq** tool calls LeadIQ to enrich a lead by email or LinkedIn URL and writes the normalized result to the shared enrichment record. Your LLM calls this tool third in a waterfall enrichment, after **enrich\_via\_zoominfo** and **enrich\_via\_apollo**, or calls it alone and returns the result directly when you name LeadIQ specifically.

**Try asking**:

- `Find this person's mobile number through LeadIQ.`
- `Enrich this lead using only LeadIQ.`
- `What's this contact's job title according to LinkedIn?`
- `Enrich this lead in LeadIQ and add the company name to improve the match: Acme Corp.`

### enrich\_lead tool

The **enrich\_lead** tool merges the ZoomInfo, Apollo.io, and LeadIQ results for a lead into one confidence-scored record and evaluates it against the enrichment threshold, without calling the provider APIs itself. Your LLM calls this tool last, after all three provider tools have run with the same email or LinkedIn URL, and only when you haven't named a specific provider. The [Waterfall Lead Enrichment MCP app](#waterfall-lead-enrichment-mcp-app) opens for review after the tool returns.

Enrichment threshold and record status

The enrichment threshold is a confidence-score cutoff that contributes to a record's status. Records can have the following statuses:

- `enriched`: The score meets the threshold and all required fields are present.
- `low_confidence`: The score falls short or a required field is missing.
- `not_found`: No provider returned a match.

Default field-level merge precedence

Each field falls back to a default winning provider unless you override it:

| Field | Default winning provider |
| --- | --- |
| `work_email` | ZoomInfo |
| `direct_phone` | ZoomInfo |
| `mobile_phone` | LeadIQ |
| `job_title` | LeadIQ (LinkedIn-sourced) |
| `company_name` | ZoomInfo |
| `company_size` | ZoomInfo |
| `seniority_level` | Inferred from `job_title` |
| All other fields | First non-null value found during the waterfall |

**Try asking**:

- `Merge the provider results and give me the enriched lead.`
- `Enrich this lead and prioritize LeadIQ over ZoomInfo for the phone number.`
- `What's the confidence score and status for this lead?`
- `Why did this lead come back as low confidence?`

## Waterfall Lead Enrichment MCP app

The Waterfall Lead Enrichment [MCP app](/en/mcp/mcp-apps) opens for review after `enrich_lead` returns. It displays the results from each provider, the merged enrichment record, and a normalized version of the merged record so you can review and modify each value. Accept the record to store it back to the shared enrichment record.

> **RECORD RETENTION PERIOD**
> 
> The server automatically deletes stored enrichment records after 30 days, so a lead whose previous result has expired needs re-enrichment.

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/databricks-data-explorer-mcp-server.md
description: >-
  The Databricks Data Explorer MCP server lets LLMs explore Unity Catalog
  tables, retrieve schemas, and run read-only SQL queries through conversation.
---

# Databricks Data Explorer MCP server

The Databricks Data Explorer MCP server enables LLMs to discover and retrieve structured data from Databricks environments governed by Unity Catalog through natural conversation. It provides tools to explore catalogs, discover tables, retrieve schema information, and run read-only queries using Unity Catalog without requiring direct interaction with the Databricks interface. Row quotas, timeouts, and concurrency quotas are applied.

## Uses

Use the Databricks Data Explorer MCP server to perform the following actions:

- Discover catalogs, schemas, tables, and views in Unity Catalog
- Search for tables by name or keyword across your data catalog
- Retrieve column definitions and table metadata
- Retrieve sample data to understand table structure and content
- Execute bounded `SELECT` queries against a designated SQL Warehouse
- Run read-only queries with automatic row quotas and timeouts
- Check execution status of long-running queries
- Retrieve results from completed asynchronous queries

### Example prompts

Use the following example prompts to invoke Databricks Data Explorer MCP server tools:

- `What catalogs are available in Databricks?`
- `Show me the schemas in the sales_data catalog.`
- `What tables exist in the customer_analytics schema?`
- `Find tables related to subscriptions.`
- `What columns are in the customer_events table?`
- `Show me a sample of data from the activity_logs table.`
- `Query the top 100 customers by revenue from last quarter.`
- `Get the status of my running query.`

## Databricks Data Explorer MCP server tools

The Databricks Data Explorer MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_catalogs](#list-catalogs-tool) | Lists available Unity Catalog catalogs. |
| [list\_schemas](#list-schemas-tool) | Lists schemas within a specified Unity Catalog catalog. |
| [list\_tables](#list-tables-tool) | Lists tables and views within a specified schema. |
| [search\_tables](#search-tables-tool) | Searches Unity Catalog tables by name or keyword. |
| [get\_table\_schema](#get-table-schema-tool) | Retrieves column definitions and metadata for a specified table. |
| [get\_table\_sample](#get-table-sample-tool) | Returns a bounded sample of rows from a table you specify. |
| [execute\_query](#execute-query-tool) | Executes a read-only SQL `SELECT` query against the configured SQL warehouse. |
| [get\_query\_status](#get-query-status-tool) | Retrieves execution status of a previously submitted asynchronous query. |
| [get\_query\_results](#get-query-results-tool) | Retrieves results of a completed asynchronous query. |

## Install the Databricks Data Explorer MCP server

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
    

## Databricks connection setup

View Databricks connection setup steps

The Databricks connector supports the following authentication types:

- [OAuth 2.0 (Service Principal)](#oauth2)
- [Personal access token](#personal-access-token)

> **USERNAME/PASSWORD AUTHENTICATION DEPRECATED**
> 
> As of July 2024, basic username/password authentication for Databricks is deprecated. Refer to the Databricks [End of life for Databricks-managed passwords](https://docs.databricks.com/aws/en/release-notes/product/2024/july#end-of-life-for-databricks-managed-passwords) documentation for more information.

### OAuth 2.0 (Service Principal) authentication

View OAuth 2.0 (Service Principal) authentication steps

You must generate the following values from Databricks to use this authentication method:

- Client ID
- Secret

#### Databricks setup for OAuth 2.0 (Service Principal) authentication

You must create a service principal to generate a client ID and secret.

##### Create a service principal

View create a service principal steps

Complete the following steps to create a service principal in Databricks:

1. As an account admin, log in to the [Account console](https://accounts.cloud.databricks.com/).
   
2. Click **Users & groups**.
   
3. Click the **Service principals** tab.
   
4. Click **Add service principal**.
   
5. Enter a name in the **New service principal display name** field.
   
6. Click **Add service principal**.
   
7. Click the **Credentials & secrets** tab.
   
8. Click **Generate secret** under the **OAuth secrets** section.
   
9. Enter the number of days in the **Lifetime (days)** field.
   
10. Click **Generate**.
    
11. Copy and save the **Secret** and **Client ID** for use in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The secret is only displayed once. If you lose it, you must create a new one.
    

#### Connect to Databricks with OAuth 2.0 (Service Principal) authentication

View connect to Databricks with OAuth 2.0 (Service Principal) steps

Complete the following steps to set up an OAuth 2.0 (Service Principal) authentication connection to Databricks in Workato:

1. Click **Create > Connection**.
   
2. Search for `Databricks` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Databricks overview](/assets/databricks-connect.B8QqhpyM.png)_Connect to Databricks_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the name of your server in the **Server hostname** field. For example, `example.cloud.databricks.com`.
   
6. Enter the **HTTP path**. For example, `sql/protocolv1/o/3957355953478232/0710-102114-bfnouzcv`.
   
7. Enter the **Port** your server uses. The default is `443`.
   
   > **CONNECTION DETAILS**
   > 
   > Refer to the Databricks [Get connection details for a Databricks compute resource](https://docs.databricks.com/aws/en/integrations/compute-details) documentation for information on how to retrieve connection details such as **Server hostname**, **HTTP path**, and **Port**.
   
8. Optional. Use the **Catalog** drop-down menu to select the catalog you plan to use for this connection. The default value is `hive_metastore`.
   
9. Optional. Use the **Schema** drop-down menu to select the schema you plan to use for this connection. The default value is `default`.
   
10. Optional. Use the **Database timezone** drop-down menu to select the timezone you plan to use. Workato uses this to convert timestamps during reads and writes.
    
11. Use the **Authentication type** drop-down menu to select **OAuth 2.0 (Service Principal)**.
    
12. Use the **Account type** drop-down menu to select the account type you plan to use.
    
13. Enter your **Client ID** and **Client secret**. Refer to [Create a service principal](#create-service-principal) for more information.
    
14. Optional. Select one or more **Scope** values from the drop-down menu. Workato uses the `sql` scope by default if none are selected.
    
15. Click **Connect**.
    

### Personal access token authentication

View personal access token authentication steps

You must generate the following value from Databricks to use this authentication method:

- Personal access token

#### Databricks setup for personal access token authentication

Generate a personal access token from a Databricks workspace.

##### Generate a personal access token

View generate a personal access token steps

Complete the following steps to create a personal access token in Databricks:

1. In your Databricks workspace, click your username and select **Settings**.
   
2. Click **Developer**.
   
3. Click **Manage** next to **Access tokens**.
   
4. Click **Generate new token**.
   
5. Enter a comment in the **Comment** field.
   
6. Enter the number of days in the **Lifetime (days)** field.
   
7. Select a **Scope**.
   
8. Select scopes from the **API scope(s)** drop-down menu.
   
9. Click **Generate**.
   
10. Copy and save the token for use in Workato.
    
    > **SAVE YOUR CREDENTIALS**
    > 
    > The token is only displayed once. If you lose it, you must create a new one.
    

#### Connect to Databricks with personal access token authentication

View connect to Databricks with personal access token steps

Complete the following steps to set up a personal access token authentication connection to Databricks in Workato:

1. Click **Create > Connection**.
   
2. Search for `Databricks` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Databricks overview](/assets/databricks-connect.B8QqhpyM.png)_Connect to Databricks_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the name of your server in the **Server hostname** field. For example, `example.cloud.databricks.com`.
   
6. Enter the **HTTP path**. For example, `sql/protocolv1/o/3957355953478232/0710-102114-bfnouzcv`.
   
7. Enter the **Port** your server uses. The default is `443`.
   
   > **CONNECTION DETAILS**
   > 
   > Refer to the Databricks [Get connection details for a Databricks compute resource](https://docs.databricks.com/aws/en/integrations/compute-details) documentation for information on how to retrieve connection details such as **Server hostname**, **HTTP path**, and **Port**.
   
8. Optional. Use the **Catalog** drop-down menu to select the catalog you plan to use for this connection. The default value is `hive_metastore`.
   
9. Optional. Use the **Schema** drop-down menu to select the schema you plan to use for this connection. The default value is `default`.
   
10. Optional. Use the **Database timezone** drop-down menu to select the timezone you plan to use. Workato uses this to convert timestamps during reads and writes.
    
11. Use the **Authentication type** drop-down menu to select **Personal Access Token**.
    
12. Enter your **Personal Access Token**. Refer to [Generate a personal access token](#generate-personal-access-token) for more information.
    
13. Click **Connect**.
    

## How to use Databricks Data Explorer MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_catalogs tool

The **list\_catalogs** tool lists available Unity Catalog catalogs. Your LLM uses this tool to identify available top-level data groupings before locating schemas or tables.

**Try asking**:

- `What catalogs are available in Databricks?`
- `Show me all the data catalogs I can access.`
- `List the top-level catalogs in Unity Catalog.`
- `What data groupings exist in my Databricks environment?`

### list\_schemas tool

The **list\_schemas** tool lists schemas within a Unity Catalog catalog you specify. Your LLM uses this tool to identify namespaces within a known catalog before locating tables.

**Try asking**:

- `Show me the schemas in the sales_data catalog.`
- `What schemas exist in the analytics catalog?`
- `List all schemas in the customer_data catalog.`
- `What namespaces are available in this catalog?`

### list\_tables tool

The **list\_tables** tool lists tables and views within a schema you specify. Your LLM uses this tool to discover candidate tables before constructing a query.

**Try asking**:

- `What tables exist in the customer_analytics schema?`
- `Show me all tables and views in the sales schema.`
- `List the available tables in customer_data.raw_events.`
- `What tables can I query in this schema?`

### search\_tables tool

The **search\_tables** tool searches Unity Catalog tables by name or keyword. Your LLM uses this tool to find tables based on business concepts when table names are unknown.

**Try asking**:

- `Find tables related to subscriptions.`
- `Search for tables containing customer activity data.`
- `Look for tables about support tickets.`
- `Find any tables with 'revenue' in the name.`

### get\_table\_schema tool

The **get\_table\_schema** tool retrieves column definitions and metadata for a table you specify. Your LLM uses this tool to understand table structure, column types, and available descriptions before constructing a SQL query.

**Try asking**:

- `What columns are in the customer_events table?`
- `Show me the schema for the sales.transactions table.`
- `What's the structure of the activity_logs table?`
- `Get the column definitions for the subscription_data table.`

### get\_table\_sample tool

The **get\_table\_sample** tool returns a bounded sample of rows from a table you specify. Your LLM uses this tool to understand the shape or typical values of a dataset without retrieving the full dataset.

**Try asking**:

- `Show me a sample of data from the activity_logs table.`
- `Get some example rows from the customer_events table.`
- `What does the data in the transactions table look like?`
- `Show me a few sample records from the subscriptions table.`

### execute\_query tool

The **execute\_query** tool executes a read-only SQL `SELECT` query against the configured SQL warehouse with automatic row quotas and timeouts. Your LLM uses this tool to retrieve structured data in response to business questions.

**Try asking**:

- `Query the top 100 customers by revenue from last quarter.`
- `Get all active subscriptions created in the last 30 days.`
- `Show me support tickets opened this week by priority.`
- `Find the total sales by region for January 2026.`

### get\_query\_status tool

The **get\_query\_status** tool retrieves execution status of a previously submitted asynchronous query. Your LLM uses this tool only when `execute_query` returns a `query_id`, indicating asynchronous execution.

**Try asking**:

- `Get the status of my running query.`
- `Check if my query has completed.`
- `What's the execution status of query jfsialsk32s?`
- `Is my data retrieval query still running?`

### get\_query\_results tool

The **get\_query\_results** tool retrieves results of a completed asynchronous query. Your LLM uses this tool after `get_query_status` indicates that execution has completed.

**Try asking**:

- `Get the results of my completed query.`
- `Show me the data from query 9dsdlkdsl.`
- `Retrieve the results of the customer analysis query.`
- `What did my query return?`

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/mailchimp-marketing-reports-mcp-server.md
description: >-
  Use the MailChimp Marketing Reports MCP server to let your LLM perform
  read-only discovery and analytics across audiences, campaigns, and contacts.
---

# MailChimp Marketing Reports MCP server

The MailChimp Marketing Reports MCP server enables LLMs to interact with MailChimp through natural conversation. It provides tools to discover audiences, campaigns, and contacts, and report on campaign performance, subscriber engagement, and audience health without requiring direct interaction with the MailChimp interface.

> **CAMPAIGN MANAGEMENT MCP SERVER**
> 
> This MCP server is read-only. Use the [MailChimp Campaign Management](/en/mcp/prebuilt-mcps/mailchimp-campaign-management-mcp-server) MCP server to create, update, send, schedule, or delete content.

## Uses

Use the MailChimp Marketing Reports MCP server to perform the following actions:

- Discover audiences (lists) in the account, including member counts.
- List campaigns and filter them by draft, scheduled, or sent status.
- Retrieve a specific campaign's settings and content for review.
- Search for a contact by email address or name across the account or within an audience.
- Analyze a sent campaign's performance, including opens, clicks, click-through rate, bounces, and unsubscribes.
- Review an individual subscriber's engagement activity across campaigns.
- Assess an audience's health through recent aggregated activity and month-by-month growth history.

### Example prompts

Use the following example prompts to invoke MailChimp Marketing Reports MCP server tools:

- `Show me all the audiences in my MailChimp account.`
- `List my draft campaigns.`
- `Which campaigns are scheduled to send this week?`
- `Show me the settings and content for my launch campaign.`
- `Find the contact for lee@example.com in my newsletter audience.`
- `How did last week's campaign perform?`
- `What's this subscriber's engagement history across our campaigns?`
- `Is my main list growing?`
- `Show me the audience health for my newsletter list.`
- `Compare the open rates on my last two campaigns.`

## MailChimp Marketing Reports MCP server tools

The MailChimp Marketing Reports MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [list\_audiences](#list-audiences-tool) | Lists the audiences (lists) in the MailChimp account. |
| [list\_campaigns](#list-campaigns-tool) | Lists campaigns in the account, with optional status filtering. |
| [get\_campaign](#get-campaign-tool) | Retrieves a single campaign's settings and content. |
| [search\_contacts](#search-contacts-tool) | Searches for contacts by email address or name, optionally within an audience. |
| [get\_campaign\_report](#get-campaign-report-tool) | Retrieves performance metrics for a sent campaign. |
| [get\_subscriber\_activity](#get-subscriber-activity-tool) | Retrieves one contact's engagement activity on an audience. |
| [get\_audience\_health](#get-audience-health-tool) | Retrieves audience growth and aggregated activity over time. |

## Install the MailChimp Marketing Reports MCP server

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
    

## API version

Workato's MailChimp connector uses MailChimp's API v2. Refer to MailChimp's [API documentation](https://mailchimp.com/developer/marketing/docs/fundamentals/#api-versions) for more information.

## MailChimp Marketing Reports connection setup

View MailChimp Marketing Reports connection setup steps

Complete the following steps to connect to MailChimp in Workato:

> **FEATURE AVAILABILITY**
> 
> The MailChimp connector isn't available to workspaces in the CN data center. This reflects local regulatory requirements and applies to our multi-tenant and [Virtual Private Workato (VPW)](/en/cloud-hosting-editions/hosting-editions#virtual-private-workato) offerings.

1. Provide a **Connection name** that identifies which MailChimp instance Workato is connected to.
   
   ![MailChimp connection](/assets/connection-setup.DX-BBZvF.png)_Create your connection_
   
2. Use the **Location** drop-down menu to select a location for your connection.
   
3. Click **Connect**. This opens a MailChimp login window.
   
4. Enter your MailChimp account username and password. A window opens displaying a summary of the access Workato is provided with for the connection.
   
5. Click **Accept** to complete the connection setup.
   

### MailChimp role requirements

Each tool's availability depends on the authenticating user's MailChimp role. A user without the required role receives a permission-denied outcome rather than a partial result. Refer to the MailChimp [Manage User Levels in Your Account](https://mailchimp.com/help/manage-user-levels-in-your-account/) guide for the complete list of role capabilities.

## How to use MailChimp Marketing Reports MCP server tools

Refer to the following sections for detailed information on available tools:

### list\_audiences tool

The **list\_audiences** tool lists the audiences (lists) in the MailChimp account. Your LLM uses this tool to return audiences with their identifiers, names, and member counts so it can choose the right audience to inspect or analyze, typically before searching contacts or checking audience health for a list that isn't yet resolved.

**Try asking**:

- `Show me all the audiences in my MailChimp account.`
- `Which lists do I have and how many contacts are in each?`
- `Find the audience I should look up for this report.`

### list\_campaigns tool

The **list\_campaigns** tool lists campaigns in the account, with optional status filtering. Your LLM uses this tool to return campaigns with their identifiers, titles, subjects, status, and target audience so it can find a campaign to inspect or analyze, filtering by status when you specify drafts, scheduled, or sent campaigns.

**Try asking**:

- `List my sent campaigns from last month.`
- `Which campaigns are still in draft?`
- `Show me all my scheduled campaigns.`

### get\_campaign tool

The **get\_campaign** tool retrieves a single campaign's settings and content. Your LLM uses this tool to confirm a campaign's subject, sender, recipient audience, status, and current content when you reference a specific campaign, typically before analyzing its performance.

**Try asking**:

- `Show me the details of my launch campaign.`
- `What was the subject and sender on last week's campaign?`
- `What content did I send in this campaign?`

### search\_contacts tool

The **search\_contacts** tool searches for contacts by email or name, optionally within a specific audience. Your LLM uses this tool to confirm whether a contact exists or to resolve a contact's identifier before checking their engagement activity. You can limit the search to a specific audience or search the entire account.

**Try asking**:

- `Find the contact for lee@example.com.`
- `Search for contacts named Smith in my newsletter audience.`
- `Is this person already in my launch list?`

### get\_campaign\_report tool

The **get\_campaign\_report** tool retrieves performance metrics for a sent campaign. Your LLM uses this tool to report opens, clicks, click-through rate, bounces, unsubscribes, and related figures for one sent campaign so you can evaluate how it performed. A report is available only once a campaign has sent.

**Try asking**:

- `How did my launch campaign perform?`
- `What's the open and click rate on last week's newsletter?`
- `Compare the bounce rates on these two sent campaigns.`

### get\_subscriber\_activity tool

The **get\_subscriber\_activity** tool retrieves one contact's engagement activity. Your LLM uses this tool to report a specific contact's opens, clicks, and unsubscribes across campaigns, resolving the audience and contact first if their identifiers are unknown.

**Try asking**:

- `How has lee@example.com engaged with our campaigns?`
- `Show me this subscriber's click history.`
- `Has this contact opened any of our recent emails?`

### get\_audience\_health tool

The **get\_audience\_health** tool retrieves audience growth and aggregated activity over time. Your LLM uses this tool to report recent aggregated activity (signups, unsubscribes, sends, opens, clicks) and month-by-month growth history for a whole audience so you can see whether it's growing and engaged.

**Try asking**:

- `Is my newsletter audience growing?`
- `Show me the engagement trend for my main list.`
- `How healthy is my launch audience right now?`

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

---

---
url: >-
  https://docs.workato.com/en/mcp/prebuilt-mcps/namely-workforce-intelligence-mcp-server.md
description: >-
  Use the Namely Workforce Intelligence MCP server to connect your LLM to Namely
  with a curated set of tools to search employees, analyze organizational
  hierarchy, aggregate workforce metrics, and perform administrative updates.
---

# Namely Workforce Intelligence MCP server

The Namely Workforce Intelligence MCP server enables LLMs to explore workforce structure, composition, and employee data at an organizational level. It provides tools to search employees, analyze organizational hierarchy, aggregate workforce metrics, and perform administrative updates through natural conversation.

## Uses

Use the Namely Workforce Intelligence MCP server when you plan to perform the following actions:

- Search for employees by name, department, location, or other attributes
- Analyze organizational hierarchy and reporting structures
- Review comprehensive employee profiles including direct reports
- Update employee profile information such as job title, department, or location
- Change reporting relationships and reassign employees to new managers
- Retrieve lists of all job titles in the organization
- Aggregate workforce metrics and demographics
- Prepare org charts or leadership briefings
- Support people analytics and workforce planning initiatives

### Example prompts

Use the following example prompts to invoke Namely Workforce Intelligence MCP server tools:

- `Who reports to Sarah Chen in the Engineering department?`
- `Find all employees in the San Francisco office.`
- `Show me everyone with 'Senior Manager' in their title.`
- `Who are the direct reports for the VP of Product?`
- `List all employees in the Marketing department.`
- `Get me the full reporting chain for Alex Johnson.`
- `Update Maria Rodriguez's job title to 'Director of Operations'.`
- `Change Jordan Kim's manager to Michael Torres.`
- `What job titles exist in our organization?`

## Namely Workforce Intelligence MCP server tools

The Namely Workforce Intelligence MCP server provides the following tools:

| Tool | Description |
| --- | --- |
| [search\_employees](#search-employees-tool) | Searches for employees matching the criteria you specify and returns profile information with organizational context. |
| [get\_employee\_detail](#get-employee-detail-tool) | Retrieves comprehensive profile information for a single employee, including direct reports if applicable. |
| [update\_employee](#update-employee-tool) | Updates specified fields on an employee's profile. |
| [update\_reporting\_relationship](#update-reporting-relationship-tool) | Changes an employee's manager to a new manager. |
| [get\_all\_job\_titles](#get-all-job-titles-tool) | Returns a list of all job titles in the organization. |

## Install the Namely Workforce Intelligence MCP server

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
    

## Namely connection setup

View Namely connection setup steps

Complete the following steps to connect to Namely in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Namely` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connection setup](/assets/connection-setup-updated.D3Nc3waz.png)_Namely connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the company account name you plan to connect to your Workato account in the **Company** field. You can find this name in your Namely URL. For example, if your URL is `http://acme.namely.com`, enter `acme` in this field.
   
6. Optional. Use the **Custom OAuth profile** drop-down menu to select a custom OAuth profile for your connection.
   
7. Click **Connect**.
   
8. Click **Allow** when prompted to authorize Workato to access your Namely account.
   

### Project property configuration

You must configure the default timezone for your Namely Workforce Intelligence MCP server at the project level.

View Project property configuration steps

Complete the following steps to configure your timezone:

1. Sign in to your Workato account and go to **Projects**.
   
2. Go to the project that contains your MCP server.
   
3. Click the **Settings** tab.
   
   ![Click the Settings tab](/assets/project-settings.99X6TiYd.png)_Click the **Settings** tab._
   
4. Select **Project properties**.
   
5. Go to the **MCP\_DEFAULT\_TIMEZONE** property and click the **Edit** (pencil) icon.
   
   ![Click the Edit (pencil) icon](/assets/edit-timezone.CiilJ_dZ.png)_Click the **Edit** (pencil) icon._
   
6. Go to the **Value** field and enter your timezone. For example: `US/Pacific`, `Australia/Sydney`, `Asia/Kolkata`, or `Europe/London`.
   

## How to use Namely Workforce Intelligence MCP server tools

Refer to the following sections for detailed information on available tools:

### search\_employees tool

The **search\_employees** tool searches for employees matching the criteria you specify and returns profile information with organizational context. Your LLM uses this tool to find colleagues in the directory, locate employees by department or location, or build lists of employees based on specific attributes.

**Try asking**:

- `Find all employees in the Engineering department.`
- `Search for everyone with 'Manager' in their job title.`
- `Who works in the New York office?`
- `Show me all employees who report to the VP of Sales.`

### get\_employee\_detail tool

The **get\_employee\_detail** tool retrieves comprehensive profile information for a single employee. It includes the employee's full reporting chain and direct reports when applicable. Your LLM uses this tool after identifying the right person through search, or when you need detailed information about an employee's role, tenure, organizational position, and team structure.

**Try asking**:

- `Tell me everything about Sarah Chen.`
- `Who does Alex Johnson report to all the way up to the CEO?`
- `Get the full profile and reporting structure for Maria Rodriguez.`

### update\_employee tool

The **update\_employee** tool updates specified fields on an employee's profile, such as job title, department, or work location. Your LLM uses this tool to make administrative changes to employee records based on promotions, transfers, or organizational changes.

**Try asking**:

- `Update Jordan Kim's job title to 'Senior Software Engineer'.`
- `Change Maria Rodriguez's department to 'Product Management'.`
- `Move Alex Johnson's work location to the Austin office.`
- `Update the job title for employee ID 12345 to 'Team Lead'.`

### update\_reporting\_relationship tool

The **update\_reporting\_relationship** tool changes an employee's manager to a new manager. Your LLM uses this tool to reassign reporting relationships when employees move between teams, after reorganizations, or when backfilling manager positions.

**Try asking**:

- `Move Alex Johnson to report to Sarah Chen.`
- `Change Jordan Kim's manager to Jade Anderson.`
- `Reassign Maria Rodriguez to the new team lead.`
- `Update the reporting relationship so Chris Lee reports to the VP of Engineering.`

### get\_all\_job\_titles tool

The **get\_all\_job\_titles** tool returns a list of all job titles in the organization. Your LLM uses this tool to understand the full range of roles across your company, ensure consistent job title usage, or gather data for workforce planning and organizational analysis.

**Try asking**:

- `What job titles exist in our organization?`
- `Show me all the different roles we have company-wide.`
- `List every job title to see our organizational structure.`
- `What are all the engineering job titles we use?`

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

---
