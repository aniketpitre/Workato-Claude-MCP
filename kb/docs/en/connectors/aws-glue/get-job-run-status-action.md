---
url: 'https://docs.workato.com/en/connectors/aws-glue/get-job-run-status-action.md'
description: The Get job run status action retrieves the status of an AWS Glue job.
---

# AWS Glue - Get job run status action

The **Get job run status** action retrieves the status of an AWS Glue job run in AWS Glue. This action returns status information including the job state, start time, and execution time. Job run history is accessible for 365 days for your workflow and job run.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the name of the job to get the status of. |
| Job run ID | Enter the ID of the job to get the status of. |
| Include predecessors | Select `Yes` to include a list of predecessor runs in the response. Select `No` the omit this from the response. |

## Output

The output for this action includes the job name, job name ID, and job run state. Refer to the [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html) documentation for a full list of output fields.

---
