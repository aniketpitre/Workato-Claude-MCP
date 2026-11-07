---
url: 'https://docs.workato.com/en/connectors/veeva-vault.md'
description: >-
  Connect Veeva Vault to Workato to retrieve, create, and update documents and
  data records across any Vault object.
---

# Veeva Vault

[Veeva Vault](https://www.veeva.com/products/vault-platform/) is a cloud-based content and data management platform built for the life sciences industry. It powers clinical, regulatory, quality, commercial, and CRM operations for pharma, biotech, and medical device companies.

The Veeva Vault connector is fully dynamic and works with all active Vault objects in your tenant, including standard objects (such as Product, Account, Country, and User) and custom objects. Field schemas are fetched from Vault's metadata API at design time, so the recipe editor reflects your actual Vault configuration.

Use the Veeva Vault connector to:

- Retrieve, create, or update documents and data records stored in Veeva Vault.
- Streamline workflows by integrating Vault actions into approval, review, or data submission processes.
- Track audit logs, system events, or record changes to help meet regulatory requirements.
- Synchronize or exchange information between Vault and other applications such as CRM, ERP, or cloud storage.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Veeva Vault REST endpoint. The request is authenticated with the active session. Refer to the [Veeva Vault API documentation](https://developer.veevavault.com/api/26.1/) for endpoint details.

## Install Veeva Vault from the community library

Complete the following steps to install the Veeva Vault connector from the [community library](https://www.workato.com/browse/connectors):

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

The Veeva Vault connector supports the following authentication types:

- [Basic authentication](#basic-auth)
- [OAuth 2.0 OpenID authentication](#authentication-oauth)

### Basic authentication

Use basic authentication to connect to Veeva Vault.

#### Connect to Veeva Vault using basic authentication

Basic authentication uses your Vault username and password to authenticate.

1. Click **Create > Connection** or press C twice.
   
2. Search for `Veeva Vault` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Vault domain in the **Vault DNS** field, for example `myvault.veevavault.com`. Don't include `https://` or a trailing slash.
   
6. Select **Basic authentication** from the **Authentication type** drop-down menu.
   
7. Optional. Select an option from the **API version** drop-down menu. Defaults to the latest generally available (GA) version. The connector supports the latest GA version and up to two prior GA versions.
   
8. Enter your Vault username (typically your email address) in the **Username** field.
   
9. Enter your Vault password in the **Password** field.
   
10. Click **Connect**.
    

### OAuth 2.0 OpenID authentication

Use OAuth 2.0 OpenID authentication to connect to Veeva Vault.

#### Veeva Vault setup

Complete the following steps to set up Veeva Vault for OAuth 2.0 OpenID authentication:

> **OPTIONALLY USE MICROSOFT ENTRA ID**
> 
> You can optionally configure Microsoft Entra ID with OAuth 2.0 OpenID. Refer to the [Veeva Vault](https://platform.veevavault.help/en/lr/43329#configure-oauth-entra-api-user-accounts) documentation for more information.

1. Go to **Admin > Settings > OAuth 2.0 / OpenID Connect Profiles**.
   
2. Click **Create**.
   
3. Enter a **Label** and **Name** for the profile.
   
4. Choose a **Status** for the profile. It's best practice to leave the profile as **Inactive** until configuration is complete.
   
5. Optional. Add a description of the profile.
   
6. Under **OAuth 2.0 / OpenID Connect Configuration**, upload your AS metadata with the **Upload AS Metadata** button.
   
7. Select an **Authorization Server Provider** from the drop-down. Starting with 20R2.2, the ADFS / Azure AD option is split into two: **ADFS** and **Azure AD** (Microsoft Entra ID). ADFS exposes the value as `ADFS`, while Azure AD exposes the value as `Azure`.
   
8. Optional. If you selected **ADFS** in the previous step, choose the **Preferred Authentication Library**. The default value is **MSAL (ADFS 2019 or later)**. We recommend selecting MSAL for ADFS 2019 or later, and ADAL otherwise. Vault File Manager uses this setting to load the appropriate Microsoft Authentication Library at runtime. Selecting the wrong option may prevent the use of advanced configuration options on the IdP side, such as custom claims.
   
9. Optional. Enter an **Access Token JWKS Endpoint**. This option is only available when you select **PingFederate** in the previous step. This field has a 500-character limit.
   
10. Select an **Identity Claim**. Choose **Identity is in the "sub" claim** to allow the AS to provide the unique user identifier in the `sub` claim of the `id_token` or `access_token` by default. If you select **Identity is in another claim**, enter the alternative claim key in the **Claim** field. This field has a 100-character limit.
    
11. Select a **User ID Type**, either **Vault User Name** or **Federated ID**.
    
12. Optional. Select the **Perform strict Audience Restriction validation** checkbox to enable audience restriction validation.
    
13. Optional. Under **Client Applications**, click **Add** and complete the required fields to set up client ID mappings between authorization servers and client applications.
    
14. Click **Save**.
    

#### Connect to Veeva Vault using OAuth 2.0 OpenID authentication

Complete the following steps to set up OAuth 2.0 OpenID authentication connection to Veeva Vault in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Veeva Vault` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Vault domain in the **Vault DNS** field, for example `myvault.veevavault.com`. Don't include `https://` or a trailing slash.
   
6. Select **OAuth 2.0 OpenID authentication** from the **Authentication type** drop-down menu.
   
7. Optional. Select an option from the **API version** drop-down menu. Defaults to the latest generally available (GA) version. The connector supports the latest GA version and up to two prior GA versions.
   
8. Enter the OAuth 2.0 OpenID profile ID configured in your Vault (`oauth_oidc_profile_id` in the Vault API docs) in the **OAuth profile ID** field.
   
9. Enter the OAuth 2.0 token endpoint from your identity provider in the **IdP token endpoint** field. For example, for Microsoft Entra ID: `https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token`.
   
10. Enter the OAuth 2.0 client ID issued by your identity provider in the **Client ID** field.
    
11. Enter the OAuth 2.0 client secret issued by your identity provider in the **Client secret** field.
    
12. Optional. Enter the OAuth 2.0 scope in the **Scope** field. For example, for Microsoft Entra ID client credentials, use `{your-client-id}/.default`.
    
13. Click **Connect**.

---

---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/new-updated-document-trigger.md
description: >-
  The New/updated document trigger runs when a document is created or updated in
  Veeva Vault.
---

# Veeva Vault - New/updated document trigger

The **New/updated document** trigger runs when a document is created or updated in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| From date | Enter the date/time to only return documents modified after. Defaults to the recipe start time if left blank. |
| Status filter | Enter a document status to filter by, such as `Approved`. |
| Document type filter | Enter a document type to filter by, such as `Procedure`. |
| Classification filter | Enter a classification to filter by, for example `SOP`. |

## Output

| Output field | Description |
| --- | --- |
| ID | The document ID. |
| Name | The document name. |
| Title | The document title. |
| Type | The document type. |
| Classification | The document classification. |
| Lifecycle | The document lifecycle. |
| Status | The document status. |
| Description | The document description. |
| Last modified date | The date the document version was last modified. |

---

---
url: >-
  https://docs.workato.com/en/connectors/veeva-vault/new-updated-record-scheduled-vql-trigger.md
description: >-
  The New/updated record (scheduled VQL) trigger runs your VQL SELECT statement
  on a fixed schedule and fires for each new or updated record in Veeva Vault.
---

# Veeva Vault - New/updated record (scheduled VQL) trigger

The **New/updated record (scheduled VQL)** trigger runs your VQL `SELECT` statement on a fixed schedule and fires for each new or updated record in Veeva Vault.

## Input

| Input field | Description |
| --- | --- |
| VQL query | Enter a VQL `SELECT` statement without a date filter. |
| Date field (cursor) | Enter the field you plan to use as the moving cursor. Use `version_modified_date__v` for documents and `modified_date__v` for vobject records. Defaults to `modified_date__v`. |
| From date | Enter a date/time to start retrieving records from. Defaults to 1 hour ago. |

## Output

| Output field | Description |
| --- | --- |
| ID | The record ID. |
| Name | The record name. |
| Version modified date | The version modified date, if the query selected it. |
| Modified date | The modified date, if the query selected it. |

---
