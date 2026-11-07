---
url: 'https://docs.workato.com/en/connectors/tavily/search-web-action.md'
description: >-
  The Search web action executes a web search using Tavily and returns ranked
  results, an optional AI-generated answer, and optional images.
---

# Tavily - Search web action

The **Search web** action executes a web search using Tavily and returns ranked results, an optional AI-generated answer, and optional images.

## Input

| Input field | Description |
| --- | --- |
| Query | Enter the search query you plan to execute with Tavily. |
| Search depth | Select either **Basic**, **Fast**, **Advanced**, or **Ultra-fast** to configure latency and relevance. Defaults to **Basic**. |
| Topic | Select the search category, such as **General**, **News**, or **Finance**. Defaults to **General**. |
| Max results | Enter the maximum number of results to return, from `0` to `20`. Defaults to `10`. |
| Chunks per source | Enter the maximum number of content snippets to return for each source, from `1` to `3`. Defaults to `3`. |
| Start date | Enter a date, in `YYYY-MM-DD` format, to return results published or updated on or after this date. |
| End date | Enter a date, in `YYYY-MM-DD` format, to return results published or updated on or before this date. |
| Include answer | Select the answer type to include in the response. **Basic** returns a quick answer. **Advanced** returns a more detailed one. |
| Include raw content | Select a format to include cleaned page content for each result, as **Markdown** or **Text**. |
| Include images | Select whether to include query-related images in the response. |
| Include image descriptions | Select whether to include a description for each image. Only included when **Include images** is enabled. |
| Include favicon | Select whether to include a favicon URL for each result. |
| Include domains | Select the domains to restrict or boost the search. The maximum is `300`. You can include one domain for each item. |
| Exclude domains | Select the domains to exclude from the search. The maximum is `150`. You can exclude one domain for each item. |
| Include domains mode | Select how the **Include domains** field is applied. `Filter` restricts to those domains. `Boost` searches the rest of the web in addition to the included domains. Requires that **Include domains** is populated. |
| Country | Select whether to boost results from this country. Only applies when **Topic** is **General**. |
| Language | Select a language to boost results in. We recommend entering **Query** in the same language. |
| Filter by language | Select whether to exclude results that don't match **Language**. Requires **Language** to be set. |
| Auto parameters | Select whether to let Tavily automatically configure other search parameters based on your query. |
| Exact match | Select whether to return only results that contain the exact phrases quoted in your query. |
| Include usage | Select whether to include credit usage information in the response. |
| Safe search | Select whether to filter out adult or unsafe content. Not supported when **Search depth** is **Fast** or **Ultra-fast**. |

## Output

| Output field | Description |
| --- | --- |
| Query | The search query that was executed. |
| Answer | The LLM-generated answer, if **Include answer** was enabled. |
| Follow-up questions | Suggested follow-up questions. |
| Images | Query-related images, if **Include images** was enabled. Each image includes a URL, title, relevance score, and description if **Include image descriptions** was enabled. |
| Results | The ranked list of search results. Each result includes a title, URL, content snippet, relevance score, raw content, favicon, ID, and any related images. |
| Auto parameters | The topic, search depth, and time range Tavily selected automatically, if **Auto parameters** was enabled. |
| Response time | The time Tavily took to process the search, in seconds. |
| Usage | The number of credits the search consumed, if **Include usage** was enabled. |
| Request ID | The unique identifier for this search request. |

---
