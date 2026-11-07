---
url: 'https://docs.workato.com/en/connectors/firecrawl/crawl-a-site-action.md'
description: >-
  Follow links from a starting URL to scrape an entire site, then check progress
  with Get crawl job status.
---

# Firecrawl - Crawl a site action

The **Crawl a site** action starts a crawl on a domain in Firecrawl and scrapes each page it discovers.

> **WAIT FOR COMPLETION**
> 
> This action submits the crawl by default, then polls every 60 seconds until the job's status is **completed** or **failed**. Select **No** for **Wait for completion** to return the job ID immediately instead, then use the [Get crawl job status](/en/connectors/firecrawl/get-crawl-job-status-action) action to check on it later.

## Input

The following input fields are the most commonly used. Refer to the Firecrawl [Crawl API](https://docs.firecrawl.dev/api-reference/endpoint/crawl-post) documentation for the complete list of input fields.

| Input field | Description |
| --- | --- |
| URL | Enter the absolute URL to crawl, for example `https://docs.firecrawl.dev`. |
| Prompt | Optional. Enter natural language to generate crawler options. Explicit fields you set override the generated values. |
| Limit | Optional. Enter the maximum pages to crawl. Costs one credit per page. The connector default is `10`. The Firecrawl API default is `10000`. Firecrawl returns a `402` error if **Limit** is higher than your remaining credits. |
| Include paths | Optional. Enter pathname regex patterns to include in the crawl, for example `blog/.*`. |
| Exclude paths | Optional. Enter pathname regex patterns to exclude from the crawl, for example `admin/.*`. |
| Crawl entire domain | Optional. Select **Yes** or **No** to follow sibling and parent internal links, not only child links. |
| Scrape options | Optional. Set formats and scrape options, such as **Only main content** or **Skip TLS verification**. This is applied to every page the crawl scrapes. Scrape options uses the same options as the [Scrape a page](/en/connectors/firecrawl/scrape-a-page-action) action. |
| Wait for completion | Optional. Select **Yes** or **No** to poll until the job finishes and returns the result. The default is **Yes**. |
| Max poll minutes | Optional. Enter the maximum minutes to poll. Valid values are 1-60. The default is `10`. This field is only available when **Wait for completion** is **Yes**. |
| Custom output fields | Optional. Add fields to create datapills for page data that the default output doesn't include. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the request was successful. |
| Status | The job's status. Options are `scraping`, `completed`, or `failed`. |
| Completed | The number of pages crawled so far. |
| Total | The total number of pages discovered. |
| Credits used | The number of credits the job used. |
| Expires at | The date and time the job's results expire. |
| Data | The crawled pages' data, one entry per page. |
| Created at | The date and time the job was created. |
| Completed at | The date and time the job finished. |
| Next | The URL to retrieve the next chunk of results, if the crawl isn't finished or the response is larger than 10 MB. Extract the value for the **Skip** field in the [Get crawl job status](/en/connectors/firecrawl/get-crawl-job-status-action) action from this URL. |

---
