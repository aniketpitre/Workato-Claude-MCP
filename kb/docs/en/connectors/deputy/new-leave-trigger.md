---
url: 'https://docs.workato.com/en/connectors/deputy/new-leave-trigger.md'
description: >-
  The New leave trigger in the Deputy connector fires when new leave records are
  created in your Deputy instance, picking them up on each poll.
---

# Deputy - New leave trigger

This trigger fetches new leave records in your Deputy instance.

![New leave trigger](/assets/new-leave-trigger.DVJUjqEw.png)_New leave trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Optional. Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new leave object.

Find out more about [leave object](https://www.deputy.com/api-doc/Resources/Leave/).

---
