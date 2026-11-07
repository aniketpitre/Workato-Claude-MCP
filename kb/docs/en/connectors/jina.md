---
url: 'https://docs.workato.com/en/connectors/jina.md'
description: >-
  Prepare clean, LLM-ready content from the web with Jina's Search Foundation
  APIs, then embed, rerank, or classify the results in your recipes.
---

# Jina

[Jina AI](https://jina.ai) provides Search Foundation APIs for reading web pages, transforming web pages into LLM-friendly markdown, web search, text segmentation, embeddings, reranking, classification, and DeepSearch research. The Jina connector lets you read, search, and process text and web content for LLM and search workflows.

Use the Jina connector to:

- Read a URL and convert it into clean markdown or JSON.
- Search the web and return LLM-friendly results.
- Segment text into tokenized chunks.
- Generate vector embeddings for text.
- Rerank documents by relevance to a query.
- Classify text with zero-shot or few-shot labels.
- Run a DeepSearch chat completion for research tasks.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Jina API endpoint. Refer to the Jina [API documentation](https://api.jina.ai/scalar) for endpoint details.

## Install Jina from the community library

Complete the following steps to install the Jina connector from the [community library](https://www.workato.com/browse/connectors):

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

The Jina connector uses API key authentication.

### Jina setup for API key authentication

Complete the following steps to create a Jina API key:

1. Go to [Jina AI](https://jina.ai/).
   
2. Click **< > API**.
   
3. Click the **API KEY & BILLING** tab.
   
4. Select **With Jina Search Foundation API** and click **Available tokens**.
   
5. Copy and save the **API key** for use in Workato.
   

### Connect to Jina using API key authentication

Complete the following steps to set up a Jina connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Jina` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Jina connection setup details](/assets/jina-connection-setup.BxmpVEq1.png)_Jina connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API key**. Refer to [Jina setup for API key authentication](#jina-setup) for more information.
   
6. Click **Connect**.

---
