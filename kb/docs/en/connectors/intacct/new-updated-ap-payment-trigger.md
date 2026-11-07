---
url: >-
  https://docs.workato.com/en/connectors/intacct/new-updated-ap-payment-trigger.md
description: >-
  The New/updated AP payment trigger in the Sage Intacct connector fires when
  posted payments and advances are created or updated in your instance.
---

# Sage Intacct - New/updated AP payment trigger

This trigger fetches new/updated records under posted payments and advances in your Sage Intacct instance.

![New/updated AP payment trigger](/assets/new-updated-ap-payment-trigger.Drz7GL5B.png)_New/updated AP payment trigger_

## Input

| Input field | Description |
| --- | --- |
| When first started, this recipe should pick up events from | Fetch trigger events from specified time. Defaults to an hour ago from time that recipe first started if left blank. Once recipe has been run or tested, value cannot be changed. Refer to [Triggers](/en/recipes/triggers#since-from) to learn more about this input field. |
| Trigger poll interval | Optional. How frequently to check for new/updated events. Defaults to 5 minutes if left blank. Minimum value allowed is 5 minutes. |

## Output

The output of this action will be a datatree that contains information about the AP payment object.

Find out more about [AP payment object](https://developer.intacct.com/api/accounts-payable/ap-payments/).
