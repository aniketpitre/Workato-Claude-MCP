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
