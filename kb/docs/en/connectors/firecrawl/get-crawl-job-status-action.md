---
url: >-
  https://docs.workato.com/en/connectors/firecrawl/get-crawl-job-status-action.md
description: >-
  Check on a crawl you started without waiting for it to finish, and page
  through large result sets with the Skip cursor.
---

# Firecrawl - Get crawl job status action

The **Get crawl job status** action retrieves a crawl job by ID in Firecrawl. Use this action to check on a job you started with the [Crawl a site](/en/connectors/firecrawl/crawl-a-site-action) action when **Wait for completion** is **No**.

## Input

| Input field | Description |
| --- | --- |
| Crawl job ID | Enter the job ID returned by **Crawl a site**. |
| Skip | Optional. Enter an offset for paging large crawl results, from the job's `next` cursor. |
| Custom output fields | Optional. Add fields to create datapills for crawled page data that the default output doesn't include. |

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
| Next | The URL to retrieve the next chunk of results, if the crawl isn't finished or the response is larger than 10 MB. Extract the value for the **Skip** field from this URL. |
