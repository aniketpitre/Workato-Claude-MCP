---
url: 'https://docs.workato.com/en/connectors/deputy/associate-employee-action.md'
description: >-
  The Associate employee action in the Deputy connector links an employee to an
  existing employee workplace and optionally an employee agreement.
---

# Deputy - Associate employee action

This action allows you to associate an employee with an existing employee workplace and/or employee agreement.

![Associate employee action](/assets/associate-employee-action.BA1N-X6e.png)_Associate employee action_

## Input

<dl><dt>Employee</dt><dd>The employee to associate items with. Supports selection from a list of available employees in your Deputy instance or manual input of the employee ID.</dd><dt>Employee workplace</dt><dd>The employee workplace to be associated with the employee. Supports selection from a list of available workplaces in your Deputy instance or manual input of the workplace ID.</dd><dt>Employee agreement</dt><dd>The employee agreement to be associated with the employee. Supports selection from a list of available agreements in your Deputy instance or manual input of the agreement ID.<br>Optional field.</dd><dt>Set workplace as primary</dt><dd>Makes the newly-associated workplace as primary workplace if set to true/1. Defaults to false/0.<br>Optional field.</dd></dl>

## Output

The output of this action is a datatree that contains information about the employee object associated.

---
