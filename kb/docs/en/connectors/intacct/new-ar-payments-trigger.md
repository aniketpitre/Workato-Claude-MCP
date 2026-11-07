---
url: 'https://docs.workato.com/en/connectors/intacct/new-ar-payments-trigger.md'
description: >-
  The New AR payment trigger in the Sage Intacct connector fires when new posted
  payments and advances are added in your instance.
---

# Sage Intacct - New AR payment trigger

This trigger fetches new records under posted payments and advances in your Sage Intacct instance.

![New AR payment trigger](/assets/new-ar-payments-trigger.Bc0L6AuH.png)_New AR payment trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new AR payment object.

Find out more about [AR payment object](https://developer.intacct.com/api/accounts-receivable/ar-payments/).

---
