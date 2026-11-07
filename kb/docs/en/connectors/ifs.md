---
url: 'https://docs.workato.com/en/connectors/ifs.md'
description: >-
  The IFS connector lets you automate ERP workflows: create, update, search, and
  delete records and trigger on new or updated records.
---

# Industrial and Financial Systems (IFS)

[Industrial and Financial Systems (IFS) Cloud](https://ifspsc2-d07.demo.ifs.cloud/landing-page/) is an enterprise resource planning (ERP) platform that helps organizations manage complex business processes including project management, manufacturing, supply chain, and field service operations. This connector allows you to automate business workflows, synchronize data across systems, and streamline operations so your team can focus on delivering value to customers.

## Prerequisites

You must complete the following to establish a connection to IFS in Workato:

- [Create an IAM client ID and client secret](#client-create)
- [Obtain your IFS realm](#realm-get)
- [Download the IFS connector from the Community library](#connector-download)

### Create an IAM client and client secret

Complete the following steps to create an IAM client and client secret in IFS:

1. Go to **Solution Manager > Access Control > Identity and Access Manager > IAM Clients** in the IFS sidebar.
   
2. Click **+** (plus) to create a new IAM client.
   
3. Set up your IAM Client for OAuth 2.0 authorization code grant and OAuth 2.0 client credentials authentication:
   
   Authorization code grant
   
   1. Provide a **Client ID**.
      
   2. Ensure the **Enabled** toggle is enabled.
      
   3. Enable **Direct Access Grants**.
      
   4. Enable **Service Accounts**.
      
   5. Click **+**(plus) and enter Workato's **Redirect URI**:
      
      ```
      https://www.workato.com/oauth/callback
      ```
      
   6. Click **OK**.
      
   
   Client credentials
   
   1. Provide a **Client ID**.
      
   2. Ensure the **Enabled** toggle is enabled.
      
   3. Enable **Direct Access Grants**.
      
   4. Enable **Service Accounts**.
      
   5. Click **OK**.
      
   
4. Copy the generated **Client Secret** and **Client ID** to use in your connection.
   
5. Refer to [Grant Permission Sets to Users](https://docs.ifs.com/techdocs/24r1/030_administration/010_security/020_permission_sets/070_grant_permission_sets_to_users/#grant_a_permission_set_to_multiple_users) for information on to grant permissions to service account users. This is required for client credentials authentication and not necessary for authorization code grant authentication.
   

### Obtain your IFS realm

Complete the following steps to obtain your IFS realm in IFS:

1. Go to **Solution Manager > Integration > API explorer** in the IFS sidebar.
   
2. Select any API from the list.
   
3. Select **Documentation > API Doc**.
   
4. Choose an endpoint and expand the **AUTHORIZATIONS** section.
   
5. Click the **Connect URL**.
   
6. Find the `authorization_endpoint` URL value. For example:
   
   ```
   https://your-instance.ifs.cloud/auth/realms/abc1d234/protocol/openid-connect/auth
   ```
   
   Your realm is the string between `/realms/` and `/protocol/`. In this example, the realm is `abc1d234`.
   
7. Copy the realm value to use in your connection.
   

### Download the IFS connector from the Community library

Complete the following steps to install the IFS connector from the [community library](https://www.workato.com/browse/connectors):

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

Complete the following steps to connect to IFS in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select **IFS** as your connection on the **New Connection** page.
   
3. Provide a unique name for the connection in the **Connection name** field.
   
   ![IFS connection](/assets/ifs-connection.CberSYlY.png)_IFS connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Connection type** drop-down to select the connection type. Workato supports **Cloud** and **On-premise** connections.
   
6. Enter your **IFS instance domain**, such as `your-instance.ifs.cloud` or `ifscloud.your-company.com`.
   
7. Use the **Authentication method** drop-down menu to select an authentication method. Workato supports OAuth 2.0 authorization code grant and OAuth 2.0 client credentials authentication.
   
8. Provide the OAuth realm for your IFS instance. You can find this in your IFS authentication URL between `/realms/` and `/protocol/`. For example, the realm in the following endpoint URL is `abc1d234`: `https://your-instance.ifs.cloud/auth/realms/abc1d234/protocol/openid-connect/auth`.
   
9. Enter your IAM client ID in the **Client ID** field. Refer to the [IAM Client](https://docs.ifs.com/techdocs/24r2/030_administration/010_security/040_iam_settings/035_iam_clients/020_authenticate_external_integration/) guide for more information.
   
10. Enter your IAM client secret in the **Client secret** field.
    
11. Optional. Provide additional scopes for this connection. Separate each value with a space or new line. `openid` and `microprofile` are automatically included.
    
12. Click **Connect**.

---
