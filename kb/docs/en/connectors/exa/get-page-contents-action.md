---
url: 'https://docs.workato.com/en/connectors/exa/get-page-contents-action.md'
description: >-
  Retrieve the text, highlights, or a summary for one or more URLs or Exa
  document IDs, and check the status of each.
---

# Exa - Get page contents action

The **Get page contents** action retrieves the text, highlights, or a summary for up to 100 known URLs or Exa document IDs.

## Input

The following are a representative set of input fields. Refer to the Exa [Contents](https://exa.ai/docs/reference/get-contents) documentation for more information on available input fields.

| Input field | Description |
| --- | --- |
| Document IDs | Enter the Exa document IDs from your searches. Each ID is 1-2048 characters. Provide either **Document IDs** or **URLs**, not both. |
| URLs | Enter the URLs to retrieve. Each URL is 1-2048 characters. Provide either **URLs** or **Document IDs**, not both. |
| Summary | Optional. Add this field to return an LLM-generated summary for each result. Leave blank to return no summary. |
| Summary schema | Optional. Define the fields of the structured summary. Add fields manually or generate a schema from a sample. Each field becomes an individual datapill. Leave blank to return a plain-text summary when you add the **Summary** field. |
| Text | Optional. Return the full page text for each result. Leave blank to skip page text. |
| Subpage targets | Optional. Enter the site sections to prioritize when crawling subpages. Each target is 1-100 characters. Leave blank to crawl subpages without a priority. |
| Subpages | Optional. Enter the number of linked subpages to crawl from each URL. Valid values are `0`\-`100`. Defaults to `0` if left blank. |
| Max age hours | Optional. Enter the maximum age of cached content in hours. Valid values are `-1` to `720`. Enter `0` to always fetch fresh content, or `-1` to always use the cache. Leave blank to use cached content when available and fetch live content otherwise. |
| Live crawl timeout (ms) | Optional. Enter the milliseconds to wait for a fresh crawl. The maximum is `90000`. Defaults to `10000` if left blank. |

## Output

The following are a representative set of output fields. Refer to the Exa [Contents](https://exa.ai/docs/reference/get-contents) documentation for more information on available output fields.

| Output field | Description |
| --- | --- |
| Request ID | The unique ID of the request. |
| Results | The retrieved pages. |
| ID (Results) | The unique ID of the page. |
| URL (Results) | The URL of the page. |
| Text (Results) | The full text of the page. Exa returns this value only when you request page text. |
| Summary (Results) | The summary of the page. Each field becomes an individual datapill when you define a **Summary schema**. |
| Subpages (Results) | The subpages Exa crawled from the page. Exa returns this value only when you set **Subpages** above `0`. |
| Statuses | The status of each requested URL or ID. Use it to find failed retrievals. |
| ID (Statuses) | The URL or ID the status applies to. |
| Status (Statuses) | The result of the retrieval. For example, `success`. |

---
