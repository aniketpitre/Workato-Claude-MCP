---
url: >-
  https://docs.workato.com/en/connectors/microsoft-fabric/query-activity-run-action.md
description: >-
  The Query activity run action enables you to query the activities inside a job
  of an item in Microsoft Fabric.
---

# Microsoft Fabric - Query activity run action

The **Query activity run** action enables you to query the activities inside a job of an item in Microsoft Fabric.

## Input

| Input field | Description |
| --- | --- |
| Workspace ID | Enter the ID of the workspace where the item is located. |
| Job ID | Enter the ID of the Job to query the activities of. |
| Last updated after | Enter the date & time of the activity from which to run the query. |
| Last updated before | Enter the date & time of the activity up to where to run the query. |
| Continuation token | Enter the token to make the next request. Useful for pagination. |
| Filters | Enter the list of operands, operators and values to add filters to the query. |
| Order by | Enter the list of orders and order by attributes to apply sorting on the query records. |

## Output

| Output field | Description |
| --- | --- |
| Continuation token | Token used for pagination. |
| values | Array of returned items. |
| Activity name | Name of the activity. |
| Activity run end | Date and time when the activity run ended. |
| Activity run ID | ID of the activity run. |
| Activity run start | Date and time when the activity run started. |
| Activity type | Type of the activity. |
| Duration in ms | Duration in milliseconds for which the activity ran. |
| Error | Error occurred during the activity, if any. |
| Linked service name | Name of any linked service. |
| Input | Key-value pairs of input data to the activity. |
| Output | Key-value pairs of output data from the activity. |
| Pipeline name | Name of the pipeline. |
| Pipeline run ID | ID of the pipeline run. |
| Status | Status of the activity. |
| User properties | User properties, if any. |
| Iteration hash | Hash of the iteration. |
| Retry attempt | Number of retry attempts, if any. |
| Recovery status | Recovery status of the pipeline. |
| Execution details | Details of the execution of the activity. |
| Integration runtime names | Names of the integration runtimes, if any. |
