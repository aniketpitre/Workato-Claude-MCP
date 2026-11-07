---
url: 'https://docs.workato.com/en/connectors/akeneo.md'
description: >-
  The Akeneo connector lets you search, retrieve, upsert, and download product
  records in Workato, and trigger recipes on product changes.
---

# Akeneo

[Akeneo](https://www.akeneo.com/) is a Product Information Management (PIM) system that helps businesses centralize, enrich, and distribute product information across all their sales channels. The Akeneo connector enables you to search, retrieve, upsert, and download product records and files in Workato, and trigger recipes when products are created or updated.

### Install the Akeneo connector from the community library

Complete the following steps to install the Akeneo connector from the [community library](https://www.workato.com/browse/connectors):

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

The Akeneo connector uses OAuth 2.0 authentication.

### Akeneo setup

Complete the following steps to get a Client ID, Client secret, Username, Password, and domain to connect to Akeneo in Workato:

1. Go to **Connect > Connection settings**, click the name of your Akeneo connection, and select the **Credentials** tab in Akeneo.
   
2. Copy the **Client ID** and **Client secret**.
   
3. Copy the auto-generated **Username** and **Password**.
   
4. Note your Akeneo domain (host), for example `my-instance.cloud.akeneo.com`.
   

### Complete setup in Workato

Complete the following steps to establish a connection to Akeneo:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Akeneo` and select it as your connection on the **New connection** page.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Create an Akeneo connection in Workato.](/assets/akeneo-connection-setup.xeZai0wH.png)_Create an Akeneo connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your client ID in the **Client ID** field.
   
6. Enter your client secret in the **Client secret** field.
   
7. Enter your username in the **Username** field.
   
8. Enter your password in the **Password** field.
   
9. Enter your Akeneo host in the **Domain** field, for example `my-instance.cloud.akeneo.com`.
   
10. Click **Connect**.

---
