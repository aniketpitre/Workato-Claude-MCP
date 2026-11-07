---
url: 'https://docs.workato.com/en/connectors/ghost.md'
description: >-
  The Ghost connector lets you manage posts and members, upload images, and
  trigger recipes on Ghost webhook events in Workato.
---

# Ghost

[Ghost](https://ghost.org) is a publishing platform for newsletters, memberships, and blogs. This connector enables you to get, create, update, and search posts and members, upload images, and trigger recipes when Ghost webhook events occur.

## Install Ghost from the community library

Complete the following steps to install the Ghost connector from the [community library](https://www.workato.com/browse/connectors):

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

The Ghost connector uses Admin API key authentication.

### Ghost setup

1. Sign in to Ghost Admin. For Ghost(Pro) sites, use [Ghost Admin](https://account.ghost.org/signin/). For self-hosted sites, go to `https://yoursite.com/ghost`.
   
2. Go to **Settings > Integrations > Add custom integration**.
   
3. Enter a name for the integration, for example `Workato`, and click **Create**.
   
4. Copy the **Admin API key**. Don't use the Content API key.
   

### Connect to Ghost using Admin API key

Complete the following steps to connect to Ghost in Workato:

1. Click **Create > Connection**.
   
2. Search for `Ghost` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Ghost connection setup](/assets/ghost-connection-setup.BZtzk_1L.png)_Ghost connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your site's URL, with no trailing slash, in the **Site URL** field. For example, `https://yoursite.ghost.io`.
   
6. Paste the Admin API key you copied earlier into the **Admin API key** field.
   
7. Click **Connect**.

---
