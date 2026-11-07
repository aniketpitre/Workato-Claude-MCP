---
url: 'https://docs.workato.com/en/connectors/deputy/new-employee-trigger.md'
description: >-
  The New employee trigger in the Deputy connector fires when new employee
  records are created in your Deputy instance, picking them up on each poll.
---

# Deputy - New employee trigger

This trigger fetches new employee records in your Deputy instance.

![New employee trigger](/assets/new-employee-trigger.C_-QJeUG.png)_New employee trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Optional. Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new employee object.

Find out more about [employee object](https://www.deputy.com/api-doc/Resources/Employee/).

---
