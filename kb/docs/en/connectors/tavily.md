---
url: 'https://docs.workato.com/en/connectors/tavily.md'
description: >-
  Tavily is a search engine built for LLMs and AI agents, offering real-time web
  search, content extraction, and deep research through a REST API.
---

# Tavily

[Tavily](https://tavily.com) is a search engine built for LLMs and AI agents, offering real-time web search, content extraction, and deep research through a REST API. The Tavily connector enables you to search the web, extract page content, map and crawl websites, and run deep research tasks in Workato.

## Install Tavily from the community library

Complete the following steps to install the Tavily connector from the [community library](https://www.workato.com/browse/connectors):

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

The Tavily connector uses API key authentication.

### Tavily setup

1. Sign in to your [Tavily account](https://app.tavily.com).
   
2. Go to **API Keys** in the Tavily dashboard and copy your API key. The key starts with `tvly-`.
   

### Connect to Tavily using API key authentication

Complete the following steps to connect to Tavily in Workato:

1. Click **Create > Connection**.
   
2. Search for `Tavily` and select it as your connection.
   
3. Enter a name for your connection in the **Connection name** field.
   
   ![Tavily connection setup](/assets/tavily-connection-setup.DUSimr4S.png)_Tavily connection setup._
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter your API key in the **API key** field.
   
6. Click **Connect**. Workato runs a test search that uses 1 credit from your Tavily account.

---
