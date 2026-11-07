---
url: 'https://docs.workato.com/en/connectors/firecrawl/search-the-web-action.md'
description: >-
  Query the live web the same way a search engine would, and optionally scrape
  the full content of each result.
---

# Firecrawl - Search the web action

The **Search the web** action searches the live web for pages, news, or images in Firecrawl.

## Input

The following input fields are the most commonly used. Refer to the Firecrawl [Search API](https://docs.firecrawl.dev/api-reference/endpoint/search) documentation for the complete list of input fields.

| Input field | Description |
| --- | --- |
| Query | Enter the search query. The maximum is 500 characters. This field supports operators such as `site:`, `intitle:`, `filetype:`, quotes, and `-`. |
| Limit | Optional. Enter the results per source type. Valid values are 1-100. The default is `10`. |
| Sources | Optional. Select the result types to return. Options are **Web**, **News**, or **Images**. The default is **Web**. |
| Categories | Optional. Select categories to filter web results. Options are **Research**, **PDF**, or **Developer**. No category filter by default. |
| Include domains | Optional. Enter hostnames to restrict results to. This field can't be used with **Exclude domains**. |
| Exclude domains | Optional. Enter hostnames to exclude from results. This field can't be used with **Include domains**. |
| Time filter (tbs) | Optional. Enter a time filter, for example `qdr:d` for the past day or `qdr:w` for the past week. |
| Country | Optional. Enter an ISO country code for geo-targeting, for example `US`. |
| Highlights | Optional. Select **Yes** or **No** to generate query-relevant highlights. The default is **Yes**. |
| Scrape options | Optional. Set formats and scrape options to include each result's full page content. Scrape options uses the same options as the [Scrape a page](/en/connectors/firecrawl/scrape-a-page-action) action. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the request was successful. |
| ID | The search's unique identifier. |
| Credits used | The number of credits the search used. |
| Warning | A warning message about the search, if any. |
| Error | The error message, if the search failed. |
| Scrape IDs | The scrape job IDs for the web, news, and image results. |
| Data | The search results, grouped into web, news, and image lists. |

---
