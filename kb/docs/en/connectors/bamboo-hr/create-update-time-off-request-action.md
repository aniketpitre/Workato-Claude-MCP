---
url: >-
  https://docs.workato.com/en/connectors/bamboo-hr/create-update-time-off-request-action.md
description: >-
  The Create/update time off request action in the BambooHR connector lets you
  create or update a time off request on behalf of an employee.
---

# BambooHR - Create/update time off request action

This action creates/updates a time off request on behalf of an employee in your BambooHR instance.

## Input

![Create/update time off request action](/assets/create-update-time-off-request-action.DJAZN57C.png)_Create/update time off request action_

| Input field | Description |
| --- | --- |
| Employee ID _required_ | The ID of the employee requesting for time off. |
| Time off type _required_ | The type of the time off requested. Select from the options provided or enter the type ID manually. |
| Start date _required_ | The start date of the time off. Select date or type it in YYYY-MM-DD format. |
| End date _required_ | The end date of the time off. Select date or type it in YYYY-MM-DD format. |
| Status _required_ | The status of the time off request. Select from the picklist or input either approved, requested or denied. |
| Break down amount per day _required_ | When enabled, a break down of the amount of time off taken by the employee per day needs to be provided. Allowed values are true or false. |
| Note | Enter any notes you want to attach to the request. By default note will be made on behalf of the requesting employee. |
| Previous request ID | When an existing request is selected, an update will be performed instead. Leave blank to create a new request. |
| Date _required when specifying amount per date_ | Select date or type it in YYYY-MM-DD format. |
| Amount _required_ | Enter a whole number indicating the number of days/hours to update the employee's balance by. You cannot specify the units to add. The unit will be whatever the time off type is configured for. |

## Output

| Output field | Description |
| --- | --- |
| Status | The status indicating the outcome of the request. |
