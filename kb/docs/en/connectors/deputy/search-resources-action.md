---
url: 'https://docs.workato.com/en/connectors/deputy/search-resources-action.md'
description: >-
  The Search resources action in the Deputy connector finds employee agreements,
  workplaces, or training records matching your search conditions.
---

# Deputy - Search resources action

This action searches for resources matching your search condition in your Deputy instance. Supported resources are:

- EmployeeAgreement
- EmployeeWorkplace
- TrainingRecord

![Search resources action](/assets/search-resources-action.DK-FZ4OA.png)_Search resources action_

## Input

<dl><dt>Resource type</dt><dd>The type of resource to be retrieved.</dd><dt>Search parameters</dt><dd>The available fields for search will be based on the resource type selected above. Note that each additional field will be treated as an `AND` query. The supported search operations are listed below.</dd></dl>

### Supported search operations

The complete list of available search operations is as follows. Note that the applicable list varies depending on the type of the fields added into the search condition.

- `eq`: Equal
- `gt`: Greater than
- `ge`: Greater than or equal
- `lt`: Less than
- `le`: Less than or equal
- `lk`: Like (Can put in % characters to match to a pattern)
- `nk`: Not like
- `ne`: not equal to
- `in`: In a given set of array values
- `nn`: Not in a given set of array values
- `is`: Is something other than 0 or NULL
- `ns`: Not something. Meaning either 0 or NULL

## Output

The output of this action is a list of datatree that contains information about the matching resources object.

---

---
url: >-
  https://docs.workato.com/en/connectors/deputy/search-operational-units-action.md
description: >-
  The Search operational units action in the Deputy connector finds operational
  units that match a given operational unit name.
---

# Deputy - Search operational units action

This action searches for operational units matching the search parameter in your Deputy instance.

![Search operational units action](/assets/search-operational-units-action.izNH3GV4.png)_Search operational units action_

## Input

<dl><dt>Operational unit name</dt><dd>The operational unit name.</dd></dl>

## Output

The output of this action will be a list of datatree that contains information about the operational units searched.

Find out more about [operational unit object](https://www.deputy.com/api-doc/Resources/OperationalUnit/).

---
