---
url: 'https://docs.workato.com/en/connectors/intacct/new-invoice-trigger.md'
description: >-
  The New invoice trigger in the Sage Intacct connector fires when new invoice
  records are created in your instance.
---

# Sage Intacct - New invoice trigger

This trigger fetches new invoice records in your Sage Intacct instance.

![New invoice trigger](/assets/new-invoice-trigger.2lUUZls4.png)_New invoice trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the new invoice object.

Find out more about [invoice object](https://developer.intacct.com/api/accounts-receivable/invoices/).

---
