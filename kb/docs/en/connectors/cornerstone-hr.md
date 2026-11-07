---
url: 'https://docs.workato.com/en/connectors/cornerstone-hr.md'
description: >-
  Cornerstone is a cloud-based human capital management (HCM) platform for
  learning and development, performance management, recruiting, and compliance.
---

# Cornerstone HR

[Cornerstone](https://www.cornerstoneondemand.com) is a cloud-based human capital management (HCM) platform for learning and development, performance management, recruiting, and compliance. This connector enables you to manage records, goals, and monitor Cornerstone HR for new events in Workato.

## Install Cornerstone HR from the community library

Complete the following steps to install the Cornerstone HR connector from the [community library](https://www.workato.com/browse/connectors):

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

The Cornerstone HR connector uses OAuth 2.0 authentication.

### Cornerstone HR setup

Complete the following steps to set up Cornerstone HR for a Workato connection:

1. Sign in to your Cornerstone domain as an administrator. Your domain is unique to your organization. For example, `workato.csod.com`
   
2. Go to **Admin > Tools > Edge > API Management > Manage OAuth 2.0 Applications**.
   
3. Click **Register New Application**.
   
4. Enter an **Application Name** and the **User ID** of an active API service user in your portal.
   
5. Select any endpoint scopes or permissions and set the **Access Token Validity Period**. The maximum **Access Token Validity Period** is `86,400 seconds / 24 hours`.
   
6. Copy and securely store the **Client ID** and **Client secret** for use in Workato.
   

Refer to [Register an application](https://csod.dev/guides/getting-started/authentication.html#register-an-application) in the Cornerstone developer documentation for more information.

### Connect to Cornerstone HR using OAuth 2.0

Complete the following steps to connect to Cornerstone HR in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for and select Cornerstone HR as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Cornerstone HR connection setup](/assets/cornerstone-hr-connection-setup.NWNcgtCn.png)_Cornerstone HR connection setup._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Cornerstone corporation name in the **Company name** field.
   
6. Enter the client ID you obtained when you registered your OAuth application in Cornerstone in the **Client ID** field.
   
7. Enter the client secret you obtained when you registered your OAuth application in Cornerstone in the **Client secret** field.
   
8. Use the **Cornerstone environment** drop-down menu to select **Stage**, **Pilot**, or **Production**.
   
9. Click **Connect**.

---
