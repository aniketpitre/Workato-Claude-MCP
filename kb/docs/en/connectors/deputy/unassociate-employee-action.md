---
url: 'https://docs.workato.com/en/connectors/deputy/unassociate-employee-action.md'
description: >-
  The Unassociate employee action in the Deputy connector removes the link
  between an employee and an existing employee workplace.
---

# Deputy - Unassociate employee action

This action allows you to unassociate an employee with an existing employee workplace. To unassociate an employee agreement, you need to use the `Associate employee` action to substitute the existing agreement with a new one.

![Unassociate employee action](/assets/unassociate-employee-action.BXSPZlSv.png)_Unassociate employee action_

## Input

<dl><dt>Employee</dt><dd>The employee to unassociate items with. Supports selection from a list of available employees in your Deputy instance or manual input of the employee ID.</dd><dt>Employee workplace</dt><dd>The employee workplace to be unassociated with the employee. Supports selection from a list of available workplaces in your Deputy instance or manual input of the workplace ID.</dd></dl>

## Output

The output of this action is a boolean. It will be `true` with response code `200` if successful.

---
