---
url: 'https://docs.workato.com/en/connectors/bamboo-hr/create-employee-action.md'
description: >-
  The Create employee action in the BambooHR connector lets you create a new
  employee record with a first name, last name, and optional fields.
---

# BambooHR - Create employee action

This action creates an employee record in your BambooHR instance.

## Input

![Create employee action](/assets/create-employee-action.BNCe_9o3.png)_Create employee action_

| Input field | Description |
| --- | --- |
| First name _required_ | The first name of the new employee record. |
| Last name _required_ | The last name fo the new employee record. |
| Employee input fields | For a full list of employee input fields, see [field names](https://documentation.bamboohr.com/docs/list-of-field-names). |

## Output

| Output field | Description |
| --- | --- |
| Location | The URL to the employee's location in your BambooHR instance. The employee ID is included in this datapill. |

> **No employee details**
> 
> This action does not return the details of the employee created. Use [Get employee details action](/en/connectors/bamboo-hr/get-employee-details-action) to retrieve the employee details by ID.
> 
> Learn how to retrieve the employee ID below.

### How to retrieve the ID of the newly created employee

The employee ID is included in the Location datapill. In the example below, the newly created employee has the ID `40598`. Use formula mode to retrieve the employee ID.

| Step | description |
| --- | --- |
| Employee URL | Response from Create employee action is the Location datapill `https://api.bamboohr.com/api/gateway.php/<acme>/v1/employees/40598`. |
| Employee ID | Switch to **Formula mode**, and parse the datapill with the following format. `<datapill>.split("/'").last` ![Find employee ID](/assets/create-employee-action-get-id.DG0egekO.png) |

---
