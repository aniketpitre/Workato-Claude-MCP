---
url: 'https://docs.workato.com/en/connectors/vercel.md'
description: Vercel is a platform for building and deploying web applications.
---

# Vercel

[Vercel](https://vercel.com/) is a platform for building and deploying web applications. The Vercel connector manages deployments, runs deployment checks, assigns aliases, and starts recipes when deployment events occur.

## Install Vercel from the community library

Complete the following steps to install the Vercel connector from the [community library](https://www.workato.com/browse/connectors):

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

The Vercel connector uses account token authentication. Workato sends the account token as a bearer token in the `Authorization` header.

### Vercel setup

Complete the following steps to create an account token in Vercel:

1. Log in to the [Vercel Dashboard](https://vercel.com/login).
   
2. Go to **Account Settings > Tokens**.
   
3. Click **Create**.
   
4. Enter a name for your token in the **Name** field.
   
5. Use the **Scopes** drop-down menu to select **Full Account**, **Team / All Projects**, or **Project**.
   
6. Select an expiration date in the **Expiration** field.
   
7. Click **Create**.
   
8. Copy and securely save your token for use in Workato.
   

### Connect to Vercel using an account token

Complete the following steps to connect to Vercel in Workato:

1. Click **Create > Connection**.
   
2. Search for `Vercel` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Vercel connection setup](/assets/vercel-connection-setup.CfXMQ9pf.png)_Create a Vercel connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the account token you created in Vercel in the **Account token** field.
   
6. Optional. Enter your team ID in the **Team ID** field if your projects belong to a team. For example, `team_abc123`. Leave this field blank to use your personal account. When set, Workato sends the team ID as the `teamId` parameter on every request.
   
7. Click **Connect**.

---
