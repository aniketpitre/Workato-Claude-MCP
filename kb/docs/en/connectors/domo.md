---
url: 'https://docs.workato.com/en/connectors/domo.md'
description: >-
  The Domo connector lets you manage accounts, datasets, users, groups,
  projects, and lists, and import or export data in Domo.
---

# Domo

[Domo](https://www.domo.com) is a cloud-based business intelligence and data platform that helps organizations connect, transform, and visualize data to drive decision-making. This connector enables you to manage objects, such as accounts, datasets, users, groups, projects, and lists, and move data in and out of datasets in Workato.

## API version

The Domo connector uses the [Domo API v1](https://developer.domo.com/).

## Install Domo from the community library

Complete the following steps to install the Domo connector from the [community library](https://www.workato.com/browse/connectors):

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

The Domo connector uses OAuth 2.0 (client credentials) authentication.

### Minimum and default scopes

When you create your Domo API client, select the scopes that match the objects your recipes use. The connector requests the following scopes:

- `data`
- `user`
- `account`
- `audit`
- `dashboard`

### Create a Domo API client

Complete the following steps in the Domo Developer portal to obtain your **Client ID** and **Client secret**:

1. Sign in to the [Domo Developer portal](https://developer.domo.com/) and go to the [New Client](https://developer.domo.com/new-client) page.
   
2. Provide a name and description for your client application.
   
3. Select the [scopes](#scopes) your recipes require.
   
4. Click **Create** to generate your client.
   
5. Record the **Client ID** and **Client secret**. You use these values to connect to Domo in Workato.
   

### Connect to Domo using OAuth 2.0

Complete the following steps to connect to Domo in Workato:

1. Click **Create > Connection**.
   
2. Search for `Domo` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Domo connection setup](/assets/domo-connection-setup.CvMFXfmB.png)_Create your connection_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Domo **Client ID**. Refer to [Create a Domo API client](#domo-setup) for more information.
   
6. Enter your Domo **Client secret**.
   
7. Click **Connect**.

---
