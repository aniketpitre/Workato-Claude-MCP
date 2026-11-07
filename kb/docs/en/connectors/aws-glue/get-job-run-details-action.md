---
url: 'https://docs.workato.com/en/connectors/aws-glue/get-job-run-details-action.md'
description: >-
  The Get job run details action retrieves the metadata for a job run in AWS
  Glue.
---

# AWS Glue - Get job run details action

The **Get job run details** action retrieves the metadata for a job run in AWS Glue. Job run history is accessible for 365 days for your workflow and job run.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the name of the job to get the details for. |
| Job run ID | Enter the ID of the job to get details for. |
| Include predecessors | Select `Yes` to include a list of predecessor runs in the response. Select `No` the omit this from the response. |

## Output

| Output field | Description |
| --- | --- |
| Job run | The requested job run metadata. This includes information such as the job run ID, job name, arguments, and more. |

---
