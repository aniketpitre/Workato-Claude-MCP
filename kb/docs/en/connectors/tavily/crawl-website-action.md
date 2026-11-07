---
url: 'https://docs.workato.com/en/connectors/tavily/crawl-website-action.md'
description: >-
  The Crawl website action traverses a website starting from a root URL and
  returns extracted content for each page.
---

# Tavily - Crawl website action

The **Crawl website** action traverses a website starting from a root URL using Tavily and returns extracted content for each page.

## Input

| Input field | Description |
| --- | --- |
| URL | Enter the root URL to begin crawling from. |
| Instructions | Enter natural-language guidance for the crawler. |
| Chunks per source | Enter the number of chunks to use for each source. Only used when the **Instructions** field is populated. |
| Select paths | Enter a regex path pattern to include in the crawl. |
| Select domains | Enter a regex domain pattern to include in the crawl. |
| Exclude paths | Enter a regex path pattern to exclude in the crawl. |
| Exclude domains | Enter a regex domain pattern to exclude in the crawl. |
| Include images | Include images found during the crawl. |
| Include favicon | Select whether to include the favicon URL for each result. |
| Include usage | Select whether to include credit usage information in the result. |

## Output

| Output field | Description |
| --- | --- |
| Base URL | The root URL the crawl started from. |
| Results | The crawled pages. Each result includes the URL, raw content, favicon, and images. |
| Response time | The time Tavily took to process the crawl, in seconds. |
| Usage | The number of credits the crawl consumed. |
| Request ID | The unique identifier for this crawl request. |

---
