---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/submit-ess-job-request.md
description: >-
  The Submit ESS job request action submits an Enterprise Scheduling Service
  (ESS) job request for the specified job definition.
---

# Oracle Fusion Cloud - Submit ESS job request action

The **Submit ESS job request** action submits an Enterprise Scheduling Service (ESS) job request for a specified job definition.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job package name | Enter the ESS job package name. |
| Job definition name | Enter the ESS job definition name. |
| Parameter list | Specify the parameters used to invoke the ESS job. Only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted Enterprise Scheduling Service job. |
