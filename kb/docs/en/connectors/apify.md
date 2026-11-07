---
url: 'https://docs.workato.com/en/connectors/apify.md'
description: >-
  Use the Apify connector in Workato to find Actors, run them, and map dataset
  items into recipe steps.
---

# Apify

[Apify](https://apify.com) is a marketplace of hosted scrapers (Actors) plus dataset storage. The Apify connector lets you find public Actors, start runs, wait for results, and pull structured dataset items into your recipes.

Use the Apify connector to:

- Discover public store Actors, then look up an Actor, build, or run by ID.
- Start an Actor and pull the structured dataset items it produces.
- Wait for a long-running Actor to finish, then map its results into later recipe steps.
- Start a recipe when an Actor run finishes, and fetch its default dataset in a follow-on step.

## Install Apify from the community library

Complete the following steps to install the Apify connector from the [community library](https://www.workato.com/browse/connectors):

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

The Apify connector uses API token authentication.

### Apify setup

Complete the following steps to get your Apify API token:

1. Sign in to the [Apify Console](https://console.apify.com).
   
2. Go to **Settings > API & Integrations**.
   
3. Click **Copy** to copy the API token in the **Personal API token** section for use in Workato.
   

### Connect to Apify using API token authentication

Complete the following steps to connect to Apify in Workato:

1. Click **Create > Connection**.
   
2. Search for `Apify` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Apify connection setup](/assets/apify-connection-setup.Blj5_zyo.png)_Apify connection setup._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your Apify API token in the **API token** field. Refer to [Apify setup](#apify-setup) for more information.
   
6. Click **Connect**.

---
