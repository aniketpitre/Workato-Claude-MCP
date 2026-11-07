---
url: 'https://docs.workato.com/en/connectors/netsuite-rest/connect.md'
description: >-
  Set up and connect NetSuite REST in Workato using OAuth 2.0 client credentials
  machine-to-machine or authorization code grant authentication.
---

# Connect to NetSuite REST on Workato

The NetSuite REST connector supports the following OAuth 2.0 authentication types:

- Client credentials (machine-to-machine)
- Authorization code grant (user-based authentication)

Select the authentication type based on your use case. Use client credentials for backend integrations. Use authorization code grant when actions require user-level access.

## Prerequisites

Ensure you have the following to connect to NetSuite in Workato:

- The privilege to [create connections](/en/user-accounts-and-teams/role-based-access/new-model/privileges-reference#project-assets) in Workato.
- Access to a NetSuite Admin account.
- An understanding of the required NetSuite permissions.

## Create an integration record in NetSuite

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
   

## Create a custom OAuth profile in Workato

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
   

## Create key and certificate files

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
   

> **CLIENT CREDENTIALS ONLY**
> 
> This step applies only to client credentials (machine-to-machine) authentication. Skip this step if you use authorization code grant.

## Create a machine-to-machine certificate in NetSuite

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
   

> **CLIENT CREDENTIALS ONLY**
> 
> This step applies only to client credentials authentication.

## Configure the Workato NetSuite REST connector

Select the authentication type based on your setup:

- [Client credentials (machine-to-machine)](#client-credentials-machine-to-machine)
- [Authorization code grant (user-based authentication)](#authorization-code-grant-user-based-authentication)

### Client credentials (machine-to-machine)

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
   

### Authorization code grant (user-based authentication)

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

---

---
url: >-
  https://docs.workato.com/en/connectors/netsuite-rest/new-classification-record-trigger.md
description: >-
  The New classification record trigger detects new classification records in
  NetSuite REST.
---

# NetSuite REST - New classification record trigger

The **New classification record** trigger detects new classification records in NetSuite REST. Use this trigger to monitor classification records that don't include created or modified date fields. The trigger uses internal ID for polling.

## Input

| Input field | Description |
| --- | --- |
| Record type | Select the NetSuite classification record type to monitor. |
| When first started, this recipe should pick up events from ID | Enter the internal ID to start polling from. The trigger processes records with IDs greater than this value. Leave empty to start from ID 0. |
| Search query | Enter a search query to filter records. For example, `name CONTAIN test`. Don't filter by internal ID. |
| Search settings | Configure how the trigger retrieves and filters records. Refer to [Record Collection Filtering](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_1545222128.html) for more information. |

Additional fields appear based on the selected **Record type**. These fields update dynamically to match the record you select.

## Output

The output fields vary based on the selected **Record type**. The trigger returns fields that correspond to the classification record you select.

For example, if you select **Analytical impact**, the output includes the following fields:

| Output field | Description |
| --- | --- |
| Acquisition Month End Date | The end date of the acquisition month associated with the analytical impact record. |
| Analytical impact event | The event type recorded for the analytical impact. |
| Analytical impact link | The reference link associated with the analytical impact record. |

---
