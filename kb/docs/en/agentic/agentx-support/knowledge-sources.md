---
url: 'https://docs.workato.com/en/agentic/agentx-support/knowledge-sources.md'
description: >-
  Connect external content as knowledge sources so your AgentX Support AI agent
  and search can answer questions from your existing systems.
---

# AgentX Support - Knowledge sources

Knowledge sources let you connect external content as reference material for your AI agent. These sources enable the agent to answer user questions using up-to-date information from your existing systems.

Knowledge sources also power the [search](/en/agentic/agentx-support/search) experience you can add to your site. You can connect multiple sources to AgentX Support, which syncs content from different systems and lets users search across them in one place.

## Create a knowledge source

Complete the following steps to create a knowledge source:

1. Go to **Knowledge Sources**.
   
2. Click **New Source**.
   
   ![Create a knowledge source](/assets/knowledge-sources.BRj1ikPN.png)_Create a knowledge source_
   
3. Enter a knowledge source name in the **Name** field.
   
4. Use the **Source** drop-down menu to select a knowledge source type. Options include:
   
   - Zendesk
   - Salesforce
   - JSON
   - Sitemap
   - Brightspot
5. Optional. Select the **Use Connection** checkbox to use an existing connection, then choose a connection from the **Connection Name** drop-down menu.
   
6. Configure additional fields based on your knowledge source type:
   
   **Sitemap**
   
   - **Sitemap URL**: The URL of your sitemap file. For example, `https://docs.acme.com/sitemap.xml`.
     
   - **URL Match** (optional): Use this to limit which URLs from the sitemap should be included.
     
   - **Fields**: Define which parts of each page should be extracted. Each field is specified using a JSON object that describes how to locate and extract content from the HTML. Common properties include:
     
     - `name`: The name of the field.
     - `type`: The format of the data, such as `"text"` or `"html"`.
     - `selector`: A CSS selector used to extract the element.
     - `xpath`: (optional) An XPath expression to extract content.
     - `attribute`: (optional) The HTML attribute to extract. For example, `"lang"`.
   
   For example:
   
   ```json
   [
     {
       "name": "title",
       "type": "text",
       "selector": "title"
     },
     {
       "name": "body",
       "type": "html",
       "selector": ".content"
     },
     {
       "name": "locale",
       "xpath": "//html[@lang]",
       "attribute": "lang"
     }
   ]
   ```
   
   **Salesforce or Brightspot**
   
   Provide the necessary details in the **Config** field.
   
7. Click **Submit**.
   

## Sync knowledge sources

Knowledge sources are automatically synced daily. You can click **Sync** to trigger a manual sync.

---
