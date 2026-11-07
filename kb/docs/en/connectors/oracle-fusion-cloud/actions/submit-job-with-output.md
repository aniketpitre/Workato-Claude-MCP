---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/submit-job-with-output.md
description: >-
  The Submit job with output action submits an Enterprise Scheduling Service
  (ESS) job request for a specified job definition and sends a callback message
  to the specified callback URL when the job completes.
---

# Oracle Fusion Cloud - Submit job with output action

The **Submit job with output** action submits an Enterprise Scheduling Service (ESS) job request for a specified job definition. The action sends a callback message to the specified URL when the job completes.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job package name | Enter the ESS job package name. |
| Job definition name | Enter the ESS job definition name. |
| Callback URL | Enter the web service callback URL to receive the ESS job status. |
| Parameter list | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted ESS job. |
