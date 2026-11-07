---
url: 'https://docs.workato.com/en/connectors/deputy/new-timesheet-trigger.md'
description: >-
  The New timesheet trigger in the Deputy connector fires when new timesheet
  records are created in your Deputy instance, picking them up on each poll.
---

# Deputy - New timesheet trigger

This trigger fetches new timesheet records in your Deputy instance.

![New timesheet trigger](/assets/new-timesheet-trigger.DKZIBCwk.png)_New timesheet trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Optional. Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new timesheet object.

Find out more about [timesheet object](https://www.deputy.com/api-doc/Resources/Timesheet/).

---
