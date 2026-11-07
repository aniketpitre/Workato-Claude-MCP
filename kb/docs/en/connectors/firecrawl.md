---
url: 'https://docs.workato.com/en/connectors/firecrawl.md'
description: >-
  Turn any URL into clean markdown, structured JSON, or a screenshot, and
  monitor pages for changes over time.
---

# Firecrawl

[Firecrawl](https://www.firecrawl.dev) turns websites into clean, AI-ready data. The Firecrawl connector lets you scrape, crawl, and search the web, and extract structured data from pages.

Use the Firecrawl connector to:

- Scrape a page to markdown, HTML, JSON, or a full-page screenshot.
- Run an Agent extraction job with a prompt, optionally constrained by a JSON schema, and check its status.
- Crawl a domain, and check the crawl job's status and page data.
- Map a site to return all of its discovered URLs.
- Search the live web for pages, news, or images.
- Detect whether a page changed since the last scrape.

You can also use [custom actions](/en/developing-connectors/custom-actions) to build a custom HTTP request to any Firecrawl API endpoint. Refer to the Firecrawl [API documentation](https://docs.firecrawl.dev/api-reference/v2-introduction) for endpoint details.

## Install Firecrawl from the community library

Complete the following steps to install the Firecrawl connector from the [community library](https://www.workato.com/browse/connectors):

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

The Firecrawl connector uses API key authentication.

### Firecrawl setup for API key authentication

Complete the following steps to retrieve a Firecrawl API key:

1. Sign in to the [Firecrawl dashboard](https://www.firecrawl.dev/app).
   
2. Go to **API Keys**. A default API key starting with `fc-` is generated for you automatically.
   
3. Click **Copy** to save the API key for use in Workato.
   

### Connect to Firecrawl with API key authentication

Complete the following steps to set up a Firecrawl connection in Workato:

1. Click **Create > Connection** or press C twice.
   
2. Search for `Firecrawl` and select it as your app.
   
3. Provide a name for your connection in the **Connection name** field.
   
   ![Firecrawl connection setup details](/assets/firecrawl-connection-setup.-WyeOzAF.png)_Firecrawl connection setup_
   
4. Use the **Location** drop-down menu to select the project where you plan to store the connection.
   
5. Enter the **API key**. Refer to [Firecrawl setup for API key authentication](#firecrawl-setup) for more information.
   
6. Click **Connect**.

---
