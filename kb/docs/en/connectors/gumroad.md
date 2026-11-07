---
url: 'https://docs.workato.com/en/connectors/gumroad.md'
description: >-
  Connect Gumroad to Workato to manage sales, subscribers, refunds, content
  access, and license keys.
---

# Gumroad

[Gumroad](https://gumroad.com) is an e-commerce platform that lets creators sell digital products, memberships, and subscriptions directly to their audience. The Gumroad connector enables you to manage sales, subscribers, refunds, content access, and license keys in Workato.

Use the Gumroad connector to:

- Sync new Gumroad sales into your CRM or accounting system.
- Revoke content access automatically when a dispute or refund occurs.
- Deliver and manage software licenses by verifying, enabling, or disabling license keys.
- Notify your team when a subscription is cancelled, updated, or restarted.

You can also use [custom actions](/en/developing-connectors/custom-actions) to send a custom HTTP request to any Gumroad API endpoint. Refer to the Gumroad [API](https://app.gumroad.com/api) documentation for endpoint details.

## Install Gumroad from the community library

Complete the following steps to install the Gumroad connector from the [community library](https://www.workato.com/browse/connectors):

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

The Gumroad connector uses access token authentication. Workato sends the access token as a bearer token in the `Authorization` header.

### Gumroad setup

Complete the following steps to create an application and generate an access token in Gumroad:

1. Sign in to your [Gumroad](https://gumroad.com/login) account.
   
2. Go to **Settings > Advanced**.
   
3. Go to the **Applications** section.
   
4. Enter an **Application name**.
   
5. Enter `https://www.workato.com/oauth/callback` in the **Redirect URI** field.
   
6. Click **Create application**.
   
7. Click **Generate access token**.
   
8. Copy and save the **Access Token** for use in Workato.
   
   > **ACCESS TOKENS DON'T EXPIRE**
   > 
   > Access tokens don't expire unless they're manually revoked. Treat the token like a password because anyone with access to it can view your account data and sales information.
   

### Connect to Gumroad using an access token

Complete the following steps to connect to Gumroad in Workato:

1. Click **Create > Connection**.
   
2. Search for `Gumroad` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Gumroad connection setup](/assets/gumroad-connection-setup.Hldvqc5b.png)_Create a Gumroad connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **Access token**. Refer to [Gumroad setup](#gumroad-setup) for steps to generate an access token.
   
6. Click **Connect**.

---
