---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/list-time-off-requests-action.md
description: >-
  The List time off requests action in the BambooHR connector lets you list time
  off requests between two dates, with filters to narrow the result.
---

# BambooHR - List time off requests action

This action lists all time off requests occurring between two specified dates. More filters can be specified to further narrow down the result.

## Input

![List time off requests action](/assets/list-time-off-requests-action._hgttR2f.png)_List time off requests action_

| Input field | Description |
| --- | --- |
| Start date _required_ | The start date of the time off. Select date or type it in YYYY-MM-DD format. |
| End date _required_ | The end date of the time off. Select date or type it in YYYY-MM-DD format. |
| Request ID | Specify a request ID to narrow the result to just this particular request. |
| Employee ID | Specify an employee ID to narrow the result to just requests from this particular employee. |
| Type | Select the type(s) of time off to narrow the result to, or input ID of each of them manually separated by comma. |
| Status | Select the status(es) of time off to narrow the result to, or input each of them manually separated by comma. |

## Output

The output of this action is a list of time off request objects, including the **List size** and **List index**. For more information on the structure of the time off request object, check out the [BambooHR documentation](https://documentation.bamboohr.com/reference/time-off-get-time-off-requests-1).
