---
url: 'https://docs.workato.com/en/connectors/clay.md'
description: >-
  Connect Clay to Workato to look up company and person profiles and search for
  companies and people.
---

# Clay

[Clay](https://www.clay.com/) is a go-to-market data platform with a proprietary database of companies and people. The Clay connector looks up company and person profiles, retrieves company funding data, and searches for companies and people.

## Install Clay from the community library

Complete the following steps to install the Clay connector from the [community library](https://www.workato.com/browse/connectors):

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

The Clay connector uses API key authentication.

### Create API key in Clay

Complete the following steps to create an API key in Clay:

1. Sign in to your [Clay](https://app.clay.com/workspaces) workspace.
   
2. Click **API and CLI > API keys**.
   
3. Click **Add API key**.
   
4. Enter a **Name**.
   
5. Select **Public API** under **Scopes**.
   
6. Click **Add API key**.
   
7. Copy and save the **API key** for use in Workato.
   
   > **SAVE THE API KEY**
   > 
   > Clay only displays the API key once. You must create a new one if you lose it.
   
8. Click **I've copied my API key**.
   

### Connect to Clay using an API key

Complete the following steps to connect your Clay account to Workato:

1. Click **Create > Connection**.
   
2. Search for `Clay` and select it as your connection on the **New Connection** page.
   
3. Enter a name for the connection in the **Connection name** field.
   
4. Use the **Location** drop-down menu to select the project or folder where you plan to store the connection.
   
5. Enter the Clay **API key**. Refer to [Create API key in Clay](#create-api-key-in-clay) for more information.
   
6. Click **Connect**.

---
