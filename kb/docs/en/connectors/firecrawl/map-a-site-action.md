---
url: 'https://docs.workato.com/en/connectors/firecrawl/map-a-site-action.md'
description: >-
  List every URL Firecrawl discovers on a domain, optionally ordered by
  relevance to a search query.
---

# Firecrawl - Map a site action

The **Map a site** action returns the URLs discovered for a domain in Firecrawl. This action costs one credit per call, not per URL.

## Input

| Input field | Description |
| --- | --- |
| URL | Enter the absolute URL to map, for example `https://docs.firecrawl.dev`. |
| Search | Optional. Enter a query to order URLs by relevance, for example `blog`. |
| Sitemap | Optional. Select how to use the sitemap. Options are **Skip**, **Include**, or **Only**. The default is **Include**. |
| Include subdomains | Optional. Select **Yes** or **No** to include subdomain URLs. The default is **Yes**. |
| Ignore query parameters | Optional. Select **Yes** or **No** to drop URLs that contain query parameters. The default is **Yes**. |
| Ignore cache | Optional. Select **Yes** or **No** to bypass the sitemap cache. The cache lasts up to seven days. The default is **No**. |
| Limit | Optional. Enter the maximum URLs to return. The maximum is 100,000. The default is `5000`. |
| Timeout (ms) | Optional. Enter the request timeout in milliseconds. The default is no timeout. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the request was successful. |
| ID | The map job's unique identifier. |
| Warning | A warning message about the map, if any. |
| Links | The discovered URLs. Each link includes a URL, title, and description. |

---
