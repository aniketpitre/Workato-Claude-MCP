---
url: 'https://docs.workato.com/en/connectors/aws-glue/list-job-runs-action.md'
description: >-
  The List job runs action retrieves a list of job runs for a specific AWS Glue
  job.
---

# AWS Glue - List job runs action

The **List job runs** action retrieves a list of job runs for a specific AWS Glue job.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the name of the job to retrieve job runs for. |
| Next token | Enter a continuation token to use pagination for the response. |
| Max results | Enter a number for the maximum number of results to return. The default is `50`. |
| Job run state | Select the state of the job runs to return. |
| Started after | Enter a date to only return job runs that started after the selected date. |
| Started before | Enter a date to only return job runs that started before the selected date. |

## Output

| Output field | Description |
| --- | --- |
| Job runs | The job runs that meet your filter criteria. |
| Next token | A continuation token for the response, if the returned list does not contain the last metric available. |

---
