---
url: >-
  https://docs.workato.com/en/connectors/oracle-fusion-cloud/actions/export-bulk-data.md
description: >-
  The Export bulk data action submits an ESS job request to export large
  datasets from Oracle Fusion Cloud.
---

# Oracle Fusion Cloud - Export bulk data action

The **Export bulk data** action submits an ESS job request to export large datasets from Oracle Fusion Cloud. After the job completes, it automatically uploads the output and log files to Universal Content Management (UCM) for download.

> **SOAP ACTION**
> 
> This action uses SOAP APIs.

## Input

| Input field | Description |
| --- | --- |
| Job name | Enter the ESS job package and job name, separated by a semicolon. |
| Parameter list | Specify the parameters used to invoke the ESS job. The only supported parameters are `submit.argument1` to `submit.argumentN`. Enter ESS job parameters in order: `submit.argument1`, `submit.argument2`, `submit.argument3` ... `submit.argumentN`. The corresponding entry in the list should be blank or passed as `#NULL` when a given parameter doesn't need to be passed or is null. If a parameter value contains a comma, enclose the parameter value within double quotes. |
| Job options | Specify processing parameters as key-value pairs, separated by commas. |
| Notification code | Enter a [two-digit number](https://docs.oracle.com/en/cloud/saas/financials/25c/oeswf/erpintegrationservice-d16510e420.html#extractAndPurge) to define when to send a bell or email notification. |
| Callback URL | Provide the web service callback URL to receive the ESS job status. Use `#NULL` if no callback is required. |

## Output

| Output field | Description |
| --- | --- |
| Result | Returns the request ID of the submitted ESS job. |
