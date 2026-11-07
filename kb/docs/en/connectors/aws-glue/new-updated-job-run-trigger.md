---
url: 'https://docs.workato.com/en/connectors/aws-glue/new-updated-job-run-trigger.md'
description: The New/updated job run trigger monitors AWS Glue for new or updated job runs.
---

# AWS Glue - New/updated job run trigger

The **New/updated job run** trigger monitors AWS Glue for new or updated job runs.

## Input

| Input field | Description |
| --- | --- |
| Trigger poll interval | Select an interval to check AWS Glue for new or updated job runs. Refer to [Polling intervals](/en/recipes/polling-intervals) for more information. |
| Job name | The name of the job to monitor for new or updated job runs. |
| Filter by job run state | Select the job run state to filter job runs. |

## Output

Action output includes the job name, job run ID, and job run state. Refer to the [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html) documentation for a full list of output fields.

---
