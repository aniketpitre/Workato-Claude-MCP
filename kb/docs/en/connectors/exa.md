---
url: 'https://docs.workato.com/en/connectors/exa.md'
description: >-
  Connect Exa to Workato to search the web, retrieve page contents, get cited
  answers, and trigger recipes from scheduled search monitors.
---

# Exa

[Exa](https://exa.ai) provides an AI-powered search API that retrieves web content using neural and keyword search, page content extraction, and answers with citations.

Use the Exa connector to:

- Search the web and return page text, highlights, or summaries.
- Retrieve text, highlights, or summaries for URLs or document IDs.
- Get an answer with cited sources.
- Create, list runs for, and delete monitors that run a search on a schedule.
- Trigger a recipe when a monitor run completes.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Exa API endpoint. Refer to the Exa [API Reference](https://exa.ai/docs/reference/search) documentation for endpoint details.

## Install Exa from the community library

Complete the following steps to install the Exa connector from the [community library](https://www.workato.com/browse/connectors):

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

The Exa connector uses API key authentication.

### Exa setup for API key authentication

Complete the following steps to generate an Exa API key:

1. Sign in to the [Exa Dashboard](https://dashboard.exa.ai).
   
2. Go to **API Keys**.
   
3. Click **Create New Key**.
   
4. Enter an **API key name**.
   
5. Click **Create a Key**.
   
6. Copy and save the **API Key** for use in Workato.
   

### Connect to Exa using API key authentication

Complete the following steps to set up an Exa connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Exa` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Exa connection setup details](/assets/exa-connection-setup.C1Ze8Arj.png)_Exa connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the API key you saved from Exa in the **API key** field. Refer to [Exa setup for API key authentication](#exa-setup) for more information.
   
6. Click **Connect**.

---
