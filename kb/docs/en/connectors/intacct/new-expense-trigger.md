---
url: 'https://docs.workato.com/en/connectors/intacct/new-expense-trigger.md'
description: >-
  The New expense trigger in the Sage Intacct connector fires when new expense
  records are created in your instance.
---

# Sage Intacct - New expense trigger

This trigger fetches new expense records in your Sage Intacct instance.

![New expense trigger](/assets/new-expense-trigger.CkOmciI7.png)_New expense trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new expense object.

Find out more about [expense object](https://developer.intacct.com/api/employee-expenses/).

---
