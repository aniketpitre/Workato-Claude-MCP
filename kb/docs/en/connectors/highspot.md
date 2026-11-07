---
url: 'https://docs.workato.com/en/connectors/highspot.md'
description: >-
  Connect to Highspot to manage sales enablement content, spots, and items
  programmatically.
---

# Highspot

[Highspot](https://www.highspot.com) is a sales enablement platform that helps teams manage, share, and track sales content to improve buyer engagement and sales effectiveness.

## API version

The Highspot connector uses the Highspot REST API. You can specify the API version during connection setup.

## Connection setup

The Highspot connector uses API key authentication.

This authentication method requires the following access and values:

- Admin access to your Highspot instance
- API credentials from Highspot

### Download Highspot from the community

Complete the following steps to install the Highspot connector from the [community library](https://www.workato.com/browse/connectors):

1. Open the recipe editor and search for a connector. Alternatively, you can search for a connector in the [community library](https://www.workato.com/browse/connectors).
   
   ![Search for recipe editor](/assets/search-on-recipe-editor.VrZpf8zl.png)_Search for community connectors in the recipe editor_
   
2. Select the community connector you plan to install.
   
3. Click **Install** to install the connector from the community library.
   
   ![Click install](/assets/install-connector.BXpGZP9K.png)_Click **Install**_
   
4. Select **Release connector**. Alternatively, select **Review code** to review and modify the connector code before releasing it to the workspace.
   
   ![Release connector](/assets/release-and-review.kWToLwmF.png)_Release the connector_
   
5. Summarize any changes you made to the connector, then click **Release** to allow workspace collaborators to use the connector in recipes.
   
   ![The Confirm release dialog](/assets/release.CpEhhA-6.png)_The **Confirm release** dialog_
   

### Highspot setup for API key authentication

Complete the following steps to retrieve your API credentials from Highspot:

1. Sign in to your Highspot account.
   
2. Click your profile image and select **Settings**.
   
3. Go to **Developer > Basics**.
   
4. Copy and save the following values for use in Workato:
   
   - **URL**: Your Highspot API instance URL. For example, `https://api-su2.highspot.com`.
   - **Key**: Your API client key.
   - **Secret**: Your API client secret.

### Connect to Highspot with API key authentication

Complete the following steps to connect to Highspot in Workato:

1. Click **Create > Connection**.
   
2. Search for `Highspot` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Connect to Highspot](/assets/connect.BQtF6-s_.png)_Connect to Highspot_
   
4. Use the **Location** drop-down menu to select the project where you plan to store your connection.
   
5. Enter the **API key** and **API secret**.
   
6. Enter the **Instance name**. For example, `https://api-su2.highspot.com`.
   
7. Enter the **API version** you plan to use. For example, `0.5`.
   
8. Click **Connect**.

---
