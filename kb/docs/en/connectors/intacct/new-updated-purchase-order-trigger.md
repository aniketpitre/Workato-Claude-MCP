---
url: >-
  https://docs.workato.com/en/connectors/intacct/new-updated-purchase-order-trigger.md
description: >-
  The New/updated purchase order trigger in the Sage Intacct connector fires
  when purchase order records are created or updated in your instance.
---

# Sage Intacct - New/updated purchase order trigger

This trigger fetches new/updated purchase order records in your Sage Intacct instance.

![New/updated purchase order trigger](/assets/new-updated-purchase-order-trigger.C-K3djvJ.png)_New/updated purchase order trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/update events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the purchase order object.

Find out more about [purchase order object](https://developer.intacct.com/api/purchasing/purchasing-transactions/).
