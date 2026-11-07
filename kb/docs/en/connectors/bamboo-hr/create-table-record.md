---
url: 'https://docs.workato.com/en/connectors/bamboo-hr/create-table-record.md'
description: >-
  The Create table record of employee action adds a new row to a selected
  BambooHR employee table.
---

# BambooHR – Create table record of employee action

The **Create table record of employee** action adds a new row to an employee's table in BambooHR. You must specify the employee's internal ID and select the target table. This action supports standard and custom tables.

You can use the [Get table records of employee](/en/connectors/bamboo-hr/get-table-records-of-employee-action) action to retrieve available row IDs from a specific table.

## Input

| Input field | Description |
| --- | --- |
| Employee ID | Enter the internal BambooHR ID of the employee. |
| Table | Choose the target table where you plan to create the record. For example, select **commission** to insert a commission record. |

Additional input fields may appear based on the selected **Table**.

## Output

| Output field | Description |
| --- | --- |
| Success | Indicates the result of the table record creation. |

---

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

---
