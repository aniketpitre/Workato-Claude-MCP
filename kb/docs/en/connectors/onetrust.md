---
url: 'https://docs.workato.com/en/connectors/onetrust.md'
description: >-
  The OneTrust connector lets you create, retrieve, search, update, and reassign
  assessments, and retrieve users in Workato.
---

# OneTrust

[OneTrust](https://www.onetrust.com) is a privacy, risk, and compliance management platform. The OneTrust connector lets you create, retrieve, search, update, and reassign assessments, and retrieve users, in Workato.

## Install OneTrust from the community library

Complete the following steps to install the OneTrust connector from the [community library](https://www.workato.com/browse/connectors):

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

The OneTrust connector supports the following authentication types:

- [Client credentials](#client-credentials-authentication)
- [API key](#api-key-authentication)

Both authentication types send a bearer token to OneTrust. The connection test reads assessments, so the credential must have read access to the Assessment Automation module.

### Client credentials authentication

Use client credentials to connect with a client ID and client secret. Workato exchanges them for an access token and refreshes the token when it expires.

#### Minimum and default scopes

Client credentials are scope-based, and the scopes required differ by endpoint. Select the scopes for the APIs you plan to use when creating your credentials. The connector uses the OneTrust Assessment APIs and the SCIM User APIs. Refer to the [OneTrust API](https://developer.onetrust.com/onetrust/reference/oauth-20-scopes) documentation for the scopes required by each endpoint.

#### OneTrust setup

Complete the following steps to set up OneTrust for client credentials authentication:

1. Click **Global settings > Access management > Client credentials** in OneTrust.
   
2. Click **Add** to create the credential.
   
3. Enter a name for your client credential. Optionally, configure **Restrict IP addresses**.
   
4. Configure **Scopes** for your client credential. Enable access to the OneTrust Assessment APIs and the SCIM User APIs. Refer to [Minimum and default scopes](#client-credentials-scopes) for more information about minimum scopes.
   
5. Copy the **Client ID** and **Client secret**.
   

#### Connect to OneTrust using client credentials

Complete the following steps to set up a client credentials connection to OneTrust in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneTrust` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![OneTrust connection setup](/assets/onetrust-connection-setup.Ccfr0g2E.png)_OneTrust connection setup._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
6. Enter your OneTrust subdomain in the **Host name** field. For example, if your OneTrust URL is `https://example.my.onetrust.com`, enter `example.my`.
   
7. Enter your OneTrust client ID in the **Client ID** field.
   
8. Enter your OneTrust client secret in the **Client secret** field.
   
9. Click **Connect**.
   

### API key authentication

Use an API key to connect with a single OneTrust-generated key.

#### OneTrust setup

Complete the following steps to set up OneTrust for API key authentication:

1. Open OneTrust and go to **Global settings > Access management > Client credentials > API keys**.
   
2. Click **Add** and create the key.
   
3. Copy the API key.
   

Refer to the [OneTrust documentation](https://my.onetrust.com/s/article/UUID-76f55697-ba16-d000-849a-d33e3d217f41?language=en_US) for more information.

#### Connect to OneTrust using an API key

Complete the following steps to set up an API key connection to OneTrust in Workato:

1. Click **Create > Connection**.
   
2. Search for `OneTrust` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **API key**.
   
6. Enter your OneTrust subdomain in the **Host name** field. For example, if your OneTrust URL is `https://example.my.onetrust.com`, enter `example.my`.
   
7. Enter your OneTrust API key in the **API key** field.
   
8. Click **Connect**.

---
