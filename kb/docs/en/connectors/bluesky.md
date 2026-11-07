---
url: 'https://docs.workato.com/en/connectors/bluesky.md'
description: >-
  The Bluesky connector lets you post, message, and monitor notifications on the
  decentralized Bluesky social network in Workato.
---

# Bluesky

[Bluesky](https://bsky.app) is a decentralized social network built on the AT Protocol. This connector enables you to look up profiles, create and delete posts and threads, upload images, send direct messages, and monitor notifications, all with a free Bluesky account and an app password. A Bluesky app password is a specific password used to connect Bluesky with other apps. This is not the same password that you use to log into your Bluesky account.

## Install Bluesky from the community library

Complete the following steps to install the Bluesky connector from the [community library](https://www.workato.com/browse/connectors):

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

The Bluesky connector uses app password authentication.

### Bluesky setup

Complete the following steps to get a Bluesky app password:

1. Go to **Settings > Privacy and security > App passwords** in your Bluesky account.
   
2. Click **Add app password**.
   
3. Turn on **DM access** in the password settings if you plan to use the **Send direct message** action.
   

### Connect to Bluesky using app password authentication

Complete the following steps to connect to Bluesky in Workato:

1. Click **Create > Connection**.
   
2. Search for `Bluesky` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Bluesky connection setup](/assets/bluesky-connection-setup.gNSZtAzR.png)_Bluesky connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Bluesky handle or account email in the **Handle or email** field. For example, `you.bsky.social`.
   
6. Paste the app password you created earlier into the **App password** field.
   
7. Leave **Entryway / service URL** as the default `https://bsky.social`, unless you connect to a self-hosted server.
   
8. Click **Connect**.

---
