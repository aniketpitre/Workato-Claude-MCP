---
url: 'https://docs.workato.com/en/connectors/deputy/update-resource-action.md'
description: >-
  The Update resource action in the Deputy connector updates a resource such as
  an employee agreement, employee workplace, or training record.
---

# Deputy - Update resource action

This action updates a resource in your Deputy instance. Supported resources are:

- EmployeeAgreement
- EmployeeWorkplace
- TrainingRecord

![Update resource action](/assets/update-resource-action.kn6VWmr_.png)_Update resource action_

## Input

<dl><dt>Resource type</dt><dd>The type of resource to be updated.</dd><dt>Resource</dt><dd>The resource to be updated. Supports selection from a list of available resources in your Deputy instance or manual input of the resource ID.</dd><dt>Resource data</dt><dd>The data for resource to be updated. Available fields will vary based on the selected resource type above.</dd></dl>

## Output

The output of this action is a datatree that contains information about the resource object after update.

---
