---
url: 'https://docs.workato.com/en/connectors/firecrawl/extract-data-action.md'
description: >-
  Send a prompt to Firecrawl's Agent to pull structured data from the web,
  polling automatically until the job completes.
---

# Firecrawl - Extract data action

The **Extract data** action runs an Agent extraction job in Firecrawl. A prompt is required, and you can optionally add a JSON schema to further constrain the extracted data. URLs are optional. Agent searches and navigates the web on its own if you leave URLs blank.

> **WAIT FOR COMPLETION**
> 
> This action submits the job by default, then polls every 60 seconds until the job's status is **completed** or **failed**. Select **No** for **Wait for completion** to return the job ID immediately instead, then use the [Get extract job status](/en/connectors/firecrawl/get-extract-job-status-action) action to check on it later.

## Input

The following input fields are the most commonly used. Refer to the Firecrawl [Agent API](https://docs.firecrawl.dev/features/agent) documentation for the complete list of input fields.

| Input field | Description |
| --- | --- |
| Prompt | Enter a natural-language description of the data to extract. The maximum is 10,000 characters. |
| JSON schema | Optional. Enter a JSON schema describing the data to extract. This schema is sent to Firecrawl only. Add matching fields in **Custom output fields** to get datapills for the extracted data. |
| URLs | Optional. Enter the URLs to focus the Agent on. |
| Enable web search | Optional. Select **Yes** or **No**. Select **No** to keep the Agent only on the URLs you provide. The default is **Yes**. |
| Max credits | Optional. Enter a credit cap for this run. The job fails with no data if the cap is reached. This connector default is `100`. The Firecrawl API default is `2500`. |
| Model | Optional. Select the model to use. Options are **Spark 2**, **Spark 1 Mini**, or **Spark 1 Pro**. The default is **Spark 2**. Firecrawl accepts the **Spark 1** options but routes crawl requests to **Spark 2**. |
| Effort | Optional. Select the reasoning budget for Spark 2. Options are **Low**, **Medium**, or **High**. |
| Wait for completion | Optional. Select **Yes** or **No** to poll until the job finishes and returns the result. The default is **Yes**. |
| Max poll minutes | Optional. Enter the maximum minutes to poll. Valid values are 1-60. The default is `10`. This field is only available when **Wait for completion** is **Yes**. |
| Custom output fields | Optional. Add fields to create datapills for extracted data fields that the default output doesn't include. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the request was successful. |
| Status | The job's status. Options are `processing`, `completed`, or `failed`. Canceled jobs also report `failed`. |
| Model | The model used for the job. |
| Effort | The reasoning budget used for the job. |
| Mode | The Agent mode used for the job, for example `extract`. |
| Expires at | The date and time the job's results expire. |
| Error | The error message, if the job failed. |
| Message | A message describing the result of the job. |
| Data | The extracted data, matching your prompt or schema. |
| Created at | The date and time the job was created. |

---

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

---

---
url: >-
  https://docs.workato.com/en/connectors/firecrawl/get-extract-job-status-action.md
description: >-
  Check the status of an Agent extraction job started by the Extract data
  action, using the job ID it returned.
---

# Firecrawl - Get extract job status action

The **Get extract job status** action retrieves an Agent job by ID in Firecrawl. Use this action to check on a job you started with the [Extract data](/en/connectors/firecrawl/extract-data-action) action when **Wait for completion** is **No**.

## Input

| Input field | Description |
| --- | --- |
| Agent job ID | Enter the ID of the Agent job to check. |
| Custom output fields | Optional. Add fields to create datapills for extracted data fields that the default output doesn't include. |

## Output

| Output field | Description |
| --- | --- |
| Success | A `true` or `false` boolean response that indicates if the request was successful. |
| Status | The job's status. Options are `processing`, `completed`, or `failed`. Canceled jobs also report `failed`. |
| Model | The model used for the job. |
| Effort | The reasoning budget used for the job. |
| Mode | The Agent mode used for the job, for example `extract`. |
| Expires at | The date and time the job's results expire. |
| Error | The error message, if the job failed. |
| Message | A message describing the result of the job. |
| Data | The extracted data, matching your prompt or schema. |
| Created at | The date and time the job was created. |

---
