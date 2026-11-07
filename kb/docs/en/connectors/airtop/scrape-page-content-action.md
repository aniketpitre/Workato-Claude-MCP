---
url: 'https://docs.workato.com/en/connectors/airtop/scrape-page-content-action.md'
description: >-
  The Scrape page content action enables you to extract the current page as
  markdown in Airtop.
---

# Airtop - Scrape page content action

The **Scrape page content** action scrapes the current browser window and returns the page content as markdown.

## Input

| Input field | Description |
| --- | --- |
| Session ID | Enter the ID of the browser session that owns the window. |
| Window ID | Enter the Airtop window ID returned when you create a window. |
| Client request ID | Enter a client-provided identifier echoed back in the response metadata. |
| Cost threshold credits | Enter a threshold to cancel the operation after this amount is exceeded. Set to `0` to disable. |
| Time threshold seconds | Enter a threshold to cancel the operation after this many seconds. Set to `0` to disable. |

## Output

| Output field | Description |
| --- | --- |
| Content type | MIME type of the scraped content. |
| Text | Scraped page content as markdown. |
| Title | Title of the scraped page. |
| Selected text | Text selected on the page at the time of scraping. |
| Meta | Metadata about the request, including credits consumed. |
| Errors | List of errors returned for the request. |
| Warnings | List of warnings returned for the request. |

---
