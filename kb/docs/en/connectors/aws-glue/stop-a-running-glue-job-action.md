---
url: >-
  https://docs.workato.com/en/connectors/aws-glue/stop-a-running-glue-job-action.md
description: >-
  The Stop a running Glue job action stops a running job for an AWS Glue job you
  select.
---

# AWS Glue - Stop a running Glue job action

The **Stop a running Glue job** action stops a job run for a AWS Glue job you select.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the name of the job run to stop. |
| Job run ID | Enter the ID of the job run to stop. |

## Output

| Output field | Description |
| --- | --- |
| Successful submissions | A list of the job runs that were successfully stopped. This includes, `Job name` and `Job run ID`. |
| Errors | Any errors that result from the action. This includes, `Job name`, `Job run ID`, and `Error detail.` |
