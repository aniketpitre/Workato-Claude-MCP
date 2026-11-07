---
url: 'https://docs.workato.com/en/connectors/airtop.md'
description: >-
  The Airtop connector lets you launch and manage cloud browser sessions and use
  AI actions to scrape, query, and interact with web pages in Workato.
---

# Airtop

[Airtop](https://airtop.ai) provides cloud browser sessions for AI agents and automation. This connector enables you to start and manage browser sessions and windows, then use AI-driven actions to load pages, scrape content, query pages with natural language, and interact with elements, all without running your own browser infrastructure.

## Install Airtop from the community library

Complete the following steps to install the Airtop connector from the [community library](https://www.workato.com/browse/connectors):

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

The Airtop connector uses API key authentication.

### Airtop setup

1. Sign in to the [Airtop portal](https://portal.airtop.ai/).
   
2. Go to **Settings > API Keys**.
   
3. Click **Create new key**.
   
4. Enter a name in the **Name** field for your key.
   
5. Click **Create** and copy the API key for use in Workato.
   

### Connect to Airtop using API key

Complete the following steps to connect to Airtop in Workato:

1. Click **Create > Connection**.
   
2. Search for `Airtop` and select it as your app.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Create an Airtop connection in Workato.](/assets/airtop-connection-setup.dNoOH1x8.png)_Create an Airtop connection in Workato._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Paste the API key you copied earlier into the **API key** field.
   
6. Click **Connect**.

---
