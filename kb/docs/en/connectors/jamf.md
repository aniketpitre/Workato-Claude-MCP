---
url: 'https://docs.workato.com/en/connectors/jamf.md'
description: >-
  Use the JAMF connector to manage Apple devices, computers, account users, and
  departments in JAMF Pro from Workato recipes.
---

# JAMF

[JAMF](https://www.jamf.com/) is a device management platform for Apple devices, including Mac, iPhone, and iPad. The JAMF connector lets you work with computers, account users, computer invitations, departments, Mac applications, and webhook events in Workato.

## API version

The connector uses the [JAMF Classic API](https://developer.jamf.com/jamf-pro/reference/classic-api) for most operations and the [JAMF Pro API](https://developer.jamf.com/jamf-pro/reference/jamf-pro-api) for computer inventory operations.

## Install JAMF from the community library

Complete the following steps to install the JAMF connector from the [community library](https://www.workato.com/browse/connectors):

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

The JAMF connector supports [client credentials authentication](#client-creds-auth).

### Client credentials authentication

Use client credentials for JAMF Pro API or the JAMF classic API.

#### JAMF setup

Complete the following steps to set up JAMF for client credentials authentication:

1. Sign in to your JAMF Pro instance as an administrator.
   
2. In the sidebar, click **Settings > System > API Roles and Clients**.
   
3. Create an API role that grants the privileges required for the objects you plan to use in your recipes. For example, grant `Read Computers`, `Create Computers`, and `Update Computers` if your recipes work with computer records.
   
   Refer to [API Roles and Clients in the JAMF documentation](https://learn.jamf.com/bundle/jamf-pro-documentation-current/page/API_Roles_and_Clients.html) for the full list of privileges.
   
4. Create an API client and assign the API role you created. JAMF Pro generates a client ID for the new client.
   
5. Select the API client and click **Generate client secret**. Copy and save the **client secret** for use in Workato. JAMF Pro displays the secret only once.
   

#### Connect to JAMF with client credentials authentication

Complete the following steps to set up a client credentials connection to JAMF in Workato:

1. Click **Create > Connection**.
   
2. Search for `JAMF` and select it as your app.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![JAMF client credentials authentication setup](/assets/client-credentials-authentication-setup.DSBS-mvC.png)_JAMF client credentials authentication setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Authentication type** drop-down menu to select **Client credentials**.
   
6. Enter the **Client ID** generated when you created the API client in JAMF Pro.
   
7. Enter the **Client secret** you generated for the API client.
   
8. Click **Connect**.

---
