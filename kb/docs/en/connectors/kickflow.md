---
url: 'https://docs.workato.com/en/connectors/kickflow.md'
description: >-
  Use the Kickflow connector to create, retrieve, update, delete, and search
  Kickflow records, and run ticket operations, from Workato recipes.
---

# Kickflow

[Kickflow](https://kickflow.com/) is a cloud-based workflow system that helps companies manage approval processes and improve business efficiency. The Kickflow connector lets you create, retrieve, update, delete, and search Kickflow records, and run additional ticket operations, from a Workato recipe.

## Install Kickflow from the community library

Complete the following steps to install the Kickflow connector from the [community library](https://www.workato.com/browse/connectors):

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

The Kickflow connector supports the following authentication types:

- [Personal access token](#pat-auth)
- [Service account token](#service-account-auth)

### Personal access token authentication

Use personal access token authentication for standard administrative or data integration tasks.

#### Kickflow setup

Complete the following steps to create a personal access token in Kickflow:

1. Sign in to [Kickflow](https://kickflow.com/).
   
2. Click the settings menu and select **Access token settings**.
   
3. Click **Create access token**.
   

### Connect to Kickflow using a personal access token

Complete the following steps to connect to Kickflow in Workato:

1. Click **Create > Connection**.
   
2. Search for `Kickflow` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Create a Kickflow connection.](/assets/kickflow-create-connection._UNas4RG.png)_Create a Kickflow connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **Personal access token**.
   
6. Enter the token you created in the **Token** field.
   
7. Click **Connect**.
   

### Service account token authentication

Use service account token authentication when you need to act on behalf of users in automated workflow.

#### Kickflow setup

Complete the following steps to set up Kickflow for service account token authentication:

1. Sign in to [Kickflow](https://kickflow.com/).
   
2. Click the grid menu and select **Admin center**.
   
3. Click **Integrations > Service account**.
   
4. Click **New access token**.
   

### Connect to Kickflow using an access token

Complete the following steps to connect to Kickflow in Workato:

1. Click **Create > Connection**.
   
2. Search for `Kickflow` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Create a Kickflow connection.](/assets/kickflow-create-connection._UNas4RG.png)_Create a Kickflow connection._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Use the **Auth type** drop-down menu to select **Service account token**.
   
6. Enter the token you created in the **Token** field.
   
7. Enter the ID of the user to impersonate in the **Impersonate user ID** field.
   
8. Click **Connect**.

---
